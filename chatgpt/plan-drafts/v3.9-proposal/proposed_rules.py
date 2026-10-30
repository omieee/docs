"""Draft v3.9 structural rules. This is a proposal, not the approved checker.

These checks inspect the plan, not Om's skills or the behaviour of PRCP.
Week-row order means planned execution order, not evidence of completion.
"""
from collections import defaultdict
import re

REQUIRED = {
    "Go": {f"G{i}" for i in range(1, 8)} | {f"A{i}" for i in range(1, 7)},
    "Kubernetes": {f"K{i}" for i in range(1, 6)} | {"K6a", "K6b", "K7a", "K7b"},
    "Controllers": {f"OP{i}" for i in range(1, 8)},
    "AWS and Terraform": {f"CL{i}" for i in range(1, 5)},
}
BASE_DEPS = [
    ("K6a", "D1"), ("K6a", "K5"), ("K7b", "K6a"),
    ("K6b", "A6"), ("K6b", "K6a"), ("F1", "O1"), ("F1", "K6b"),
    ("MC2", "L3"), ("MC2", "Y8a"), ("MC5", "L4"),
    ("A1", "G7"), ("A3", "S5"), ("C1", "D1"), ("C1", "Y1"),
    ("P4", "Y8a"), ("H6", "H2"), ("OP1", "G7"), ("OP1", "K5"),
    ("OP4", "OP3"), ("OP4", "K6a"), ("OP4", "A2"),
    ("CL2", "CL1"), ("CL3", "CL2"), ("CL3", "K6a"),
    ("CL4", "CL3"), ("CL4", "C1"), ("K3", "D1"),
]


def chain(*units):
    return [(later, earlier) for earlier, later in zip(units, units[1:])]


DEPS = sorted(set(BASE_DEPS + [("CL3", "K6b")] +
                  chain(*[f"G{i}" for i in range(1, 8)]) +
                  chain("A1", "A2", "A3", "A4", "A5", "A6") +
                  chain("K1", "K2", "K3", "K4", "K5") +
                  chain(*[f"OP{i}" for i in range(1, 8)])))
WEEK = re.compile(r"^\| W(\d+) · ([^|]*?) · ([\d.]+)h \| (.*?) \| ([^|]*) \|$", re.M)
ITEM = re.compile(r"\*\*([^*]+)\*\* ([\d.]+)h(?:: ([^·]*))?")


def section(text, number):
    m = re.search(rf"^## {number}\. .*?$", text, re.M)
    if m is None:
        raise ValueError(f"missing section {number}")
    end = re.search(r"^## \d+\. ", text[m.end():], re.M)
    return text[m.end():m.end() + end.start()] if end else text[m.end():]


def parse(text):
    """Reject malformed/duplicate rows instead of silently dropping them."""
    errors = []
    try:
        sec6, sec14 = section(text, 6), section(text, 14)
    except ValueError as exc:
        return {}, {}, {}, [f"Schema: {exc}"]
    budgets = {}
    for label, value in re.findall(r"^\| ([A-Z]{1,2}\d{1,2}[ab]?) [^|]*\| ([\d.]+) \|", sec6, re.M):
        if label in budgets:
            errors.append(f"Schema: duplicate unit {label}")
        budgets[label] = float(value)
    weeks, gates = {}, defaultdict(list)
    candidate_rows = [line for line in sec14.splitlines() if re.match(r"^\| W\d", line)]
    matches = list(WEEK.finditer(sec14))
    if len(candidate_rows) != len(matches) or not matches:
        errors.append("Schema: malformed or absent week rows")
    for match in matches:
        n, _, _, body, proof = match.groups()
        n = int(n)
        if n in weeks:
            errors.append(f"Schema: duplicate W{n}")
        items = []
        for label, value, description in ITEM.findall(body):
            hours = float(value)
            if hours <= 0:
                errors.append(f"Schema: W{n} {label} must have positive hours")
            items.append(("H6" if label == "Mock" else label, hours, description))
        if len(items) != len(re.findall(r"\*\*[^*]+\*\*", body)):
            errors.append(f"Schema: W{n} has an unparsed item")
        weeks[n] = items
        for gate in re.findall(r"\bGATE ([ABC])\b", proof):
            gates[gate].append(n)
    return budgets, weeks, dict(gates), errors


def structural_errors(budgets, weeks, gates, deps=DEPS):
    errors = []
    first, last = {}, {}
    for week, items in sorted(weeks.items()):
        for index, (label, _, _) in enumerate(items):
            first.setdefault(label, (week, index))
            last[label] = (week, index)
    for pillar, units in REQUIRED.items():
        for unit in sorted(units):
            if unit not in budgets or budgets[unit] <= 0:
                errors.append(f"Core: {pillar} unit {unit} absent or unfunded in section 6")
            if unit not in first:
                errors.append(f"Core: {pillar} unit {unit} absent from section 14")
    for dependent, prerequisite in deps:
        if dependent not in first:
            continue
        if prerequisite not in last:
            errors.append(f"Order: {dependent} has no scheduled prerequisite {prerequisite}")
        elif first[dependent] <= last[prerequisite]:
            errors.append(f"Order: {dependent} starts at {first[dependent]} before {prerequisite} finishes at {last[prerequisite]}")
    for gate in "ABC":
        if len(gates.get(gate, [])) != 1:
            errors.append(f"Gate: expected exactly one GATE {gate}")
    if all(len(gates.get(gate, [])) == 1 for gate in "ABC"):
        a, b, c = (gates[gate][0] for gate in "ABC")
        if not a < b < c:
            errors.append("Gate: A, B and C must be in increasing weeks")
        for unit in sorted(set.union(*REQUIRED.values())):
            if unit in last and last[unit][0] >= b:
                errors.append(f"Core: {unit} must finish before Gate B, not in or after its week W{b}")
    labs = [(week, hours) for week, items in sorted(weeks.items())
            for label, hours, _ in items if label == "CL3"]
    if len(labs) != 4 or any(abs(hours - 3) > 1e-9 for _, hours in labs):
        errors.append(f"Cloud labs: CL3 needs four unsplit 3h entries; found {labs}")
    return errors


def check(text):
    budgets, weeks, gates, errors = parse(text)
    if errors:
        return errors
    errors += structural_errors(budgets, weeks, gates)
    try:
        sec5 = section(text, 5)
    except ValueError as exc:
        return errors + [f"Schema: {exc}"]
    protected = re.search(r"\*\*Never cut:\*\*([^\n]+)", sec5)
    if not protected or not all(re.search(word, protected.group(1), re.I)
                                for word in (r"\bAWS\b|\bpublic cloud\b", r"\bTerraform\b")):
        errors.append("Core: explicitly protect AWS/public cloud and Terraform in the never-cut list")
    return errors

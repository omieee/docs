"""Check the Phase 1 master plan for internal consistency.

Usage: python3 check_plan.py Phase1_Master_Plan_v3.3.md
Run by whichever coach edits the plan. Exit code 0 means PASS.
"""
import datetime
import re
import sys
from collections import defaultdict

CAP, LIGHT_CAP, LIGHT_WEEKS = 15, 8, {0, 5, 12, 13}
NON_UNIT = {"DSA", "Setup", "Gate", "Proof", "Proofs and weekly close"}
DEPS = [("K6", "D1"), ("K6", "A6"), ("F1", "O1"), ("MC4", "L4"), ("MC2", "L3"), ("A1", "G7")]

text = open(sys.argv[1], encoding="utf-8").read()
errors = []

# Section 6: unit budgets
sec6 = text.split("## 6. Curriculum by track")[1].split("## 7.")[0]
budget = {u: float(h) for u, h in re.findall(r"^\| ([A-Z]\d) [^|]*\| ([\d.]+) \|", sec6, re.M)}
mc = re.search(r"^\| MC1-MC6 \| ([\d.]+) \|", sec6, re.M)
budget["MC"] = float(mc.group(1)) if mc else 0.0
dsa_budget = float(re.search(r"### 6\.6 DSA \(([\d.]+) hrs", sec6).group(1))
total_budget = float(re.search(r"\*\*Scheduled from Oct 1: ([\d.]+) hours", text).group(1))

# Section 14: week rows
sec14 = text.split("## 14. Week map from Oct 1")[1]
scheduled, first, last = defaultdict(float), {}, {}
grand = 0.0
for m in re.finditer(r"^\| W(\d+) · [^|]*?· ([\d.]+)h \| (.*?) \| [^|]* \|$", sec14, re.M):
    week, label, body = int(m.group(1)), float(m.group(2)), m.group(3)
    items = [(lab, float(h)) for lab, h in re.findall(r"\*\*([^*]+)\*\* ([\d.]+)h", body)]
    week_sum = sum(h for _, h in items)
    cap = LIGHT_CAP if week in LIGHT_WEEKS else CAP
    if abs(week_sum - label) > 1e-9:
        errors.append(f"W{week}: items sum to {week_sum}h but the row says {label}h")
    if label > cap + 1e-9:
        errors.append(f"W{week}: {label}h exceeds the {cap}h cap")
    grand += week_sum
    for lab, h in items:
        key = "MC" if lab.startswith("MC") else ("H6" if lab == "Mock" else lab)
        scheduled[key] += h
        if lab not in NON_UNIT:
            first.setdefault(lab, week)
            last[lab] = week

for unit, b in sorted(budget.items()):
    if abs(scheduled.get(unit, 0.0) - b) > 1e-9:
        errors.append(f"{unit}: section 6 says {b}h, week map schedules {scheduled.get(unit, 0.0)}h")
for unit in scheduled:
    if unit not in budget and unit not in NON_UNIT:
        errors.append(f"{unit}: scheduled in the week map but missing from section 6")
if abs(scheduled["DSA"] - dsa_budget) > 1e-9:
    errors.append(f"DSA: section 6.6 says {dsa_budget}h, week map schedules {scheduled['DSA']}h")
if abs(grand - total_budget) > 1e-9:
    errors.append(f"Total: section 5 says {total_budget}h, week map sums to {grand}h")
for later, earlier in DEPS:
    if later in first and earlier in last and first[later] < last[earlier]:
        errors.append(f"{later} starts in W{first[later]} before {earlier} ends in W{last[earlier]}")


# Added Oct 5 (v3.3): checks the original script skipped
weeks = [(int(m.group(1)), m.group(2), float(m.group(3)), m.group(4), m.group(5))
         for m in re.finditer(r"^\| W(\d+) · ([^|]*?) · ([\d.]+)h \| (.*?) \| ([^|]*) \|$", sec14, re.M)]
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
def sunday(n):
    return datetime.date(2026, 10, 5) + datetime.timedelta(days=7 * (n - 1) + 6)
for i, (n, dates, *_rest) in enumerate(weeks):
    if n != i:
        errors.append(f"Week numbers not contiguous: found W{n} at position {i}")
        break
    if n == 0:
        continue
    s, e = sunday(n) - datetime.timedelta(days=6), sunday(n)
    exp = f"{MON[s.month-1]} {s.day}-{e.day}" if s.month == e.month else f"{MON[s.month-1]} {s.day}-{MON[e.month-1]} {e.day}"
    if dates != exp:
        errors.append(f"W{n}: dates '{dates}' should be '{exp}'")

# Phase totals: section 4 table and section 5 total row against the week map
phase_of, cur = {}, None
for line in sec14.split("\n"):
    m = re.match(r"^### (1[abc]) ", line)
    if m:
        cur = m.group(1)
    m = re.match(r"^\| W(\d+) ·", line)
    if m:
        phase_of[int(m.group(1))] = cur
phase_sum = {p: sum(lab for n, _, lab, _, _ in weeks if phase_of[n] == p) for p in ("1a", "1b", "1c")}
sec4 = text.split("## 4. ")[1].split("## 5.")[0]
for p, h in re.findall(r"^\| (1[abc]) [^|]*\| [^|]*\| ([\d.]+) \|", sec4, re.M):
    if abs(float(h) - phase_sum[p]) > 1e-9:
        errors.append(f"Section 4: {p} says {h}h, week map has {phase_sum[p]}h")
sec5 = text.split("## 5. ")[1].split("## 6.")[0]
m = re.search(r"1a ([\d.]+), 1b ([\d.]+), 1c ([\d.]+) \|", sec5)
for p, h in zip(("1a", "1b", "1c"), m.groups()):
    if abs(float(h) - phase_sum[p]) > 1e-9:
        errors.append(f"Section 5 total row: {p} says {h}h, week map has {phase_sum[p]}h")

# Section 5 track rows and section 6 headers against section 6 units
units = {u: h for u, h in budget.items() if u != "MC"}
def group(prefixes):
    return sum(h for u, h in units.items() if u[0] in prefixes)
ver = scheduled["Proofs and weekly close"] + scheduled["Gate"] + scheduled["Setup"]
tracks = [("PRCP", group("PYDCOF"), "6.1"), ("Go", group("GA"), "6.2"), ("Kubernetes", group("K"), "6.3"),
          ("HLD", group("H"), "6.4"), ("LLD", group("L") + budget["MC"], "6.5"), ("DSA", dsa_budget, "6.6"),
          ("Supporting", group("S"), "6.7"), ("Stories", group("R"), "6.8"), ("Verification", ver, None)]
rows = [float(h) for name, h in re.findall(r"^\| ([^|*][^|]*) \| [^|]+ \| ([\d.]+) \|", sec5, re.M)][:len(tracks)]
for (name, want, sec), got in zip(tracks, rows):
    if abs(got - want) > 1e-9:
        errors.append(f"Section 5 {name} row says {got}h, units add to {want}h")
    if sec:
        hm = re.search(rf"^### {re.escape(sec)} [^\n]*\(([\d.]+) hrs", text, re.M)
        if hm and abs(float(hm.group(1)) - want) > 1e-9:
            errors.append(f"Section {sec} header says {hm.group(1)}h, units add to {want}h")
pm = re.search(r"Postgres ([\d.]+), Python depth ([\d.]+)", sec5)
if pm and (float(pm.group(1)) != group("P") or float(pm.group(2)) != group("Y")):
    errors.append(f"Section 5 PRCP row: Postgres {pm.group(1)} / Python {pm.group(2)}, units give {group('P')} / {group('Y')}")
vm = re.search(r"unit proofs and weekly close ([\d.]+), gates ([\d.]+), Oct 1 procedure ([\d.]+)", sec5)
if vm and (float(vm.group(1)), float(vm.group(2)), float(vm.group(3))) != (scheduled["Proofs and weekly close"], scheduled["Gate"], scheduled["Setup"]):
    errors.append("Section 5 verification split does not match the week map")

# Gate headings in section 4 name the Sunday of their gate week
for n, _, _, _, proof in weeks:
    g = re.search(r"GATE ([ABC])", proof)
    if g:
        d = sunday(n)
        if f"**Gate {g.group(1)} ({MON[d.month-1]} {d.day}).**" not in sec4:
            errors.append(f"Section 4: Gate {g.group(1)} heading should read ({MON[d.month-1]} {d.day}), gate week is W{n}")

print(f"Weeks checked: {len(re.findall(r'^\| W\d+ ·', sec14, re.M))}, total {grand}h, DSA {scheduled['DSA']}h")
if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS: every week fits its cap and sums to its label, every unit matches section 6, totals and dependencies hold, "
      "week dates run on, phase and track totals match sections 4 and 5, gate dates match")

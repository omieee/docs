"""Check the Phase 1 master plan for internal consistency.

Usage: python3 check_plan.py Phase1_Master_Plan_v3.6.md
Run by whichever coach edits the plan. Exit code 0 means PASS.

v3.6 adds: two-letter and split unit labels (OP1, CL2, K6a, Y8b, MP, RR), section 6.10-6.12,
the campaign line inside the map, light weeks in 2027, the continuity (gap) rule per track,
and a fragmentation warning. Section 5 rows are matched by name, not by position.
"""
import datetime
import re
import sys
from collections import defaultdict

CAP, LIGHT_CAP = 12, 7
LIGHT_WEEKS = {0, 5, 12, 13, 56, 64, 65}   # W0 short; Diwali 2026; year end 2026; Diwali 2027; year end 2027
NON_UNIT = {"DSA", "Setup", "Gate", "Proofs and weekly close", "Campaign"}
DEPS = [("K6a", "D1"), ("K6a", "K5"), ("K7b", "K6a"), ("K6b", "A6"), ("K6b", "K6a"),
        ("F1", "O1"), ("F1", "K6b"), ("MC2", "L3"), ("MC2", "Y8a"), ("MC5", "L4"),
        ("A1", "G7"), ("A3", "S5"), ("C1", "D1"), ("C1", "Y1"), ("P4", "Y8a"), ("H6", "H2"),
        ("OP1", "G7"), ("OP1", "K5"), ("OP4", "OP3"), ("OP4", "K6a"), ("OP4", "A2"),
        ("CL2", "CL1"), ("CL3", "CL2"), ("CL3", "K6a"), ("CL4", "CL3"), ("CL4", "C1")]
# Continuity rule (section 6.12): idle weeks allowed in a row, before and after the track's foundation unit closes
GAP_TRACKS = {"Go": "G7", "Kubernetes": "K5", "LLD": "L3", "HLD": "H2", "Operators": "OP5", "Cloud": "CL2"}
LIMIT_LEARNING, LIMIT_AFTER = 1, 3
UNIT_RE = r"(?:[A-Z]{1,2}\d{0,2}[ab]?)"

text = open(sys.argv[1], encoding="utf-8").read()
errors, warnings = [], []

# Section 6: unit budgets per subsection
sec6 = text.split("## 6. Curriculum by track")[1].split("## 7.")[0]
budget, unit_sec, sec_hdr = {}, {}, {}
for block in re.split(r"^### ", sec6, flags=re.M)[1:]:
    m = re.match(r"(6\.\d+) [^\n]*?\(([\d.]+) hrs", block)
    if not m:
        continue
    sec, hdr_h = m.group(1), float(m.group(2))
    sec_hdr[sec] = hdr_h
    for u, h in re.findall(rf"^\| ({UNIT_RE}) [^|]*\| ([\d.]+) \|", block, re.M):
        budget[u] = float(h); unit_sec[u] = sec
    mc = re.search(r"^\| MC0-MC8 \| ([\d.]+) \|", block, re.M)
    if mc:
        budget["MC"] = float(mc.group(1)); unit_sec["MC"] = sec
dsa_budget = float(re.search(r"### 6\.6 DSA \(([\d.]+) hrs", sec6).group(1))
total_budget = float(re.search(r"\*\*Scheduled from Oct 1: ([\d.]+) hours", text).group(1))
for sec, hdr_h in sec_hdr.items():
    if sec == "6.6":
        continue
    got = sum(h for u, h in budget.items() if unit_sec[u] == sec)
    if abs(got - hdr_h) > 1e-9:
        errors.append(f"Section {sec} header says {hdr_h}h, its units add to {got}h")

# Section 14: week rows
sec14 = text.split("## 14. Week map from Oct 1")[1]
weeks = [(int(m.group(1)), m.group(2), float(m.group(3)), m.group(4), m.group(5))
         for m in re.finditer(r"^\| W(\d+) · ([^|]*?) · ([\d.]+)h \| (.*?) \| ([^|]*) \|$", sec14, re.M)]
scheduled, first, last = defaultdict(float), {}, {}
items_by_week = {}
grand = 0.0
small = 0
for n, _, label, body, _ in weeks:
    items = [(lab, float(h), t) for lab, h, t in re.findall(r"\*\*([^*]+)\*\* ([\d.]+)h(?:: ([^·]*))?", body)]
    items_by_week[n] = items
    week_sum = sum(h for _, h, _ in items)
    cap = LIGHT_CAP if n in LIGHT_WEEKS else CAP
    if abs(week_sum - label) > 1e-9:
        errors.append(f"W{n}: items sum to {week_sum}h but the row says {label}h")
    if label > cap + 1e-9:
        errors.append(f"W{n}: {label}h exceeds the {cap}h cap")
    grand += week_sum
    for lab, h, _ in items:
        key = "MC" if re.fullmatch(r"MC\d", lab) else ("H6" if lab == "Mock" else lab)
        scheduled[key] += h
        if key not in NON_UNIT:
            first.setdefault(key, n); last[key] = n
        if lab not in NON_UNIT and lab not in ("RR", "MP") and h < 0.5 - 1e-9:
            small += 1

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

# Week numbers and dates
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

# Section 5 track rows, matched by their first word, against section 6 and the map
def sec_sum(sec):
    return sum(h for u, h in budget.items() if unit_sec[u] == sec)
ver = scheduled["Proofs and weekly close"] + scheduled["Gate"] + scheduled["Setup"]
want = {"PRCP": sec_sum("6.1"), "Go": sec_sum("6.2"), "Kubernetes": sec_sum("6.3"), "HLD": sec_sum("6.4"),
        "LLD": sec_sum("6.5"), "DSA": dsa_budget, "Supporting": sec_sum("6.7"), "Stories": sec_sum("6.8"),
        "Operators": sec_sum("6.10"), "Cloud": sec_sum("6.11"), "Continuity": sec_sum("6.12"),
        "Verification": ver, "Campaign": scheduled["Campaign"]}
seen = set()
for name, h in re.findall(r"^\| ([A-Za-z]+)[^|]* \| [^|]+ \| ([\d.]+) \|", sec5, re.M):
    if name in want:
        seen.add(name)
        if abs(float(h) - want[name]) > 1e-9:
            errors.append(f"Section 5 {name} row says {h}h, units and map give {want[name]}h")
for name in want:
    if name not in seen:
        errors.append(f"Section 5 has no {name} row")

# Gate headings in section 4 name the Sunday of their gate week
for n, _, _, _, proof in weeks:
    g = re.search(r"GATE ([ABC])", proof)
    if g:
        d = sunday(n)
        if f"**Gate {g.group(1)} ({MON[d.month-1]} {d.day} {d.year}).**" not in sec4:
            errors.append(f"Section 4: Gate {g.group(1)} heading should read ({MON[d.month-1]} {d.day} {d.year}), gate week is W{n}")

# Continuity rule (section 6.12)
def tracks(lab, txt):
    if lab == "RR":
        m = re.match(r"(Go|Kubernetes|HLD|LLD|Operators|Cloud):", (txt or "").strip())
        return {m.group(1)} if m else set()
    if lab == "Gate":
        if "Gate A" in (txt or ""):
            return {"Go", "Kubernetes", "HLD"}
        if "Gate B" in (txt or "") or "checklist" in (txt or ""):
            return set(GAP_TRACKS)
        return set()
    if lab.startswith("OP"):
        return {"Go", "Kubernetes", "Operators"}
    if lab.startswith("CL"):
        return {"Cloud", "Kubernetes"} if lab == "CL3" else {"Cloud"}
    if lab == "MP" or re.fullmatch(r"MC\d", lab) or re.fullmatch(r"L\d", lab):
        return {"LLD"}
    if lab == "Mock" or re.fullmatch(r"H\d", lab):
        return {"HLD"}
    if re.fullmatch(r"(G|A)\d", lab):
        return {"Go"}
    if re.fullmatch(r"K\d[ab]?", lab):
        return {"Kubernetes"}
    return set()
gate_c = max(n for n, *_r, proof in weeks if "GATE C" in proof)
contact = {t: [n for n, its in items_by_week.items() if any(t in tracks(l, x) for l, _, x in its)] for t in GAP_TRACKS}
for t, ws in contact.items():
    if not ws:
        continue
    pu = GAP_TRACKS[t]
    for a, b in zip(ws, ws[1:] + [gate_c + 1]):
        idle = b - a - 1
        if b > gate_c + 1 or idle <= 0:
            continue
        limit = LIMIT_LEARNING if a < last.get(pu, 10**6) else LIMIT_AFTER
        if idle > limit:
            errors.append(f"Continuity: {t} idle {idle} weeks after W{a} (limit {limit})")
if small:
    warnings.append(f"{small} unit pieces under 0.5h (fragmentation warning only, section 6.12)")

print(f"Weeks checked: {len(weeks)}, total {grand}h, DSA {scheduled['DSA']}h, campaign {scheduled['Campaign']}h")
for w_ in warnings:
    print("WARNING:", w_)
if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS: every week fits its cap and sums to its label, every unit matches section 6, totals and dependencies hold, "
      "week dates run on, phase and track totals match sections 4 and 5, gate dates match, "
      "and no track breaks the continuity rule")

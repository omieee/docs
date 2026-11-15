"""Check the Phase 1 master plan for internal consistency.

Usage: python3 check_plan.py Phase1_Master_Plan_v3.9.md
Run by whichever coach edits the plan. Exit code 0 means PASS.

v3.6 adds: two-letter and split unit labels (OP1, CL2, K6a, Y8b, MP, RR), section 6.10-6.12,
the campaign line inside the map, light weeks in 2027, the continuity (gap) rule per track,
and a fragmentation warning. Section 5 rows are matched by name, not by position.

v3.7 adds: no coaching-owner wording outside the change log unless it says there is none or that it
was withdrawn; the human live-coding mock (section 6.6 #13) scheduled before Gate B; the international
slice in a harvest week of 1a and of 1b before Gate B; the four-line Gate C readiness record; the gate
dates in sections 1, 4 and 11 agreeing with the gate weeks; section 14's stated hours and DSA total.

v3.8 adds: every teaching part in the map (weeks from W4) carries a typed use step in real code
("Use in PRCP (code):", "Use in the agent (code):", "Use on kind (code):" or "(explain)"); no unit part starts
in a week with under 30 minutes; no row names a listed tool or test style before the first week of the unit that teaches it;
K3 after D1; section 7 no longer says DSA alone keeps spaced review; section 6 states the use rule and
section 6.12 the warm-up and the optional bedside cards (the rule checks the optional-cards marker).

v3.9 adds (Nov 15 2026): MC labels kept apart for prerequisite checks (MC2 after L3 and Y8a, MC5 after L4 were never
checked in v3.8); a prerequisite that ends in the same week must come earlier in that row; every v3.9 unit must exist in
section 6 (no pillar can disappear); CL3 runs only in whole 3-hour sessions and after K6b; DS1 after G7 and H3 and
with its use steps; the token rules, the recognition-first DSA rule and the measured-pace forecast must be present.

v3.9 r2 adds (Nov 15 2026, after ChatGPT's verification): E1 and its dependencies; Gate A and Gate B items close before
their gate week; every dated DSA review sits inside its week and names the right weekday; the live week references in
sections 4, 6 and 14 match the map; each Go row's Learning Go chapters agree between its text and its resource key and
with the declared map, and G2 covers chapters 2 to 5; the W7-W12 run sheet exists and its moved hours add up; the
available-time scenarios, the short-week rule and the release-evidence table are present.
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
        ("CL2", "CL1"), ("CL3", "CL2"), ("CL3", "K6a"), ("CL4", "CL3"), ("CL4", "C1"), ("K3", "D1"),
        ("CL3", "K6b"), ("DS1", "G7"), ("DS1", "H3"),   # v3.9
        ("E1", "P1"), ("E1", "P4"), ("E1", "S5"), ("C1", "E1"), ("A3", "E1"), ("OP4", "E1")]   # v3.9 r2
REQUIRED_UNITS = ["P1", "P2", "P3", "P4", "E1", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7a", "Y7b", "Y8a", "Y8b", "D1", "D2", "C1", "O1",
                  "F1", "AI1", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "A1", "A2", "A3", "A4", "A5", "A6", "K1", "K2", "K3",
                  "K4", "K5", "K6a", "K6b", "K7a", "K7b", "H1", "H2", "H3", "H4", "H5", "H6", "DS1", "L1", "L2", "L3", "L4",
                  "MC", "MP", "OP1", "OP2", "OP3", "OP4", "OP5", "OP6", "OP7", "CL1", "CL2", "CL3", "CL4", "RR"]   # v3.9
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
first_pos, last_pos = {}, {}   # v3.9: item positions, for order inside a week
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
    for pos_, (lab, h, _) in enumerate(items):
        key = "MC" if re.fullmatch(r"MC\d", lab) else ("H6" if lab == "Mock" else lab)
        scheduled[key] += h
        if key not in NON_UNIT:
            first.setdefault(key, n); last[key] = n
            if key == "MC":   # v3.9: keep MC2, MC5 and the rest apart for the prerequisite rules
                first.setdefault(lab, n); last[lab] = n
                first_pos.setdefault(lab, pos_); last_pos[(lab, n)] = pos_
            first_pos.setdefault(key, pos_) if first[key] == n else None
            last_pos[(key, n)] = pos_
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
    elif later in first and earlier in last and first[later] == last[earlier]:   # v3.9: same week, so check the order in the row
        if first_pos.get(later, 0) < last_pos.get((earlier, last[earlier]), 0):
            errors.append(f"{later} starts in W{first[later]} before {earlier} ends in the same row")
# v3.9: no unit may disappear from section 6
for u in REQUIRED_UNITS:
    if u not in budget:
        errors.append(f"Unit inventory: {u} is missing from section 6")
# v3.9: CL3 only in whole 3-hour sessions (each lab is applied and destroyed in the same session, section 6.11)
for n, its in items_by_week.items():
    cl3 = sum(h for lab, h, _ in its if lab == "CL3")
    if cl3 > 1e-9 and abs(cl3 - 3.0) > 1e-9:
        errors.append(f"CL3: W{n} has {cl3:g}h of CL3, not one whole 3-hour session")

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
    if lab == "DS1":   # v3.9 r2: Go code on Maelstrom, a distributed-systems (HLD) proof
        return {"Go", "HLD"}
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
# ---------------- v3.7 rules ----------------
body = text.split("## 13. Change log")[0]

for sent in re.split(r"(?<=[.!?|])\s+|\n", body):
    if re.search(r"coaching owner", sent, re.I) and not re.search(r"no coaching owner|withdraw", sent, re.I):
        line = body.count("\n", 0, body.find(sent)) + 1
        errors.append(f"Coaching owner: line {line} names a coaching owner (Om, Oct 23 14:56: equal partners, none)")

gate_b = max(n for n, *_r, proof in weeks if "GATE B" in proof)
hm = [n for n, its in items_by_week.items() for l, _, t in its
      if l == "DSA" and (t or "").strip().startswith("Human live-coding mock")]
if not hm:
    errors.append("Human live-coding mock (section 6.6 #13) is not in the week map")
elif min(hm) >= gate_b:
    errors.append(f"Human live-coding mock is in W{min(hm)}, not before Gate B (W{gate_b})")
if "13. **Human live-coding mock" not in sec6:
    errors.append("Section 6.6 has no rule 13 for the human live-coding mock")
for ph in ("1a", "1b"):
    ok = [n for n, its in items_by_week.items() if phase_of.get(n) == ph and n < gate_b
          for l, _, t in its if l == "Campaign" and "JD harvest" in (t or "") and "international" in (t or "")]
    if not ok:
        errors.append(f"International slice: no {ph} harvest week before Gate B names it (section 8, F1)")
rr = re.search(r"\*\*Readiness record[^\n]*", sec4)
if not rr or not all(f"({i})" in rr.group(0) for i in (1, 2, 3, 4)) or "Only line 1 decides Gate C" not in rr.group(0):
    errors.append("Gate C: the four-line readiness record (section 4) is missing or incomplete")

gdate = {}
for n, *_r, proof in weeks:
    g = re.search(r"GATE ([ABC])", proof)
    if g:
        d = sunday(n)
        gdate[g.group(1)] = f"{MON[d.month-1]} {d.day} {d.year}"
want_line = f"Gate A {gdate['A']}, Gate B {gdate['B']}, Gate C {gdate['C']}"
sec1 = text.split("## 1. ")[1].split("## 2.")[0]
if not re.search(r"Forecast \(v[\d.]+\): " + re.escape(want_line), sec1):
    errors.append(f"Section 1 decision 4: forecast should read {want_line}")
if not re.search(r"forecast is " + re.escape(want_line), sec4):
    errors.append(f"Section 4 intro: forecast should read {want_line}")
sec11 = text.split("## 11. ")[1].split("## 12.")[0]
if f"Phase 2 starts after Gate C, now forecast {gdate['C']}" not in sec11:
    errors.append(f"Section 11: Phase 2 should start after Gate C, {gdate['C']}")
intro = sec14.split("**How to use a row.**")[0]
mh = re.search(r"([\d.]+) scheduled hours", intro)
if not mh or abs(float(mh.group(1)) - grand) > 1e-9:
    errors.append(f"Section 14 intro: scheduled hours should be {grand:g}")
md = re.search(r"DSA totals ([\d.]+)", intro)
if not md or abs(float(md.group(1)) - dsa_budget) > 1e-9:
    errors.append(f"Section 14 intro: DSA total should be {dsa_budget:g}")

# ---------------- v3.8 rules ----------------
# Use in real code within 7 days (section 6): every teaching part in the map carries its use step
REQUIRE_USE = {"DS1", "Y3", "Y4", "Y5", "Y8a", "Y8b", "P2", "P3", "G2", "G3", "G4", "G5", "G6", "G7", "K3", "K4", "K5", "L1", "L2", "L3", "L4"}
USE_EXEMPT = ("Reference counting", "Checklist D cold re-run", "WAL on commit", "OOP pillars", "Types, composite types and control, first contact")   # knowledge-only parts, or done before v3.8
for n, its in items_by_week.items():
    if n < 4:
        continue
    for lab, h_, t in its:
        t = (t or "").strip()
        if lab in REQUIRE_USE and not t.startswith(USE_EXEMPT) and not re.search(r"Use (in PRCP|in the agent|on kind) \((code|explain)\):", t):
            errors.append(f"Use step: W{n} {lab} has no typed use in real code ('{t[:50]}...')")
        # 30-minute start rule (A3): a unit part never starts in a week with under 30 minutes
        if lab not in NON_UNIT and lab not in ("RR", "MP", "Mock") and not re.fullmatch(r"MC\d", lab) and h_ < 0.5 - 1e-9 and "(continued)" not in t:
            errors.append(f"Small start: W{n} {lab} starts a part with {h_:g}h (under 30 minutes)")
# Taught before named (section 6.12): a listed term may appear in a row only from its teaching unit's first week
TERMS = {"table-driven": "G6", "-race": "G7", "`yield`": "Y3", "asyncio": "Y4", "mypy": "Y1", "EXPLAIN": "P3",
         "errgroup": "A2", "Hypothesis": "Y6", "envtest": "OP6", "`IN`": "P2", "subquer": "P2"}
for n, its in items_by_week.items():
    if n < 4:
        continue
    for lab, _, t in its:
        for term, unit in TERMS.items():
            if term in (t or "") and unit in first and n < first[unit]:
                errors.append(f"Taught before named: W{n} {lab} names {term} before {unit} teaches it (W{first[unit]})")
sec7 = text.split("## 7. ")[1].split("## 8.")[0]
if "DSA alone keeps continuous spaced review" in sec7:
    errors.append("Section 7: spaced review is limited to DSA again (v3.8 gives every topic warm-ups and cards)")
if "**Use in real code within 7 days" not in sec6:
    errors.append("Section 6: the use rule (Use in real code within 7 days) is missing")
sec612 = sec6.split("### 6.12")[1] if "### 6.12" in sec6 else ""
if "**Warm-up (v3.8).**" not in sec612:
    errors.append("Section 6.12: the warm-up rule is missing")
if "**Bedside cards (v3.8, optional).**" not in sec612:
    errors.append("Section 6.12: the bedside cards rule is missing")

if small:
    warnings.append(f"{small} unit pieces under 0.5h (fragmentation warning only, section 6.12)")

print(f"Weeks checked: {len(weeks)}, total {grand}h, DSA {scheduled['DSA']}h, campaign {scheduled['Campaign']}h")
for w_ in warnings:
    print("WARNING:", w_)

# ---------------- v3.9 rules ----------------
if "**Token rules (v3.9" not in text.split("## 1. ")[0]:
    errors.append("Section 0: the v3.9 token rules are missing")
if "14. **Recognition first (v3.9" not in sec6:
    errors.append("Section 6.6: the recognition-first rule (14) is missing")
if "**Measured pace at the Nov 15 re-forecast (v3.9):**" not in sec4:
    errors.append("Section 4: the measured-pace forecast is missing")

# ---------------- v3.9 r2 rules ----------------
MONS = {m: i + 1 for i, m in enumerate(MON)}
DAYS = "Mon Tue Wed Thu Fri Sat Sun".split()
gate_a = max(n for n, *_r, proof in weeks if "GATE A" in proof)
# Gate items close before their gate week (section 4)
for u in ["P2", "P3", "P4", "G7", "K7a", "MC3"]:
    if u not in last or last[u] >= gate_a:
        errors.append(f"Gate A item {u} ends in W{last.get(u)}, not before the Gate A week (W{gate_a})")
if "H6" not in first or first["H6"] >= gate_a:
    errors.append("Gate A item Mock 1 is not before the Gate A week")
for u in ["A2", "A3", "A4", "A5", "E1", "C1", "O1", "OP7", "CL3", "CL4", "K7b", "F1", "MC7", "AI1"]:
    if u not in last or last[u] >= gate_b:
        errors.append(f"Gate B item {u} ends in W{last.get(u)}, not before the Gate B week (W{gate_b})")
# Dated reviews and any dated DSA item sit inside their week, on the right weekday (ChatGPT's finding 2)
for n, its in items_by_week.items():
    if n < 7:
        continue
    s_ = sunday(n) - datetime.timedelta(days=6)
    for lab, _, t in its:
        if lab != "DSA":
            continue
        for dname, mon, day in re.findall(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2})\b", t or ""):
            hits = [s_ + datetime.timedelta(days=k) for k in range(7)
                    if (s_ + datetime.timedelta(days=k)).month == MONS[mon] and (s_ + datetime.timedelta(days=k)).day == int(day)]
            if not hits:
                errors.append(f"Dated review: W{n} names {dname} {mon} {day}, outside the week")
            elif DAYS[hits[0].weekday()] != dname:
                errors.append(f"Dated review: W{n} names {dname} {mon} {day}, but that date is a {DAYS[hits[0].weekday()]}")
# Live week references in the text match the map (ChatGPT's finding 5)
def wk(pred):
    return sorted({n for n, its in items_by_week.items() for l, _, t in its if pred(l, (t or "").strip())})
sec68 = sec6.split("### 6.8")[1].split("### 6.9")[0] if "### 6.8" in sec6 else ""
sec66 = sec6.split("### 6.6")[1].split("### 6.7")[0] if "### 6.6" in sec6 else ""
sec64 = sec6.split("### 6.4")[1].split("### 6.5")[0] if "### 6.4" in sec6 else ""
sec61 = sec6.split("### 6.1")[1].split("### 6.2")[0] if "### 6.1" in sec6 else ""
tail = sec14.split("### 1c")[1] if "### 1c" in sec14 else ""
u1 = wk(lambda l, t: l == "DSA" and t.startswith("Unseen set 1"))
u2 = wk(lambda l, t: l == "DSA" and t.startswith("Unseen set 2"))
blind = wk(lambda l, t: l == "DSA" and "blind mixed sets" in t)
hm = wk(lambda l, t: l == "DSA" and t.startswith("Human live-coding mock"))
nauk = wk(lambda l, t: l == "R1" and t.startswith("Naukri live"))
aloud = wk(lambda l, t: l == "R2" and t.startswith("Tell the first two stories aloud"))
write = wk(lambda l, t: l == "R2" and t.startswith("Write the first two honest stories"))
mocks = wk(lambda l, t: l == "Mock")
refresh = wk(lambda l, t: l == "Campaign" and t.startswith("JD harvest refresh"))
y3 = wk(lambda l, t: l == "Y3")
blind_pre = [n for n in blind if n < gate_b]
c1_weeks = [n for n, *_r in weeks if phase_of.get(n) == "1c"]
ANCHORS = [
    ("6.6 #12 set 1", sec66, r"Set 1 runs in the Gate A week \(W(\d+)\)", u1[:1]),
    ("6.6 #12 set 2", sec66, r"Set 2 runs in the Gate B week \(W(\d+)\)", u2[:1]),
    ("6.6 #7 blind sets", sec66, r"In the weeks before Gate B \(W(\d+)-W(\d+);", blind_pre[:1] + blind_pre[-1:]),
    ("6.6 #13 human mock", sec66, r"once before Gate B \(W(\d+) in v3\.9", hm[:1]),
    ("6.8 R1 Naukri", sec68, r"Naukri complete and live about 15 days before Gate A \(W(\d+)\)", nauk[:1]),
    ("6.8 R1 proof", sec68, r"Naukri live by W(\d+);", nauk[:1]),
    ("6.8 R2 written", sec68, r"stories are written in W(\d+)-W(\d+)", write[:1] + write[-1:]),
    ("6.8 R2 aloud", sec68, r"told aloud in voice mode in W(\d+)-W(\d+)", aloud[:1] + aloud[-1:]),
    ("6.4 mock 2", sec64, r"\(mock 2 is in W(\d+)\)", mocks[1:2]),
    ("6.1 Y3", sec61, r"The last four topics finish in W(\d+), after Gate A", y3[-1:]),
    ("4 unseen set 1", sec4, r"Also in the Gate A week \(W(\d+)\), but never a Gate A item: unseen set 1", u1[:1]),
    ("4 unseen set 2", sec4, r"Plus unseen set 2 \(W(\d+),", u2[:1]),
    ("4 blind sets", sec4, r"latest blind mixed set before the gate \(W(\d+)-W(\d+)\)", blind_pre[-2:]),
    ("4 Naukri gate list", sec4, r"Naukri \(live since W(\d+),", nauk[:1]),
    ("4 Naukri applications", sec4, r"Naukri goes live about 15 days before Gate A \(W(\d+)\)", nauk[:1]),
    ("4 harvest refresh", sec4, r"using the W(\d+) harvest refresh", refresh[:1]),
    ("14 1c note", tail, r"1c keeps study light on purpose \(W(\d+) [\d.]+h, W(\d+) [\d.]+h, W(\d+) [\d.]+h, W(\d+) [\d.]+h\)", c1_weeks),
]
for name, where, rx, want in ANCHORS:
    m = re.search(rx, where)
    if not m:
        errors.append(f"Week reference ({name}): the sentence is missing")
    elif [int(g) for g in m.groups()] != want:
        errors.append(f"Week reference ({name}): text says {', '.join('W' + g for g in m.groups())}, the map has {', '.join(f'W{w}' for w in want)}")
m = re.search(r"1c keeps study light on purpose \((W\d+ [\d.]+h(?:, W\d+ [\d.]+h)*)\)", tail)
if m:
    for wn, hh in re.findall(r"W(\d+) ([\d.]+)h", m.group(1)):
        lab_h = {n: lab for n, _, lab, _, _ in weeks}.get(int(wn))
        if lab_h is None or abs(lab_h - float(hh)) > 1e-9:
            errors.append(f"Week reference (14 1c note): W{wn} is {lab_h}h in the map, the note says {hh}h")
# Go chapters: text and resource key agree, and both follow the declared Learning Go map (ChatGPT's proposal check)
LG2_MAP = {"G2": {2, 3, 4, 5}, "G3": {6, 7}, "G4": {9}, "G5": {8}, "G6": {10, 11, 15}, "G7": {12, 14}, "A1": {13}}
def nums(txt):
    out = set()
    for a, b in re.findall(r"(\d+)(?:-(\d+))?", txt):
        out |= set(range(int(a), int(b or a) + 1))
    return out
g2_seen = set()
for n, its in items_by_week.items():
    if n < 4:
        continue
    for lab, _, t in its:
        if lab not in LG2_MAP or not t:
            continue
        body_, _, key = t.partition("[")
        prose = set()
        for m in re.finditer(r"Learning Go 2e (chapters? [\d][\d\- ,]*(?:(?:,? and |, )(?:chapter )?\d+)*)", body_):
            prose |= nums(m.group(1))
        mk = re.search(r"LG2 \(ch ([\d\-, ]+)\)", key)
        keyed = nums(mk.group(1)) if mk else set()
        if prose and not prose <= keyed:
            errors.append(f"Go map: W{n} {lab} text names Learning Go chapter {sorted(prose - keyed)}, its resource key says {sorted(keyed)}")
        if keyed and not keyed <= LG2_MAP[lab]:
            errors.append(f"Go map: W{n} {lab} cites Learning Go chapter {sorted(keyed - LG2_MAP[lab])}, outside {lab}'s declared chapters {sorted(LG2_MAP[lab])}")
        if lab == "G2":
            g2_seen |= keyed
if not {2, 3, 4, 5} <= g2_seen:
    errors.append(f"Go map: G2 never cites Learning Go chapter {sorted({2, 3, 4, 5} - g2_seen)} (the Go strategy's step 1 is chapters 2-4, then 5)")
# The W7-W12 run sheet (ChatGPT's proposal 1): every week present, moved hours add up to the row less the week's time
sheet = sec14.split("**Run sheet, W7 to W12")[1].split("**Resource key")[0] if "**Run sheet, W7 to W12" in sec14 else ""
if not sheet:
    errors.append("Section 14: the W7-W12 run sheet is missing")
else:
    rows_ = {int(m.group(1)): m for m in re.finditer(r"^\| W(\d+) \([^,]+, ([\d.]+)h row\) \| [^|]+ \| [^|]+ \| ([^|]+) \| ([^|]+) \|$", sheet, re.M)}
    labels = {n: lab for n, _, lab, _, _ in weeks}
    for n in range(7, 13):
        if n not in rows_:
            errors.append(f"Run sheet: W{n} is missing")
            continue
        m = rows_[n]
        row_h = float(m.group(2))
        if abs(row_h - labels[n]) > 1e-9:
            errors.append(f"Run sheet: W{n} says a {row_h}h row, the map has {labels[n]}h")
        cap_n = LIGHT_CAP if n in LIGHT_WEEKS else CAP
        for c, cell in ((9, m.group(3)), (6, m.group(4))):
            c_ = min(c, cap_n)
            mm = re.match(r"\s*([\d.]+)h:", cell)
            op = re.search(r"\(([\d.]+)h left open\)", cell)
            moved, open_ = float(mm.group(1)) if mm else -1.0, float(op.group(1)) if op else 0.0
            if abs((moved - open_) - max(0.0, labels[n] - c_)) > 1e-9:
                errors.append(f"Run sheet: W{n} at {c}h moves {moved}h with {open_}h open; the row less {c_}h is {max(0.0, labels[n] - c_)}h")
if "**Available-time scenarios (v3.9 r2)" not in sec4:
    errors.append("Section 4: the available-time scenarios (v3.9 r2) are missing")
if "**Short weeks (v3.9 r2" not in sec14:
    errors.append("Section 14: the short-week rule (v3.9 r2) is missing")
# v3.9 final (ChatGPT's 16:22 review, finding 1): hiring dates follow the gates
ma = re.search(r"After Gate A \(([A-Z][a-z]{2} \d{1,2} \d{4})\): normal application volume", sec4)
if not ma or ma.group(1) != gdate["A"]:
    errors.append(f"Applications: normal volume should start after Gate A ({gdate['A']}), text says {ma.group(1) if ma else 'nothing'}")
mb = re.search(r"an offer after Gate B \(([A-Z][a-z]{2} \d{1,2} \d{4})\) means joining around ([A-Z][a-z]+) (\d{4})", sec4)
gb_d = sunday(gate_b) + datetime.timedelta(days=1)   # the first day an offer after Gate B can be accepted
j_m, j_y = (gb_d.month + 3 - 1) % 12 + 1, gb_d.year + (gb_d.month + 3 - 1) // 12
FULL = "January February March April May June July August September October November December".split()
if not mb or mb.group(1) != gdate["B"] or mb.group(2) != FULL[j_m - 1] or int(mb.group(3)) != j_y:
    errors.append(f"Applications: an offer after Gate B ({gdate['B']}) with 3 months' notice means joining around {FULL[j_m - 1]} {j_y}")
if "**Gate A record (v3.9 final" not in sec4:
    errors.append("Section 4: the four-line Gate A record (v3.9 final) is missing")
if "fixed-work illustrations (v3.9 final)" not in sec4:
    errors.append("Section 4: the slower-pace dates are not labelled fixed-work illustrations (v3.9 final)")
if "**Release evidence (v3.9 r2" not in sec6:
    errors.append("Section 6.1: the release-evidence case table (v3.9 r2) is missing")

if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS: every week fits its cap and sums to its label, every unit matches section 6, totals and dependencies hold, "
      "week dates run on, phase and track totals match sections 4 and 5, gate dates match in sections 1, 4 and 11, "
      "no track breaks the continuity rule, no coaching owner is named, the v3.7 international items are in place, "
      "every teaching part carries a typed use step, no part starts with under 30 minutes, no row names a tool before "
      "the unit that teaches it, gate items close before their gate, dated reviews sit in their week, the week references "
      "match the map, the Go chapters match the declared map, and the W7-W12 run sheet adds up")

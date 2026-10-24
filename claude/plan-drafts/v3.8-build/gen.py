"""Build the v3.8 week map (section 14) from units.py and the week spec below."""
import datetime
import sys
from collections import defaultdict, OrderedDict
from units import U, MP_TEXT, MP_LOOP, total

EPS = 1e-9
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
LIGHT = {5, 12, 13, 56, 64, 65}          # Diwali 2026, year end 2026, Diwali 2027, year end 2027


def sunday(n):
    return datetime.date(2026, 10, 5) + datetime.timedelta(days=7 * (n - 1) + 6)


def dates(n):
    if n == 0:
        return "Oct 1-4"
    s, e = sunday(n) - datetime.timedelta(days=6), sunday(n)
    return f"{MON[s.month-1]} {s.day}-{e.day}" if s.month == e.month else f"{MON[s.month-1]} {s.day}-{MON[e.month-1]} {e.day}"


def cap(n, phase):
    if n in LIGHT:
        return 7.0
    return 12.0


# ---------------- DSA segments ----------------
DSA_DONE = {
    0: [(2.0, "Due colds first: 143 and 19 (day 7); then the stack lesson and NEW 20 Valid Parentheses [NC]")],
    1: [(3.5, "NEW 155 Min Stack, 739 Daily Temperatures (monotonic stack), done; 739 closed Oct 17 after two repair slots [NC]")],
    2: [(1.0, "Due colds: 155 D3 and D7, 739 D1 and D3, 20 D14 [NC]")],
    3: [(2.5, "Due colds first: 739 D7, 141 D28, 19 D28, 143 D28, 155 D14; then binary search lessons 14-15; NEW 704 Binary Search and 74 Search a 2D Matrix coded, interviews Oct 23 and Oct 25 [NC]")],
}
DSA_SEG = [
    ("new", 3.5, "Due colds first (704 and 74 D7, 739 D14, 155 D28); the 704 and 74 repairs in their own slots; then NEW 875 Koko Eating Bananas [NC]"),
    ("new", 2.5, "Sorting lessons 10-12: insertion, merge and quick sort as DRILLs, not counted (v3.6 funds lessons v3.5 named but did not budget) [NC]"),
    ("new", 3.5, "Recursion lessons 8-9, trees 16-17; NEW 226 Invert Binary Tree, 104 Maximum Depth [NC]"),
    ("new", 4.0, "Queue lesson 7 and tree DFS and BFS lessons 19-20 (v3.6 funds them); NEW 102 Level Order Traversal; colds [NC]"),
    ("new", 3.5, "NEW 98 Validate BST; heap lessons 23-25; NEW 703 Kth Largest in a Stream [NC]"),
    ("new", 3.5, "NEW 1046 Last Stone Weight, 973 K Closest Points [NC]"),
    ("new", 3.5, "Intervals explainer; NEW 56 Merge Intervals, 57 Insert Interval [NC]"),
    ("new", 3.5, "Prefix sums lesson; NEW 303 Range Sum Query, 560 Subarray Sum Equals K [NC]"),
    ("new", 3.5, "Backtracking lesson 22; NEW 78 Subsets, 39 Combination Sum (40 total) [NC]"),
    ("colds_a", None, "Colds only: due spaced re-solves, D90s included (section 6.6 #6) [NC]"),
    ("gateA", 3.5, "Unseen set 1: four problems Om has never solved (2 Easy, 2 Medium) from the families studied so far, no pattern label, one a day; the pattern, its signal words and the structural reason aloud before coding; scored and recorded, never a Gate A item; one 30-minute repair slot (section 6.6 #12) [NC]"),
    ("new", 2.5, "Graph lessons 28-31; NEW 200 Number of Islands [NC]"),
    ("new", 2.5, "Topological sort lesson; NEW 994 Rotting Oranges, 210 Course Schedule II [NC]"),
    ("new", 2.5, "Union-find built from scratch, NEW 684 Redundant Connection; Dijkstra, NEW 743 Network Delay Time [NC]"),
    ("new", 2.5, "DP lessons 32-33; NEW 70 Climbing Stairs, 62 Unique Paths [NC]"),
    ("new", 2.5, "Greedy, NEW 53 Maximum Subarray; Trie, NEW 208 Implement Trie [NC]"),
    ("new", 2.5, "Bit manipulation, NEW 136 Single Number (50 total, all 16 families) [NC]"),
    ("colds_b", None, "Colds only: due spaced re-solves, D90s included (section 6.6 #6) [NC]"),
    ("blind", 21.0, "Colds; blind mixed sets of solved problems, no pattern label, the last one just before Gate B (section 6.6 #7) [NC]"),
    ("gateB", 3.0, "Unseen set 2: four problems Om has never solved (1 Easy, 3 Medium) from any of the 20 families, no pattern label, one a day; a Gate B item, 3 of 4 inside the box (section 6.6 #12) [NC]"),
    ("new", 5.0, "NEW 133 Clone Graph, 417 Pacific Atlantic Water Flow, 198 House Robber [NC]"),
    ("new", 4.0, "NEW 322 Coin Change, 1143 Longest Common Subsequence (55 total); performance gate practice [NC]"),
]
DSA_TOTAL = 146.0

# ---------------- done rows W0-W3 ----------------
DONE = {
    0: [("Setup", 1.0, "Oct 1 procedure: evidence, gap diagnosis, change control, freeze")],
    1: [("Y2", 1.0, None), ("G1", 0.5, None), ("Proofs and weekly close", 0.5, "")],
    2: [("G1", 2.5, None), ("P1", 0.5, None), ("Proofs and weekly close", 0.5, "")],
    3: [("MC0", 1.25, None), ("MC1", 2.5, None), ("R1", 1.0, None), ("R1", 1.0, None), ("L1", 1.0, None), ("P1", 2.25, None), ("Proofs and weekly close", 0.5, "")],
}

# ---------------- lane queues ----------------
def parts(label, idx=None):
    ps = range(len(U[label]["parts"])) if idx is None else idx
    return [(label, i) for i in ps]


LANES = {
    "PY": parts("Y3", [0]) + parts("P1", [2]) + parts("Y7a") + parts("P1", [3]) + parts("D1") + parts("Y8a")
          + parts("Y3", [1, 2, 3, 4, 5]) + parts("P2") + parts("P3") + parts("P4") + parts("S5") + parts("Y3", [6, 7, 8, 9])
          # ---- 1b ----
          + parts("Y1") + parts("C1") + parts("S1", [1, 2]) + parts("AI1") + parts("Y4")
          + parts("O1") + parts("Y5") + parts("D2") + parts("S2") + parts("Y6") + parts("Y8b")
          + parts("S3") + parts("S4") + parts("Y7b") + parts("F1"),
    "GO": parts("G2") + parts("G3") + parts("G4") + parts("G5") + parts("G6") + parts("G7") + parts("A1")
          + parts("A2") + parts("A3") + parts("A4") + parts("A5") + parts("A6")
          + parts("OP1") + parts("OP2") + parts("OP3") + parts("OP4") + parts("OP5") + parts("OP6") + parts("OP7"),
    "K": parts("K1") + parts("K2") + parts("K3") + parts("K4") + parts("K5") + parts("K7a")
         + parts("K6a") + parts("CL1") + parts("CL2") + parts("CL3") + parts("CL4") + parts("K6b"),
    "KB": parts("K7b"),
    "L": parts("L1", [1, 2]) + parts("L2") + parts("L3") + parts("L4"),
    "H": parts("H1") + parts("H2") + parts("H3") + parts("H4") + parts("H5"),
    "CAR": parts("R3", [0]) + parts("R2", [0, 1, 2, 3, 4]) + parts("R1", [2]) + parts("R1", [3]) + parts("R2", [5])
           + parts("R3", [1]) + parts("R4") + parts("R3", [2]),
}
LANE_ORDER = ["CAR", "GO", "K", "KB", "L", "H", "PY"]   # PY last: it takes the remainder

# ---------------- week spec ----------------
from spec import SPEC, GATES, PHASE_END, CAMP, DSA_HOURS, NOTES

# ---------------- build ----------------
pos = {lane: [0, 0.0] for lane in LANES}           # (item index, hours used in that item)
part_started = set()
rows = OrderedDict()
used = defaultdict(float)
first, last = {}, {}
contact = defaultdict(set)                          # track -> weeks with contact
GAP_TRACK = {"G": "Go", "A": "Go", "K": "Kubernetes", "L": "LLD", "M": "LLD", "H": "HLD"}


def track_of(label):
    if label.startswith("OP"):
        return ["Go", "Kubernetes", "Operators"]
    if label.startswith("CL"):
        return ["Cloud"] + (["Kubernetes"] if label in ("CL3",) else [])
    if label == "AI1":
        return []
    if label in ("Mock",):
        return ["HLD"]
    if label == "MP" or label.startswith("MC") or label.startswith("L"):
        return ["LLD"]
    if label[0] in ("G", "A") and label[1].isdigit():
        return ["Go"]
    if label[0] == "K" and label[1].isdigit():
        return ["Kubernetes"]
    if label[0] == "H" and label[1].isdigit():
        return ["HLD"]
    return []


def pour(lane, hours, week, items):
    q = LANES[lane]
    while hours > EPS:
        i, h_used = pos[lane]
        if i >= len(q):
            if lane == "PY":
                raise SystemExit(f"W{week}: lane {lane} has no work left, {hours}h unplaced")
            return hours
        label, pi = q[i]
        ph, ptxt = U[label]["parts"][pi]
        # v3.8 (A3): a lane never starts a new part with under 30 minutes; the hours go to the PY lane instead,
        # and the PY lane leaves them open
        if (label, pi) not in part_started and h_used < EPS and hours < 0.5 - EPS and ph >= 0.5 - EPS:
            return hours   # the PY lane leaves these minutes open (warm-ups, setup)
        for dep in U[label]["deps"]:
            if dep in U and (used[dep] < total(dep) - EPS):
                if label not in first:
                    raise SystemExit(f"W{week}: {label} would start before {dep} is complete ({used[dep]}/{total(dep)})")
        take = min(hours, ph - h_used)
        cont = (label, pi) in part_started and h_used > EPS
        items.append((label, round(take, 4), ptxt + (" (continued)" if cont else "")))
        part_started.add((label, pi))
        used[label] += take
        hours -= take
        if abs(take - (ph - h_used)) < EPS:
            pos[lane] = [i + 1, 0.0]
        else:
            pos[lane] = [i, h_used + take]


dsa_pos = [0, 0.0]
dsa_started = set()


def dsa_pour(hours, week, items, phase):
    while hours > EPS:
        i, hu = dsa_pos
        kind, h, txt = DSA_SEG[i]
        if kind in ("colds_a", "colds_b"):
            # flexible pool: consume everything asked unless the next fixed segment must start
            items.append(("DSA", round(hours, 4), txt + (" (continued)" if i in dsa_started else "")))
            dsa_started.add(i)
            hours = 0
            return
        if kind == "gateA" and phase != "gateA":
            raise SystemExit(f"W{week}: DSA reached unseen set 1 outside the Gate A week")
        take = min(hours, h - hu)
        cont = i in dsa_started and hu > EPS
        items.append(("DSA", round(take, 4), txt + (" (continued)" if cont else "")))
        dsa_started.add(i)
        hours -= take
        if abs(take - (h - hu)) < EPS:
            dsa_pos[0], dsa_pos[1] = i + 1, 0.0
        else:
            dsa_pos[1] = hu + take


def skip_pool():
    if DSA_SEG[dsa_pos[0]][0] in ("colds_a", "colds_b"):
        dsa_pos[0], dsa_pos[1] = dsa_pos[0] + 1, 0.0


mp_count = 0
history = {t: [] for t in ["Go", "Kubernetes", "LLD", "HLD", "Operators", "Cloud"]}
PHASE_UNIT = {"Go": "G7", "Kubernetes": "K5", "LLD": "L3", "HLD": "H2", "Operators": "OP5", "Cloud": "CL2"}
RR_TEXT = {
    "Go": "Go: from a blank file, from memory, rewrite one closed Go kata and its tests as that unit wrote them, and add one changed case [section 6.12]",
    "Kubernetes": "Kubernetes: on kind, rebuild one closed lab from memory (apply, break, fix) and paste the `kubectl` output [section 6.12]",
    "HLD": "HLD: redraw one building block or practice design from memory, out loud, with one failure mode and the option you rejected [section 6.12]",
    "LLD": "LLD: a 40-minute small problem from a blank file with your own asserts [section 6.12]",
    "Operators": "Operators: re-implement one reconcile step from memory and run it under envtest [section 6.12]",
    "Cloud": "Cloud: write a small Terraform module from memory and run `terraform plan`; no apply [section 6.12]",
}
gate_week = {g: w for w, g in GATES.items()}
rr_count = 0

import spec as _sp
LAST = getattr(_sp, "LAST", max(SPEC))
for n in range(0, LAST + 1):
    items = []
    if n in DONE:
        for d in DSA_DONE.get(n, []):
            items.append(("DSA", d[0], d[1]))
        for lab, h, txt in DONE[n]:
            if txt is None:
                # find the part text for this label (first part not yet fully used)
                acc = used[lab]
                for ph, ptxt in U[lab]["parts"]:
                    if acc < ph - EPS:
                        txt = ptxt
                        break
                    acc -= ph
                for i_, (ph, ptxt) in enumerate(U[lab]["parts"]):
                    pass
            items.append((lab, h, txt))
            if lab in U:
                used[lab] += h
        # mark started parts and lane positions for done work
        rows[n] = items
        for lab, h, _ in items:
            if lab in U:
                first.setdefault(lab, n); last[lab] = n
                for t in track_of(lab):
                    history[t].append(n)
        continue
    s = SPEC[n]
    phase = s.get("phase")
    c = cap(n, phase)
    # DSA
    dh = s.get("DSA", DSA_HOURS(n, phase))
    if s.get("dsa_skip_pool"):
        skip_pool()
    dsa_pour(dh, n, items, s.get("dsa_phase", phase))
    for xh, xt in s.get("dsa_extra", []):
        items.append(("DSA", xh, xt))
    if s.get("dsa_after"):
        skip_pool()
    # fixed
    proofs = 0.5 if n in LIGHT else 0.75
    camp = CAMP(n, phase)
    if "camp" in s:
        camp = s["camp"]
    fixed = [("Proofs and weekly close", proofs, "")]
    if camp > EPS:
        fixed.append(("Campaign", camp, s.get("camp_text", "Applications, calibration interviews and referral messages; an unused hour moves to the next unit in the row (section 8)")))
    for g in s.get("gate", []):
        fixed.append(g)
    for mc in s.get("MC", []):
        ph, ptxt = U[mc]["parts"][0]
        fixed.append((mc, ph, ptxt)); used[mc] += ph
    if "Mock" in s:
        mi = s["Mock"]
        ph, ptxt = U["H6"]["parts"][mi]
        fixed.append(("Mock", ph, ptxt)); used["H6"] += ph
    if s.get("MP"):
        txt = MP_TEXT[mp_count] if mp_count < len(MP_TEXT) else MP_LOOP
        mp_count += 1
        fixed.append(("MP", 1.0, txt))
    for extra in s.get("extra", []):
        lab, h, pi = extra
        ph, ptxt = U[lab]["parts"][pi]
        fixed.append((lab, h, ptxt)); used[lab] += h
    lane_items = []
    budget = c - sum(x[1] for x in items) - sum(x[1] for x in fixed)
    for lane in LANE_ORDER:
        if lane == "PY":
            continue
        h = s.get(lane, 0.0)
        if h > EPS:
            left = pour(lane, h, n, lane_items) or 0.0
            budget -= (h - left)
    # contacts so far this week
    this = set()
    for lab, _, _ in fixed + lane_items:
        for t in track_of(lab):
            this.add(t)
    for t in s.get("contacts", []):
        this.add(t)
    # gap rule: insert RR where the idle run would break the limit
    rrs = []
    for t, hist in history.items():
        if not hist or t in this:
            continue
        if n > gate_week["C"]:
            continue
        idle = n - hist[-1] - 1          # idle weeks before this one
        pu = PHASE_UNIT[t]
        learning = (pu not in last) or (last[pu] >= n) or (used[pu] < total(pu) - EPS)
        limit = 1 if learning else 3
        if idle + 1 > limit:             # this week would also be idle
            rrs.append(("RR", 0.75, RR_TEXT[t]))
            this.add(t)
    rr_count += len(rrs)
    budget -= sum(x[1] for x in rrs)
    if budget < -EPS:
        raise SystemExit(f"W{n}: over cap by {-budget}h; items {[(x[0], x[1]) for x in items + fixed + lane_items + rrs]}")
    py_items = []
    if s.get("no_fill"):
        i, hu = pos["PY"]
        q = LANES["PY"]
        rem = sum(U[l]["parts"][p][0] for l, p in q[i:]) - hu
        if rem > EPS:
            pour("PY", min(rem, budget), n, py_items)
    elif budget > EPS:
        if s.get("PY_max") is not None and budget > s["PY_max"] + EPS:
            raise SystemExit(f"W{n}: PY remainder {budget} exceeds PY_max")
        pour("PY", budget, n, py_items)
    week_items = items + lane_items + py_items + rrs + fixed
    rows[n] = week_items
    for lab, h, _ in week_items:
        if lab in U:
            first.setdefault(lab, n); last[lab] = n
        if lab == "Mock":
            first.setdefault("H6", n); last["H6"] = n
        for t in track_of(lab):
            if n not in history[t]:
                history[t].append(n)
    for lab, _, _ in rrs:
        pass
    for t in this:
        if n not in history[t]:
            history[t].append(n)

# ---------------- report ----------------
if __name__ == "__main__" and "--report" in sys.argv:
    for n, its in rows.items():
        s = sum(h for _, h, _ in its)
        labs = " ".join(f"{l}:{h:g}" for l, h, _ in its)
        print(f"W{n:<2} {dates(n):<14} {s:5.2f} | {labs}")
    print()
    for lane, (i, hu) in pos.items():
        q = LANES[lane]
        rem = sum(U[l]["parts"][p][0] for l, p in q[i:]) - hu
        print(f"lane {lane}: at {q[i] if i < len(q) else 'END'} remaining {rem:g}h")
    print("DSA pos", dsa_pos, DSA_SEG[dsa_pos[0]][0] if dsa_pos[0] < len(DSA_SEG) else "END")
    for lab in U:
        if abs(used[lab] - total(lab)) > EPS:
            print(f"UNIT {lab}: used {used[lab]:g} of {total(lab):g}")
    print("RR reps:", rr_count, "MP sessions:", mp_count)
    for t, hist in history.items():
        print(t, hist)

if __name__ == "__main__" and "--totals" in sys.argv:
    tot = defaultdict(float)
    for n, its in rows.items():
        for l, h, t in its:
            tot[l] += h
    print({k: round(v, 2) for k, v in sorted(tot.items())})
    print("grand", sum(tot.values()))
    for n, its in rows.items():
        for l, h, t in its:
            if l == "DSA":
                print(f"W{n} DSA {h:g}: {t[:70]}")

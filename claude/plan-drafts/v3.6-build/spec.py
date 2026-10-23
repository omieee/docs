"""Week spec for v3.6. PY takes whatever is left in the week."""
LIGHT = {5, 12, 13, 56, 64, 65}
GATES = {30: "A", 68: "B", 72: "C"}
PHASE_END = {"1a": 30, "1b": 68, "1c": 72}
NOTES = {}
SPEC = {}


def phase_of(n):
    return "1a" if n <= PHASE_END["1a"] else ("1b" if n <= PHASE_END["1b"] else "1c")


def DSA_HOURS(n, phase):
    p = phase_of(n)
    if p == "1a":
        return 1.5 if n in LIGHT else 2.25
    if p == "1b":
        if n in LIGHT:
            return 1.0
        return 1.5 if (31 <= n <= 41 or n == 57) else 1.75
    return 2.25


def CAMP(n, phase):
    p = phase_of(n)
    if n == 4:
        return 0.0
    if p == "1a":
        return 0.5 if n in LIGHT else 0.75
    if p == "1b":
        return 0.5 if n in LIGHT else 1.0
    return 3.0


def w(n, **kw):
    SPEC.setdefault(n, {}).update(kw)


for n in range(4, PHASE_END["1c"] + 1):
    w(n, phase=phase_of(n))

# ---------------- 1a: W4-W30 ----------------
w(4, MP=True, CAR=1.5, K=1.5, L=1.5)
w(5, GO=2.0, K=0.5)
w(6, MP=True, camp=2.0, camp_text="JD harvest, part 1: 20 or more live postings classified with the section 8 fields; lane-size check", GO=1.0, K=1.5, CAR=1.0)
w(7, MP=True, camp=2.0, camp_text="JD harvest, part 2: lane counts and the lane decision; referral map; Nov 15 re-forecast inputs", GO=1.5, K=1.0, L=1.5)
w(8, MP=True, GO=1.5, K=1.5, L=1.0, CAR=1.0)
w(9, MP=True, GO=1.5, K=1.5, L=1.5)
w(10, MP=True, GO=1.5, K=1.5, L=1.0, CAR=1.0)
w(11, MP=True, GO=1.5, K=1.5, L=1.5)
w(12, GO=1.0, K=1.0, H=1.0)
w(13, GO=1.0, L=1.0, H=1.0)
w(14, MP=True, GO=1.5, K=1.5, L=1.5, H=1.0)
w(15, GO=1.5, K=1.5, L=1.5, H=1.0, CAR=1.0)
w(16, MP=True, GO=1.5, K=1.5, L=1.5, H=1.0)
w(17, GO=1.5, K=1.5, L=1.5, H=1.0, CAR=1.0)
w(18, MC=["MC2"], GO=1.5, K=1.0, H=1.5)
w(19, MP=True, GO=1.75, K=1.5, H=1.5, CAR=1.0)
w(20, GO=1.75, K=1.5, H=1.5)
w(21, MP=True, GO=1.75, K=1.5, H=1.5, CAR=1.0)
w(22, GO=1.75, K=1.5, H=1.5)
w(23, MP=True, GO=1.5, K=1.0, H=1.5, CAR=1.0)
w(24, MC=["MC3"], GO=1.5, K=1.0, H=1.5)
w(25, MP=True, GO=1.5, K=0.5, H=0.5, CAR=1.0)
w(26, GO=1.5, Mock=0)
w(27, MP=True)
w(28, CAR=1.0)
w(29, MP=True)
w(30, contacts=["Go", "Kubernetes", "HLD"], DSA=3.5, dsa_skip_pool=True, dsa_phase="gateA", gate=[("Gate", 4.0, "Gate A: Go practical, Checklist B fundamentals half, K8s audit 10/15, DSA 40/24, reps 1-3 scored, Mock 1 scored")], extra=[("S1", 0.5, 0)])

# ---------------- 1b: W31-W66 ----------------
GB = 68
MC_WEEKS = {33: "MC4", 40: "MC5", 47: "MC6", 57: "MC7"}
MOCK_WEEKS = {49: 1, 59: 2}
KB_WEEKS = {35: 1.0, 38: 0.75, 41: 0.75, 44: 0.75, 49: 0.75}
L_WEEKS = {36: 1.0, 37: 1.0, 38: 1.0}
CAR_1B = {31: 2.0, 42: 1.0, 45: 1.25, 46: 1.25, 52: 1.0, 59: 1.5, 60: 1.5}
CL3_WEEKS = {51: 3.0, 52: 3.0, 53: 0.0, 54: 3.0, 55: 3.0}
mp_flip = True
for n in range(31, GB):
    light = n in LIGHT
    kw = {}
    if light:
        kw.update(GO=1.5, H=0.5)
    else:
        kw.update(GO=2.5 if n >= 58 else 2.0, K=1.0, H=1.5)
    if n in CL3_WEEKS:
        kw["K"] = CL3_WEEKS[n]
    if n in MC_WEEKS:
        kw["MC"] = [MC_WEEKS[n]]
    if n in MOCK_WEEKS:
        kw["Mock"] = MOCK_WEEKS[n]
        kw["H"] = 0.0
    if n in KB_WEEKS:
        kw["KB"] = KB_WEEKS[n]
    if n in L_WEEKS:
        kw["L"] = L_WEEKS[n]
    if n in CAR_1B:
        kw["CAR"] = CAR_1B[n]
    if not light and n not in MC_WEEKS and n not in MOCK_WEEKS:
        if mp_flip:
            kw["MP"] = True
        mp_flip = not mp_flip
    w(n, **kw)
w(58, camp=2.0, camp_text="JD harvest refresh with the same section 8 fields, for resume v2")
w(GB, contacts=["Go", "Kubernetes", "HLD", "LLD", "Operators", "Cloud"], DSA=3.0, dsa_skip_pool=True,
  gate=[("Gate", 5.0, "Gate B: checklists A to F; K8s audit plus live challenge; craft demo; controller on kind with envtest green; PRCP on AWS from the README; 3 mocks; last 2 reps pass; latest blind set 80%; unseen set 2 at 3 of 4; stories")])

# ---------------- 1c: W69-W72 ----------------
w(69, no_fill=True, CAR=2.0)
w(70, no_fill=True, CAR=2.0, MC=["MC8"])
w(71, no_fill=True, Mock=3)
w(72, no_fill=True, camp=2.5, contacts=["Go", "Kubernetes", "HLD", "LLD", "Operators", "Cloud"],
  gate=[("Gate", 2.5, "Re-run every checklist (A to F) cold [section 7]"),
        ("Gate", 4.0, "Gate C: DSA 8 of 10 cold, 8 reps, 4 mocks, 5 stories, both deep dives")])
LAST = 72
w(31, K=0.0)
w(68, camp=0.25, camp_text="Gate week: only replies to live processes")
w(69, H=1.0)

w(57, dsa_skip_pool=True)
w(68, no_fill=True)
w(40, DSA=1.75)

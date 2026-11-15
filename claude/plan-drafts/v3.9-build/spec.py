"""Week spec for v3.9 (v3.8 re-forecast on Nov 15 2026). v3.8's content weeks keep their order; K1_INS weeks are added before Gate A
and K2_INS before the two Gate B repair weeks, because v3.9 adds hours (warm-ups, Go at the measured pace, the finalizer fix, the
distributed-systems proof). Light weeks stay on their calendar dates. PY takes whatever is left in the week."""
import os
K1_INS = int(os.environ.get("K1_INS", "3"))
K2_INS = int(os.environ.get("K2_INS", "6"))
LIGHT = {5, 12, 13, 56, 64, 65}
GA = 30 + K1_INS
GB = 70 + K1_INS + K2_INS
GC = GB + 4
GATES = {GA: "A", GB: "B", GC: "C"}
PHASE_END = {"1a": GA, "1b": GB, "1c": GC}
NOTES = {}
SPEC = {}


def phase_of(n):
    return "1a" if n <= PHASE_END["1a"] else ("1b" if n <= PHASE_END["1b"] else "1c")


def x_of(n):
    """v3.8 content week for a v3.9 1b week (None for an added fill week)."""
    x = n - K1_INS
    if x <= 67:
        return x
    x2 = n - K1_INS - K2_INS
    return x2 if x2 >= 68 else None


def DSA_HOURS(n, phase):
    p = phase_of(n)
    if p == "1a":
        return 1.5 if n in LIGHT else 2.25
    if p == "1b":
        if n in LIGHT:
            return 1.0
        x = x_of(n)
        return 1.5 if (x is not None and (31 <= x <= 41 or x == 57)) else 1.75
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

# ---------------- 1a: W4-W29 as v3.8 (W4-W6 are done rows in gen.py) ----------------
w(4, MP=True, CAR=1.5, K=1.5, L=1.5)
w(5, GO=2.0, K=0.5)
w(6, MP=True, camp=2.0, camp_text="JD harvest, part 1: 20 or more live postings classified with the section 8 fields; lane-size check", GO=1.0, K=1.5, CAR=1.0)
w(7, MP=True, camp=2.5, camp_text="JD harvest, part 2 (a study of what employers want at Om's level, not a job search; Om, Oct 28): lane counts and the lane decision; referral map; Om reads the international slice and marks his international top 5 (v3.7, +0.5h)", GO=1.5, K=1.0, L=1.5, CAR=1.25)  # v3.9: R3 in Om's leave week (Om, Nov 1)
w(8, MP=True, GO=1.5, K=1.5, L=1.25, CAR=1.0)
w(9, MP=True, GO=1.5, K=1.5, L=1.75)
w(10, MP=True, GO=1.5, K=1.5, L=1.25, CAR=1.0)
w(11, MP=True, GO=1.5, K=1.5, L=1.75)
w(12, GO=1.25, K=1.0, H=1.0)
w(13, GO=1.25, L=1.25, H=1.0)
w(14, MP=True, GO=1.75, K=1.5, L=1.5, H=1.0)
w(15, GO=1.75, K=1.5, L=1.5, H=1.0, CAR=1.0)
w(16, MP=True, GO=1.75, K=1.5, L=1.5, H=1.0)
w(17, GO=1.75, K=1.5, L=1.75, H=1.0, CAR=1.0)  # v3.9: L3's last 0.25h before MC2 (Claude's Oct 30 review, point 4)
w(18, MC=["MC2"], GO=1.75, K=1.0, H=1.5)
w(19, MP=True, GO=2, K=1.5, H=1.5, CAR=1.0)
w(20, GO=2, K=1.5, H=1.5)
w(21, MP=True, GO=2, K=1.5, H=1.5, CAR=1.0)
w(22, GO=2, K=1.5, H=1.5)
w(23, MP=True, GO=1.75, K=1.0, H=1.5, CAR=1.0)
w(24, MC=["MC3"], GO=1.75, K=1.0, H=1.5)
w(25, MP=True, GO=1.75, K=0.5, H=0.5, CAR=1.0)
w(26, GO=1.5, K=1.0, Mock=0)  # v3.9: K=1 in W26-W27 so K7a closes before Gate A
w(27, MP=True, K=1.0)
w(28, K=1.0)   # v3.9: the Naukri hour moves to W31, about 15 days before Gate A
w(29, MP=True)
# v3.9: weeks added before Gate A for the hours v3.9 adds in 1a (warm-ups from W7, Go at the measured pace, the W4-W6 carry-over)
for i in range(K1_INS):
    w(30 + i, MP=(i % 2 == 0), GO=1.0, H=0.5)   # mostly Python and Postgres: P4 is a Gate A item
w(GA - 2, extra=[("R1", 1.0, 2)])
w(GA - 1, CAR=0.25)                # v3.9: the two older stories are written before Gate A   # v3.9: Naukri is date-bound (about 15 days before Gate A), so it is placed, not poured
w(GA, contacts=["Go", "Kubernetes", "HLD"], DSA=3.5, dsa_skip_pool=True, dsa_phase="gateA", gate=[("Gate", 4.0, "Gate A: Go practical, Checklist B fundamentals half, K8s audit 10/15, DSA 40/24, reps 1-3 scored, Mock 1 scored")], extra=[("S1", 0.5, 0)])

# ---------------- 1b ----------------
MC_WEEKS = {33: "MC4", 40: "MC5", 47: "MC6", 57: "MC7"}
MOCK_WEEKS = {49: 1, 59: 2}
KB_WEEKS = {36: 1.0, 38: 0.75, 41: 0.75, 44: 0.75, 49: 0.75}
L_WEEKS = {36: 1.0, 37: 1.0, 38: 1.25}
CAR_1B = {31: 2.0, 42: 1.0, 45: 1.25, 46: 1.25, 52: 1.0, 59: 1.5, 60: 1.5}
CL3_X = [51, 52, 54, 55]           # v3.8's four 3-hour CL3 sessions (moved below, after K6b, by CL3_WEEKS)
GO_FILL = float(os.environ.get("GO_FILL", "3.0"))
CL3_WEEKS = {57: 3.0, 58: 3.0, 59: 3.0, 66: 3.0}   # v3.9: four atomic 3-hour CL3 sessions, after K6b (ChatGPT F2)
K_HOLD = {55, 56, 60, 61, 62, 63}
K6B_WEEK = {54: 2.0}                             # K6b right after CL2, before any AWS session                       # no 1-hour CL3 slivers between sessions
mp_flip = True
pending = []                        # heavy specials bumped off a light calendar week
for n in range(GA + 1, GB):
    light = n in LIGHT
    x = x_of(n)
    kw = {}
    if light:
        kw.update(GO=1.5, H=0.5)
    else:
        kw.update(GO=(GO_FILL if x is None else (2.5 if x >= 58 else 2.0)), K=1.0, H=1.5)
    spec_mc = MC_WEEKS.get(x) if x else None
    spec_mock = MOCK_WEEKS.get(x) if x else None
    if light and (spec_mc or spec_mock is not None):
        pending.append((spec_mc, spec_mock)); spec_mc, spec_mock = None, None
    elif not light and pending and not spec_mc and spec_mock is None:
        spec_mc, spec_mock = pending.pop(0)
    if n in CL3_WEEKS and not light:
        kw["K"] = CL3_WEEKS[n]
    if n in K_HOLD and not light:
        kw["K"] = 0.0
    if n in K6B_WEEK and not light:
        kw["K"] = K6B_WEEK[n]
    if spec_mc:
        kw["MC"] = [spec_mc]
    if spec_mock is not None:
        kw["Mock"] = spec_mock
        kw["H"] = 0.0
    if x in KB_WEEKS:
        kw["KB"] = KB_WEEKS[x]
    if x in L_WEEKS:
        kw["L"] = L_WEEKS[x]
    if x in CAR_1B:
        kw["CAR"] = CAR_1B[x]
    if not light and not spec_mc and spec_mock is None:
        if mp_flip:
            kw["MP"] = True
        mp_flip = not mp_flip
    w(n, **kw)
assert not pending, pending
w(58 + K1_INS, camp=2.5, camp_text="JD harvest refresh with the same section 8 fields, India and international slices, for resume v2 and the Gate B region decision; Om re-marks both top 5 lists (v3.7, +0.5h)")
w(32 + K1_INS, dsa_extra=[(2.0, "Human live-coding mock (v3.7, section 6.6 #13; v3.8: moved from W61 to just after Gate A, before valuable loops): one problem Om has not seen, with a stranger on a peer mock platform, aloud, in English, 1 hour with turns, plus booking and a 30-minute review; scored on the DSA proof rules [PEER]")])
w(GB, contacts=["Go", "Kubernetes", "HLD", "LLD", "Operators", "Cloud"], DSA=3.0, dsa_skip_pool=True,
  gate=[("Gate", 5.0, "Gate B: checklists A to F; K8s audit plus live challenge; craft demo; controller on kind with envtest green; PRCP on AWS from the README; 3 mocks; human live-coding mock scored; last 2 reps pass; latest blind set 80%; unseen set 2 at 3 of 4; stories; region decision recorded")])

# ---------------- 1c ----------------
w(GB + 1, no_fill=True, CAR=2.25)
w(GB + 2, no_fill=True, CAR=2.0, MC=["MC8"])
w(GB + 3, no_fill=True, Mock=3, CAR=1.25)
w(GC, no_fill=True, camp=2.5, contacts=["Go", "Kubernetes", "HLD", "LLD", "Operators", "Cloud"],
  gate=[("Gate", 2.5, "Re-run every checklist (A to F) cold [section 7]"),
        ("Gate", 4.0, "Gate C: DSA 8 of 10 cold, 8 reps, 4 mocks, 5 stories, both deep dives; the four-line readiness record (section 4)")])
LAST = GC
w(GA + 1, K=0.0)
w(GB, camp=0.25, camp_text="Gate week: only replies to live processes")
w(GB + 1, H=1.0)

w(57 + K1_INS, dsa_skip_pool=True)
w(GB, no_fill=True)
# v3.7 and v3.8 each added a week before Gate B (Gate B repairs); v3.9's added weeks sit just before them
w(GB - 2, no_fill=True, MP=False)
w(GB - 1, no_fill=True, MP=False)
w(40 + K1_INS, DSA=1.75)

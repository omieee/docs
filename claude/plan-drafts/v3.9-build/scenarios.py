"""v3.9 r2: short weeks and available-time scenarios, from the same build gen.py makes (Claude, Nov 15 2026).

python3 scenarios.py runsheet   prints the W7-W12 run sheet for section 14 (markdown)
python3 scenarios.py dates      prints fixed-work illustrations: the gate dates if only 14, 12, 9 or 6 hours of plan work get done
                                each week from W7, without and with the weekly close repeated in the extra calendar weeks

The run sheet replays each week on its own, at 9 and at 6 hours, with one fixed order (section 14, "Short weeks"):
  1. dated DSA reviews (never skipped, section 6.6 #9);
  2. the weekly close (20 minutes), the proof of each unit that closes that week (15 minutes each) and the
     warm-ups of the sessions actually held (5 minutes a desk session, about one session per 2 hours);
  3. a watched track that would break its idle limit if it skipped this week (section 6.12);
  4. the last slice of each unit that closes this week;
  5. everything else: DSA new work, then PRCP's lane (it carries the chain to Gate A), Go, Kubernetes, LLD, HLD,
     stories, the practice session, the campaign.
Work that does not fit moves to the next week and goes first there. Nothing is cut (section 5).
"""
import datetime
import math
import sys

import gen
from gen import rows, U, LIGHT, total, sunday, dates
from spec import PHASE_END

EPS = 1e-9
WATCH_FOUNDATION = {"Go": "G7", "Kubernetes": "K5", "LLD": "L3", "HLD": "H2", "Operators": "OP5", "Cloud": "CL2"}


def track(lab):
    return gen.track_of(lab)


def close_weeks():
    cw = {}
    for lab in U:
        ws = [n for n, its in rows.items() for l, h, t in its if l == lab]
        if ws and abs(gen.used[lab] - total(lab)) < EPS:
            cw[lab] = max(ws)
    return cw


CLOSE = close_weeks()


def last_contact_before(t, n):
    ws = [m for m, its in rows.items() if m < n and any(t in track(l) for l, _, _ in its)]
    return max(ws) if ws else None


def limit(t, n):
    pu = WATCH_FOUNDATION[t]
    closed = pu in CLOSE and CLOSE[pu] < n
    return 3 if closed else 1


def q(h):
    """round up to a quarter hour"""
    return math.ceil(h * 4 - EPS) / 4


def replay(n, cap):
    its = [(l, h, t or "") for l, h, t in rows[n]]
    closing = [l for l in CLOSE if CLOSE[l] == n and n >= 7]
    sessions = max(1, round(cap / 2))
    keep, order = [], []
    # 1. dated reviews
    for l, h, t in its:
        if l == "DSA" and t.startswith("Dated reviews"):
            keep.append((l, h, t))
    # 2. close, unit proofs, warm-ups
    proofs = q((20 + 15 * len(closing) + 5 * sessions) / 60)
    row_proofs = sum(h for l, h, _ in its if l == "Proofs and weekly close")
    proofs = min(proofs, row_proofs)
    keep.append(("Proofs and weekly close", proofs, ""))
    rest_proofs = row_proofs - proofs
    # 3. a watched track at its idle limit
    protected = set()
    for t in WATCH_FOUNDATION:
        lc = last_contact_before(t, n)
        if lc is None:
            continue
        if n - lc - 1 + 1 > limit(t, n):          # skipping this week would break the limit
            for l, h, txt in its:
                if t in track(l) and l not in ("RR",):
                    protected.add((l, txt)); break
            else:
                for l, h, txt in its:
                    if l == "RR" and txt.startswith(t):
                        protected.add((l, txt)); break
    # 4. last slices of closing units, 5. the rest in row order
    others = [(l, h, t) for l, h, t in its if not (l == "DSA" and t.startswith("Dated reviews")) and l != "Proofs and weekly close"]
    prio = lambda it: (0 if (it[0], it[2]) in protected else (1 if it[0] in closing else 2))
    others.sort(key=lambda it: (prio(it), rest_rank(it[0])))
    used = sum(h for _, h, _ in keep)
    moved = []
    for l, h, t in others:
        room = cap - used
        cont = "(continued)" in t or l == "DSA"
        whole = l in ("MP", "RR", "Mock", "Gate") or (l.startswith("MC") and l[2:].isdigit())   # one sitting each
        if room >= h - EPS:
            keep.append((l, h, t)); used += h
        elif not whole and room >= 0.25 - EPS and (cont or room >= 0.5 - EPS):   # a split keeps the 30-minute start rule
            keep.append((l, room, t)); moved.append((l, h - room, t)); used += room
        else:
            moved.append((l, h, t))
    if rest_proofs > EPS:
        moved.append(("Proofs and weekly close", rest_proofs, "warm-ups and proofs of the moved work"))
    return keep, moved, protected, closing


def rest_rank(lab):
    """5. the rest: DSA first (rule 8), then PRCP's lane, which carries the chain to Gate A (P1, then D1, then K3;
    P2 to P4), then Go, Kubernetes, LLD, HLD and stories in the order of Om's priority list (section 5), then the
    practice session, then the campaign"""
    if lab == "DSA":
        return 0
    if lab[0] in "PDYECS" and lab[1:2].isdigit() or lab in ("Y7a", "Y7b", "Y8a", "Y8b", "AI1", "F1", "O1"):
        return 1
    if lab[0] in "GA" and lab[1:2].isdigit() or lab == "DS1" or lab.startswith("OP"):
        return 2
    if lab[0] == "K" or lab.startswith("CL"):
        return 3
    if lab[0] == "L" and lab[1:2].isdigit():
        return 4
    if lab[0] == "H" and lab[1:2].isdigit():
        return 5
    if lab[0] == "R" and lab[1:2].isdigit():
        return 6
    if lab == "RR":
        return 7
    if lab == "MP" or (lab.startswith("MC") and lab[2:].isdigit()) or lab == "Mock":
        return 8
    return 9


ORDER = {"DSA": 0, "RR": 50, "MP": 51, "Mock": 53, "Campaign": 60, "Gate": 70}


def gen_order(it):
    lab = it[0]
    if lab.startswith("MC") and lab[2:].isdigit():
        return 52
    return ORDER.get(lab, 10)


def name(l, t):
    if l == "DSA":
        return "DSA new work" if not t.startswith("Dated") else "dated reviews"
    if l == "Proofs and weekly close":
        return "warm-ups and proofs that go with it"
    if l == "Campaign":
        return "harvest part 1" if "part 1" in t else ("harvest part 2" if "part 2" in t else "campaign")
    if l == "MP":
        return "MP " + t.split(":")[0].replace("Machine coding practice ", "") if t.startswith("Machine coding practice ") and t[24:25].isdigit() else "MP"
    return l


def fmt(h):
    return f"{h:g}h"


def summarise(moved):
    agg = {}
    for l, h, t in moved:
        k = name(l, t)
        agg[k] = agg.get(k, 0) + h
    return ", ".join(f"{k} {fmt(v)}" for k, v in agg.items()) or "nothing"


# The first block and the proof of each week, by hand; checked against the row below so the text cannot drift.
HAND = {
    7: ("Mon Nov 16, desk: 704 D28 cold (10-minute box); then the Go warm-up and step C, `go-notes.md` and Learning Go chapter 2's exercises typed and run (30 minutes); 74 D28 cold in its own later slot the same day. Read the 875 note at bedside before Wednesday",
        "704 and 74 D28 asserts green in `dsa-python`; the 875 fresh question scored; `go-notes.md` and the chapter 2 exercises in `learning-go-sandbox`; the kube-system Pod lines and the kubelet line in `k8s-notes.md`, then K1's unit proof; the MP3 commit; Om's marks in the harvest sheet",
        ["G2", "K1", "MP", "Campaign"]),
    8: ("Mon Nov 23: the next sorting lesson (DSA first); then Go step E, the second Learn Go with Tests sitting",
        "875 D28, 206 D90 and 21 D90 asserts green (Thu to Sat); L1 closed with its cold explanation; the Environment repository started with a test on `prcp_test`; story drafts started; the lane decision and the three claim lines written at the Nov 29 close",
        ["L1", "P1", "R2", "Campaign"]),
    9: ("Mon Nov 30: recursion lesson 8 (DSA first); then Go step F, the Go module in PRCP's `agent/` folder with the `append` test",
        "NEW 226 and 104 with tests from the problem statements; step G, the shared-backing-array test explained cold, so the slices part is done; the Environment repository done and the Probe repository started; at the Dec 6 close, the re-forecast from W7-W9's three numbers (section 5)",
        ["G2", "P1", "K2"]),
    10: ("First desk block after the leave (count the office days first): the queue lesson (DSA first); then Boot.dev chapter 8, Loops",
         "The Probe repository done with its foreign-key test; the ProbeResult repository started; the two story drafts written except a last 15-minute pass in W15; L2's SRP or OCP fix in PRCP, tests green; the MP6 commit",
         ["G2", "P1", "R2", "L2"]),
    11: ("The K2 drill on kind, 10 tasks, no notes, so K2 closes this week",
         "K2 closed: 8 of 10 drill tasks and the apply chain at 7/10; the loops part's `strings.Builder` report test in `agent/`; the `002` link table applied in CI and in both local databases",
         ["K2", "G2", "P1"]),
    12: ("Mon Dec 21: 141 D90 cold (10-minute box); then P1's last slice, the decision and its links saved in one transaction",
         "P1 closed: tests green on a fresh clone, a save with a link to a missing result leaves nothing behind, the P1 interview; 141, 19 and 143 D90 asserts green; H1's first full mock watched",
         ["P1", "H1"]),
}


def runsheet():
    out = ["| Week | First block | What proves the week worked (the full row done) | If only 9 hours: moves to the next week | If only 6 hours: moves to the next week |", "| --- | --- | --- | --- | --- |"]
    for n in range(7, 13):
        cap = 7 if n in LIGHT else 12
        row_h = sum(h for _, h, _ in rows[n])
        labs = {l for l, _, _ in rows[n]}
        first, proof, must = HAND[n]
        for m in must:
            assert m in labs, (n, m, labs)
        cells = []
        for c in (9, 6):
            c_ = min(c, cap)
            keep, moved, protected, closing = replay(n, c_)
            mh = sum(h for _, h, _ in moved)
            kh = sum(h for _, h, _ in keep)
            assert abs(kh + mh - row_h) < EPS and kh <= c_ + EPS, (n, c, kh, mh, row_h)   # allocations sum, the week fits
            open_ = c_ - kh
            cells.append((f"{fmt(mh)}: {summarise(moved)}" if mh > EPS else "0h: nothing moves") + (f" ({fmt(open_)} left open)" if open_ > EPS else ""))
        out.append(f"| W{n} ({dates(n)}, {fmt(row_h)} row) | {first} | {proof} | {cells[0]} | {cells[1]} |")
    return "\n".join(out)


# ---------------- available-time scenarios ----------------
def week_of(d):
    return (d - datetime.date(2026, 10, 5)).days // 7 + 1


LIGHT_CAL = set(LIGHT) | {week_of(datetime.date(2028, 10, 17)), week_of(datetime.date(2028, 12, 25)), week_of(datetime.date(2029, 1, 1)),
                          week_of(datetime.date(2029, 11, 5)), week_of(datetime.date(2029, 12, 25)), week_of(datetime.date(2030, 1, 1))}


def scenario(rate, start=7, close_h=0.0):
    """close_h > 0 (v3.9 final, ChatGPT's 16:22 finding 2): every calendar week also spends close_h on its weekly close,
    so the extra weeks a lower rate needs carry their own closes; the map's own weeks already hold theirs."""
    need = {}
    acc = 0.0
    for n in sorted(rows):
        if n < start:
            continue
        acc += (7.0 if n in LIGHT else 12.0) - close_h     # each map week's full time, open hours included, less its close
        for g, gw in (("A", PHASE_END["1a"]), ("B", PHASE_END["1b"]), ("C", PHASE_END["1c"])):
            if n == gw:
                need[g] = acc
    res, done, k = {}, 0.0, start
    while len(res) < 3:
        done += (min(rate, 7.0) if k in LIGHT_CAL else rate) - close_h
        for g in ("A", "B", "C"):
            if g not in res and done >= need[g] - EPS:
                s = sunday(k)
                res[g] = f"{s.strftime('%b')} {s.day} {s.year}"
        k += 1
    return res, need


if __name__ == "__main__":
    if sys.argv[1:] == ["runsheet"]:
        print(runsheet())
    elif sys.argv[1:] == ["dates"]:
        for r in (14, 12, 9, 6):
            res, need = scenario(r)
            res2, _ = scenario(r, close_h=1 / 3)
            print(r, "fixed work:", res, "| with a 20-minute close in every calendar week:", res2)

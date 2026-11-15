import sys, datetime
import gen
from gen import rows, U, dates, sunday, total, used, LIGHT
from spec import GATES, PHASE_END

NOTES = {
    0: "Oct 1 handoff recorded; amendments accepted and the file frozen",
    1: "Done as shown (v3.4 records W1 and W2 as done). Closes Y2",
    2: "Done as shown. Closes G1. W2 capacity check fired Oct 18: map rebuilt at 12h (v3.4)",
    3: "Done as shown. MC1 scored FAIL 2/10 (Oct 20); MC0 taught Oct 19",
    4: "Done as shown (v3.9 records W4-W6 at plan hours from the logs; measured minutes are in phase1-log.md). R3 not done: Om moved it to his leave",
    5: "Diwali week, done as shown. G2's first contact on the Learning Go order (approved Nov 3). Calibration lane open; Om is not applying now",
    6: "Done as shown. Nov 9-10 lost to an office incident; G2 and R2 not done. Nov 15: W6 close and the v3.9 re-forecast",
    7: "v3.9 starts. Om's leave, Mon Nov 16 to Fri Dec 4: the usual 2-2.5h a day; on a day with more time, pull the next day's work forward (Om, Nov 15). R3 pitch in the leave (Om). Lane decision from the harvest (section 8); Om decides F2 and F3b at this close, Nov 22 (v3.7)",
    8: "Leave week",
    9: "Leave week (back at the office Mon Dec 7)",
    15: "First two stories told aloud, voice mode (v3.9: W15, was W10, because R3 and R2 slipped in W4-W6; Om is not applying, so no calibration call waits on them)",
    11: "PRCP's own image on kind from K3 (D1 done in W9-W11)",
    12: "Light week",
    13: "Light week",
    30: "Added before Gate A (v3.9): Python and Postgres finish P4",
    31: "Added before Gate A (v3.9). Naukri goes live, about 15 days before Gate A",
    32: "Added before Gate A (v3.9)",
    33: "GATE A. Unseen set 1 recorded",
    34: "Normal application volume from here, including up to 4 international calibration applications (section 4, v3.7)",
    35: "Human live-coding mock (section 6.6 #13; v3.8: moved from W61)",
    56: "Diwali week 2027",
    57: "AWS session 1 of 4 (CL3), after K6b (v3.9)",
    61: "JD harvest refresh for resume v2, India and international slices",
    64: "Light week",
    65: "Light week",
    72: "Added before Gate B (v3.9): the Go lane finishes the controller",
    77: "Added week before Gate B (v3.7)",
    78: "Second added week before Gate B (v3.8): F1 finishes",
    79: "GATE B. Good referrals open; the international search runs in parallel from here; region decision recorded",
    80: "Full application push in both markets; interviews peak",
    83: "GATE C",
}
ORDER = {"DSA": 0, "RR": 50, "MP": 51, "Mock": 53, "Campaign": 60, "Gate": 70, "Proofs and weekly close": 80}


def key(it):
    lab = it[0]
    if lab.startswith("MC") and lab[2:].isdigit():
        return 52
    return ORDER.get(lab, 10)


def fmt(h):
    return f"{h:g}"


def phase(n):
    return "1a" if n <= PHASE_END["1a"] else ("1b" if n <= PHASE_END["1b"] else "1c")


# closing weeks
close_week = {}
for lab in U:
    weeks = [n for n, its in rows.items() for l, h, t in its if l == lab or (lab == "H6" and l == "Mock")]
    if weeks and abs(used[lab] - total(lab)) < 1e-9:
        close_week[lab] = max(weeks)

out = []
heads = {
    "1a": f"### 1a Foundations: W0 to W{PHASE_END['1a']}, Oct 1 2026 to {sunday(PHASE_END['1a']).strftime('%b')} {sunday(PHASE_END['1a']).day} {sunday(PHASE_END['1a']).year}",
    "1b": f"### 1b Build and design: W{PHASE_END['1a']+1} to W{PHASE_END['1b']}, {(sunday(PHASE_END['1a']+1)-datetime.timedelta(days=6)).strftime('%b')} {(sunday(PHASE_END['1a']+1)-datetime.timedelta(days=6)).day} {(sunday(PHASE_END['1a']+1)-datetime.timedelta(days=6)).year} to {sunday(PHASE_END['1b']).strftime('%b')} {sunday(PHASE_END['1b']).day} {sunday(PHASE_END['1b']).year}",
    "1c": f"### 1c Convert: W{PHASE_END['1b']+1} to W{PHASE_END['1c']}, {(sunday(PHASE_END['1b']+1)-datetime.timedelta(days=6)).strftime('%b')} {(sunday(PHASE_END['1b']+1)-datetime.timedelta(days=6)).day} to {sunday(PHASE_END['1c']).strftime('%b')} {sunday(PHASE_END['1c']).day} {sunday(PHASE_END['1c']).year}",
}
cur = None
for n, its in rows.items():
    p = phase(n)
    if p != cur:
        if cur is not None:
            out.append("")
        out.append(heads[p]); out.append("")
        out.append("| Week | Work, hours and resources | Proof due |"); out.append("| --- | --- | --- |")
        cur = p
    its = sorted(its, key=key)
    parts = []
    for lab, h, t in its:
        if lab == "Proofs and weekly close":
            parts.append(f"**Proofs and weekly close** {fmt(h)}h")
        else:
            parts.append(f"**{lab}** {fmt(h)}h: {t}")
    tot = sum(h for _, h, _ in its)
    closes = [l for l, w in close_week.items() if w == n and n > 2]
    closes = [("MOCK" if l == "H6" else l) for l in closes]
    proof = NOTES.get(n, "")
    if n > 3:
        if closes:
            proof = (proof + "; " if proof else "") + "Closes " + ", ".join(closes)
        elif not proof:
            proof = "Work in progress"
    out.append(f"| W{n} · {dates(n)} · {fmt(tot)}h | {' · '.join(parts)} | {proof} |")
open(sys.argv[1], "w").write("\n".join(out) + "\n")
print("written", len(rows), "weeks")

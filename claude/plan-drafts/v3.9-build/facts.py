"""v3.9 r2: print the numbers the text of sections 4, 5, 6 and 14 quotes, straight from the build (Claude, Nov 15 2026).
Run: python3 facts.py   (the same build gen.py makes; K1_INS and K2_INS from spec.py)."""
import datetime
from collections import defaultdict
import gen
from gen import rows, U, sunday, dates, LIGHT, total
from spec import PHASE_END, GATES

tot = defaultdict(float)
phase = {"1a": 0.0, "1b": 0.0, "1c": 0.0}
for n, its in rows.items():
    p = "1a" if n <= PHASE_END["1a"] else ("1b" if n <= PHASE_END["1b"] else "1c")
    for l, h, t in its:
        tot[l] += h
        phase[p] += h
grand = sum(tot.values())
sec = defaultdict(float)
for lab in U:
    sec[U[lab]["sec"]] += total(lab)


def first_last(pred):
    ws = [n for n, its in rows.items() for l, h, t in its if pred(l, t or "")]
    return (min(ws), max(ws)) if ws else (None, None)


def d(n):
    s = sunday(n)
    return f"{s.strftime('%b')} {s.day} {s.year}"


ga, gb, gc = PHASE_END["1a"], PHASE_END["1b"], PHASE_END["1c"]
F = {
    "weeks": len(rows), "last": max(rows), "grand": grand, "campaign": tot["Campaign"], "learning": grand - tot["Campaign"],
    "dsa": tot["DSA"], "proofs": tot["Proofs and weekly close"], "gates": tot["Gate"], "setup": tot["Setup"],
    "rr": tot["RR"], "mp": tot["MP"], "phase": phase, "sec": dict(sec),
    "GA": (ga, d(ga)), "GB": (gb, d(gb)), "GC": (gc, d(gc)),
    "unseen1": first_last(lambda l, t: l == "DSA" and t.startswith("Unseen set 1")),
    "unseen2": first_last(lambda l, t: l == "DSA" and t.startswith("Unseen set 2")),
    "blind": first_last(lambda l, t: l == "DSA" and "blind mixed sets" in t),
    "human_mock": first_last(lambda l, t: l == "DSA" and t.startswith("Human live-coding mock")),
    "naukri": first_last(lambda l, t: l == "R1" and t.startswith("Naukri live")),
    "aloud": first_last(lambda l, t: l == "R2" and t.startswith("Tell the first two stories aloud")),
    "r2_write": first_last(lambda l, t: l == "R2" and t.startswith("Write the first two honest stories")),
    "mock": [n for n, its in rows.items() for l, h, t in its if l == "Mock"],
    "y3_tail_end": first_last(lambda l, t: l == "Y3")[1],
    "refresh": first_last(lambda l, t: l == "Campaign" and t.startswith("JD harvest refresh")),
    "cl3": [n for n, its in rows.items() for l, h, t in its if l == "CL3"],
    "k6b": first_last(lambda l, t: l == "K6b"),
    "mc": {l: n for n, its in rows.items() for l, h, t in its if l.startswith("MC") and l[2:].isdigit()},
    "open15": [n for n, its in rows.items() if n >= 7 and n not in LIGHT and abs(sum(h for _, h, _ in its) - 11.75) < 1e-9],
    "under_cap": [(n, sum(h for _, h, _ in its)) for n, its in rows.items() if n > gb - 3 and sum(h for _, h, _ in its) < (7 if n in LIGHT else 12) - 1e-9],
    "units_span": {u: first_last(lambda l, t, u=u: l == u) for u in ["P1", "D1", "E1", "C1", "A3", "G2", "K1", "K2", "K3", "Y8a", "L3", "P4", "G7", "K7a", "DS1", "OP4", "OP7", "F1"]},
}
if __name__ == "__main__":
    for k, v in F.items():
        print(k, v)

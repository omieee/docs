"""Merge Claude's and ChatGPT's run-1 harvest CSVs into one count table with 95% Wilson ranges.

Run from the repo root: python3 -I claude/harvest/work/merge.py
Go and Python codes: Claude's from build.py; ChatGPT's 8 rows hand-coded by Claude from their langs fields.
"""
import csv, math, pathlib, sys, importlib.util

root = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("build_codes", pathlib.Path(__file__).parent / "build.py")
cl = list(csv.DictReader(open(root / "claude/harvest/2026-10-27-claude.csv")))
cg = list(csv.DictReader(open(root / "chatgpt/harvest/2026-10-27-chatgpt.csv")))

# Read Claude's hand codes from the Coding sheet instead of re-running build.py.
from openpyxl import load_workbook
wb = load_workbook(root / "claude/harvest/2026-10-27-claude.xlsx", data_only=True)
codes = {r[0]: {"go": r[4], "python": r[5]} for r in wb["Coding"].iter_rows(min_row=2, values_only=True)}
CG_GO = {"CG-001": "allowed", "CG-002": "required", "CG-003": "required", "CG-004": "none", "CG-005": "none",
         "CG-006": "allowed", "CG-007": "preferred", "CG-008": "allowed"}
CG_PY = {"CG-001": "allowed", "CG-002": "none", "CG-003": "none", "CG-004": "required", "CG-005": "required",
         "CG-006": "allowed", "CG-007": "none", "CG-008": "allowed"}
for r in cl:
    r["_go"], r["_py"] = codes[r["id"]]["go"], codes[r["id"]]["python"]
for r in cg:
    r["_go"], r["_py"] = CG_GO[r["id"]], CG_PY[r["id"]]

urls = [r["url"] for r in cl + cg]
assert len(urls) == len(set(urls)), "duplicate URL across coaches"


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - m) / d), min(1.0, (c + m) / d))


india = [r for r in cl + cg if r["region"] == "India"]
intl = [r for r in cg if r["region"] != "India"]
dated_india = [r for r in india if r["posted"] != "unknown"]

tests = [
    ("Lane a (Python-led backend infra)", lambda r: r["lane"] == "a"),
    ("Lane b (Go and Kubernetes platform)", lambda r: r["lane"] == "b"),
    ("Lane c (controllers and operators)", lambda r: r["lane"] == "c"),
    ("Lane d (data-infrastructure platforms)", lambda r: r["lane"] == "d"),
    ("Go required or an allowed choice", lambda r: r["_go"] in ("required", "allowed")),
    ("Go required, no alternative", lambda r: r["_go"] == "required"),
    ("Python required or an allowed choice", lambda r: r["_py"] in ("required", "allowed")),
    ("Kubernetes controllers required or preferred", lambda r: r["k8s_controllers"] in ("required", "preferred")),
    ("Helm required or preferred", lambda r: r["helm"] in ("required", "preferred")),
    ("Helm required", lambda r: r["helm"] == "required"),
    ("Terraform required or preferred", lambda r: r["terraform"] in ("required", "preferred")),
    ("ai_infra app", lambda r: r["ai_infra"] == "app"),
    ("ai_infra platform", lambda r: r["ai_infra"] == "platform"),
    ("ai_infra engine", lambda r: r["ai_infra"] == "engine"),
    ("AI skill required (any kind)", lambda r: r["ai_req"] == "required"),
]

out = []
out.append(f"| Item | India, all ({len(india)}) | 95% range | India, dated only ({len(dated_india)}) | 95% range |")
out.append("| --- | --- | --- | --- | --- |")
for label, f in tests:
    k = sum(1 for r in india if f(r))
    kd = sum(1 for r in dated_india if f(r))
    lo, hi = wilson(k, len(india))
    lod, hid = wilson(kd, len(dated_india))
    out.append(f"| {label} | {k} ({k/len(india):.0%}) | {lo:.0%}-{hi:.0%} | {kd} ({kd/len(dated_india):.0%}) | {lod:.0%}-{hid:.0%} |")
print("\n".join(out))
print()
print(f"India rows: Claude {sum(1 for r in cl)}, ChatGPT {sum(1 for r in cg if r['region']=='India')}; "
      f"international (ChatGPT only): {len(intl)} -> " + ", ".join(f"{r['country']} {r['employer']} lane {r['lane']}" for r in intl))

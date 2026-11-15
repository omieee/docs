"""v3.9 r2: reproduce the release-evidence case table in section 6.1 (Claude, Nov 15 2026).

Usage: python3 gate_cases.py <path to a PRCP checkout's src folder>
       (checked on PRCP PR #11 at ae974b0: git fetch origin 'refs/pull/11/head', then pass .../src)

The left column runs PRCP's own `decide()`. The right column runs the same `decide()` on the output of a
coach-side reference for E1's evidence step, kept here only so the table can be checked; Om writes his own in E1.
"""
import sys
from http import HTTPMethod

sys.path.insert(0, sys.argv[1])
from prcp.gate import decide, GateStatus                      # noqa: E402
from prcp.models import (ProbeStatus, create_environment, create_http_probe,  # noqa: E402
                         create_probe_result, create_service)

env = create_environment("staging")
svc = create_service("pay", "https://pay.example")
A = create_http_probe(env, svc, HTTPMethod.GET, "/health")
B = create_http_probe(env, svc, HTTPMethod.GET, "/ready")
REQUIRED = [A.id, B.id]
R, OLD = "r42", "r41"


def res(probe, status, release):
    r = create_probe_result(probe, status, 200 if status == ProbeStatus.PASS else None, None, 5.0 if status == ProbeStatus.PASS else None)
    return r, release


def evidence(required, release, received):
    """One entry per required probe, only for this release; a required probe with no result becomes UNKNOWN."""
    by_probe = {}
    for r, rel in received:
        if rel == release and r.probe.id in required:
            by_probe[r.probe.id] = r                      # which one wins on a repeat is E1's ADR decision
    probes = {A.id: A, B.id: B}
    return [by_probe.get(pid) or create_probe_result(probes[pid], ProbeStatus.UNKNOWN, None, None, None) for pid in required]


a_ok = res(A, ProbeStatus.PASS, R)
CASES = [
    ("Nothing", [], GateStatus.UNKNOWN, GateStatus.UNKNOWN),
    ("A passes, B never reports", [a_ok], GateStatus.PASS, GateStatus.WARN),
    ("The same passing A twice, B never reports", [a_ok, a_ok], GateStatus.PASS, GateStatus.WARN),
    ("A and B both pass", [a_ok, res(B, ProbeStatus.PASS, R)], GateStatus.PASS, GateStatus.PASS),
    ("A passes, B's only pass is for the previous release", [a_ok, res(B, ProbeStatus.PASS, OLD)], GateStatus.PASS, GateStatus.WARN),
    ("A passes, B reports UNKNOWN", [a_ok, res(B, ProbeStatus.UNKNOWN, R)], GateStatus.WARN, GateStatus.WARN),
    ("A passes, B fails", [a_ok, res(B, ProbeStatus.FAIL, R)], GateStatus.BLOCK, GateStatus.BLOCK),
]
bad = 0
for name, received, want_today, want_e1 in CASES:
    today = decide([r for r, _ in received]).status
    with_e1 = decide(evidence(REQUIRED, R, received)).status
    ok = today == want_today and with_e1 == want_e1
    bad += not ok
    print(f"{'ok ' if ok else 'BAD'} {name:52} today {today:8} with E1 {with_e1}")
print("ALL CASES MATCH THE SECTION 6.1 TABLE" if not bad else f"{bad} MISMATCH(ES)")
sys.exit(1 if bad else 0)

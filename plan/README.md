# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05. Current: v3.8, approved by Om on 2026-10-24 (14:32 IST): every teaching part ends with a typed use step in real code (Python and SQL in PRCP, Go in the probe agent from G2, Kubernetes with PRCP's own image on kind, LLD in PRCP), 5-minute session warm-ups (trial W4-W5), optional logged bedside cards, no row naming an untaught tool, the first spoken stories in W10, the human live-coding mock in W32, an office-code fallback, and a structure freeze until the Nov 15 re-forecast. It folds in ChatGPT's 10-point audit of the same day. Gates: A May 2 2027, B Feb 6 2028, C Mar 5 2028; 834.5 scheduled hours. It replaces v3.7 (sha256 `31d6753c48138696`) in both projects. Draft, build scripts and negative tests: `claude/plan-drafts/` and `claude/plan-drafts/v3.8-build/`.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.8.md` | `25bb309e79a610f2` |
| `check_plan.py` | `6c55bf0713278013` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.8.md`; it must print PASS (7 fragmentation warnings are expected and do not block).
- **Changing the plan:** frozen until the Nov 15 2026 re-forecast except for the three triggers in section 9 (an untaught prerequisite blocking this week's work, repeated failed learning on one unit, a real market change with dated evidence). A coach drafts the change (section 9), rebuilds with the generator in `claude/plan-drafts/v3.8-build/`, runs `check_plan.py` to PASS and the negative tests to FAIL as expected, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day.
- Old versions stay in git history; nothing older is kept as a separate file.

# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.3.md` | `c4b4cf6d33a05be1` |
| `check_plan.py` | `3bcff4edee48d1b6` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.3.md`; it must print PASS.
- **Changing the plan:** a coach drafts the change (section 9), runs `check_plan.py` to PASS, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day.
- Old versions stay in git history; nothing older is kept as a separate file.

# Phase 1 plan: master copy

The plan and its checker live here, and the same files are uploaded to both the Claude and ChatGPT projects. Approved by Om on 2026-10-05. Current: v3.5, committed by Claude on 2026-10-20 after Om approved it in chat (unseen DSA sets in W24 and W48, the pattern-signal question, safeguard 13). It waits for Om to upload it to both projects; v3.4 (uploaded 2026-10-18, sha256 `a8717a0d890e199b`) governs until then.

| File | sha256 (first 16) |
|---|---|
| `Phase1_Master_Plan_v3.5.md` | `3aa6efedf5d2ae9e` |
| `check_plan.py` | `a79087bb8dcf039d` |

- **Verify your project copy:** `sha256sum <file>` must match the table. Run `python3 check_plan.py Phase1_Master_Plan_v3.5.md`; it must print PASS.
- **Changing the plan:** a coach drafts the change (section 9), runs `check_plan.py` to PASS, and Om approves. The approved file is committed here first, with the table updated, then uploaded to both projects the same day.
- Old versions stay in git history; nothing older is kept as a separate file.

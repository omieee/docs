# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 6fcebd7 + this commit · 2026-10-17 10:35 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/ (sha c4b4cf6d33a05be1). Week: W2 Oct 12-18, closes Sun Oct 18 together with W1 (ChatGPT voice check pending for both).
- W1 done: Y2 baseline 0 solid / 6 shaky / 13 missing. NEW 155 PASS Oct 11. G1 PASS Oct 13 (PR #2 087baf3, 5/6); suggest merging PR #2. Next Go: G2 per W3 row.
- DSA 24 / 17. NEW 739 PASS Oct 17 (4/6; D3 COLD PASS e459c37). 155 D7 PASS Oct 17. Due: 20 D14 Oct 18 (state complexity first; add a "(])" assert), 739 D7 Oct 20, 141 D28 Oct 20, 19 D28 Oct 21, 143 D28 Oct 22, 155 D14 Oct 24.
- Om pattern (155, 739): executes and traces right, leaves out the "why". Ask for the reason at every step. Om sometimes sends one submission to both coaches: check the other log before any verdict.
- DSA rule (Om approved Oct 6): label NEW/DRILL/COLD first. COLD = approach + complexity first, problem-derived asserts, 10m Easy / 15m Medium + 5m verify, no interview. Any miss: score once, teach, queue one repair for a later DSA slot. NEVER retry same session.
- MC1 slipped W0, W1 and Oct 14. Om: Mon Oct 19 or Tue Oct 20 (Claude suggests Mon), pin at Sunday close: 90 min timed, no AI, Om types "60" at minute 60 for the change, raw notes committed first, 60-min review after. Never fragments.
- Capacity: plan assumes 15 hrs/week. W2 check Oct 18 (s5): under 10 avg since Oct 1 means re-forecast that Sunday. Logged so far: P1 Block 1 [25m] Oct 14 only.
- Dynamic-time protocol (both coaches, Oct 14): Om opens with minutes + mode; one block; save line; [NNm] logged per block. Voice blocks = ChatGPT. Long-chat warning rule posted Oct 15.
- Laptop (Oct 15-16, contingency): RAM starvation proven, fixed with +16 GB (21 GiB usable), load-tested, cooling healthy on a fan stand. Record claude/resources/laptop-2026-10-16.md. K1 kind no longer RAM-blocked. Hours to contingency, Om gives the number Sunday.
- Artifacts: Oct 15-16 have P1 commits in learning-python-sandbox (no two-day gap; Claude first missed this repo, corrected). Repos to check: docs, dsa-python, learning-go-sandbox, learning-python-sandbox, lld-patterns, platform-reliability-control-plane.
- P1 prereqs: Block 1 (context managers) read + video Oct 14; Tx exercise coded Oct 15-16 (learning-python-sandbox branch omieee/initial-setup, 42be54a: context_managers/Tx.py, tests/test_Tx.py, CI file), not reviewed yet. Still open: Tx review + why answer, Block 2 (yield fixtures), Block 3 (dataclass ==), each video first.
- R1: resume v1 doc drafted (975886e6), Om fills blanks. Conflict for Sunday: Om (Oct 14) updates Naukri only ~15 days before interview-ready vs R1 "profiles live in October".
- Sunday agenda: cue time (Om: study block 10am-1pm most days; Claude proposed 10:00 cue, unconfirmed), DSA 45-min daily cap (pending), MC day for W3, contingency hours, R1 conflict, office-Go result and gap diagnosis still open.
- Weak spots to aim at: context managers, pytest fixtures, dataclass ==; why set lookup is O(1); iterators, generators, decorators (Om asked; plan W16-W17).
- Operating model (Om approved Oct 5): owner = coach Om starts with; misses repaired by that coach; other coach runs later retention; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict.
- Go second pass: Go in Action 2e (claude/resources/go-in-action-2e.md). Boot.dev Learn Go optional desk practice. Bedside no-audio map: claude/resources/bedside-reading.md.

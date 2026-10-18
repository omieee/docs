# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 7267e5a + this commit · 2026-10-18 11:58 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/. W2 closed PARTIAL (proposed, phase1-log); ChatGPT spoken check for W1 and W2 still pending. W3 = Oct 19-25.
- CAPACITY (Oct 18): s5 check fired. About 13h of 33 scheduled done since Oct 1. Om: 2h a day target, bad days 30 min. Claude recommends 12h scheduled weeks (14 gross): Gate A Mar 21, B Sep 5, C Sep 26 2027. At 14h: Feb 28, Jul 25, Aug 8. PENDING Om's pick, then rebuild week map + check_plan PASS + re-upload.
- Amendment to draft (max 5): capacity and dates; R1 (LinkedIn now, Naukri ~15 days before interview-ready, no Premium); cue 10:30 AM; DSA rule; two-coach model text from Oct 5.
- DSA 24 / 17. 20 D14 PASS Oct 18 (7d3c30e, assert fix 291dfad). Due: 739 D7 and 141 D28 Oct 20 (one may slide a day under the cap), 19 D28 Oct 21, 143 D28 Oct 22, 155 D14 Oct 24, 20 D28 Nov 1. Carried: binary search lessons 14-15, NEW 704.
- DSA rule APPROVED Oct 18: 45 min a day max, one item per session, clock paused on interruptions; a miss: teach in a separate later slot, retry in another. Label NEW/DRILL/COLD first. Never same-session retry.
- Om pattern (155, 739): executes and traces right, leaves out the "why"; asserts miss the one case that isolates a bug (20: "(])"). Ask for the reason and the isolating case.
- MC1: Mon Oct 19, morning block after the cue; 90 min timed, no AI, "60" at minute 60, raw notes committed first, 60-min review can be a later day. Never fragments.
- Cue 10:30 AM daily (Om to calendar it). Office 1-2 days a week from now; Om flags short days.
- P1 prereqs: Block 1 PASS Oct 17 (PR #1 7b450d4). Block 2 (yield fixtures) packet given Oct 17: merge PR #1, video, fixture lab on a new branch, predictions in raw notes first. Then Block 3 (dataclass ==), then psycopg.
- Open PRs to merge (all passed): dsa-python #9, learning-go-sandbox #2, learning-python-sandbox #1.
- R1: resume v1 draft (975886e6) blanks for Om; LinkedIn live in October; Naukri later.
- Office-Go test FAIL (Oct 18): no Go work, AI writes what comes. Go = study track only. Office Go counts only via the office proof path, never AI-written.
- Gap diagnosis: Claude drafted "no fixed cue or protected slot, time set by son and office; fix = 10:30 cue + minutes logged per block"; Om's yes pending.
- Contingency: 2 used (laptop), 48 left.
- Token rule (Om, Oct 18): use the docs token only with Om's explicit OK each time. Ask when stuck.
- Own process rules: today's list = due colds + every open WIP item in all six repos; quote a claim and test the generous reading before scoring it wrong; plant bugs with PYTHONDONTWRITEBYTECODE=1.
- Operating model: owner = coach Om starts with; misses repaired by that coach; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict.

# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ 09cd383 + this commit · 2026-10-19 18:36 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- Plan: v3.3, master in plan/. W2 closed PARTIAL (proposed, phase1-log); ChatGPT spoken check for W1 and W2 still pending. W3 = Oct 19-25.
- PLAN: v3.4 GOVERNING (Om uploaded to both projects Oct 18; ChatGPT confirmed sha256 a8717a0d890e199b + PASS); master in plan/ with README hashes (Claude synced 23:20). 565.5h, 12h weeks, gates Mar 21, Sep 5, Sep 26 2027. Coach safeguards in s0. Next: s9 GAP draft for the MC0 method lesson (+1.5h). Nov 15 re-forecast from logged minutes only.
- v3.4 contents: 12/7/9 caps, W1-W2 as done, R1 (LinkedIn now, Naukri W22, no Premium), cue 10:30, DSA session rule s6.6 #11, two-coach model + per-block minutes in s0, office-Go FAIL in s10, Phase 2 dates follow Gate C.
- DSA 24 / 17 (NEW 704 and 74 not counted until their Fri Oct 23 interviews). Open: dsa-python PR #10 95dfe22, code correct, tests 1/7 planted, ruff E501 x2. Due: Tue 739 D7 (after MC1) + 704 D1; Wed 141 D28, 19 D28, 74 D1; Thu 143 D28, 704 D3, 74 D3; Fri fix PR #10 + NEW interviews; Sat 155 D14; Mon Oct 26 704 D7, 74 D7. Binary search lesson 14 done Oct 19, lesson 15 Wed.
- DSA rule APPROVED Oct 18: 45 min a day max, one item per session, clock paused on interruptions; a miss: teach in a separate later slot, retry in another. Label NEW/DRILL/COLD first. Never same-session retry.
- Om pattern (155, 739): executes and traces right, leaves out the "why"; asserts miss the one case that isolates a bug (20: "(])"). Ask for the reason and the isolating case.
- MC0/MC1 (Om, Oct 18 23:07): ChatGPT TEACHES the machine coding method lesson Mon Oct 19 (Om never sat a round). Claude = VERIFIER + INVIGILATOR: MC1 Tue Oct 20 (holiday) morning, 90 min, no AI, raw notes first, Om types "60" -> Claude gives the change (prepare one, never commit it to docs before the rep), commit at 90; Claude fresh-clones, runs, plants bugs, scores s7 rubric, one verdict; ChatGPT teaches the 60-min review. Claude MONITORS ChatGPT vs s0 safeguards: log breaks (rule + evidence); a break costing Om time or understanding (rules 1-6) = Claude takes the lead next block. ChatGPT GitHub writes failing: need Om's relay. Tue: 739 D7 after MC1, 141 D28 Wed.
- Cue 10:30 AM daily (Om to calendar it). Office 1-2 days a week from now; Om flags short days.
- P1 prereqs: Block 1 PASS Oct 17 (PR #1 7b450d4, merged c39ca00). Block 2 RESTART from zero (Oct 18 coach error, Om had never seen pytest): step 1 what pytest is, step 2 fixture with return, step 3 fixture with yield; one runnable example each; nothing beyond the plan line (no xfail, no tricks). Resource PCC 3e ch 11. Then Block 3 (dataclass ==), then psycopg.
- Open PRs to merge (all passed): dsa-python #9, learning-go-sandbox #2, learning-python-sandbox #1.
- R1: resume v1 draft (975886e6) blanks for Om; LinkedIn live in October; Naukri later.
- Office-Go test FAIL (Oct 18): no Go work, AI writes what comes. Go = study track only. Office Go counts only via the office proof path, never AI-written.
- Gap diagnosis: Claude drafted "no fixed cue or protected slot, time set by son and office; fix = 10:30 cue + minutes logged per block"; Om's yes pending.
- Contingency: 2 used (laptop), 48 left.
- Token rule (Om, Oct 18): use the docs token only with Om's explicit OK each time. Ask when stuck.
- Own process rules: follow the 12 s0 coach safeguards (v3.4) every session; plant bugs with PYTHONDONTWRITEBYTECODE=1; check IST time with the clock tool before any timestamp.
- Operating model: owner = coach Om starts with; misses repaired by that coach; packets UNIT | STATUS | EVIDENCE | GAP | ASK; one gate verdict.

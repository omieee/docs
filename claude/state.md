# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ this commit · 2026-10-29 23:12 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- ROLE: equal partner with ChatGPT; no coaching owner (Om, Oct 23 14:56). WRITE plain Indian-style English, full sentences, explain every technical word first time, clear over short. Say every "why" out loud in questions too (Om, Oct 29: "mind needs to be spoken out").
- OM'S OCT 29 RULES: video first for any new topic, ask prerequisites first, no proof question until Om says a topic is clear; questions must name the column, line and what is saved (no clipped style). He keeps going until he says "stop for the day"; ask his active minutes at the end. Oct 29 23:10: boxes are a guide, not a stop; judge flow, suggest a break only if it truly drags or he is frustrated; log minutes quietly, don't raise them (DSA 45-min cap: asked, open).
- PLAN: v3.8 in plan/ (25bb309e79a610f2, checker 6c55bf0713278013 PASS), 834.5h, gates May 2 2027, Feb 6 2028, Mar 5 2028. Frozen until Nov 15 except section 9 triggers.
- W4 (Oct 26-Nov 1, 12h): DSA colds done (704 and 74 D7 Oct 26, 739 D14 Oct 27), teaching slots done Oct 27-28, lesson 15 Oct 28; NEW 875 code done Oct 29. K1 ChatGPT (PARTIAL cold, repairs passed). L1 open (ChatGPT check PARTIAL Oct 26; PRCP use note in docs/ not done). Y3 part 1 done Oct 25. MP1 SKILL SHOWN Oct 28. Y7a in progress. R3 not started. Sun Nov 1: 20 D28, then the weekly close.
- 875 (Oct 29): PR #14 `8021257`, 0/149,180 wrong, 8/9 planted caught (`le = 0` survives: add one assert with answer 1, no re-score). [25m], video first, closed-book, no AI. NEW interview (mechanism, trace, transfer, pattern signal) due in the next DSA slot, Fri Oct 30.
- Y7a (Oct 29): part check PARTIAL 3/6 after retries (Protocol, repository, conftest). Unit proof open: paragraph in; SQL Q1 2/2; Q2 1/2 taught, retry (gate_decision RESTRICT to CASCADE) unanswered; Q3 (probe_result id with no source) to ask. Then the verdict. Records in claude/tests/python/2026-10-29-Y7a-*.md.
- DSA 26 / 19. Next colds: 20 D28 Sun Nov 1, 704 and 74 D14 Mon Nov 2, 155 D28 Nov 7, 739 D28 Nov 10.
- P1 next: psycopg 3 prerequisite (W5, ask first). GO: G2 W5, teach `t *testing.T` and `strings.Builder` first (RR1 slip).
- Continuity: Go last Oct 24 (W4 idle week), Kubernetes K1 Oct 26, LLD MP1 Oct 28.
- Coach errors W4 (Claude): Oct 26 K1 resource (contributing), Oct 27 x3, Oct 29 video-first [10m] and clipped questions [2m].
- Local Postgres 16 works in the container (run as user claude); used for SQL teaching with real output.
- Pushes: add_repo push refused at 14:11 Oct 29, granted at 21:11 on Om's yes. No token use.
- Own process rules: fetch every branch and PR head before saying anything is missing; push a coach-error line before the reply that admits it; minutes from message times, elapsed vs active, ask only to confirm; check the clock before any timestamp; plant bugs with PYTHONDONTWRITEBYTECODE=1.

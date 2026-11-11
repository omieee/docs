# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ this commit · 2026-11-11 22:32 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- NOW W6 Nov 9-15 (12h row). Om back Nov 11 (gap Nov 7-10 ended): 739 D28 PARTIAL, 155 D28 PASS (dsa-python PR #19), P1 save point done (PRCP PR #11 cc08ebf), P1 step 2 part 1 taught. Coach arrangement after Nov 8 not decided by Om; he opened Claude Nov 10-11.
- NEXT (Thu Nov 12): 875 D14 COLD (15m box, approach and complexity at the top), then P1 step 2 commit: FastAPI 0.136.3 runs code after `yield` after the response by default (failed commit still 201); `scope="function"` runs it before. Then POST twice 201/409, restart, GET.
- P1: Om's yield dependency without commit is local, unpushed by design (POST 201, GET 404, POST 201 seen and explained 22:26). API tests use `dependency_overrides` (in-memory), so they stay green.
- AT IDLE LIMIT: Kubernetes (last Oct 26) and LLD (last Oct 30): K1 kubectl drill and MP2 must run in W6. Go last Nov 4 (step B): W6 may be its idle week, then W7 must have Go. Go runs from `claude/plan-drafts/2026-11-03-go-appendix-nov4-15.md`, next step C.
- 875: NEW retry PARTIAL 5.5/8 Nov 3; D7 PARTIAL Nov 5 (ChatGPT, complexity missing). Owed: yes/no pattern teaching (note `claude/notes/2026-11-06-LC875-teaching-note.md`, read status unverified), then one fresh question in another slot. Colds: 704 and 74 D28 Mon Nov 16.
- R3 deferred by Om to his 15-working-day leave after W6. Campaign: Om not applying.
- Nov 15: re-forecast from logged minutes; batch list `claude/plan-drafts/2026-11-15-batch.md`. ChatGPT's CoachOps review request (chatgpt/outbox Nov 6) unanswered; Om decides.
- ROLE: equal partner with ChatGPT; no owner. Plain Indian-style English, explain every technical word first time, clear over short. Om's Oct 29 rules: video first for new topics, ask prerequisites first, no proof question until Om says clear; boxes are a guide, judge flow; DSA about 1h at most on a 2h day (pending approval).
- PLAN: v3.8 (25bb309e79a610f2), frozen until Nov 15. DSA 26 / 19. Contingency 9.24 used, 40.76 left.
- Om's Postgres: Docker `prcp-pg`, postgres:18.6, user/password prcp, dbs `prcp` and `prcp_test`. Container has Postgres 16 for demos.
- Own process rules: fetch every branch and PR head before saying anything is missing; push a coach-error line before the reply that admits it; minutes from message times; check the clock before any timestamp; check the taught list before any lesson.

# Claude state (cache only, max 20 lines)
Reflects omieee/docs @ e0f92a3 + this commit · 2026-10-25 11:05 IST. Before a verdict, gate or plan change, read the canonical logs and outboxes.
- ROLE: equal partner with ChatGPT; no coaching owner (Om, Oct 23 14:56). WRITE plain Indian-style English, full sentences, explain every technical word first time, clear over short. Om's Oct 25 view: too much of his time goes in monitoring Claude; errors he catches count even when logged 0m.
- PLAN: v3.8 in plan/ (25bb309e79a610f2, checker 6c55bf0713278013 PASS), 834.5h, gates May 2 2027, Feb 6 2028, Mar 5 2028. Frozen until Nov 15 except section 9 triggers.
- W3 CLOSE (Claude, Oct 25): PARTIAL. Om active about 18.3h vs 12 (estimate). DSA about 7.3h vs 2.5h; L1 2.6h vs 1h. LinkedIn not live. Coach errors: Claude 11 (70m measured, Om caught 6), ChatGPT 3. Contingency 3.2 used, 46.8 left.
- W4 (Oct 26-Nov 1, 12h): DSA 2.25h (Mon 704 and 74 D7 + one fresh question each; Tue 739 D14; Sun Nov 1 20 D28; lesson 15 then NEW 875), R3 1.5, K1 1.5 (ask first), L1 1.5, Y3 1 (generators; Om never used yield beyond fixtures), Y7a 0.75, MP1 1h Tue Oct 27 (fallback Sat Oct 31; Claude runs it), close 0.75. Warm-up trial W4-W5 (5 min recall at the start of each non-DSA desk session).
- DSA 24 / 17. 704 and 74 count only after their NEW retries. D90 column added Oct 25. 155 D14 test fix done (d576731). 155 D28 Nov 7.
- TEACHING DONE FOR RETRIES: 704 (Oct 24, window rule, `return left`, sorted is the signal); 74 (Oct 25, three moves per round, STOP case, overlapping rows break it).
- P1: pytest basics, yield fixtures, dataclass equality all PASS (W3 plus W4's P1 hour). Next P1 item: psycopg 3 prerequisite (W5, ask first). L1 closes W7. GO: RR1 slipped Oct 24 (`t *testing.T`, `strings.Builder`); teach both at G2 start (W5).
- MC1 FAIL 2/10 (Oct 20). Input-reading drill (20-30m) waits for Om's yes or no.
- Open PRs: lld-patterns #2, learning-go-sandbox #3, learning-python-sandbox #3. Merged Oct 25: dsa-python #10, learning-python-sandbox #6.
- Continuity: Go last used Oct 24, W4 is its one idle week, G2 W5. K1 starts W4. LLD last Oct 22.
- Cue 10:30 AM daily. Office 1-2 days a week (often Mon, Wed, Fri).
- Pushes: add_repo push was refused at 09:31 and granted at 11:03 on retry; writable clone in /home/claude/docs. No token use.
- Own process rules: fetch every branch and PR head before saying anything is missing; push a coach-error line before the reply that admits it; minutes from message times, elapsed vs active, ask only to confirm; check the clock before any timestamp; plant bugs with PYTHONDONTWRITEBYTECODE=1.

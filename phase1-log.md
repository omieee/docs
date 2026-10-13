# Phase 1 log
Source of truth: Phase1_Master_Plan_v3.3.md (uploaded to the Claude project 2026-10-05)

## Weekly closes
(Sunday: paste the section 7 template here, newest on top)

```
WEEK 1: PARTIAL (proposed by Claude from git, CI and tracker facts, 2026-10-11 17:30 IST; ChatGPT spoken check pending, one combined close)
Focused hours, planned / actual (bedside required items included): 15 / not logged (Om: "variable"; logging starts W2)
Actual vs planned hours, each unit closed: Y2 1h planned, actual not logged; NEW 155 actual not logged
Largest overrun or underrun, and why: underrun: MC1, R1, L1, P1 got 0 of 9.5h planned (Sev 1 Oct 9, on-call Oct 10-11, no cue time); LC141 D14 ran about 2h on Oct 6 against a 15-min cold box, coach process error, excluded per the Oct 6 amendment
Contingency used this week / total used / remaining (of about 50): 0 / 0 / 50
Planned: DSA 3.5h (NEW 155, NEW 739), MC1 2.5h, Y2 1h, G1 0.5h, R1 3h, L1 1h, P1 3h, proofs 0.5h
Completed (with commit hashes): Y2 baseline (0ddf130): 0 solid / 6 shaky / 13 missing. NEW 155 PASS (640354f, f17e69b; PARTIAL Oct 10, repair correct Oct 11, interview 4/6). Colds: 20 D1 PASS (47153c1), 141 D14 FAIL then repaired (566dea4), 19 D14 PASS (4d7796f), 20 D3 PASS (0168425), 143 D14 PARTIAL (781a8f4), 20 D7 PARTIAL (8647552), 155 D1 PASS (42c157e)
Not completed: NEW 739; MC1 (second week missed); G1 (PR #2 open at ae56955: go build fails on sub1, dead main in helloworld, TestAdd has one case, English branch untested; Integers and Iteration not done); R1; L1; P1
DSA total / cold: 23 / 16
Machine coding reps: 0
Design mocks: 0
Git and production evidence: dsa-python PR #8 open (head 42c157e); learning-go-sandbox PR #2 open (ae56955); no PRCP or lld-patterns commits since Oct 1
Execution gaps (days with no artifact): Oct 9 (Sev 1). 14-day tripwire (Sep 28-Oct 11): 12 of 14 days with an artifact, no two-day gap, not hit
Carry-forward: NEW 739 (monotonic stack explainer first), MC1, G1 rest, R1 3h, L1 1h, P1 3h; LC20 D14: complexity first, add a "(])" assert
Next week's scope: capped at 15h, in this order: DSA colds (155 D3 Oct 13, 155 D7 Oct 17, 20 D14 Oct 18) and NEW 739 (about 3h); MC1 on one named clean 90-min day plus review (2.5h); G1 to close per the W2 row (3h); R1 resume v1 plus Naukri and LinkedIn live, October deadline (3h); L1 (1h); P1 Python prerequisites (1.5h); proofs (0.5h). Slips to W3 in row order: P1 psycopg, W2 NEW 704 and binary search lessons, K1, H1, R3, L1 W2 part. Capacity check Oct 18 uses W2's logged hours (W0 and W1 unlogged)
Change-control trigger: NO
Om inputs: weekend on-call done for 2026; now about 1 weekday on-call a month and about 2 on-call weekends a year. Sev frequency not given. Cue time not set (open since Oct 1)
Spoken check (ChatGPT): pending
```

```
WEEK 0: FAIL (provisional: W0 DSA PASS; MC1 and Y2, the week's closing units, not done)
Focused hours, planned / actual (bedside required items included): 8 / [Om to fill]
Largest overrun or underrun, and why: [Om to fill]
Contingency used this week / total used / remaining (of about 55): 0 / 0 / 55
Planned: Setup 1h, DSA 2h, R1 1h, MC1 2.5h, Y2 1h, G1 0.5h
Completed (with commit hashes): 143 D7 PASS (d500d1a); to_list cycle fix (aa2219d); 19 D7 FAIL, copied (cb546b7), redo PASS (49d4a5e); 682 DRILL (e692c3f); NEW 20 (2aa3ae4), cold proof 5/6 after one prompt (ChatGPT); phase1-log created (c7f5da1); plan v3.2 teach-first amendment approved and uploaded (Oct 5)
Not completed: MC1, Y2, G1, R1 (no commits in lld-patterns or learning-go-sandbox since Oct 1); Oct 1 items: office-Go result, gap diagnosis, cue time [Om to confirm]
DSA total / cold: 22 / 14
Machine coding reps: 0
Design mocks: 0
Git and production evidence: dsa-python PR #7 merged (6836f9b), PR #8 open
Execution gaps (days with no artifact): None; artifacts on all 4 days Oct 1-4. 14-day tripwire not hit
Carry-forward: MC1 and Y2 first in W1, then G1 and R1's W0 hours; 682 space O(n) and spec-example tests; LC 20 tests ("(]", "]", "((")
Next week's scope: W1 row in order, capped at 15h; whatever doesn't fit slips to W2 (expect K1 and H1). Re-forecast at the W2 capacity check, Oct 18. W1 colds: 20 D1 Oct 5, 141 D14 Oct 6, 20 D3 and 19 D14 Oct 7, 143 D14 Oct 8, 20 D7 Oct 11
Change-control trigger: YES: v3.2 teach-first coaching (GAP 71, approved by Om, check_plan PASS, 0 hours added)
```

## DSA tracker
| Problem | First solved | D1 | D3 | D7 | D14 | D28 | Result |
|---|---|---|---|---|---|---|---|
| 155 Min Stack | 2026-10-10 | 10-11 PASS (42c157e, Claude) | 10-13 PARTIAL (cf49bd9, Claude) | due 10-17 | due 10-24 | due 11-07 | NEW PASS (640354f, f17e69b, Claude): PARTIAL Oct 10 (interview 3/6), repair correct Oct 11, final 4/6; code correct, planted bugs 5/5 |
| 20 Valid Parentheses | 2026-10-04 | 10-05 PASS (47153c1) | 10-07 PASS (0168425) | 10-11 PARTIAL (8647552), 10-15 min | due 10-18 | due 11-01 | D7 code and CI #87 PASS; D7 complexity not recorded before coding, so D7 PARTIAL. No repeat today; D14 Oct 18 |
| 143 Reorder List | 2026-09-24 | 09-25 | missed | 10-02 PASS (1d late) | 10-08 PARTIAL (781a8f4), independent cold authorship not verified | due 10-22 | CI #84 green, algorithm and tests correct; D14 commit reuses unchanged D7 logic, no same-day retry |
| 19 Remove Nth From End | 2026-09-23 | - | 09-26 | 10-02 FAIL (copied), 10-03 PASS | 10-07 PASS (4d7796f) | due 10-21 | Correct dummy/two-pointer solution; CI 82 green. Minor notation slip only: use O(L) for list length rather than O(n), since n is the deletion index |
| 141 Linked List Cycle | 2026-09-22 | - | 09-25 | 09-29 | 10-06 FAIL, repair complete (566dea4) | due 10-20 | Original COLD had real code-correctness bugs, so it was not a clean pass. Same-day repair is correct and CI run 81 green. The extra mechanism/trace/trade-off interview was invalid for a spaced COLD and is discarded. No further work until D28 |
| 21 Merge Two Sorted Lists | 2026-08-30 | - | - | - | - | 09-27 | schedule complete |
| 206 Reverse Linked List | 2026-08-29 | - | - | - | - | 09-26 | schedule complete |
| 707 Design Linked List | 2026-08-29 | - | - | - | - | - | no cold in git; counted to match the Oct 1 total of 21 |
| 977 Squares of a Sorted Array | 2026-07-21 |  |  |  |  |  | pre-plan; no cold in git |
| 344 Reverse String | 2026-07-21 |  |  |  |  |  | pre-plan; no cold in git |
| 11 Container With Most Water | 2026-07-21 |  |  |  |  |  | pre-plan; no cold in git |
| 128 Longest Consecutive Sequence | 2026-07-20 |  |  |  |  |  | pre-plan; no cold in git |
| 347 Top K Frequent Elements | 2026-07-20 |  |  |  |  |  | pre-plan; no cold in git |
| 238 Product of Array Except Self | 2026-07-17 |  |  |  |  |  | pre-plan; no cold in git |
| 643 Maximum Average Subarray I | 2026-07-15 |  |  |  |  |  | pre-plan; colds 07-15, 07-21 |
| 3 Longest Substring Without Repeating | 2026-07-04 |  |  |  |  |  | pre-plan; colds 07-04, 07-21 |
| 121 Best Time to Buy and Sell Stock | 2026-06-12 |  |  |  |  |  | pre-plan; cold 07-21 |
| 167 Two Sum II | 2026-06-12 |  |  |  |  |  | pre-plan; cold 07-21 |
| 125 Valid Palindrome | 2026-06-12 |  |  |  |  |  | pre-plan; cold 07-21 |
| 49 Group Anagrams | 2026-06-08 |  |  |  |  |  | pre-plan; cold 07-21 |
| 1 Two Sum | 2026-05-23 |  |  |  |  |  | pre-plan; cold 06-12 |
| 242 Valid Anagram | 2026-05-23 |  |  |  |  |  | pre-plan; cold 07-21 |
| 217 Contains Duplicate | 2026-05-23 |  |  |  |  |  | pre-plan; cold 07-21 |
| 682 Baseball Game | 2026-10-03 |  |  |  |  |  | DRILL, not counted; space O(n) and tests fix open |

Count check: 23 counted rows = 23 total; 16 rows with a cold = 16 cold (155 D1 on 10-11).

## Contingency
| Week | Unit | Hours | Reason | Total used | Remaining (of ~50 from v3.3; ~55 before) |
|---|---|---|---|---|---|
| W0 | - | 0 | - | 0 | 55 |

## Later-refactor log
- 2026-10-06: SCORING FRAMEWORK GAP under review with both coaches: replace binary/global verdict behavior with task-specific rubrics; default bands where no explicit rubric exists are PASS >=85, PARTIAL 70-84, DEVELOPING 50-69, FAIL <50; preserve explicit machine-coding/design/checklist thresholds; second non-PASS on the same gap switches to learning mode; verdict preflight must name task type, rubric, evidence, untaught exclusions and next action. Pending Om approval before plan edit.
- 2026-10-06: APPROVED AMENDMENT by Om for DSA miss handling: no same-session retry loops. A failed NEW/COLD attempt is preserved and scored once; the exact bug or taught-concept gap is recorded and put in a bounded repair queue. Repair happens in a later DSA slot, never by repeatedly rewording questions the same day. Untaught concepts remain TEACHING GAP, not FAIL. Scheduled colds keep priority; repair cannot steal time from other tracks.
- 2026-10-06: PROCESS BUG found in LC141 D14: ChatGPT applied the NEW-DSA 3-question unit interview to a spaced COLD re-solve and also tested an untaught formal Floyd proof. v3.3 actually defines COLD as approach + complexity before coding, problem-derived asserts, and a 10 min Easy / 15 min Medium timebox; NEW DSA gets the mechanism/trace/transfer interview. Effective immediately both coaches must label DSA work NEW/DRILL/COLD before questioning and use only that path. Untaught material = TEACHING GAP, not cold FAIL. Separate GAP pending Om approval: audit whether DSA's protected/daily allocation is overweight versus India senior-loop evidence.
- 2026-10-05: check_plan.py docstring still names v3.1. Done Oct 5: upgraded script uploaded to the Claude project.
- 2026-10-05: coach test-folder rule, Checklist D coverage gap and Fluent Python placement are in the v3.3 draft; done: v3.3 uploaded to the Claude project Oct 5.
- 2026-10-05: plan and checker master copy now in `plan/` (Om approved). Next plan revision: write this into section 12 (file hygiene). No re-upload needed until then.
- 2026-10-05: two-coach operating model approved by Om (Claude outbox 5b3428f, ChatGPT outbox ca831e4). Write into plan section 0 at the next revision.

## Verdict log
(newest on top)
- 2026-10-13 LC155 D3 COLD PARTIAL (cf49bd9, Claude): code and tests correct; Way 3 time written as O(n), it is O(1); fix at D7 Oct 17. Authorship confirmed by Om (code from memory, tests reused); O(n) recorded as a writing slip.
- 2026-10-11 NEW 155 Min Stack PASS (Claude): queued repair answered correctly in the next DSA slot (space-saving pop check is really ==, and why); interview final 4/6. Was PARTIAL Oct 10.
- 2026-10-11 LC155 D1 COLD PASS (42c157e, Claude): approach and complexity first; full and space-saving versions both correct (0/20,000 vs brute force); planted bugs 5/5 caught; about 20 min.
- 2026-10-11 LC20 D7: one verdict, PARTIAL (ChatGPT). Claude withdraws its PASS: complexity before coding is required for a COLD (s7). Om took 10-15 min.
- 2026-10-11 12:49 IST LC20 D7 COLD PARTIAL (8647552, ChatGPT): stack implementation correct, CI #87 green; D7 source states approach but omits complexity proof. No extra interview/retry; D14 Oct 18. Record `chatgpt/tests/dsa/2026-10-11-LC20-D7-COLD.md`.
- 2026-10-11 LC20 D7 COLD PASS (8647552, Claude): correct on all 2,015,539 bracket strings up to length 8, 71 green; complexity not written before coding; add a mismatched-closer assert such as "(])" at D14.
- 2026-10-10 NEW 155 Min Stack PARTIAL (640354f, f17e69b, Claude): code correct (0/20,000 mismatches vs brute force), tests catch 5/5 planted bugs; interview 3/6 scored once, transfer local FAIL on the space-saving pop/push rules, taught; same-session retries were a Claude slip vs the Oct 6 amendment and are not counted; one repair question queued for the next DSA slot (max 5 min). Record: claude/tests/dsa/2026-10-10-LC155-NEW-min-stack.md
- 2026-10-07 LC20 D3 COLD PASS (0168425, ChatGPT): correct stack solution and complexity; CI 83 green; no extra interview.
- 2026-10-07 LC19 D14 COLD PASS (4d7796f, ChatGPT): correct approach and implementation, CI run 82 green; O(n) vs O(L) notation retained as a minor note only, no retry.
- 2026-10-06 LC141 D14 record corrected (ChatGPT): original COLD remains FAIL on code correctness; repair 566dea4 is correct with CI run 81 green. The added 3-question interview was invalid for a spaced COLD under v3.3 and its scores are discarded. No further work until D28.
- 2026-10-06 LC141 D14 retry-2 FAIL (adabe02, ChatGPT): CI green, but test now expects None; implementation still violates the bool return contract. Test must require False, and code must satisfy it.
- 2026-10-06 LC141 D14 retry FAIL (e528730, ChatGPT): CI green and dereference crash fixed, but odd-length acyclic input returns `None`; add explicit False after loop and a strict boolean assertion.
- 2026-10-06 LC141 D14 FAIL (51288a4, ChatGPT): CI green but hidden even-length acyclic case crashes at `fast.next.next`; repair loop guard and explicit False path, then retry.
- 2026-10-05 Plan v3.2 canonical: ChatGPT merge plus 3 Claude fixes; uploaded to the Claude project, byte-identical, check_plan PASS 503h; v3.1 removed; project instructions updated. ChatGPT project: Om to verify.
- 2026-10-04 W0 DSA PASS: LC20 cold proof 5/6 after one prompted fix (ChatGPT); LC20 tests still need "(]", "]", "((".
- 2026-10-04 W0 close: FAIL provisional (DSA only; MC1, Y2, G1, R1 not done); DSA 22/14.
- 2026-10-04 NEW 20 PARTIAL (2aa3ae4): code, approach and complexity correct; 2 planted bugs survived; add "(]", "]", "((". Claude closed it on code alone, without the cold questions.
- 2026-10-03 682 Baseball DRILL (e692c3f): code correct; space O(n) fix and spec examples 27 and 0 pending.
- 2026-10-03 19 D7 PASS closed (49d4a5e): 62/62 green, 4/4 planted bugs caught, docstring gap n+1 and O(L) fixed.
- 2026-10-03 19 D7 trace PASS: slow ends before target, gap n+1, fast ends at None.
- 2026-10-02 19 D7 FAIL: code copied from Sep 26 file (cb546b7, Om confirmed); redone Oct 3.
- 2026-10-02 to_list cycle-masking bug fixed (aa2219d): now raises on a cycle; planted missing-cut bug in 143 caught.
- 2026-10-02 143 D7 PASS (d500d1a): 61/61 green on Claude clone; approach written, complexity missing.
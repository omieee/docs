# Phase 1 log
Source of truth: Phase1_Master_Plan_v3.3.md (uploaded to the Claude project 2026-10-05)

## Weekly closes
(Sunday: paste the section 7 template here, newest on top)

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
| 20 Valid Parentheses | 2026-10-04 | 10-05 PASS (47153c1) | due 10-07 | due 10-11 | due 10-18 | due 11-01 | NEW PASS; cold proof 5/6 after one prompt (ChatGPT); LC20 tests fixed (474569e); D1 tests still miss the unclosed-opener assert |
| 143 Reorder List | 2026-09-24 | 09-25 | missed | 10-02 PASS (1d late) | due 10-08 | due 10-22 |  |
| 19 Remove Nth From End | 2026-09-23 | - | 09-26 | 10-02 FAIL (copied), 10-03 PASS | due 10-07 | due 10-21 |  |
| 141 Linked List Cycle | 2026-09-22 | - | 09-25 | 09-29 | due 10-06 | due 10-20 |  |
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

Count check: 22 counted rows = 22 total; 15 rows with a cold = 15 cold (20 added D1 on 10-05).

## Contingency
| Week | Unit | Hours | Reason | Total used | Remaining (of ~50 from v3.3; ~55 before) |
|---|---|---|---|---|---|
| W0 | - | 0 | - | 0 | 55 |

## Later-refactor log
- 2026-10-05: check_plan.py docstring still names v3.1. Done Oct 5: upgraded script uploaded to the Claude project.
- 2026-10-05: coach test-folder rule, Checklist D coverage gap and Fluent Python placement are in the v3.3 draft; done: v3.3 uploaded to the Claude project Oct 5.
- 2026-10-05: plan and checker master copy now in `plan/` (Om approved). Next plan revision: write this into section 12 (file hygiene). No re-upload needed until then.
- 2026-10-05: two-coach operating model approved by Om (Claude outbox 5b3428f, ChatGPT outbox ca831e4). Write into plan section 0 at the next revision.

## Verdict log
(newest on top)
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
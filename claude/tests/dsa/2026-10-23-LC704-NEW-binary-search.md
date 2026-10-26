# LC704 Binary Search: first-time interview (Claude)

- Type: NEW DSA unit proof (plan s7: mechanism, trace, transfer, pattern-signal question from v3.5). Scored once, no same-session teaching or retry (s6.6 #11).
- Prerequisite: NeetCode binary search lesson 14 watched Oct 19 before the code (95dfe22); D1 and D3 re-solves passed Oct 21 and Oct 22. Taught, so scores stand.
- Artifact: dsa-python PR #10 head `3384b4a`, `Topics_Learning/Binary_Search/Simple_Binary_Search.py`. Claude fresh clone Oct 23 10:10 IST: 91 passed. Code correct vs brute force earlier (95dfe22, 0/6,513).
- Questions sent 10:12 IST, answers 10:52, Q3 clarification 10:54. Written, in chat, no notes, no code, no AI. Time: about [42m] elapsed, active not reported (logged as elapsed, not as an overrun).
- Owner note: ChatGPT's state.md (09:19) says Om moved coaching to ChatGPT this morning. Om opened this interview with Claude at 10:11, so Claude scored it. One verdict.
- Restored 2026-10-24 11:10 IST from the Oct 23 chat (claude.ai/chat/5685cee4-00d3-47c0-b4c8-af02d7595b13), text unchanged. On Oct 23 the file was written to a different folder from the clone that was committed, so commit 256c3d4 did not include it (coach error, logged Oct 24).

## Questions as asked and answers verbatim

**Q1 (mechanism).** In your 704 code, each time the loop runs, the search window is from `left` to `right`. What does the code know for sure about the target and this window? Then: why `left = mid + 1` and not `left = mid`? What would go wrong with `left = mid`?

> So when we calculate mid, we check if the target > or < mid .. as the initial array is sorted so just be checking mid we can say the target will not be < or > in either cases . the reason we move to mid + 1 or mid - 1 because we already check if target is > or < mid and if target is = mid that is we found the target and return that mid position and is in else part. Also if we keep left = mid there is a possiblity we will be in infinite loop when item is not found

Score 1/2. Right: mid is already checked, so leaving it out with `mid + 1` is safe; `left = mid` can loop forever. Missing: a clear statement of what stays true every round (if the target is in the list, it is somewhere between `left` and `right`; everything outside has been ruled out). Generous reading tested: "the target will not be < or > in either cases" says one side is ruled out after checking mid, not the whole-window rule.

**Q2 (trace).** Trace by hand: `nums = [-3, 0, 2, 5, 9, 12, 15]`, `target = 10`. For each round of the loop, write `left`, `right`, `mid` and `nums[mid]`. Then write `left` and `right` when the loop stops, and what the function returns.

> l = 0 , r = 6, m = 3, m[m] = 5;  10 > 5
> l = 4 , r = 6, m = 5, m[m] = 12; 10 < 12
> l = 4 , r = 4, m = 4, m[m] = 9; 10 > 9
> l = 5 , r = 4 While loop fails returns -1

Score 2/2. Every round right ("m[m]" read as `nums[mid]`).

**Q3 (transfer).** New problem you have not done. Same kind of sorted list, no repeats. If the target is in the list, return its index. If not, return the index where it would go so the list stays sorted. Example: `[1, 3, 5, 6]`, target `4` gives `2`. Starting from your 704 code, what is the smallest change, and why does it give the right index?

> As we saw in previous example in the last step when we are returning false at that time see what is the position of l and r: l = 5 , r = 4 While loop fails returns -1 .. so if we have to insert 10 it has to be 1 pos after position l and every thing after that should move one pos right

Neutral clarification (rule 9, wording "1 pos after position l" was unclear): "For the Q2 list and target 10, which exact index number would your changed function return? Just the number."

> It will return 5

Score 1/2 (needed a prompt). Right: the index (5, which is `left` when the loop stops) and the idea of using where `left` ends. Missing: the code change itself (`return left` in place of `return -1`) and why `left` is the right place.

**Q4 (pattern signal).** Here is the 704 problem in short: a list of different integers, sorted from small to large, and a target; return the target's index, or -1 if it is not there; your solution must run in O(log n) time. Which words in it tell you "use binary search"? Name two and say what each one lets you do. Then: if the O(log n) line were removed, would you still pick binary search? Why?

> sorted from small to large and in O(log n) time. this tell me to use binary search. The first one tels we can safely say if target is greter than mid or lesser than mid we can safely move in relvant direction and second line say we have to halve our search area evry iteration

Score 1/2. Both signals named and each one's use is right. Second part (O(log n) line removed) not answered.

**Total 5/8. No wrong conclusion. Verdict: PARTIAL.** Code and trace solid; the "why" is thin in Q1, Q3 and Q4. Same shape as 155 and 739 before their repairs.

## Correct answers (for the later teaching slot)

- Q1: every round keeps one rule: if the target is in the list at all, it is between `left` and `right`. A comparison with `nums[mid]` rules out mid and one whole side, so `mid + 1` / `mid - 1` drop only places the target cannot be. With `left = mid`, when `left == right` (or `right == left + 1`) and the target is bigger than `nums[mid]`, `left` never moves. Example `[1, 3]`, target 3: mid 0, 3 > 1, left stays 0, forever, even though 3 is in the list. So the loop can hang even when the target exists, not only when it is missing.
- Q3: change `return -1` to `return left`. When the loop stops (`left = right + 1`), every value before `left` is smaller than the target and every value from `left` on is bigger, so `left` is the first place the target fits. Check: `[1, 3, 5, 6]`, target 4 ends at `left = 2`.
- Q4: yes. "Sorted" is the real signal: one comparison throws away half. O(log n) only confirms it. Without that line, linear search also works, but binary search is the better answer and the one an interviewer expects for a sorted list.

## Repair queue

- Teaching: a separate later DSA slot, Sat Oct 24 after the 155 D14 and 19 D28 colds, about 10 min, Claude: the window rule with the `[1, 3]` hang, then `return left` with a trace.
- Retry: one fresh question in new wording at the 704 D7 cold, Mon Oct 26. Correct = NEW 704 PASS and it counts. Wrong = carries to D14, no loop.
- 704 is not counted until then (same as 155 and 739).

## Retry, Mon Oct 26 (Claude), after the D7 cold PASS (94d6a47)

- Separate item from the cold (s6.6 #11). Teaching was Sat Oct 24 [12m]. Sent 10:35 IST, answered 10:41, written in chat, no notes, no code, no AI. [6m].

**Question as asked.** `nums = [2, 4, 6, 8]`, target `7`, your 704 code with `while left <= right`. (a) When the loop stops, what are `left` and `right`? If the function had to return the place where 7 should go to keep the list sorted, which index is that, and in one sentence why is it right (what is true of every value before it, and every value from it onwards)? (b) Someone changes `right = mid - 1` to `right = mid`. Give one small list and target where the loop never stops, and say in one line why. (c) If the problem did not say "O(log n)", would you still pick binary search for 704? One line why.

**Answer verbatim.**

> 1. when loop stops left is at positin where value currently is 8 and instead of returning -1 will return left pointer right is 1 pos back of it which currently points at 6 all values before it will be lesser than 7 and all values after it will be greater than 7
> 2. `nums = [1,3]` and target `3` will break becaue it will run for ever .. because mid alone cal let window always same while mid - 1 decreases the window size each iteration
> 3. Yes I would still chose because the list is sorted .. O(logN) is just liek second confirmation that we should use bin search

**Scoring.**

- (a) Right. Generous reading tested (rule 9): left at the 8 is index 3, right at the 6 is index 2, return left = 3; everything before index 3 is below 7 and the value at it is above 7. Clears the Q3 gap (`return left` and why).
- (b) Wrong. [1, 3] with target 3 is the taught case for `left = mid`. With `right = mid` it does not hang: mid 0, 3 > 1, left becomes 1; mid 1, found, returns 1. The reason given (the window stops shrinking) is right in general, but the example is the old one, not worked for the changed line. A list that hangs: [5] with target 3 (mid 0, 3 < 5, right = 0, forever), or [1, 3] with target 0.
- (c) Right. Sorted is the real signal; O(log n) only confirms. Clears the Q4 gap.

**Result: retry 2 of 3 right. NEW 704 PASS, final 7/8** (Oct 23 5/8, plus Q3 and Q4 cleared), same rule as the LC739 repair that passed at 1/2 on Oct 17. The (b) miss stays recorded: the taught counterexample was recalled, not rebuilt for the mirror line. Teaching only, in a later separate slot of about 5 minutes (s6.6 #11), not scored; no further retry, since NEW 704 is closed. 704 now counts.

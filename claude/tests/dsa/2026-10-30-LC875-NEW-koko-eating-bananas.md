# LC875 Koko Eating Bananas: first-time interview (Claude)

- Type: NEW DSA unit proof (plan s7: mechanism, trace, transfer, pattern-signal question with its structural reason). Scored once, no same-session teaching or retry (s6.6 #11).
- Prerequisite: NeetCode binary search lessons 14 (Oct 19) and 15 "Search Range" (Oct 28, with 374 as a DRILL); Om watched the NeetCode 875 video before coding closed-book on Oct 29 (no AI, his report). Taught, so scores stand.
- Artifact: dsa-python PR #14 head `8021257` (merge `cd0bceb`), `Topics_Learning/Linked_List/LC_875_Koko_Eating_Banana.py`. Claude fresh clone Oct 29: 97 passed, ruff clean; 0/149,180 wrong vs brute force; deliberate mistakes 8/9 caught (`le = 0` survives; one assert with answer 1 still to add, no re-score).
- Questions sent about 10:28 IST, answers 10:40. Written in chat, no notes, no code open, no AI. Om had a hard stop at 10:55 (call 11:00). About [12m] active.
- Claude ran the Q2 trace and the Q3 example before scoring (piles [4, 9, 6], h 6 returns 4 in 4 rounds, hours 5, 10, 7, 6; weights [3, 2, 2, 4, 1, 4], 3 days gives 6).

## Questions as asked and answers verbatim

**Q1 (how it works).** In your code, when `hours <= h`, you do `res = min(res, k)` and `r = k - 1`, and the loop carries on. Why not just `return k` right there? And why is it safe to never look at any speed above k again?

> The reason we don't stop there is first of all question asks the least value of k .. and whenwe are doing hours <= h it means there is still possiblity that k can be even lower but we still want to preserve the latest k hence min(res, k).. it is safe not to look above because anything above the current k will be higher that current k and as the question is to find minimum

Score 2/2. Right: a smaller k may still work, so the search goes on; every speed above a working k is bigger, so none can be the smallest.

**Q2 (trace).** `piles = [4, 9, 6]`, `h = 6`. Run your code by hand. For each round of the loop, write `le`, `r`, `k`, `hours`, and which branch runs. Then write `le` and `r` when the loop stops, and what the function returns.

> 1: le=1, r=9, k=5, hours=6, branch: hours <= h runs
> 2: le=1, r=4, k=2, hours=10, branch: else runs
> 3: le=3, r=4, k=3, hours=7, branch: else runs
> 4: le=4, r=4, k=4, hours=6, branch: hours <= h runs
> Loop stops: le=4, r=3
> Returns: 4

Score 1.5/2. Every `le`, `r`, `k`, every branch, the end values and the return are right. One slip: round 1 hours is 5 (1 + 2 + 2), not 6. The branch is the same, so nothing after it changes.

**Q3 (changed problem).** A new problem you have not done. Packages with weights `[3, 2, 2, 4, 1, 4]` must be shipped in this order within `3` days. Each day the ship loads packages in order until the next one would go over its capacity C, and a package cannot be split. Find the smallest C that ships everything in 3 days (the answer here is 6). Using your 875 idea: (a) What are the smallest and the largest C you would search between, and why? (b) What replaces your `hours` loop, and what in your 875 code stays the same?

> Too much for asmall session this can be a good serate LC to be solved .. still i will answer hours will be replaced by days smallest will be 1 and largest will be sum of all containers

Score 1/2. (a) Largest C = sum of all weights: right, reason not given. Smallest C = 1: wrong; C must be at least the heaviest package (4 here), because a package cannot be split; with C below that, the greedy day count is not valid (for example weights [5, 5], 3 days, C = 1 counts 3 days and wrongly passes). (b) Days replace hours: right in name; how the days are counted and what stays the same (the binary search loop, `res`, `r = mid - 1` on a pass) not said.

Om's comment that Q3 was heavy for a 30-minute slot is fair: noted, transfer questions to stay smaller (not a safeguard break).

**Q4 (pattern signal).** The 875 problem in short: there are piles of bananas and h hours. Each hour, Koko picks one pile and eats k bananas from it; if the pile has fewer, she eats them all and waits out that hour. Find the smallest k that lets her finish within h hours. Which words in it tell you "use binary search"? There is no sorted list in this problem, so what plays the part of the sorted list, and why does binary search still work?

> The sorted idea comes from creating the minimum and maximum range we know what the maximum will tghe k value will be and then in that range we try to find the minimum k and that range is sorted [1 to max k]

Score 0.5/2. Partly right: the speeds 1 to max(piles) are in order and act as the list. Missing: the words ("smallest k" plus "within h hours": the least value that meets a limit), and the structural reason (the yes/no test "finishes within h" flips only once: every speed below the answer fails, every speed from the answer up passes, because a faster speed never needs more hours). Generous reading tested: "in that range we try to find the minimum k" names the goal, not the signal words or why halving is safe.

## Result

NEW 875 PARTIAL, 5/8. No wrong conclusion in the code questions; one local wrong answer (Q3 smallest C). Not counted until the retry; DSA stays 26 / 19.

Teaching in a later separate slot (about 10 min, not scored): (1) the yes/no test flips once, shown on 875 speeds 1 to 9 for the Q2 piles; (2) the signal words "smallest ... within"; (3) why the 1011-style lower bound is the heaviest package, with the [5, 5] counterexample. Then one fresh retry, smaller, in another slot. Q2 hours slip: one line in the teaching slot.

Colds from first solve Oct 29: D1 due Oct 30, slides to Sat Oct 31 (today's slot was the interview); D3 Nov 1, D7 Nov 5, D14 Nov 12, D28 Nov 26, D90 2027-01-27.

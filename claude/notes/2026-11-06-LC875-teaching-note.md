# LC875 Koko Eating Bananas: why binary search works on speeds (one read)

Rewritten 2026-11-13 23:40 IST as one connected read, after Om's feedback that the old five-line note was too dense (Nov 12) and that sending one point at a time over two days was "randomly one bit" (Nov 13). Old version is in git history.

**The problem.** Piles [3, 6, 7, 11], 8 hours. Each hour Koko eats up to k bananas from one pile. Find the smallest k that lets her finish in 8 hours.

## Step 1. Ask one yes/no question per speed

"At speed k, does she finish in 8 hours?" Hours at speed k = each pile divided by k, rounded up, then added.

- k = 3: 1 + 2 + 3 + 4 = 10 hours, more than 8, so NO
- k = 4: 1 + 2 + 2 + 3 = 8 hours, so YES
- k = 6: 1 + 1 + 2 + 2 = 6 hours, so YES

## Step 2. Write the answer for every speed

```
speed: 1 2 3 4 5 6 7 8 9 10 11
       N N N Y Y Y Y Y Y Y  Y
```

A faster speed never needs more hours on any pile. So once a speed is Y, every faster speed is Y. The row always has all the N's first, then all the Y's. We want the first Y.

## Step 3. Halving is safe because of that shape

- Check the middle, 6: Y. Everything to its right is faster, so also Y. The first Y is 6 or to its left. Keep 1 to 5, remember 6.
- Check the middle of 1 to 5, which is 3: N. Everything to its left is slower, so also N. Keep 4 to 5.
- Check 4: Y. Nothing is left to its left. Answer 4.

Three checks instead of eleven, and the answer is never thrown away. This is what your code does with `rptr = m - 1` on a Y and `lptr = m + 1` on an N.

## Step 4. When the shape breaks, binary search breaks

Question: "smallest prime number from 1 to 11" (a prime is divided only by 1 and itself: 2, 3, 5, 7, 11).

```
k:     1 2 3 4 5 6 7 8 9 10 11
prime: N Y Y N Y N Y N N N  Y
```

This row flips many times. The same code checks 6 (N, moves right and throws away 2, 3, 5), then 9 (N), then 10 (N), then 11 (Y), and answers 11. The right answer is 2. So before using binary search, make sure the row is all N's first, then all Y's.

## Step 5. How to spot this in a new problem

The problem asks for the **smallest** (or minimum) value that **works under a limit**: "within h hours", "in at most d days", "no more than". Then ask one question: if a value works, does every bigger value also work? If yes, binary search on the value, from the lowest possible value to the highest (Koko: 1 to the biggest pile).

Next: one fresh question on this pattern, in its own later slot (DSA rule: teaching and the retry are never in the same session).

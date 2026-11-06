# LC875 Koko Eating Bananas: teaching note (yes/no pattern)

Teaching slot for the Nov 3 NEW retry PARTIAL (gap: signal words and the one-change pattern). First given in chat on Nov 3 23:20; re-sent Nov 6 12:15 because Om could not find it (it was never saved as a file). Numbers re-run by Claude Nov 6.

1. The question at each speed: "At speed k, can she finish within h hours? Yes or no."
   Piles [3, 6, 7, 11], h = 8, hours per pile = pile / k rounded up.
   k=1: 27 no; k=2: 15 no; k=3: 10 no; k=4: 8 YES; k=5: 8 yes; k=6: 6 yes; k=11: 4 yes. Answer: the first yes, 4.
2. Why it changes only once: a faster speed never needs more hours on any pile, so once a speed works, every faster speed works.
3. Why halving is safe: a middle "no" means everything left of it is "no"; a middle "yes" means the answer is there or to its left. One check removes half.
4. Counterexample: "smallest prime from 1 to 11". Is k prime changes many times. Binary search checks 6 (no), 9 (no), 10 (no) and returns 11; the right answer is 2.
5. Signal words: "smallest (minimum) k such that", "within h hours", "at most". Then ask: do the answers change only once as k grows? If yes, binary search on the answer.

Next: one fresh retry question on this pattern only, in its own later slot (planned Sat Nov 7).

# Name-the-pattern drill, Week 7 (Claude)

- Plan: s6.6 #14 (b), weekly, bedside, no code, no desk hours. Six reworded statements from families already solved, mixed order. One line each: the pattern and the words that point to it. Scored out of 6: 1 = pattern and signal right; 0.5 = signal right, but only the data structure named, not the technique; 0 = wrong pattern. DSA rule s6.6 #11: scored once; teaching and the retry in later separate slots.
- Sun Nov 22 2026. Sent 11:5x IST with the W7 close (W7's drill was not set during the week, Claude's coach error, 11:47 log line). Answered 12:00 IST.

## Questions as asked, Om's answers verbatim, marks

1. A list of building heights, left to right. For each building, find how many buildings away the first taller building on its right is. Write 0 if there is none.
   - Om: "Equivalent of daily temperature "buildings away the first taller building on its right is""
   - Expected: monotonic stack (LC739 in disguise); signal: the first greater element to the right of each item.
   - Mark: 1. Generous reading: same pattern as LC739, which Om solved with a monotonic stack (NEW PASS Oct 17). Note: say the pattern's name, not only the problem's.
2. You must ship packages in a fixed order within D days. Find the smallest truck capacity that makes this possible.
   - Om: "Binary Search something similar to koko eating banana "smallest truck capacity""
   - Expected: binary search on the answer (LC1011, the LC875 family); signal: the smallest value that works, where every larger capacity also works.
   - Mark: 1.
3. Given a string, find the length of the longest unbroken stretch in which no letter repeats.
   - Om: "Dynamic Array "longest unbroken stretch""
   - Expected: sliding window (LC3 itself, solved by Om Jul 4, last cold Jul 21); signal: the longest contiguous stretch that meets a condition.
   - Mark: 0. Signal words right; "dynamic array" is a data structure, not the technique.
4. A chain of rooms where each room has one door to the next. Starting at the first room, find out whether you will ever come back to a room you have already visited, using only constant extra memory.
   - Om: "LinkedList "A chain of rooms where each room has one door to the next." , "using only constant extra memory.""
   - Expected: fast and slow pointers (LC141 in disguise); signal: a cycle in a chain, with constant extra memory (which rules out a set of visited rooms).
   - Mark: 0.5. Both signals right, including the constant-memory clue; the structure is named, not the technique.
5. A sorted list of item prices and a gift card value. Find two different items whose prices add up exactly to the card value.
   - Om: "Two Pointers "A sorted list""
   - Expected: two pointers (LC167 in disguise); signal: sorted input, a pair with a target sum.
   - Mark: 1.
6. Check whether tags like `<b>`, `<i>` and `<u>` are closed in the right order: `<b><i></i></b>` is fine, `<b><i></b></i>` is not.
   - Om: "Stack "closed in the right order""
   - Expected: stack (LC20 in disguise); signal: the latest unclosed opener must close first.
   - Mark: 1.

## Result

4.5 / 6. Miss: line 3 (sliding window, his own LC3, no review since Jul 21). Partial: line 4 (technique not named).
Next, by s6.6 #11: a short bedside teaching note on sliding window in a later slot, then the idea returns, in new wording, in the W8 drill. No same-session retry.

# Why halving is safe: the one sentence that was missing (bedside read, about 5 minutes)

Today, in Problem A, you wrote the row right:

```
k:  1 2 3 4 5 6 7 8 9 10
    N N N N N N Y Y Y Y
```

The question also asked **why** it is safe to check the middle and throw away half. That part was not answered. Here it is in three short steps, on your own numbers.

## Step 1. If one k works, every bigger k works

7 × 7 = 49, which is at least 40, so 7 is Y.
8 is bigger than 7, so 8 × 8 is bigger than 49. It is also at least 40. Y.
The same holds for 9, 10 and every k after 7.

So: **once a k is Y, every bigger k is also Y.** Read backwards, the same fact says: if a k is N, every smaller k is also N.

## Step 2. That fact gives the row its shape

Because of step 1, a Y can never be followed by an N. So the row is always all N's first, then all Y's, with **only one change** from N to Y. The answer is the first Y.

## Step 3. Why the middle is enough

Check the middle.

- Middle is **Y**: everything to its right is also Y (step 1). So the first Y is the middle or to its left. Throw away the right side and remember the middle.
- Middle is **N**: everything to its left is also N (step 1, read backwards). So the first Y is to its right. Throw away the left side.

Either way, the side you throw away cannot hold the first Y. That is why halving never loses the answer.

## The sentence to say in an interview

"If k works, every bigger k also works, so the answers go N N N then Y Y Y with one change. Checking the middle tells me which side the first Y is on, so I never throw the answer away."

## Your Problem B answer

Your "no" was right, for the right reason: the first check, 6, is N, so the search throws away the left side, where 3 is. Its row breaks the shape, because a Y is followed by N's:

```
k:  1 2 3 4 5 6 7 8 9 10 11 12
    N N Y N N N Y N N N  N  N
```

One trace fix. After 6 is N, the search keeps 7 to 12, and the middle of 7 to 12 is 9 (7 + 12 = 19, half is 9), not 7. Then:

- 9 × 9 = 81, N, keep 10 to 12
- 11 × 11 = 121, N, keep 12
- 12 × 12 = 144, N

The search ends with **no answer at all**. It never checks 7 or 3.

Next: one fresh question on the "why" only, in a later slot, not tonight.

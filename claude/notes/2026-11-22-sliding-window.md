# Sliding window, for tonight's bedside read

In this morning's drill, line 3 was your own LC3 from July: "longest unbroken stretch with no repeated letter". You read the signal right. You only needed the name of the method, so here it is again.

**What it is.** You keep a window over the string: a left edge and a right edge, and only the letters between them count. The right edge moves forward one letter at a time. When the window breaks the rule (here, a letter repeats), you move the left edge forward until the rule holds again. The answer is the best window you saw on the way.

**Watch it on "pwwkew".** The window is the letters between left and right.

| Right edge reads | What happens | Window | Best so far |
| --- | --- | --- | --- |
| p | add it | p | 1 |
| w | add it | pw | 2 |
| w | repeat, so move left past p, then past the old w | w | 2 |
| k | add it | wk | 2 |
| e | add it | wke | 3 |
| w | repeat, so move left past the old w | kew | 3 |

The answer is 3.

**Why it is fast.** Each letter comes into the window once and goes out at most once. That is the same reason you gave for Daily Temperatures: pushed once, popped at most once. So it is about 2n steps, O(n). Brute force checks every start with every end, which is about n x n stretches.

**The signal, in one line.** Longest, shortest or maximum, plus an unbroken stretch (substring, subarray, consecutive days), plus a rule the stretch must keep. If the items do not have to sit next to each other, it is not a window.

**Why "dynamic array" was not it.** A dynamic array is where you keep things: Python's list, which grows as you add. Sliding window is how you search. The drill asks for the how.

Try this in your head, no answer needed tonight: in "abba", what does the window look like after each letter?

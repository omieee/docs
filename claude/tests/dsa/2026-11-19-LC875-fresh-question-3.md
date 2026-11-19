# LC875 Koko Eating Bananas: third fresh question, why it fits and why halving is safe (Claude)

- Type: the one fresh question owed after the Nov 18 second fresh question (PARTIAL 2/4). It is part of 875's NEW retry, not a spaced cold. Scored once; no teaching or retry in this session (s6.6 #11).
- Taught before: bedside read `claude/notes/2026-11-18-LC875-fit-vs-safe.md` (two questions that sound alike: 'why does it fit' asks for the words, 'why is it safe' asks for the fact), sent Nov 18 night. Om, Nov 19 09:19: read it last night. Separate slot from the teaching: yes (Wed night vs Thu morning).
- Asked Thu Nov 19 about 09:20 IST. Answer sent 09:34, so about 14m elapsed vs a 15-minute box. Om did not write a start time. Cold in chat: no notes, no code, no AI.
- Claude ran the numbers before asking: time = ceil(48 / s). For s = 1 to 12: 48, 24, 16, 12, 10, 8, 7, 6, 6, 5, 5, 4 minutes. At most 5 minutes: N N N N N N N N N Y Y Y, answer s = 10. First middle (1 + 12) // 2 = 6, 8 minutes, N, keep 7 to 12.
- Scoring set before the answer (Claude's working, the same scheme as Nov 18; written into this file after the answer): Q1 2 points (1 for 'smallest speed', 1 for 'at most 5 minutes'). Q2 2 points (1 for the fact: a faster speed never makes the download slower, so if s works every bigger s works, or if s fails every smaller s fails; 1 for the link: so the row is N's then Y's with one change, and the middle tells which side the first Y is on). PASS 3.5 or 4 with the fact given as the answer to Q2; PARTIAL 2 to 3; FAIL below 2. The 'Asked:' lines are recorded, not scored.

## Question as asked

A file is 48 MB. At a download speed of s MB per minute, the download takes 48 ÷ s minutes, rounded up. You want the smallest speed s, from 1 to 12, that finishes the download in at most 5 minutes. You don't need to solve it.

1. Which words in this problem tell you binary search fits?
2. After you check the middle speed, binary search throws away half the speeds without checking them. Why is that safe? Answer in one or two sentences, in this problem's own words (speed, minutes).

Start each answer with an "Asked:" line, the habit from last night's note.

## Om's answer, verbatim

> So as your question says there is 48 Mb total task which needs to be done within 12 min so the range is from 1 to 12 Min we have to find the smallest possible speed. So what happens is for say we doenald at 1 Mb/min to complete 48 MB we need 48 Min that is above 12 so now lets look 2 then we need 24 Min at 3 we need 16 Min .. at 4 we need 12 Min at 5 we need 10 Min, at 6 we need 8 MB/Min, at 7 we need 7Min, at 8 we need 6, At 9 we need 6, At 10 -> 5, At 11 -> 5, At 12 we need 4 ... So can you see a pattern 1->NO, 2->No, 3->No, 4->No, 5->No, 6->No, ... 11 -> Yes, 12 -> Yes
>
> 1. So by looking at the pattern we can say the words "smallest speed s" and "atmost 5 min"
> 2. It is safe because if the mid number say 6MB/Min is not good enough nothing less than 6MB will be good enough.. So we can safely discard looking 1-5 and fix our focus on right side and calculate the next mid and see if that is enough or not if not then again discard

## Scores

- Q1 2/2. 'smallest speed s' and 'atmost 5 min': both signal words, and the right kind of answer for 'why does it fit'.
- Q2 2/2. Fact 1/1: 'if the mid number say 6MB/Min is not good enough nothing less than 6MB will be good enough' is the fact in its fail-side form (if s fails, every smaller s fails), given as the answer to 'why is it safe'. This was the open gap from Nov 18, where Q1 gave the signal words instead. Link 1/1: his No ... Yes row above the answers, plus 'discard 1-5 and fix our focus on right side', says the first Yes can only be right of the middle. Generous reading tested (s0 rule 9): 'discard 1-5' leaves 6 unnamed, but 'focus on right side' puts 6 out too; not unclear, so no neutral question.

## Recorded, not scored

- No 'Asked:' lines were written.
- The opening line misread the numbers: it says the task 'needs to be done within 12 min' and checks 48 minutes against 12. In the question, 12 is the highest speed and the limit is 5 minutes. The answers themselves use 5 minutes correctly, so no score changes. This is the reading slip the 'Asked:' habit is meant to catch.
- Interview polish, logged once: add the reason behind the fact, 'because a slower speed can never take fewer minutes'. Computing all 12 speeds was not needed; binary search checks only about 4 middles.

## Result

PASS, 4/4. 875's NEW retry closes: all gaps from Oct 30 (direction, lower bound, signal words, the yes/no pattern, why halving is safe) are now closed, in four separate slots. 875 counts from today: DSA 27 / 20. 875 D28 on Thu Nov 26 is a separate spaced cold with no interview.

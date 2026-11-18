# LC875 Koko Eating Bananas: second fresh question, why halving is safe (Claude)

- Type: the one fresh question owed after the Nov 14 fresh question (PARTIAL 4.5/6), on the why only. Scored once; no teaching or retry in this session (s6.6 #11).
- Taught before: bedside read `claude/notes/2026-11-14-LC875-why-halving-is-safe.md`, read Nov 16-17 (Om: 'Finished reading' Nov 17 00:10). Separate slot from the teaching: yes (Wed morning vs Tue 00:10).
- Asked Wed Nov 18 09:37 IST. Om's start 09:39, answer sent 09:43, so [4m] vs a 15-minute box. Cold in chat: no notes, no code, no AI.
- Claude ran the numbers before asking: time = ceil(60 / p). For p = 1 to 10: 60, 30, 20, 15, 12, 10, 9, 8, 7, 6 minutes. At most 8 minutes: N N N N N N N Y Y Y, answer p = 8. First middle (1 + 10) // 2 = 5, 12 minutes, N, keep 6 to 10.
- Scoring set before the answer: Q1 2 points (1 for the fact: more printers never make the job slower, so if p fits every bigger p fits, or if p fails every smaller p fails; 1 for the link: so the row is N's then Y's with one change, and the middle tells which side the first Y is on). Q2 2 points (the same fact used on the N side: fewer than 5 printers take at least 12 minutes, so they also fail). PASS 3.5 or 4 with the fact stated; PARTIAL 2 to 3; FAIL below 2.

## Question as asked

A print job has 60 pages. With p printers working together, the job takes 60 ÷ p minutes, rounded up. You want the smallest p, from 1 to 10, that finishes the job in at most 8 minutes. You don't need to solve it.

1. Before checking any number, explain to an interviewer in one or two sentences why binary search on p is safe here. Use this problem's own words (printers, minutes).
2. The first middle is p = 5: 60 ÷ 5 = 12 minutes, which is too slow. Binary search now throws away 1, 2, 3 and 4 without checking any of them. How do you know none of them can be the answer?

## Om's answer, verbatim

> Start: 9:39
>
> 1. Binary search should be the approach because we are asked smallest p and at most 8 minutes gives us the hint that binary search should work
> 2. Because if with value 5 it is taking 12 minutes nothing less than 5 will finish faster than 12 minutes hence it is safe to throw everything left including 5 and left will become 5 + 1 = 6

## Scores

- Q1 0/2. Generous reading tested (s0 rule 9): the answer names the signal words ('smallest p', 'at most 8 minutes'), which tell you binary search fits; that is the Nov 14 Q1 question, not this one. It gives no reason why throwing away half is safe: neither the fact (more printers never make it slower) nor the one-change row. Not unclear, so no neutral question was needed.
- Q2 2/2. Right, in Om's own words: fewer than 5 printers cannot finish faster than 12 minutes, so they are all too slow and can go, 5 included, and the left end moves to 6. This is the fact itself, used on the side where it matters. First time in four tries that Om states it unprompted.

## Result

PARTIAL, 2/4. Closed today: the fact behind halving (Q2). Still open: giving that fact as the answer when asked 'why is it safe', instead of the signal words. 875 not counted yet; DSA stays 26 / 19.

Section 9 trigger 2 (repeated failed learning on one unit), Claude's call, Om decides: not raised. The missing reason was produced correctly in Q2, so the understanding has landed; what remains is answering the question that was asked. If Om or ChatGPT reads it the other way, it goes to Om.

Next (s6.6 #11): a short teaching read in a later, separate slot (bedside tonight is fine): 'why does it fit' and 'why is it safe' are two different questions, with Om's own Q2 sentence as the model answer. Then one fresh question, both questions together, in a slot after that, not the same night. 875 D28 on Thu Nov 26 is a separate cold with no interview.

# MC1 Snake and Ladder: timed rep 1 (diagnostic)

- Date: Tue 2026-10-20 IST. Week W3 (Oct 19-25), Phase1_Master_Plan_v3.4, s6.5 rep 1.
- Invigilator and verifier: Claude. 60-min review: ChatGPT (from these findings).
- Clock: started 12:11 IST when the problem link was given; Claude kept the time (Om's ask). No pause. Minute-60 change given 13:11. Submitted 13:41. Commit `d78048e` at 13:40:37. Active **[90m]**.
- Spec: workat.tech practice page only (https://workat.tech/machine-coding/practice/snake-and-ladder-problem-zgtac9lxwntg). Editorial not opened (Om). No AI (Om).
- Artifact: lld-patterns PR #2, branch head `d78048e`, folder `mc01-snake-and-ladder/`.
- Rules settled before the clock (Om, 12:07): plain `assert` tests in a separate file count fully (pytest not taught yet); concurrency not asked, so it is left out: 5 parts, 10 marks, pass = runs end to end and 7/10.

## Om's requirement questions during the rep, verbatim, with Claude's interviewer answers

1. 12:16 Om: "Can i assume input only from cli or do i need to build afile parser"
   Claude: reading from the command line is enough; no file parser needed; input format as on the page.
2. 12:18 Om: pasted the sample input, then "are the inputs : 62 5 is snake head at 62 ad 5 is tail correct .. so will the inpout be in this format of some list"
   Claude: yes, `62 5` = head 62, tail 5; `2 37` = ladder from 2 to 37; input is plain text lines in that order (snake count and lines, ladder count and lines, player count and names), not a ready-made Python list.
3. 12:19 Om: "it says unique random each time but python's random() doesnot gurantee the next roll wil not give same value does that need to be taken care of ?"
   Claude: no; a die can repeat; each roll is a random value 1 to 6.
4. 12:20 Om: "...will it be automated like automatically the code will play one for player 1 and next roll for player 2 or each time i need to click any button"
   Claude: fully automatic; turns go in input order; one printed line per move; stops when a player reaches 100.
5. 12:21 Om: "Ok Now i am taking notes"

## Minute-60 change, as given at 13:11

1. If a player rolls a 6, the same player rolls again straight away.
2. If a player rolls three 6s in a row in the same turn, all three rolls are cancelled. The player goes back to the position they had before the first 6, and the turn passes to the next player.
3. Print one line for every roll, in the same format as before.
4. Add at least one test for this new rule.

## Evidence (Claude's own fresh fetch and run, `git fetch origin refs/pull/2/head`)

- `python3 main.py < sample` (the page's sample, plus the empty line the program waits for): prints only the input prompt, then loops forever; killed by `timeout 10`, exit 124. No move lines, no winner.
- Probes on the committed functions (PYTHONDONTWRITEBYTECODE=1):
  - `getInputs()` on the sample: players `Gaurav`, `Sagar` right; 9 snakes right, as ints; ladders = `[('93', '73')]`: one entry, read from a snake line, as strings (main.py line 53 `range(number_of_ladder, number_of_ladder + 1)`).
  - `Player.SetPos(5)` returns 0 and leaves pos 0: it saves only positions above 100 (player.py line 10), the opposite of the rule.
  - `move_pos` with the correct snake and ladder lists: at 0 rolling 2 (ladder 2 to 37) returns 2; at 60 rolling 2 (snake 62 to 5) returns 62; at 78 rolling 3 (ladder 81 to 100, last in the list) returns 100. Only the last snake and the last ladder are ever applied: the `else` branches (lines 81-82, 87-88) overwrite an earlier match, and the ladder loop also overwrites the snake result.
- Game loop (lines 100-102): the value from `move_pos` is not stored, `next_player` never changes, nothing is printed, and the condition `p1.pos != 100 or p2.pos != 100` does not stop when one player reaches 100.
- `src/snake.py` and `src/ladder.py` are empty; `Board` is created but unused; player count fixed at two (last two lines).
- Minute-60 rule: not started. Tests: none.
- Planted-bug check (Claude changes code on purpose in a copy to see whether the tests catch it): not run, there are no tests.
- Notes: `docs/idea.md` came in the same single commit as the code (13:40); the plan asks for raw notes committed before coding. Logged once, not scored.

## What is right

- The requirement notes capture the core rules correctly, including start at 0, exact 100 to win, overshoot means no move, snake head to tail, ladder bottom to top.
- Snake parsing and the dice (`random.randint(1, 6)`) are correct.
- Files split by concern (src/, main.py, docs/).
- Om asked four useful clarifying questions in the first 10 minutes (input source, input format, dice repeats, automatic play), which is the MC0 method in use.

## Score (s7 machine-coding rubric, 0-2 each; concurrency left out by Om's rule)

| Part | Score | Why |
| --- | --- | --- |
| Runs end to end | 0 | Hangs on the sample; no move lines, no winner |
| Domain model | 1 | Right nouns (Board, Player, Snake, Ladder), but only Player has behaviour; Snake and Ladder empty; turns and rules live in loose functions in main.py with no owner |
| Extensibility after the minute-60 change | 0 | Not started |
| Readability | 1 | Short and split into files, but misleading names (`new_pos = roll_dice()` holds the dice value; `ladder_top_bottom` holds bottom then top), mixed naming styles (`GetPos` vs `move_pos`), the `getInputs` docstring is the sample input, unused `Board` |
| Tests | 0 | None |
| **Total** | **2/10** | |

**Verdict: FAIL** (does not run end to end; 2/10 against a pass of 7/10). Rep 1 is the diagnostic rep by plan (s6.5); it is now scored. Gate A needs reps 1 and 2 scored; Gate B needs the latest two reps to pass.

## Design interview

Not run today. The program does not run, so the unit cannot close today whatever the answers, and the gaps above are the 60-min review's teaching (ChatGPT, Om's Oct 18 split). Claude told Om plainly that this changes what Claude said before the rep.

## Gaps for the 60-min review (ChatGPT), in order

1. Getting a thin end-to-end path running first: read input, loop over turns, move, print, stop on a winner, before splitting into files.
2. A function's returned value must be stored and used (line 102), and turn switching.
3. Checking every snake and ladder, not overwriting a match (the `else` pattern), and chained jumps.
4. Behaviour ownership: which class owns the turn loop and the board rules (MC0 found the same gap).
5. Testing a game with random dice (how to test the minute-60 rule at all).
6. Time use: no commit or runnable check before minute 90.

## Om's own account of the time (13:57 IST, after the verdict)

- Om (verbatim): "I took most of the time in reading input ony around an hour minimum"
- Om (13:58, verbatim): "also few syntax ionside reafding" (Python syntax problems inside the input-reading code)
- Om also said (13:46): "90 minutes is too less for this type of problem"
- Reading: about 60 of 90 minutes went into reading the text input (lines, split, int). This is the largest single cause of the FAIL, more than class design. DSA practice never reads input (LeetCode passes arguments), so Om has not practised line-based input in Python.
- For the review (method): in a round, ask whether the sample can be hard-coded in `main` first, get the game running on it, and add input reading last.
- For the plan (new recommendation, not yet drafted in s9): a short Python lesson and drill on reading line-based input before rep 2 (W14). Om decides.

# MP2 machine coding practice: read counted input with one moving pointer (Claude)

- Type: machine coding practice session 2 (s6.5, `claude/plan-drafts/2026-10-20-mc-practice-proposal.md` session 2). Low stakes: "skill shown" or "not yet", no 0-10 score.
- Sat Nov 14 2026. Warm-up dropped (coach error 21:03, logged). Ask-first question asked twice, not answered; Om said "lets go", so the first teaching step doubled as the check ("tell me which line is new"). Step 1 (moving `i`, fruits and dairy example, run by Claude first) 21:06, Om "clear" 21:07. Step 2 (MC1's `range(number_of_ladder, number_of_ladder + 1)` read line 8, a snake line, instead of 8 ladders; a count of 0 needs no extra code, `["0", "1", "milk"]` prints `[] ['milk']`) 21:08, Om "clear" 21:11. Problem given 21:12 (timetable, SAMPLE and NO_ROOMS, three proofs for the asserts). No AI.
- Evidence: lld-patterns PR #4, commit 9daf64b (21:45). Om messaged 22:31. Om's box: about 39m (21:06-21:45) of 60.

## Claude's check (fresh checkout of 9daf64b, after Om's box)

- `pytest mp02`: 2 passed (mp01 still 3 passed).
- Deliberate mistakes in a copy, 6/6 caught by Om's asserts: teachers start at line 0, rooms start one early, rooms miss last, classes start one early, classes miss last, class count read from the rooms count.
- Also right: zero teachers `(0, 1, 1, ...)`, zero classes at the end `(1, 1, 0, ...)`.
- Counterexample run: SAMPLE plus a fourth section `"1", "H1 Diwali"` after the classes returns `(-1, -1, -1, '', '', '')`. Cause: classes are read from their start up to the end of the list (`class_end_number = len(sample) - 1`), so the class count is never used to stop, and the holiday lines are taken as classes. A moving `i` reads exactly 4 class lines and stops on `"1"` (Claude's run: 3 2 4, `i` at 12).
- How the code reads: every start is worked out from the counts (`no_to_teachers + 2`, `(no_to_teachers + no_of_rooms + 1) + 2`), the MC1 way shown as the counterexample in step 2, and a special `else` branch for 0 rooms (its two values are never used). No moving `i`.
- Spec, noted once (not the session's point): the task asked for `read_timetable(lines)` returning three lists of split lines; the code is `validate_sample` returning counts and the last lines as strings, with a -1 result when counts do not match.

## Result

NOT YET (the one skill, a single moving pointer, was not used). Shown: asserts that cover all three required proofs and catch 6/6 mistakes; correct output on both given inputs and the zero cases.

One finding: positions are worked out from counts, and the last section is read to the end of the list, so any line after the classes breaks it (the holidays counterexample).

Why question (asked 22:3x, answer in Om's own slot): why does the moving `i` stop after exactly 4 class lines, while this code also takes the holiday lines?

Next: by the practice rule, "not yet" means the same skill again with a NEW problem in the next session (W7's MP slot).

## Correction (Claude, 22:40 IST, after Om's 22:35 message; verdict changed)

Om (22:35), verbatim in part: "after giving question you can't plant bugs .. do any of your previous question cover these situation", quoting the three required proofs.

Om is right. The task said "three sections, always in this order", and the three proofs asked for (SAMPLE counts, SAMPLE last items, NO_ROOMS) are exactly what his tests prove. The holidays input adds a fourth section, so it breaks the stated format; it is not a fault in his code and is withdrawn as evidence, together with the why question built on it. Within the stated format the code has no defect found.

Result corrected to **SKILL SHOWN**: counted input read correctly, including a 0 count, in about 33 minutes of coding (21:12-21:45), all three proofs right, 6/6 deliberate mistakes caught; MC1 spent about 60 minutes on input and read the wrong ladder lines. Note, no effect on the result: the taught method (one moving `i`) was not used; positions are worked out from the counts. The spec note on the return shape stays as recorded. Next MP session: skill 3 (make random things testable). Coach error logged in `claude-log-entries.md` (22:40).

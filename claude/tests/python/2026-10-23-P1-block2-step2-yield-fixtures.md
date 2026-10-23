# P1 Block 2 step 2: pytest fixtures with yield (Claude)

- Type: teaching block inside P1 prerequisites (plan P1 row: "pytest fixtures with `return` then `yield`"). Part check, not a unit close (P1 closes in W6).
- Ask first (14:05 IST): "Never used yield". Taught from zero, only as: stop at `yield`, give the value to the test, come back after the test. Generators left for Y3.
- Video: Nick (NotesByNick), "pytest Basics: Yield Fixtures", youtube.com/watch?v=kYtYbYDiGKk, 0:00-5:02. Claude read the full transcript before giving it. Om watched it (14:35).
- Practice: 12-line yield fixture, prediction written first (both right), then run passing and failing.
- Artifact: learning-python-sandbox PR #5 `c8b275c`, `tests/test_pytest_with_yield.py`. Claude fresh fetch: 1 passed, prints SETUP, TEST, `.`, TEARDOWN. Om's pasted failing run (`== 7`): FAILED, then TEARDOWN printed.
- Questions sent about 14:38, answers 14:43. Written, cold, no running, no notes, no AI.
- Time: 14:05 to 14:43 elapsed, which includes Claude's video search; Om's own active part not reported (roughly 20-25 min).

## Questions as asked and answers verbatim

**Q1 (mechanism).** Using your failing run (`== 7`), describe step by step what happens from the moment pytest starts `test_sum` until the end. At each step, say where control is: in the fixture or in the test.

> First it goes to fixture and then prints the first line "SETUP: making the list" then the list is prepared and yeiled after this control goes back to to the first line of test and "TEST: running" is printed . then the next line in test only test fails then the test ends and control moves back to next line of yield and "TEARDOWN: clearing the list" gets printed and then the last line executes and clear the list.

Score 2/2. Every step and the place of control right, including the return to the line after `yield` after a failure.

**Q2 (failure).** Someone changes `yield data` to `return data` and leaves the two lines below it as they are. What happens to those two lines, and how would the output look different?

> After returning the data and test either passing or failing "TEARDOWN: clearing the list" this will not get printed nor the next line where we are clearing the data will happen

Score 2/2. Right: nothing after `return` runs, so no TEARDOWN line and no cleanup, pass or fail.

**Q3 (transfer).** Add a second test `test_append` (appends 4, asserts length 4). pytest runs `test_sum` first, then `test_append`. How many times do SETUP and TEARDOWN print, and in what order? Would `test_sum` be affected if `test_append` ran first? Why?

> 2 times setup and tear down will be printed Setup->TearDown then for second test Setup->Teardown .. No affect on either of them as both will gets it's own fitures data

Score 2/2. Right count and order (SETUP, TEARDOWN, SETUP, TEARDOWN), and right reason: the fixture runs fresh for each test, so each test gets its own new list.

**Total 6/6. Step 2 PASS.** No teaching needed. Next in P1: Block 3, dataclass equality (ask first what Om knows), then the psycopg prerequisite.

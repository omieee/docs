# P1 Block 2, step 1: pytest basics (unit interview)

- Date: 2026-10-22 (Thu), W3. Coach: Claude. Label: P1 prerequisite, unit interview (section 7), cold, written in chat.
- Ask-first (Oct 21 16:29, Om): pytest so far = "just vanila assert".
- Plan line (W3 row, P1): pytest basics (what pytest is, how it finds and runs tests, reading a failure), fixtures with `return` then `yield`, then dataclass equality.
- Resource (checked by Claude the same day, transcript read 14:14:44 to 14:30:26): freeCodeCamp "Python API Development - Comprehensive Course for Beginners" (Sanjeev Thiyagarajan), https://www.youtube.com/watch?v=0sOvCWFmrtA&t=51291s, chapters "Testing Intro" (14:14:51) and "Writing your first test" (14:17:19), stop at 14:30:22. Om watched further on his own, through parametrize (14:35:29) and fixtures (14:48:37), and said (15:55): "lot better vide i understtod basic parameteris and fixture also". Then Python Crash Course 3e ch 11, "A Failing Test" and "Responding to a Failed Test".

## Artifact

- learning-python-sandbox PR #2, `558decd` (16:56:55). Claude fresh fetch and run: 22 passed, ruff check and format clean (CI runs ruff check, ruff format --check, pytest).
- New: `basic_pytest_learning/calculator.py` with a parametrized `test_add` (parametrize is Y6 scope, not scored here); `basic_pytest_learning/banking_system.py` with two `return` fixtures (`zero_bal_account`, `initial_bal_account`) used by 8 tests.
- Deliberate mistakes on a copy, 5 of 8 caught: add subtracts, multiply adds, withdraw allows overdraft, deposit does nothing, withdraw does nothing (all caught); withdrawing exactly the full balance blocked, negative deposit accepted, negative withdraw accepted (missed, no test for these edges). `test_withdraw_from_a_zero_balance_acoount` never calls `withdraw`. Practice file, not a spec'd unit: noted once, not blocking.
- Also in the PR, not scored: `tests/test_fixture_lab.py`, `notes/fixture-lab.md` (xfail table) and a print change in `context_managers/Tx.py`; these match the Oct 18 Block 2 lab that was taught above Om's level (coach error, logged Oct 18).

## Questions and answers (verbatim)

**Q1.** You ran `make test`, and pytest ran your new tests without you naming any file. How did pytest find `test_add`? What would happen if you renamed `tests/test_calculator.py` to `tests/calc_check.py`?

Om: "pytest checks for files either test_* or *_test also looks for functions starting names like test_* it will auto discover that is pytests autodiscovery feature ..  this will not work calc_check .. if we want to test it we have to specifically say "pytest tests/calc_check.py""

Score 2/2. Right: file names `test_*.py` or `*_test.py`, functions starting with `test`; a renamed file is not collected unless its path is passed.

**Q2.** (Real output from `add` changed to subtract on a copy.)

```
>       assert expected == calc.add(first_num, second_num)
E       assert 8 == 2
E        +  where 2 = add(5, 3)

tests/test_calculator.py:11: AssertionError
FAILED tests/test_calculator.py::test_add[5-3-8] - assert 8 == 2
```

Which line tells you the test failed, which value is the expected one and which is the actual one, and how do you know which is which?

Om: "This is teh actual error why asert failed: E assert 8 == 2 and this line tells the assertion failed: tests/test_calculator.py:11: AssertionError .. here expected was 8 but got 2 .. if you closly look these two line : assert expected == calc.add(first_num, second_num) E assert 8 == 2 it says what is expected before == and what value will you get after =="

Score 2/2. Right: 8 expected, 2 actual, read by matching the `E` line to the source line of his own assert; file and line 11 found. Note given after scoring (not a miss): pytest prints the two sides in the order the assert was written; it does not know which one is expected. `assert calc.add(5, 3) == 8` would print `assert 2 == 8`.

**Q3.** In `test_banking_system.py`, `test_add_deposit_to_zero_bal_account` deposits 10 into `zero_bal_account`. Then pytest runs `test_withdraw_from_a_zero_balance_acoount`, which uses the same fixture. Does that second test see a balance of 0 or 10? Why?

Om: "No it doesnot see because a fixtures life span is function scope and as soo as that test ends teardown happens and each tests getra fresh copy of fixture"

Score 2/2. Right: it sees 0; the fixture function runs again for each test (function scope by default), so each test gets a new `OmBank()`. Note given after scoring: with a `return` fixture there is no teardown code to run; teardown code is what `yield` adds (next step).

## Result

- 6/6, no prompts, no correctness errors. P1 Block 2 step 1 (pytest basics) PASS. Fixture with `return`: used correctly in running code and explained (Q3).
- Next: fixtures with `yield` (setup, yield, teardown), then Block 3 dataclass equality, then psycopg.
- Minutes: about [125m] against a 60-minute box: video about 60 (estimated from the range Om watched), practice 60 (15:57 to 16:56, planned 25), check about 8 (16:58 to 17:06). Om chose to continue ("now only", 15:57) and answered the check after being told the overrun in minutes.

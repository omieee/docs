# P1 step 2 cold check: commit timing, scope, `with` dependency, monkeypatch

**Date:** 2026-11-12, 17:38 to 17:48 IST. **Coach:** Claude. **Unit:** P1 (open). This is a step check, not the P1 unit verdict.
**Conditions:** from memory, no notes, no code, no AI (stated to Om before the questions).
**Taught before asking (claude/taught/python.md, all Nov 12 or earlier):** code after `yield` runs after the response by default; `scope="function"`; `with psycopg.connect()` commits on clean exit and rolls back on error; FastAPI throws the endpoint's error in at `yield`; `monkeypatch.setenv` undoes itself when the test ends; aborted transaction (Nov 6).
**Evidence of the work:** PRCP PR #11 ae974b0, Claude's fresh checkout, 92 passed, deliberate mistakes caught (see claude-log-entries.md, 2026-11-12 17:38).

## Questions as asked and Om's answers, verbatim

**Q1.** Your dependency is `with psycopg.connect(os.environ["PRCP_DSN"]) as conn: yield PgServiceRepository(conn)` but an endpoint uses plain `Depends(get_service_repository)`, without `scope="function"`. A POST inserts a row, and then the commit fails. What status code does the client get, is the row saved, and why?

> 1. Client will see 201 ... well before the actual commit will happen .. commit wil eventual;l happen

Neutral question (safeguard 9, "commit will eventually happen" was unclear against a failing commit): "After that request, is the row in the database: yes or no?"

> No

**Score: PASS.** 201, response sent before the commit, row not saved.

**Q2.** Now with `scope="function"` on. The same service name is POSTed a second time. Trace step by step from the request arriving to the client seeing 409. Say what happens at the `yield` line, to the transaction, and to the connection.

> 2. so second time connectin will be yielded .. first time already is saved so will throw 409 error and then conn

**Score: PARTIAL.** Connection yielded and duplicate leads to 409: right. Missing: the error thrown back in at `yield`, the `with` rolling back the failed transaction, the connection closed, then the handler sending 409.
**Taught on the spot:** six-step trace (open, yield, INSERT fails, DuplicateServiceError, error thrown in at `yield`, `with` rolls back and closes, handler 409), tied to the Nov 6 aborted-transaction lesson.

**Q2b (retry, new wording).** In one request, an endpoint does one INSERT successfully, and then its own code raises a `ValueError`. With your `with`-based dependency, what happens to that successful INSERT, and where exactly does your dependency find out about the error?

> 2b INSERT gets rolledback .. after the erros goes to the dependency

**Score: PASS** (working recall: rolled back, and the error is delivered into the dependency; "at the yield line" not named, not gated per the recall calibration).

**Q3.** A teammate writes a new integration test, but instead of monkeypatch puts `os.environ["PRCP_DSN"] = os.environ["PRCP_TEST_DSN"]` at the top of the test. The test passes. What can go wrong because of that line, and why doesn't `monkeypatch.setenv` have this problem?

> 3. The actual environemt got overwritten not actuall code wil start pushing into test db

**Score: PARTIAL.** Overwrite and test-database consequence: right. Missing: it lasts for the rest of the pytest run (every later test sees it, order-dependent results), and monkeypatch restores the old value when the test ends, pass or fail.
**Taught on the spot:** process-only change that is never undone; order dependence; monkeypatch restores on pass or fail.

**Q3b (retry, new wording).** A test calls `monkeypatch.setenv("PRCP_DSN", "x")`, and then one of its asserts fails halfway. In the next test of the same run, what is `PRCP_DSN`, and why?

> 3b PRCP_DSN is actual value in environment monkek patch scope is till that test

**Score: PASS.**

## Result

Q1 PASS · Q2 PARTIAL, retry PASS · Q3 PARTIAL, retry PASS. The original misses stay recorded. Step check passed after repair; P1 stays open (repositories for the other entities, and the `scope="function"` guard test, still to come).

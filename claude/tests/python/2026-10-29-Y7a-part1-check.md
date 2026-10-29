# Y7a PRCP code walk, part 1: part check on Protocol, repository and conftest (Claude)

- Plan content: W4 row, Y7a 0.75h "PRCP code walk, part 1: before P1 changes them, explain the repository Protocols, schemas and `conftest.py` fixtures line by line; fix or log what you cannot defend" (section 6.1: 1h; proof "each module explained without notes"). This is a part check, not the unit close: `sql/001-init.sql` and the line-by-line walk remain.
- Taught first (Oct 29): ArjanCodes "Protocols vs ABCs in Python" (youtube.com/watch?v=dryNwWvSd4M, 1:53-9:21, chapters checked by fetch Oct 29), a job-advert explanation, a runnable Driver example (Claude ran it), the repository picture on `main.py` line 104 and `dependencies.py`, NotesByNick "pytest Basics: The conftest.py File" (youtube.com/watch?v=t0R6zNNS4-8, title and channel checked by fetch Oct 29). Fresh-per-test fixtures taught Oct 22 and Oct 23 (P1 records). Om said "all three clear" (15:15) and asked for questions.
- Out of scope, not asked: the `client` fixture's `dependency_overrides` and `TestClient` (Y7b, W68; plan BUG logged); mypy (Y1).
- Questions sent 15:16 IST, answers 15:46, neutral prompts on Q2 and Q3 15:47, answers 15:49. Written in chat, from memory, no notes, no code run, no AI (Om's terms for the check).
- PRCP at `7958798`.

## Questions as asked and answers verbatim

**Q1 (mechanism, conftest).** You add a new test in `tests/api/test_probes.py`: `def test_x(service_repository): ...` with no import line. Step by step, how does this test get its object? And if two tests both ask for `service_repository`, do they get the same object or separate ones? Why does that matter for PRCP's tests?

> pytest invokes without explicitly import the conftest.py file .. service_repository fixture will be available . if two test needs it both will get seprate fixture not the same

Score 1/2. Right: pytest loads `conftest.py` with no import; separate objects for two tests. Missing: how the test gets it (pytest matches the parameter name `service_repository` to the fixture of that name, calls the fixture function and passes in what it returns), and why separate matters (each test starts with an empty repository, so data saved in one test cannot leak into another).

**Q2 (trade-off, repository).** Suppose line 104 in `main.py` did not call `repository.save(...)` and instead wrote the environment straight into a dict defined in `main.py`. In P1, when you move PRCP to Postgres, what would you have to change in that design, compared with today's design?

> We would have to create the full functinaly to save the database

Neutral prompt (rule 9, two readings possible): "In the dict design, which file or files would you have to change? And in today's design, which file or files? Just name them."

> Model would have changed there some thing like save_environ function should be there that would take dict and save it

Score 0/2 (prompted). Missing: the difference between the designs. Dict design: every storage line in `main.py` (environments 104, 117, 133; services 56, 67, 83; probes 162, 170, 187) is rewritten for Postgres, mixed with the API code. Today's design: one new class with the same three methods in `repository.py`, one line changed in `dependencies.py`, `main.py` unchanged. Not an inverted invariant, so no local FAIL.

**Q3 (failure, Protocol).** [`test_in_memory_environment_repository_matches_protocol` pasted in the question.] Someone deletes the `list_all` method from `InMemoryEnvironmentRepository`. Does this test still pass or fail? Why? And does the test really prove what its name says?

> Test would stil pass as we are not using the list or could fail because Protocol is not satisfied

Neutral prompt (two opposite answers given): "If you had to pick one, pass or fail, which one, and why? And does the test prove what its name says?"

> It would pass .. because we are not explicity depended on listing it and Protocol is not strictly checked by python so test would pass

Score 1/2 (prompted). Right after the prompt: passes, because the test never calls `list_all` and Python does not check the `EnvironmentRepository` annotation. Missing: that the test therefore does not prove what its name says (it checks only `save` and `get_by_name`).

**Subtotal 2/6 before teaching.** Retries below.

## Teaching and retries

(added as they happen)
**Q2 taught (15:51):** the dict design puts storage lines in about nine places inside `main.py`, all rewritten for Postgres; today's design adds one class in `repository.py`, changes one line in `dependencies.py`, and leaves `main.py` unchanged.

**Q2 retry (fresh wording, 15:51).** Later, PRCP moves probe results from Postgres into a different store, say a file. With today's design, which files change, which file stays untouched, and why does it stay untouched?

> Wil add a new InDatabaseProbeReposity implement the 3 methods and in dependencies.py point this to [`_probe_repository = InMemoryProbeRepository()` ... `return _probe_repository`] to the [`_probe_repository = InDatabaseProbeRepository()`]. So may be similar way we can also divide dev, prod, pre-prd db also (but i agree its better to keep those switches when db object creation is happening)

Retry correct: a new class with the Protocol's methods, one line changed in `dependencies.py`, nothing else listed (generous reading: `main.py` untouched). He used the probe repository and a database instead of probe results and a file; identifiers are not graded (s7). The "why `main.py` stays untouched" not stated; given after scoring: it only calls the Protocol's methods. Q2 item scores 1 (prompted miss stays recorded). His dev/pre-prod/prod point is right: same class, a different connection setting at creation time.

**Q1 taught (15:56):** pytest matches the parameter name to a fixture of exactly that name (test file first, then `conftest.py`), calls it and passes in what it returns; counterexample: a parameter `svc_repo` gives "fixture 'svc_repo' not found". Separate objects matter because a shared one makes results depend on test order (test A saves, test B expects empty).

Om (15:59): "2nd one i actuall ment the same reason but in mind .. so yes mind needs to be spoken out." Score unchanged (no new evidence).

**Q1 retry (fresh wording, 15:56).** `def test_empty(environment_repository): assert environment_repository.list_all() == []` runs right after another test that saved `prod` into its own `environment_repository`. Pass or fail? What does pytest do, step by step, to hand `test_empty` its object?

> Its pass because it will get the fresh copy without any previous test data  that is created .. pytest looks for environment_repository fixture fist in it;'s own file then look for any conftest.py if found passed directly what ever that fixture return/yields (in some situation it can yield also) and then the test contionuews

Retry correct: passes, with the reason (fresh copy per test); lookup by the fixture's name, own file first, then `conftest.py`; the returned or yielded value is passed in. Q1 item stays 1 (retry scores 1).

**Q3 taught (16:03):** the `: EnvironmentRepository` hint is ignored by Python; the test calls only `save` and `get_by_name`, so it proves only that; with `list_all` deleted it stays green, so the name claims more than it checks. Options: rename to what it checks, or log until Y1 (mypy).

**Q3 retry (fresh wording, 16:03).** [`test_in_memory_service_repository_matches_protocol` pasted.] Someone breaks `InMemoryServiceRepository.list_all` so it always returns `[]`. Does this test catch the bug? Why or why not? What name would say only what this test really checks?

> It wont fail because Protocol adherence are not checked by Python itself and in code (test) no where we are calling that list function ... so yes Python will be happy

Retry correct on the mechanism: not caught, because the test never calls `list_all`. Precision given after scoring: here the Protocol is still satisfied (the method exists, it just returns the wrong thing), so the only reason is that the test never calls it. The rename part was not answered; it is taken as Y7a's fix-or-log decision for Om, not scored. Q3 item stays 1.

## Result

Part check: 2/6 cold, 3/6 after three correct retries (Q1 1, Q2 1 prompted, Q3 1 prompted). PARTIAL. No correctness error left open. Y7a stays open: `sql/001-init.sql`, the line-by-line walk, and the fix-or-log decision on the two over-named `..._matches_protocol` tests (`tests/test_repository.py` lines 78 and 106).

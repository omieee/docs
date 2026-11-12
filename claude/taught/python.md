# Python and psycopg: what Om has been taught

Purpose: the same rule as `go.md` (Go strategy, approved Nov 3 2026 16:45): before any Python, pytest or psycopg lesson, the coach checks every concept it uses against this list. Started Nov 4 2026 with psycopg; the earlier Python units (Y2 baseline, P1 Python prerequisites, Y3 first part, Y7a) are added in the all-track audit due Sat Nov 14.

## Taught

| Concept | Source | Date | Evidence |
| --- | --- | --- | --- |
| `with` statement and context managers | P1 Block 1, RP | Oct 17 | `claude-log-entries.md` |
| psycopg 3: `psycopg.connect(DSN)`, `conn.execute(...)`, `.fetchone()` returns a tuple, `with` closes the connection | P1 psycopg part 1, step 1 | Nov 4 | Om's run on `prcp-pg` |
| `%s` placeholders with a values tuple; one-item tuple needs a trailing comma; why not an f-string | P1 psycopg part 1, step 2 | Nov 4 | Om: "%s is like place holder and we pass values as tupple" |
| A transaction is private until COMMIT; another connection sees only committed data; ROLLBACK throws the change away; psycopg sends BEGIN before the first statement, psql autocommits | P1 psycopg part 1, step 3 | Nov 4 | Om's guess (reader sees it) broken by output (1,); Om explained it after |
| `with psycopg.connect()` commits on a clean exit, rolls back on an error inside the block | P1 psycopg part 1, step 4 | Nov 4 | Om explained it right at 10:36 |
| Check-then-insert is not safe: another connection's uncommitted row is invisible, so both checks pass; the second INSERT waits, then gets `UniqueViolation`; one connection per app copy, and workers or replicas mean several copies; the UNIQUE constraint is the real guard | P1 step 1 | Nov 6 | Claude's two-connection run (None, waiting, UniqueViolation); Om (11:00): "i don't need to check if row exist ... if pg returns errors i will raise DuplicateError". Om did not run the two-terminal demo |
| `try/except SomeError as e`, `raise MyError(...) from e`; catch only the error you expect | P1 step 1 | Nov 6 | Om's `save` in PRCP PR #11 8dd0aad |
| After one failed statement, Postgres refuses every later statement in that transaction (`InFailedSqlTransaction`) until ROLLBACK | P1 step 1 | Nov 6 | Taught 11:26; Om explained it Nov 11 15:53 (warm-up, held): "the transaction failed in step 2 .. so how will anything after that will pass"; Claude added the until-ROLLBACK part |
| `Annotated[T, extra]`: Python keeps T as the type and ignores the extra note; FastAPI reads a `Depends(...)` note and injects the value; a named alias (`ServiceRepoDep`) reuses it | P1 step 2, part 2 | Nov 12 | Om ran the `get_type_hints` demo; used `ServiceRepoDep` on 4 endpoints (PR #11 30166a3) |
| `Depends(..., scope="request")` (default): code after `yield` runs after the response is sent; `scope="function"`: right after the endpoint, before the response | P1 step 2, part 2 | Nov 12 | Om's two demos: failed commit gave 201, then 500; Om: "yes clear" (16:11) |
| A `with psycopg.connect()` yield dependency: commit on clean exit, rollback when the endpoint raises (FastAPI throws the error in at `yield`), always close | P1 step 2, part 2 | Nov 12 | Om asked when it should roll back and chose `with` himself (16:16); curl 201, 409, restart, 200 |
| pytest's built-in `monkeypatch` fixture: `monkeypatch.setenv(NAME, value)` changes an environment variable for one test and pytest undoes it when the test ends, pass or fail | P1 step 2, part 3 | Nov 12 | Sticky-note diagram and a two-test demo; Om: "Ahh got it"; used in `tests/api/test_pg_service.py` (PR #11 ae974b0) |

## Seen once, not yet taught as a topic

| Concept | Where | Date | Full topic |
| --- | --- | --- | --- |
| `try/except`, `raise ValueError(...)` (used to force an error) | psycopg step 4 | Nov 4 | Y3 exceptions (catch and re-raise taught Nov 6, see above) |
| Postgres server-side parameters `$1`, `$2` in the statement log | psycopg steps 3-4 | Nov 4 | P1 reference pass |
| FastAPI dependency with `yield` has the same shape as a pytest `yield` fixture: code before `yield` runs when a request arrives, the yielded value goes to the endpoint, code after `yield` runs after the endpoint; each request gets its own connection | P1 step 2, part 1 | Nov 11 | Side-by-side with Om's `pg_conn` and a trace of one POST; Om (19:15): "clear"; Om asked why the type is `ServiceRepository` (Protocol, taught in Y7a) and whether connections are opened twice (repository receives one; whoever opens it owns commit or rollback) |
| Without a commit, a request's INSERT is thrown away when its connection closes, so the next request (its own connection) cannot see it | P1 step 2, part 1 | Nov 11 | Om's run without commit: POST 201, GET 404, POST again 201 (no 409); Om explained it (22:26): "created but not committed and each request is a separate transaction ... first one never committed" |

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

## Seen once, not yet taught as a topic

| Concept | Where | Date | Full topic |
| --- | --- | --- | --- |
| `try/except`, `raise ValueError(...)` (used to force an error) | psycopg step 4 | Nov 4 | Y3 exceptions |
| Postgres server-side parameters `$1`, `$2` in the statement log | psycopg steps 3-4 | Nov 4 | P1 reference pass |

# Y7a PRCP code walk, part 1: unit proof (Claude)

- Plan content: section 6.1 Y7a (1h): "Before P1 changes them: the repository Protocols, schemas and `conftest.py` fixtures, explained line by line; fix or log what you cannot defend". Proof: "Each module explained without notes". W4 row 0.75h. Section 7 unit proof: artifact, tests, one paragraph from memory (what, why, what you rejected), three cold questions.
- Scope used: `src/prcp/repository.py`, the four repository fixtures in `tests/conftest.py`, `sql/001-init.sql`. Out of scope, not asked: the `client` fixture's `dependency_overrides` and `TestClient` (Y7b; plan BUG logged), mypy (Y1).
- Artifact: PRCP main `7958798`. Claude fresh clone Oct 29: 87 passed, 100% coverage. `sql/001-init.sql` loaded into Claude's own Postgres 16.15 without errors.
- Teaching before the proof: see `2026-10-29-Y7a-part1-check.md` (Protocol, repository, conftest; part check PARTIAL 3/6 after retries) and the SQL gap check (16:28-16:41: BIGSERIAL vs UUID, CASCADE vs RESTRICT, timestamptz taught with real Postgres output; Om said clear to each).
- Written in chat, from memory, no notes, no AI (Om's terms). Paused 17:01-20:59 for an office call; Om was asked not to look anything up in between.

## Part 1: paragraph from memory (received 17:00, verbatim)

> 1. So we create a protocol with three function save, get_all, get_by_name .. and then there can be many Repositories like one that saves things in memory, or databases , or file Repositories that will implement the same functions and then we will return in dependencies which repository to use .. The benefit of this we at the api level don't need to care which class is internally called and no change is required to implement at main.py level ......... I would reject a seprate object level save and get_all because that will tightly get couplled at api level and for each change of way we want to store data we need to change at api level aswell .......  conftest.py file is where we keep the fixtures and it is avaiable for all test we don't need to specificall import thsi file and each test gets it's own fresh copy of test fixture and one test is not dependent on previous test results .. conftest.py is build in this way because to make fixtures easily avaiable for each test and gurantees each test will get fresh state of that returned or yielded object ... i would reject adding same fixtures at each file level beacause that will be reped code and if we have change some thing in fixture we need to change at multiple place
> 2. sql init is for making the initial structure for our prcp project it creates teh structure of our prcp project by initializing empty tables for env, service, probe and possible validations at da layer itsel keeping it all in simple file make it easy to create and destroy the db

Notes: repository and conftest: what, why and a rejected alternative, each with a reason ("get_all" for `list_all`; identifiers not graded). SQL: what only; why thin ("easy to create and destroy the db"); no rejected alternative.

## Part 2: three cold questions on `sql/001-init.sql`

Sent 17:00, re-sent 20:59.

**Q1 (failure).** Environment `stage` has 1 probe, and that probe has 1 probe result. You run `DELETE FROM environment WHERE name = 'stage';`. What happens to the environment, the probe and the result? Why?

Om (21:00): "It depends on what the foreign clause is is it casscade or restrict ?" Claude (21:01), a clarification of the question, not a prompt: use PRCP's file as it is, `probe` → `environment` CASCADE, `probe_result` → `probe` RESTRICT (the question should have said so).

> it will not allow delete : because if only first was there then both environment and related probes would have got deleted .. but probe_result points to probe and restrict is there so that will not allow delete to happen

Score 2/2. Right and unprompted: the whole delete is refused, nothing is deleted; the CASCADE would remove the probe, but the result's RESTRICT blocks deleting the probe, so the statement fails. Matches Claude's own Postgres run (ERROR on `fk_probe_probe_result`; environment, probe and result counts 1, 1, 1 after).

**Q2 (trade-off).** `probe` → `environment` uses `ON DELETE CASCADE`, but `probe_result` → `probe` uses `ON DELETE RESTRICT`. Why would someone choose RESTRICT for the results? What does it protect, and what does it cost you?

> RESTRICT is there because no past probe should be ever deleted with it's resulsts still in probe_results table ... and hence not allowing the environment to be deleted ... so this will not allow me to create a same probe in same environment if in past same probe has already run for same envirnment .. we can't create because we have set it to unique

Score 1/2. Right: the cost, specific and valid (an environment with results cannot be deleted; a probe with results can never be removed, so with the four-column UNIQUE its slot stays taken and the same probe cannot be created again). Partly: what it protects is a restatement of the rule (a probe with results cannot be deleted); why that matters is not said (results are PRCP's history, the evidence behind gate decisions; CASCADE would erase it silently with one delete). Generous reading tested: "past probe ... results still" points at keeping results, but gives no reason they matter.

**Q2 taught (21:08):** results are PRCP's history, the evidence behind gate decisions; CASCADE would erase them silently with one environment delete (a `prod` for `preprod` typo); RESTRICT makes deleting history a deliberate two-step act; costs as Om named, plus results growing until cleaned.

**Q2 retry (fresh wording, 21:08), unanswered.** `gate_decision` → `service` also uses RESTRICT (lines 101-104). A teammate wants CASCADE "so deleting a retired service is one easy command". What would PRCP lose, and why does that matter?

Om (21:09): "understood and done for the day". Block stopped. Q2 retry and Q3 open for the next session. No verdict.

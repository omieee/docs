"""v3.9 unit ledger (v3.8 plus the Nov 15 2026 re-forecast: Go on Learning Go 2e order, Kubernetes on the KodeKloud CKA course order, the finalizer fix, the distributed-systems proof). v3.8 unit ledger (v3.6 base; v3.8 adds a use step in real code to every teaching part): every unit, its section, its parts (hours, text with resources)."""
from collections import OrderedDict

U = OrderedDict()


def unit(label, sec, parts, deps=()):
    U[label] = {"sec": sec, "parts": parts, "deps": list(deps)}


# ---------- 6.1 PRCP core ----------
unit("P1", "6.1", [
    (0.5, "Python prerequisite Block 1, context managers and `with`, done Oct 17 [RP (\"Python's with Statement: Manage External Resources Safely\")]"),
    (2.25, "Python prerequisites left after Block 1, Block 2 restarted Oct 18 from zero: pytest basics (what pytest is, how it finds and runs tests, reading a failure), done Oct 22; then fixtures with `return` [PCC (ch 11), RP, PYTEST (fixtures), MCODING]"),
    (1.0, "Fixtures with `yield`, right after Y3's generator basics, then dataclass equality [PYTEST (fixtures), RP, MCODING]"),
    (4.25, "psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script); then one use case end to end through the real database, including one specified failure: the Service repository and `POST /services` on Postgres (done Nov 4-12, PRCP PR #11) [PSY]"),
    (3.5, "Repositories for Environment, then Probe, on the Service pattern (v3.9 r2: sized against PRCP PR #11 ae974b0): Environment save, get and list with its duplicate mapped and a saved row read back through a new connection; Probe looks up its environment and service ids first, with two plain lookups (the nested queries P2 teaches come later), saves the method and expected status, and maps a missing parent (foreign-key error) to a domain error, tested. Reuse what October taught (v3.8): the rollback fixture is a `yield` fixture and each transaction uses `with` [PSY]"),
    (5.5, "Repositories for ProbeResult, then GateDecision with its evidence (v3.9 r2): ProbeResult gets the id the table already requires, set by `create_probe_result` the way `create_http_probe` sets a probe's id, and a test that another probe's result stays out; then a `002` SQL file adds the table linking a decision to the result ids it used, applied in CI and in both local databases; the decision and its links are saved in one transaction, and a link to a result id that does not exist makes the whole save fail, so no half decision survives, tested; tests green on a fresh clone. The commit-failure test for the API dependency (`monkeypatch.setattr`, not taught yet) waits for Y6 [PSY, PG (Constraints: foreign keys)]"),
])
unit("P2", "6.1", [
    (6.25, "SQL correction, lesson before exercise: SQLBolt lessons on joins, outer joins and NULLs, then its subqueries and set-operations topics (IN, UNION); then pgexercises Joins and Subqueries. Use in PRCP (code): one repository query that joins probes to their results and one with a subquery, each tested on `prcp_test` [SQLBOLT, PG-TUT (Window Functions), PGEX]"),
    (5.25, "SQLBolt aggregates and order of execution, then pgexercises Aggregation (GROUP BY, HAVING); window functions lesson, then the window exercises. Use in PRCP (code): pass rate per service with GROUP BY and the latest result per probe with a window function, each tested [SQLBOLT, PG-TUT (Window Functions), PGEX]"),
    (3.75, "pgexercises Working with Timestamps and Modifying Data; 3 timed unseen problems set by the assistant. Use in PRCP (code): results from the last 24 hours, and one UPDATE inside a transaction, each tested [SQLBOLT, PG-TUT (Window Functions), PGEX]"),
], deps=["P1"])
unit("P3", "6.1", [
    (2.5, "Isolation intuition before the docs. Use in PRCP (code): run the demo on PRCP's own tables [TS-ISO, CMU (Multi-Version Concurrency Control)]"),
    (3.5, "B-tree, composite order, index-only scans; EXPLAIN ANALYZE; ADR. Use in PRCP (code): the index and the plans are on PRCP's results table [UTIL (Anatomy of an Index, The Where Clause), PG (Indexes, Using EXPLAIN), CMU (Join Algorithms)]"),
    (3.5, "Isolation levels, MVCC, row locks, deadlocks; two-session demos. Use in PRCP (code): both demos on PRCP's tables [INTERDB (Concurrency Control), PG (Concurrency Control), CMU (Two-Phase Locking)]"),
    (2.5, "WAL on commit, pooling, replication and failover, VACUUM; code-read how `psycopg_pool` hands out a connection [INTERDB (VACUUM, WAL, Replication), PG (Reliability and the Write-Ahead Log, Routine Vacuuming, High Availability), HN]"),
], deps=["P2"])
unit("P4", "6.1", [
    (4.5, "SQLAlchemy 2.0: port repositories, same tests [SQLA]"),
    (4.5, "Alembic: an expand, backfill, contract migration with old and new app versions running together; a quick N+1 check [SQLA, ALEMBIC]"),
], deps=["P1", "Y8a"])
unit("Y1", "6.1", [
    (4.0, "PRCP has no mypy config yet: type hints, `Optional`, generics, `Callable`; install and configure mypy; then `mypy --strict` clean on `src/prcp` [PYDOCS (typing), MYPY (Getting started, Using mypy with an existing codebase)]"),
])
unit("Y2", "6.1", [(1.0, "Checklist D baseline, cold [section 7]")])
unit("Y3", "6.1", [
    (1.0, "Generators, first part (v3.6, moved forward for P1): what `yield` does, how a generator pauses and resumes, so `yield` fixtures make sense. Use in PRCP (code): the psycopg rollback fixture in P1 (W5-W8) is a `yield` fixture [RP (\"How to Use Generators and yield in Python\"), MCODING]"),
    (2.75, "Names and references: everything is an object, `is` vs `==`, mutable vs immutable, how arguments are passed. Use in PRCP (code): a test proving `decide()` does not change the list it is given; find one place where PRCP shares a mutable object and fix or log it [RP (\"Shallow vs Deep Copying of Python Objects\": the mutable vs immutable part), FLUENT (ch 6), MCODING]"),
    (1.75, "Shallow vs deep copy: the `copy` module, copies of nested lists. Use in PRCP (code): return copies from one in-memory repository, or show with a test why a shallow copy is enough there [RP (\"Shallow vs Deep Copying of Python Objects\"), FLUENT (ch 6)]"),
    (3.25, "Hashing: what a hash table does, the `__eq__` and `__hash__` contract, why a list cannot be a dict key, list, dict and set costs. Use in PRCP (code): a frozen dataclass key (service, environment) for the latest GateDecision in a dict, with a test that equal keys find the same entry; say why `ProbeResult` cannot be a key [FLUENT (ch 3), MCODING]"),
    (2.75, "Iterables vs iterators: the iterator protocol, what a `for` loop really does, why an iterator gets used up. Use in PRCP (code): a test that a generator passed to `decide()` is used up by its first `any()`, then the fix [RP (\"Iterators and Iterables in Python: Run Efficient Iterations\"), FLUENT (ch 17)]"),
    (1.75, "Generators, rest: generator expressions, lazy evaluation. Use in PRCP (code): count failed results with a generator expression, without building a list [RP (\"How to Use Generators and yield in Python\"), FLUENT (ch 17), MCODING]"),
    (3.25, "Functions as objects: `*args` and `**kwargs`, scope and the LEGB rule, `nonlocal`, closures. Use in PRCP (code): `checker.py` already takes its HTTP getter as an argument; write a closure that fixes the timeout and use it in a test [RP (\"Python args and kwargs: Demystified\", \"Python Scope and the LEGB Rule\", \"Python Closures: Common Use Cases and Examples\"), FLUENT (ch 7, 9)]"),
    (3.25, "Decorators: what `@` does, wrappers, `functools.wraps`, decorators with arguments, PRCP's route decorators. Use in PRCP (code): a timing decorator on `decide()` with `functools.wraps`, tested; explain `@app.get` in `api/main.py` [RP (\"Primer on Python Decorators\"), FLUENT (ch 9), ARJAN]"),
    (2.75, "Exceptions: the hierarchy, `try`, `except`, `else`, `finally`, `raise from`, custom exceptions such as PRCP's `exceptions.py`. Use in PRCP (code): one new exception raised with `raise ... from`, with a test on `__cause__` [RP (\"Python Exceptions: An Introduction\"), FLUENT (ch 18)]"),
    (2.25, "Context managers in depth: what `__exit__` receives, suppressing an exception, `contextlib.contextmanager`. Use in PRCP (code): a `contextmanager` transaction that rolls back on error, used in one repository, with a test for the error path [RP (\"Python's with Statement: Manage External Resources Safely\"), FLUENT (ch 18)]"),
])
unit("Y4", "6.1", [
    (2.75, "asyncio from zero: coroutines vs functions, `await`, the event loop, tasks. Use in PRCP (code): an async version of one probe check with httpx's `AsyncClient`, tested [RP-ASYNC, MCODING]"),
    (4.25, "`TaskGroup`, semaphores, cancellation, timeouts. Use in PRCP (code): probe checks run in a `TaskGroup` under one timeout, tested; add goroutines vs asyncio tasks to `go-notes.md` (moved here from G7) [RP-ASYNC, BEAZ, PYDOCS (asyncio)]"),
    (7.5, "Bounded async fan-out; starvation lab and write-up. Use in PRCP (code): the fan-out is PRCP's local probe runner [RP-ASYNC, PYDOCS (asyncio)]"),
], deps=["Y3"])
unit("Y5", "6.1", [
    (5.25, "Threads from zero (start, join, a shared-counter race and its lock fix), processes, the GIL, threads vs processes vs asyncio; state the Python version and GIL mode you ran. Use in PRCP (code): the race and its lock fix on a counter inside PRCP's in-memory result repository, tested on a controlled schedule [PYDOCS (threading, profile), BEAZ]"),
    (2.0, "GIL, threads vs processes vs asyncio, `cProfile` before and after. Use in PRCP (code): profile PRCP's fan-out [PYDOCS (profile), BEAZ]"),
], deps=["Y4"])
unit("Y6", "6.1", [
    (4.5, "pytest beyond the basics: fixture scopes, `conftest.py`, parametrize, `monkeypatch`, `tmp_path`; then Hypothesis on the evidence step and `decide()` together (v3.9 r2): no PASS unless every required probe has a passing result for this release, for every generated list (the r1 property, no PASS unless every result is positive, holds even when a required probe never reports); the API commit-failure test with `monkeypatch.setattr` carried from P1 [PYTEST, HYP]"),
])
unit("Y7a", "6.1", [
    (1.0, "PRCP code walk, part 1 (v3.6, moved forward): before P1 changes them, explain the repository Protocols, schemas and `conftest.py` fixtures line by line; fix or log what you cannot defend [section 6.1]"),
])
unit("Y7b", "6.1", [
    (4.0, "PRCP code walk, part 2: every other pre-plan module explained cold (Pydantic schemas, FastAPI `Depends` and `dependency_overrides`, the `client` fixture with FastAPI `TestClient` (moved here from Y7a, v3.9), Enums, exceptions, `decide()`); fix or log what you cannot defend [section 6.1]"),
])
unit("Y8a", "6.1", [
    (3.25, "Classes from the ground up (v3.6, moved before MC2): `__init__` and `self`, instance vs class attributes, `@classmethod` and `@staticmethod`, special methods, `Enum`; credit what L1 already showed. Use in PRCP (code): a `@classmethod` constructor such as `ProbeResult.from_row` for psycopg rows, tested [RP (\"Object-Oriented Programming (OOP) in Python\", \"Python's Magic Methods: Leverage Their Power in Your Classes\"), FLUENT (ch 11), PYDOCS (enum)]"),
    (2.75, "Dataclasses in depth (v3.6, moved before MC2): generated methods, `field()`, the mutable-default trap, `frozen`, `slots`. Use in PRCP (code): decide which `models.py` dataclasses should be frozen, fix any mutable default with `field(default_factory=...)`, tested [RP (realpython.com/python-data-classes), FLUENT (ch 5)]"),
])
unit("Y8b", "6.1", [
    (2.75, "Inheritance, MRO and `super()`, cooperative multiple inheritance. Use in PRCP (code): explain each `super().__init__` in `exceptions.py` and test that catching `PRCPError` catches every child [RP (realpython.com/python-super), FLUENT (ch 14)]"),
    (2.5, "ABC vs Protocol: nominal vs structural typing, `abstractmethod`, `runtime_checkable`, PRCP's repository Protocols (abstract classes were first met in L1). Use in PRCP (code): say which repository Protocol a new Postgres class satisfies and prove it with mypy or a test [RP (\"Implementing Interfaces in Python: ABCs and Protocols\", \"Python Protocols: Leveraging Structural Subtyping\"), FLUENT (ch 13)]"),
    (1.5, "Reference counting, reference cycles, the `gc` module [RP (\"Memory Management in Python\"), FLUENT (ch 6)]"),
    (1.5, "Checklist D cold re-run; repair what is still shaky [section 7]"),
])
unit("E1", "6.1", [
    (4.0, "Release evidence (v3.9 r2): each probe result names the release it probed (an Alembic migration); a pure function, before `decide()`, keeps one result per required probe of the service and environment, and only for this release, and turns a required probe with no result into UNKNOWN; `decide()` itself does not change. Tests from the case table in section 6.1: nothing received, A passes and B never reports, the same A twice, B's pass from the previous release, both pass. ADR: what counts as evidence, who owns the required list, and which result wins when one probe reports twice for the same release [section 6.1]"),
    (3.5, "The gate endpoint: PRCP loads the probes and this release's results from Postgres, runs the evidence step and `decide()`, saves the decision with the result ids it used (P1's repository) and returns it; an integration test where B's only pass belongs to the previous release and the answer is not PASS; the coach removes the evidence step and the missing-B test must fail [section 6.1]"),
], deps=["P1", "P4", "S5"])
unit("D1", "6.1", [
    (3.0, "Multi-stage Dockerfile, non-root user, `.dockerignore` [NANA-DOCKER, DOCKER]"),
    (2.0, "Compose with Postgres and healthchecks [NANA-DOCKER (Compose), DOCKER]"),
], deps=["P1"])
unit("D2", "6.1", [(3.0, "Namespaces, cgroups, layers, PID 1 and SIGTERM [DOCKER]")], deps=["D1"])
unit("C1", "6.1", [
    (4.0, "CI: lint, mypy, tests, coverage, image build [GHA]"),
    (4.5, "Self-gating: PRCP gates its own release through E1's endpoint, with the commit as the release; a planted failing probe blocks it and a required probe that never reports does not promote it (v3.9 r2, the same case table as E1) [GHA]"),
], deps=["D1", "Y1", "E1"])
unit("O1", "6.1", [
    (5.5, "`/metrics`, `/live`, `/ready`; counter, gauge, histogram; label cardinality; load experiment: throughput, p50/p95/p99, saturation point, one bottleneck; v3.9 r2: the report records the input rate, the accepted rate, the error rate, p95, the hardware and the duration, the H3 ADR's prediction next to what was seen, and, if the load generator tops out first, the highest rate actually shown with the server's limit left unknown [PROM, VEGETA, SRE (ch 6)]"),
    (5.5, "PromQL on your own metrics; one symptom alert; SLI and SLO; USE and RED; tracing concepts: trace, span, context propagation, sampling [PROM, USE]"),
], deps=["D1"])
unit("AI1", "6.1", [
    (3.0, "AI-assisted delivery checkpoint (v3.6): one bounded PRCP change with an AI tool after the design is decided; write the expected cases yourself before the AI drafts tests; log every suggestion accepted or rejected and why; inspect one failure case; then a 60-minute timed AI-assisted change on a small repo you have not seen [section 7 (AI use)]"),
], deps=["Y7a"])
unit("F1", "6.1", [
    (7.0, "ADR index; README leads with the verdict and covers kind and AWS; a short ADR on Keptn, Argo Rollouts, Flagger (uses OP3's reading); known limitations; tag `v1.0.0`; stranger test [GHA]"),
    (5.0, "Game day on kind: inject a database or probe-timeout failure, let the alert fire, diagnose, mitigate, write a postmortem and runbook [section 6.1]"),
], deps=["O1", "K6b"])

# ---------- 6.2 Go ----------
unit("G1", "6.2", [(3.0, "Install Go, Hello World, Integers, Iteration [FCC-Go ch 1-3, LGWT, GOBYEX for lookups]")])
unit("G2", "6.2", [
    (2.0, "Types, composite types and control, first contact (done Nov 2-4): Boot.dev Learn Go chapters 1-3 and chapter 9 lessons 1-9; Learning Go 2e chapter 2, and chapter 3 from Arrays to Strings, Runes and Bytes (Go appendix steps A-B) [BOOTDEV (Learn Go ch 1-3, 9), LG2 (ch 2-3)]"),
    (4.0, "Slices in code (Go appendix steps C, E, F, G; v3.9 sizes G2 at Om's measured reading pace of Nov 3; r2: step D's standalone `strings.Builder` drill is dropped, Om, Nov 6): start `go-notes.md` (a slice is not a Python list copy; `'a'` is a rune; Go does not mix `int` and `float64`) and type and run Learning Go 2e chapter 2's exercises; Learn Go with Tests, Arrays and slices, in two sittings, its test file written from a blank page. Use in the agent (code): start the Go module in PRCP's `agent/` folder; the probe targets are a slice, with a test on what `append` to a copy does [LG2 (ch 2-3), LGWT (Arrays and slices), GO-SLICES]"),
    (3.0, "Loops and control, in the approved order (v3.9 r2; the Go strategy's step 1 names Learning Go chapter 4 and Boot.dev chapter 8, which r1 left out): Boot.dev chapter 8 (Loops, six lessons), then Learning Go 2e chapter 4 (blocks and shadowing, `for` four ways, `for range` over a string giving runes, `switch`) and its exercises. Use in the agent (code): a `for range` loop that writes one line per probe target into a `strings.Builder` (strings taught in their own context, Om, Nov 6), with a test on the report text [BOOTDEV (Learn Go ch 8), LG2 (ch 4)]"),
    (2.5, "Functions as values (v3.9, the Go strategy's order): Boot.dev chapter 4's lessons left, then Learning Go 2e chapter 5 (functions as values, closures, `defer`). Use in the agent (code): a `ProbeFunc` type passed as a value, with a test that a fake function is called once per target [BOOTDEV (Learn Go ch 4), LG2 (ch 5)]"),
])
unit("G3", "6.2", [
    (2.5, "Pointers before methods (v3.9: moved from G4, Learning Go order): `*` and `&`, nil, when Go copies a value; Boot.dev chapter 11, then Learning Go 2e chapter 6. Use in the agent (code): a function that updates a `Result` through a pointer, with a test proving the caller sees the change [BOOTDEV (Learn Go ch 11), LG2 (ch 6)]"),
    (5.0, "Structs, methods and interfaces; value vs pointer receivers; embedding. Boot.dev chapters 5-6, Learning Go 2e chapter 7, then Learn Go with Tests. Use in the agent (code): `Probe` and `Result` structs, a method on `Result`, and a `Prober` interface with a fake prober in the test [BOOTDEV (Learn Go ch 5-6), LG2 (ch 7), LGWT (Structs, methods and interfaces)]"),
])
unit("G4", "6.2", [(3.0, "Errors: the nil-interface trap, `errors.New`, `%w`, `errors.Is` and `errors.As`, panic and recover; Go vs Python note: nil vs None, error values vs exceptions. Boot.dev chapter 7, Learning Go 2e chapter 9, then Learn Go with Tests. Use in the agent (code): probe errors wrapped with `%w`, and a test that `errors.Is` finds a timeout through the wrapping [BOOTDEV (Learn Go ch 7), LG2 (ch 9), LGWT (Pointers and errors, Error types), GO-ERRORS, GO100]")])
unit("G5", "6.2", [(3.5, "Maps; generics. Boot.dev chapters 10 and 15, Learning Go 2e chapter 8, then Learn Go with Tests. Use in the agent (code): a registry map from probe name to `Prober`, with a test for a missing name [BOOTDEV (Learn Go ch 10, 15), LG2 (ch 8), LGWT (Maps, Generics)]")])
unit("G6", "6.2", [
    (1.0, "Modules, packages and tooling (v3.9, the G1 leftovers in the Go strategy): `go.mod`, package layout, `go vet`, `gofmt`, `go doc`; Boot.dev chapter 12, Learning Go 2e chapters 10-11. Use in the agent (code): split the agent into two packages, each with a test [BOOTDEV (Learn Go ch 12), LG2 (ch 10-11)]"),
    (5.0, "Writing tests and design for tests: Learning Go 2e chapter 15, then dependency injection, mocking, HTTP server and `httptest` in Learn Go with Tests. Use in the agent (code): an HTTP prober with the `http.Client` injected, tested against an `httptest` server [LG2 (ch 15), LGWT (Dependency Injection, Mocking, HTTP server)]"),
])
unit("G7", "6.2", [
    (4.0, "Goroutines, channels, select, closed-channel reads: Boot.dev chapter 13, Learning Go 2e chapter 12, then Learn Go with Tests. Use in the agent (code): run the probers in goroutines and collect results over a channel; run `go test -race` [BOOTDEV (Learn Go ch 13), LG2 (ch 12), LGWT (Concurrency, Select), PIKE]"),
    (4.0, "`sync.Mutex` vs `RWMutex`, `WaitGroup`, context; scheduler model (G, M, P) and GC basics. Boot.dev chapter 14, Learning Go 2e chapters 12 and 14. Use in the agent (code): a `WaitGroup` and a per-probe `context.WithTimeout`, with a test that a slow server is cut off [BOOTDEV (Learn Go ch 14), LG2 (ch 12, 14), LGWT (Sync, Context), GO-CONTEXT, GO-PIPELINES, ARDAN (Scheduling in Go, Garbage Collection in Go)]"),
])
unit("A1", "6.2", [(6.0, "Sequential agent (v3.6: starts right after G7; v3.8: from the skeleton built in G2-G7): config, `net/http`, per-probe timeout; code-read the timeout fields of the `net/http` Client [LG2 (ch 13), LGWT (HTTP server, JSON), EFFGO]")], deps=["G7"])
unit("A2", "6.2", [(9.0, "`errgroup` with `SetLimit` (the only concurrency model in the agent), cancellation; `-race` clean; prove the active probe count stays bounded and a slow probe is cancelled; v3.9: a down target becomes a failed `ProbeResult` and never cancels the other probes (the errgroup context is cancelled once `Wait` returns or one function errors), with a test [PIKE, GO-PIPELINES, ERRGROUP]")], deps=["A1"])
unit("A3", "6.2", [(5.0, "POST results to E1's ingestion path, each naming the release it probed (v3.9 r2), retries with backoff and jitter, idempotency key; prove two simultaneous pushes with one key, and a lost response followed by a retry, create one record [SRE (ch 22)]")], deps=["A2", "S5", "E1"])
unit("A4", "6.2", [(5.0, "`log/slog`, `client_golang` metrics, graceful SIGTERM that stops new work and finishes in-flight probes within a stated limit; code-read how a `client_golang` histogram records a value [GO-SLOG, CLIENTGO]")], deps=["A3"])
unit("A5", "6.2", [(6.0, "Leak lab: remove a timeout, find it in pprof, fix it, add a test; record the load and the observation window [GO-PPROF, GO100]")], deps=["A2"])
unit("A6", "6.2", [(5.0, "Static binary image; ADR on control plane vs data plane [DOCKER]")], deps=["A4", "D1"])
unit("DS1", "6.4", [
    (3.5, "Distributed-systems proof, part 1 (v3.9): set up Maelstrom; Gossip Glomers challenges 1 (Echo) and 2 (Unique ID Generation) in Go, checked by Maelstrom's Jepsen-based checker. Use in the agent (code): the agent's result IDs come from the same coordination-free scheme, with a test that two agents never produce the same ID [GG, MAELSTROM]"),
    (6.0, "Part 2: challenge 3 (Broadcast), from one node to a partitioned multi-node cluster; why gossip converges and what a partition does to it. Use in PRCP (explain): how config would reach a very large agent fleet, push vs pull vs gossip, written into the scale-envelope ADR [GG, MAELSTROM, KLEP]"),
    (3.5, "Part 3: challenge 4 (Grow-Only Counter) on Maelstrom's sequentially consistent key-value store. Use in PRCP (explain): per-agent probe counters merged in the control plane without a lost update [GG, MAELSTROM]"),
], deps=["G7", "H3"])


# ---------- 6.3 Kubernetes ----------
unit("K1", "6.3", [
    (1.5, "kind cluster up, first pod (done Oct 26) [KK (Core Concepts: Pods, Pods with YAML, and the Pods demo), KIND]"),
    (2.5, "Core Concepts, architecture lessons in the course's own order (v3.9, Om Nov 13): Cluster Architecture, Docker vs containerd, etcd (skip the optional etcd commands), kube-apiserver, kube-controller-manager, kube-scheduler, kubelet, kube-proxy. Use on kind (code): name each Pod `kubectl get pods -n kube-system` shows on your kind cluster and what it does, then write where kubelet runs and why it is not in that list (it is a process on the node, not a Pod), one line each in `k8s-notes.md` [KK (Core Concepts), KIND]"),
])
unit("K2", "6.3", [(5.0, "Core Concepts, workload lessons in the course's order: ReplicaSets, Deployments, Services, Namespaces, Imperative Commands, each with its practice test; then the `kubectl` drill (get, describe, logs, exec, events, `-o yaml`), moved here because the course's Imperative Commands lab uses `create deployment`, `scale` and `expose`; controller anatomy beyond the course: watch, cache, work queue, reconcile, requeue with backoff, finalizers, owner references, leader election. Use on kind (code): the drill on your kind cluster, its output pasted into `k8s-notes.md` [KK (Core Concepts), K8S]")], deps=["K1"])
unit("K3", "6.3", [
    (3.25, "Scheduling, in the course's order: labels and selectors, taints and tolerations, node selectors and node affinity, resource requirements and limits, DaemonSets, static pods; then requests, limits and QoS classes. Use on kind (code): PRCP's own image (from D1) as a Deployment with requests and limits, and a label selector that picks only its pods [KK (Scheduling), K8S (QoS)]"),
    (3.25, "Logging and Monitoring, then Application Lifecycle Management in the course's order: rolling updates and rollbacks (rollout status, history, undo), commands and arguments, environment variables, multi-container and init containers, autoscaling (HPA vs VPA vs cluster autoscaler); plus StatefulSet vs DaemonSet vs Job and the three probe types. Use on kind (code): roll PRCP out to a new tag and undo it; liveness and readiness probes on PRCP's `/health` and `/ready` [KK (Logging and Monitoring; Application Lifecycle Management), K8S (Workloads, probes)]"),
], deps=["K2", "D1"])
unit("K4", "6.3", [(4.25, "ConfigMap env vs volume and Secret (taught in the course's Application Lifecycle section), then Security in the course's order: authentication, kubeconfig, API groups, authorization, RBAC, cluster roles, ServiceAccounts, security contexts, network policies; skip certificate creation and TLS, which are CKA exam-only. Use on kind (code): PRCP's settings from a ConfigMap and a Secret, and a ServiceAccount with no extra rights [KK (Application Lifecycle Management: ConfigMaps, Secrets; Security), K8S (RBAC good practices)]")], deps=["K3"])
unit("K5", "6.3", [(4.25, "Storage basics (volumes, persistent volumes and claims, enough for Postgres on kind in K6a), then Networking in the course's order: pod networking and CNI, Service networking (iptables mode, EndpointSlices), cluster DNS and CoreDNS, Ingress; CNI vs CSI at architecture level; skip the kubeadm install sections. Use on kind (code): a Service in front of PRCP, reached by DNS name from another pod [KK (Storage; Networking), K8S (Virtual IPs)]")], deps=["K4"])
unit("K7a", "6.3", [
    (2.5, "Troubleshooting, the course's last section: scenarios 1-3 on a sample app: CrashLoopBackOff, Pending, OOMKilled [KK (Troubleshooting: Application Failure labs), LEARNK8S, K8S (Debug)]"),
    (1.5, "Scenarios 4-5: Service without endpoints; an object stuck on a finalizer [KK (Troubleshooting labs), LEARNK8S, K8S (Debug)]"),
], deps=["K5"])
unit("K6a", "6.3", [(3.0, "PRCP on kind, part 1 (v3.6, moved forward): Postgres and the PRCP API; Services, ConfigMap, Secret, probes, limits; manifests in the repo [K8S, KIND]")], deps=["D1", "K5"])
unit("K7b", "6.3", [
    (1.0, "Scenario 6 on PRCP: CPU throttling vs a memory-limit kill [LEARNK8S, K8S (Debug), ARDAN (Kubernetes CPU and memory limits)]"),
    (0.75, "Scenario 7 on PRCP: an aggressive liveness probe killing pods under load [LEARNK8S, K8S (Debug)]"),
    (0.75, "Scenario 8 on PRCP: a bad rollout: status, history, undo [LEARNK8S, K8S (Debug)]"),
    (0.75, "Scenario 9 on PRCP: ConfigMap as env vs volume after an update [LEARNK8S, K8S (Debug)]"),
    (0.75, "Scenario 10 on PRCP: DNS resolution failing inside a pod; KodeKloud control-plane and worker-node labs only as optional bonus [LEARNK8S, K8SAF, K8S (Debug)]"),
], deps=["K6a"])
unit("K6b", "6.3", [(2.0, "PRCP on kind, part 2: add the Go agent; its ServiceAccount sets `automountServiceAccountToken: false` and gets no Role; the assistant deploys all parts from a fresh clone [K8S, KIND]")], deps=["A6", "K6a"])

# ---------- 6.4 HLD ----------
unit("H1", "6.4", [
    (2.5, "Delivery framework; watch one full mock [HI, HI-YT]"),
    (2.5, "Framework dry run, then a first full design on paper, graded [HI]"),
])
unit("H2", "6.4", [
    (7.0, "Load balancing, caching, CDN, queues, rate limiting [HI (Core Concepts), BBG]"),
    (5.0, "Object storage, WebSocket vs SSE, IDs, storage selection [HI (Key Technologies), BBG]"),
], deps=["H1"])
unit("H3", "6.4", [
    (4.5, "Replication and quorums, lectures 5.1-5.3 [KLEP]"),
    (4.5, "Partitioning, consistent hashing, consistency models, lectures 7.2-7.3 [KLEP, HI]"),
    (2.0, "PRCP scale envelope ADR (v3.9): the real problem PRCP solves (most outages start with a change) and the numbers it must hold: Om's IKS fleet as the measured base (200-300 clusters, about 19,000 workers), then a design target of a million probed endpoints with stated inputs (v3.9 r2, for example one result per endpoint a minute at about 500 bytes: about 16,700 results a second, 1.44 billion a day, 720 GB a day of raw payload before indexes, replication and retention): agents sharded by service, results aggregated per wave, `decide()` still pure, the first limit you expect and the observation that would prove you wrong; O1 measures against the same inputs. Use in PRCP (explain): the scale-envelope ADR committed to `docs/adr/` [SRE, SREWB (Appendix C), KLEP]"),
], deps=["H2"])
unit("H4", "6.4", [
    (5.0, "Failure models, consensus, Raft, leases, split brain, lectures 2.1-2.4 and 6.1-6.2 [KLEP]"),
    (4.0, "Overload, cascading failure, retries, idempotency [SRE (ch 21-22)]"),
    (4.0, "2PC vs Saga vs outbox, delivery semantics, DLQ, multi-region, lecture 7.1 [KLEP, SRE (ch 23)]"),
], deps=["H3"])
unit("H5", "6.4", [
    (5.5, "Practice, one-page skeleton then spoken: multi-tenant PRCP at 10,000 services (isolation, quotas, noisy neighbours, per-tenant limits, blast radius); a job scheduler [HI, PRIMER]"),
    (2.5, "Practice (v3.6): a Kubernetes fleet upgrade orchestrator for 300 clusters and 19k nodes, from your IKS work: waves, maintenance windows, drain and replace, health gates, pause and rollback [HI, PRIMER]"),
    (4.5, "Practice: payment or reservation; rate limiter [HI, PRIMER]"),
    (2.5, "Practice (v3.6): a global deployment system with canary steps and automated gates across regions [HI, PRIMER]"),
    (2.5, "Practice: notification service [HI]"),
], deps=["H4"])
unit("H6", "6.4", [
    (3.0, "Mock 1, with a human peer when one is available, else the assistant (v3.6: moved before normal application volume; v3.8: a human first; only taught material is scored) [HI]"),
    (3.0, "Mock 2 with a human [Peers, or a paid expert mock per section 6.9]"),
    (3.0, "Mock 3 [HI]"),
    (3.0, "Mock 4 with a human [Peers, or a paid expert mock per section 6.9]"),
], deps=["H2"])

# ---------- 6.5 LLD and machine coding ----------
unit("L1", "6.5", [
    (1.0, "OOP pillars, interface vs abstract class, composition [ARJAN, RG]"),
    (2.75, "Association, aggregation, coupling and cohesion (v3.6: 1h more, from W3's measured pace). Use in PRCP (explain): name one association, one aggregation and one composition among `models.py`'s classes, and one coupling problem in `api/main.py`, in a short note in `docs/` [ARJAN]"),
    (0.5, "Composition over inheritance, cold explanation. Use in PRCP (explain): explain it with `checker.py`, which takes its HTTP getter as a parameter instead of subclassing [ARJAN]"),
])
unit("L2", "6.5", [
    (2.75, "SOLID: SRP, OCP, LSP. Use in PRCP (code): find one SRP and one OCP problem (for example the probe endpoints in `api/main.py`) and fix one, tests green [ARJAN]"),
    (2.75, "SOLID: ISP, DIP; violation and fix for each. Use in PRCP (code): show where `api/dependencies.py` applies DIP through the repository Protocols, and fix one ISP or DIP problem [ARJAN]"),
], deps=["L1"])
unit("L3", "6.5", [
    (3.75, "Strategy, Factory, Observer. Use in PRCP (code): probe types as a Strategy and their creation as a Factory, replacing one `if` chain, tests green [RG, ARJAN]"),
    (3.75, "State, Decorator; class and sequence diagrams. Use in PRCP (explain): a class diagram of the domain and a sequence diagram of one probe run, committed to `docs/`; v3.9: all L3 teaching ends before MC2, and L3 closes right after MC2 with the rep 2 diagram [RG]"),
], deps=["L2"])
unit("L4", "6.5", [
    (1.0, "Where the lock goes; lock granularity. Use in PRCP (explain): decide where the lock goes in the in-memory result repository and why, for the next part to build [PYDOCS (threading)]"),
    (2.0, "A thread-safe class with a test that fails without the lock. Use in PRCP (code): the class is the in-memory result repository [PYDOCS (threading, queue)]"),
], deps=["L3"])
MC_PARTS = [
    ("MC0", 1.25, "Machine coding method (MC0), taught and dry-run Oct 19, 75 min measured (v3.6 records it) [section 6.5]"),
    ("MC1", 2.5, "Rep 1: Snake and Ladder, 90 min timed, no AI, raw notes committed before any cleanup, then a 60-minute review [WAT]"),
    ("MC2", 2.5, "Rep 2: Splitwise, 90 min timed plus review [WAT]"),
    ("MC3", 2.5, "Rep 3 (v3.6): Parking Lot, clean, no AI (the Sep 28 attempt was AI-assisted practice), 90 min timed plus review [ALLD]"),
    ("MC4", 2.5, "Rep 4: in-memory relational datastore with keys, indexes and constraints [WAT, ALLD]"),
    ("MC5", 2.5, "Rep 5: thread-safe key-value store with TTL, or a job scheduler (the concurrency rep) [WAT]"),
    ("MC6", 2.5, "Rep 6: reservation system, AI-assisted: architecture first, every generated line read, tests required, log of what AI proposed, accepted and rejected [WAT]"),
    ("MC7", 2.5, "Rep 7 (v3.6): Elevator system, 90 min timed plus review [ALLD]"),
    ("MC8", 2.5, "Rep 8: cab or gym booking [WAT]"),
]
for lab, h, txt in MC_PARTS:
    unit(lab, "6.5", [(h, txt)])
U["MC2"]["deps"] = ["L3", "Y8a"]
U["MC5"]["deps"] = ["L4"]
MP_TEXT = [
    "Machine coding practice 1: look at every item before deciding; one small search problem (match 2nd, match last, no match); trace the first non-match and write the asserts before coding [section 6.5]",
    "Machine coding practice 2: read counted input with one moving pointer (timetable input; a section count of 0) [section 6.5]",
    "Machine coding practice 3: make random things testable (coin-toss race with the tosses passed in) [section 6.5]",
    "Machine coding practice 4: one owner of state (wallet transfers: return or mutate, written in the docstring) [section 6.5]",
    "Machine coding practice 5: thin working version first (ticket counter; something prints by minute 10) [section 6.5]",
    "Machine coding practice 6: who owns which behaviour (a 40-line script moved into 2-3 classes; uses L1) [section 6.5]",
    "Machine coding practice 7: absorb a change in one place (taxi fare; night charge arrives at minute 35) [section 6.5]",
    "Machine coding practice 8: dress rehearsal, all skills together (tiny vending machine, 60 min) [section 6.5]",
]
MP_LOOP = "Machine coding practice: the skill the latest rep scored lowest, on a fresh small problem (section 6.5 loop) [section 6.5]"

# ---------- 6.6 DSA handled separately ----------

# ---------- 6.7 Supporting ----------
unit("S1", "6.7", [
    (0.5, "Checklist A baseline, cold, recorded per section 7 [section 7]"),
    (2.5, "Locks, condition variables, semaphores [OSTEP (Concurrency)]"),
    (2.5, "Common concurrency bugs, mapped to Go and Python [OSTEP, BEAZ]"),
])
unit("S2", "6.7", [
    (1.5, "DNS, TCP handshake, TLS cost, with `dig`, `curl -v`, `openssl s_client` [JVNS, MWDNS, HPBN, HN]"),
    (4.5, "HTTP/2, pooling, timeouts vs deadlines, L4 vs L7, retry amplification; `ss` for connection states; one `tcpdump` capture of a handshake [HPBN, HN]"),
    (2.0, "Diagnose a planted timeout on a real probe request with `dig`, `curl -v`, `ss`, `tcpdump`, name the slow layer, then write it up [HPBN]"),
])
unit("S3", "6.7", [(3.0, "gRPC: protobuf evolution, streaming, deadlines, status codes [GRPC]")])
unit("S4", "6.7", [(5.0, "Process vs thread, virtual memory, file descriptors, page cache, OOM, signals, practised on a misbehaving process with `ps`, `top`, `/proc`, `lsof`, `strace`, `ulimit` [OSTEP (Virtualization)]")])
unit("S5", "6.7", [(6.0, "API design; authn vs authz, JWT, mTLS; a written rule for which probe targets are allowed (server-side request forgery, OWASP API7); OWASP pass over PRCP (v3.6: before A3 opens ingestion) [OWASP]")])

# ---------- 6.8 Stories ----------
unit("R1", "6.8", [
    (1.0, "Resume v1 draft"),
    (1.0, "LinkedIn live, every field filled, notice 90 days; no Premium (commute time is fine, Om's Oct 21 rule)"),
    (1.0, "Naukri live, every filter field filled, notice 90 days, about 15 days before Gate A (Om, Oct 18); on a layoff notice it goes live that day"),
    (2.0, "Resume refresh: Go is now listable"),
])
unit("R2", "6.8", [
    (2.0, "Write the first two honest stories (registry cost, IKS upgrades); fix the registry figures [section 6.8]"),
    (1.0, "Tell the first two stories aloud in voice mode, with two follow-ups each (v3.8: moved from W23; calibration calls before this are diagnostic) [section 6.8]"),
    (2.0, "Write the third honest story (Circuit Breaker) [section 6.8]"),
    (3.0, "Two dated older stories (v3.6): the GetMyUni build (what you wrote alone, decisions, outcome) and one tech-lead delivery decision; for every story, separate what you wrote, decided, reviewed and coordinated; confirm your exact part in the IBM Circuit Breaker CRD before any resume line [section 6.8]"),
    (1.0, "Tell each story aloud; answer follow-ups [section 6.8]"),
    (2.0, "New work stories; monthly rehearsal [section 6.8]"),
])
unit("R3", "6.8", [
    (1.5, "60-second pitch and recruiter answers"),
    (2.5, "5-minute PRCP narrative, timed; outline one production system you owned for a deep dive [section 6.8]"),
    (4.0, "Two 30-minute deep dives, timed: PRCP, and one sanitized production system you owned [section 6.8]"),
])
unit("R4", "6.8", [(3.0, "Resume v2 against the classified JD harvest (section 8)")])

# ---------- 6.10 Operators ----------
unit("OP1", "6.10", [(6.5, "Controller and CRD concepts beyond K2: CRD anatomy (group, version, kind, schema validation, status subresource), desired vs observed state, level-triggered reconcile, informer, lister and cache, work queue and rate-limited requeue, `observedGeneration` and conditions, owner references, finalizers, leader election, controller RBAC, admission webhooks in concept, client-go vs controller-runtime, Kubebuilder vs Operator SDK; v3.9: what the Kubebuilder test environment runs (an API server and etcd only: no built-in controllers and no garbage collection, so owner-reference clean-up is never seen there) [KK (CKA 2025 updates: Custom Resource Definition, Custom Controllers, Operator Framework), KB (Architecture, Quick Start), KK-OPS if live in your subscription]")], deps=["G7", "K5"])
unit("OP2", "6.10", [(5.0, "Operator 1 read end to end: `kubernetes/sample-controller` on kind. Run it, then trace main, the shared informers, event handlers, the work queue, `syncHandler`, the Deployment it creates for a `Foo`, owner references and the status update; change replicas, delete the Deployment, watch it come back; a one-page trace with a sequence diagram [SAMPLE-CTRL, KIND]")], deps=["OP1"])
unit("OP3", "6.10", [(6.0, "Operator 2 read end to end: Argo Rollouts' analysis controller on kind. Run a canary with an AnalysisTemplate using the `web` provider; trace how the Rollout creates an AnalysisRun, how measurements become Successful, Failed or Inconclusive, the requeue interval, and how the Rollout pauses or aborts; map Inconclusive to PRCP's UNKNOWN; a one-page trace [ARGO-RO, KIND]")], deps=["OP2"])
unit("OP4", "6.10", [(9.5, "Build in PRCP: scaffold `prcp-gate-controller` with Kubebuilder; a `ReleaseGate` CRD (spec: service, environment, PRCP endpoint; status: decision, conditions, `observedGeneration`, last evaluated); the reconcile asks PRCP's API for the GateDecision and writes status; the controller never decides, `decide()` stays in Python; v3.9: the reconcile registers the gate in PRCP by the object's UID (a small PRCP endpoint and table, with a test), so the finalizer in OP5 has something real to remove [KB (Tutorial: Building CronJob, as the worked example), KIND]")], deps=["OP3", "K6a", "A2"])
unit("OP5", "6.10", [(8.5, "Correct controller behaviour: idempotent reconcile, conditions, requeue with backoff on UNKNOWN or a PRCP error (UNKNOWN never promotes), a finalizer that removes the gate registration (by UID) from PRCP on delete, with a test that a delete while PRCP is down keeps the finalizer until PRCP answers, Events recorded [KB]")], deps=["OP4"])
unit("OP6", "6.10", [(9.0, "Tests: envtest integration tests against a fake PRCP (`httptest`): create gives PASS in status; PRCP down gives UNKNOWN and a requeue; delete runs the finalizer; a spec change moves `observedGeneration`; v3.9: a stale PRCP answer (a decision for an older generation) is ignored, and the suite output proves each envtest case ran; table-driven unit tests for the HTTP client [KB (Writing tests, envtest)]")], deps=["OP5"])
unit("OP7", "6.10", [(6.0, "Deploy and defend: image, least-privilege RBAC from the markers (read every rule), leader election with 2 replicas, kill the leader and watch the takeover; debug with logs, Events and `kubectl describe`; ADR: why a controller is PRCP's Kubernetes-native interface and only an adapter [KB, K8S, KIND]")], deps=["OP6"])

# ---------- 6.11 Cloud and Terraform ----------
unit("CL1", "6.11", [(8.0, "AWS foundations, mapped from IBM Cloud: account with MFA and a $10 budget alarm, IAM users vs roles vs policies and least privilege, regions and AZs, VPC (CIDR, public and private subnets, route tables, internet and NAT gateways and NAT cost, security groups vs NACLs), EC2, S3, RDS and EKS in outline; the IBM Cloud to AWS and GCP mapping table from memory (was S6) [AWS-CPE, EKSWS (Intro), AWS-FREE]")])
unit("CL2", "6.11", [(8.0, "Terraform fundamentals: providers, resources, variables, outputs, locals, state (local, then an S3 backend with locking), plan, apply, destroy, data sources, `for_each` vs `count`, one module of your own, `fmt` and `validate`, import and drift; only free or near-free resources [TF-TUT (Get Started - AWS, then Modules and State), FCC-TF]")], deps=["CL1"])
unit("CL3", "6.11", [(12.0, "PRCP on AWS with Terraform: your own VPC module (2 AZs), EKS through `terraform-aws-modules/eks` with every input explained, RDS Postgres in private subnets, images in ECR; deploy the K6 manifests, smoke-test the gate, then `terraform destroy` the same day; a runbook and a cost log [TF-AWS-EKS, EKSWS (Fundamentals), TF-TUT]")], deps=["CL2", "K6a"])
unit("CL4", "6.11", [(5.0, "IaC in CI: `fmt`, `validate` and `plan` on every PR through GitHub OIDC (no static keys), the plan as a PR artifact, remote state, one drift check; ADR on state, module boundaries and OIDC [GH-OIDC, GHA, TF-TUT]")], deps=["CL3", "C1"])

TRACK_SEC = {
    "6.1": "PRCP", "6.2": "Go", "6.3": "Kubernetes", "6.4": "HLD", "6.5": "LLD",
    "6.7": "Supporting", "6.8": "Stories", "6.10": "Operators", "6.11": "Cloud",
}


def total(label):
    return sum(h for h, _ in U[label]["parts"])

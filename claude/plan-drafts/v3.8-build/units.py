"""v3.8 unit ledger (v3.6 base; v3.8 adds a use step in real code to every teaching part): every unit, its section, its parts (hours, text with resources)."""
from collections import OrderedDict

U = OrderedDict()


def unit(label, sec, parts, deps=()):
    U[label] = {"sec": sec, "parts": parts, "deps": list(deps)}


# ---------- 6.1 PRCP core ----------
unit("P1", "6.1", [
    (0.5, "Python prerequisite Block 1, context managers and `with`, done Oct 17 [RP (\"Python's with Statement: Manage External Resources Safely\")]"),
    (2.25, "Python prerequisites left after Block 1, Block 2 restarted Oct 18 from zero: pytest basics (what pytest is, how it finds and runs tests, reading a failure), done Oct 22; then fixtures with `return` [PCC (ch 11), RP, PYTEST (fixtures), MCODING]"),
    (1.0, "Fixtures with `yield`, right after Y3's generator basics, then dataclass equality [PYTEST (fixtures), RP, MCODING]"),
    (7.25, "psycopg 3 prerequisite first (Getting Started: basic usage, passing parameters, transactions; a 15-line insert, select, rollback practice script); then one use case end to end through the real database, including one specified failure; then repositories for all 5 entities with rollback tests. Reuse what October taught (v3.8): the rollback fixture is a `yield` fixture and each transaction uses `with` [PSY]"),
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
    (4.5, "pytest beyond the basics: fixture scopes, `conftest.py`, parametrize, `monkeypatch`, `tmp_path`; then Hypothesis on `decide()` [PYTEST, HYP]"),
])
unit("Y7a", "6.1", [
    (1.0, "PRCP code walk, part 1 (v3.6, moved forward): before P1 changes them, explain the repository Protocols, schemas and `conftest.py` fixtures line by line; fix or log what you cannot defend [section 6.1]"),
])
unit("Y7b", "6.1", [
    (4.0, "PRCP code walk, part 2: every other pre-plan module explained cold (Pydantic schemas, FastAPI `Depends` and `dependency_overrides`, Enums, exceptions, `decide()`); fix or log what you cannot defend [section 6.1]"),
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
unit("D1", "6.1", [
    (3.0, "Multi-stage Dockerfile, non-root user, `.dockerignore` [NANA-DOCKER, DOCKER]"),
    (2.0, "Compose with Postgres and healthchecks [NANA-DOCKER (Compose), DOCKER]"),
], deps=["P1"])
unit("D2", "6.1", [(3.0, "Namespaces, cgroups, layers, PID 1 and SIGTERM [DOCKER]")], deps=["D1"])
unit("C1", "6.1", [
    (4.0, "CI: lint, mypy, tests, coverage, image build [GHA]"),
    (4.0, "Self-gating: PRCP gates its own release [GHA]"),
], deps=["D1", "Y1"])
unit("O1", "6.1", [
    (5.5, "`/metrics`, `/live`, `/ready`; counter, gauge, histogram; label cardinality; load experiment: throughput, p50/p95/p99, saturation point, one bottleneck [PROM, VEGETA, SRE (ch 6)]"),
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
unit("G2", "6.2", [(3.5, "Arrays and slices: `len` vs `cap`, `append`, aliasing; start the Go vs Python list in `go-notes.md` (a slice is not a Python list copy). First file from a blank page with `t *testing.T` and a `strings.Builder` (the Oct 24 rep slipped on both). Use in the agent (code): start the Go module in PRCP's `agent/` folder; the probe targets are a slice, with a test on what `append` to a copy does [FCC-Go ch 8, LGWT, GO-SLICES]")])
unit("G3", "6.2", [(5.0, "Structs, methods and interfaces; receivers. Use in the agent (code): `Probe` and `Result` structs, a method on `Result`, and a `Prober` interface with a fake prober in the test [FCC-Go ch 4-5, LGWT]")])
unit("G4", "6.2", [(5.5, "Pointers and errors: `*` and `&`, the nil-interface trap, `%w`, `errors.Is` and `errors.As`; Go vs Python note: nil vs None, error values vs exceptions. Use in the agent (code): probe errors wrapped with `%w`, and a test that `errors.Is` finds a timeout through the wrapping [FCC-Go ch 6 and 11, LGWT (Pointers and errors, Error types), GO-ERRORS, GO100]")])
unit("G5", "6.2", [(3.5, "Maps; Generics chapter. Use in the agent (code): a registry map from probe name to `Prober`, with a test for a missing name [FCC-Go ch 9 and 15, LGWT (Maps, Generics)]")])
unit("G6", "6.2", [(5.0, "Dependency injection, mocking, HTTP server, httptest. Use in the agent (code): an HTTP prober with the `http.Client` injected, tested against an `httptest` server [LGWT (Dependency Injection, Mocking, HTTP server)]")])
unit("G7", "6.2", [
    (4.0, "Goroutines, channels, select, closed-channel reads. Use in the agent (code): run the probers in goroutines and collect results over a channel; run `go test -race` [FCC-Go ch 13, LGWT (Concurrency, Select), PIKE]"),
    (4.0, "`sync.Mutex` vs `RWMutex`, `WaitGroup`, context; scheduler model (G, M, P) and GC basics. Use in the agent (code): a `WaitGroup` and a per-probe `context.WithTimeout`, with a test that a slow server is cut off [FCC-Go ch 14, LGWT (Sync, Context), GO-CONTEXT, GO-PIPELINES, ARDAN (Scheduling in Go, Garbage Collection in Go)]"),
])
unit("A1", "6.2", [(6.0, "Sequential agent (v3.6: starts right after G7; v3.8: from the skeleton built in G2-G7): config, `net/http`, per-probe timeout; code-read the timeout fields of the `net/http` Client [LGWT (HTTP server, JSON), EFFGO]")], deps=["G7"])
unit("A2", "6.2", [(8.0, "`errgroup` with `SetLimit` (the only concurrency model in the agent), cancellation; `-race` clean; prove the active probe count stays bounded and a slow probe is cancelled [PIKE, GO-PIPELINES, ERRGROUP]")], deps=["A1"])
unit("A3", "6.2", [(5.0, "POST results, retries with backoff and jitter, idempotency key; prove two simultaneous pushes with one key, and a lost response followed by a retry, create one record [SRE (ch 22)]")], deps=["A2", "S5"])
unit("A4", "6.2", [(5.0, "`log/slog`, `client_golang` metrics, graceful SIGTERM that stops new work and finishes in-flight probes within a stated limit; code-read how a `client_golang` histogram records a value [GO-SLOG, CLIENTGO]")], deps=["A3"])
unit("A5", "6.2", [(6.0, "Leak lab: remove a timeout, find it in pprof, fix it, add a test; record the load and the observation window [GO-PPROF, GO100]")], deps=["A2"])
unit("A6", "6.2", [(5.0, "Static binary image; ADR on control plane vs data plane [DOCKER]")], deps=["A4", "D1"])

# ---------- 6.3 Kubernetes ----------
unit("K1", "6.3", [
    (1.5, "kind cluster up, first pod [KK (Core Concepts intro), KIND]"),
    (2.5, "`kubectl` drill: get, describe, logs, exec, events, `-o yaml` [KK (Imperative Commands with kubectl, and its practice test), K8S]"),
])
unit("K2", "6.3", [(5.0, "Architecture: every component; the chain after `kubectl apply`; controller anatomy: watch, cache, work queue, reconcile, requeue with backoff, finalizers, owner references, leader election [KK (Core Concepts: etcd, API server, controller manager, scheduler, kubelet, kube-proxy), K8S]")], deps=["K1"])
unit("K3", "6.3", [
    (3.25, "Pods, Deployment to ReplicaSet, rollout status, history, undo. Use on kind (code): PRCP's own image (from D1) as a Deployment; roll out a new tag, then undo it [KK (Pods, ReplicaSets, Deployments practice tests; Application Lifecycle: Rolling Updates and Rollbacks), K8S (Workloads)]"),
    (3.25, "StatefulSet vs DaemonSet vs Job; requests, limits, QoS; the three probe types; HPA vs VPA vs cluster autoscaler. Use on kind (code): requests, limits and liveness and readiness probes on PRCP's `/health` and `/ready` [KK (Scheduling: Resource Requirements, DaemonSets), K8S (StatefulSet, Job and CronJob, probes, QoS)]"),
], deps=["K2", "D1"])
unit("K4", "6.3", [(4.25, "Services, EndpointSlices, the Service dataplane (iptables mode, not IPVS internals), cluster DNS; CNI vs CSI at architecture level. Use on kind (code): a Service in front of PRCP, reached by DNS name from another pod [KK (Networking: Service Networking, DNS, CoreDNS, Ingress), K8S (Virtual IPs)]")], deps=["K3"])
unit("K5", "6.3", [(4.25, "ConfigMap env vs volume, Secret, ServiceAccount, RBAC least-privilege lab. Use on kind (code): PRCP's settings from a ConfigMap and a Secret, and a ServiceAccount with no extra rights [KK (Application Lifecycle: ConfigMaps, Secrets; Security: RBAC, ServiceAccounts), K8S (RBAC good practices)]")], deps=["K4"])
unit("K7a", "6.3", [
    (2.5, "Scenarios 1-3 on a sample app: CrashLoopBackOff, Pending, OOMKilled [KK (Troubleshooting: Application Failure labs), LEARNK8S, K8S (Debug)]"),
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
    (3.75, "State, Decorator; class and sequence diagrams. Use in PRCP (explain): a class diagram of the domain and a sequence diagram of one probe run, committed to `docs/` [RG]"),
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
unit("OP1", "6.10", [(6.0, "Controller and CRD concepts beyond K2: CRD anatomy (group, version, kind, schema validation, status subresource), desired vs observed state, level-triggered reconcile, informer, lister and cache, work queue and rate-limited requeue, `observedGeneration` and conditions, owner references, finalizers, leader election, controller RBAC, admission webhooks in concept, client-go vs controller-runtime, Kubebuilder vs Operator SDK [KK (CKA 2025 updates: Custom Resource Definition, Custom Controllers, Operator Framework), KB (Architecture, Quick Start), KK-OPS if live in your subscription]")], deps=["G7", "K5"])
unit("OP2", "6.10", [(5.0, "Operator 1 read end to end: `kubernetes/sample-controller` on kind. Run it, then trace main, the shared informers, event handlers, the work queue, `syncHandler`, the Deployment it creates for a `Foo`, owner references and the status update; change replicas, delete the Deployment, watch it come back; a one-page trace with a sequence diagram [SAMPLE-CTRL, KIND]")], deps=["OP1"])
unit("OP3", "6.10", [(6.0, "Operator 2 read end to end: Argo Rollouts' analysis controller on kind. Run a canary with an AnalysisTemplate using the `web` provider; trace how the Rollout creates an AnalysisRun, how measurements become Successful, Failed or Inconclusive, the requeue interval, and how the Rollout pauses or aborts; map Inconclusive to PRCP's UNKNOWN; a one-page trace [ARGO-RO, KIND]")], deps=["OP2"])
unit("OP4", "6.10", [(8.0, "Build in PRCP: scaffold `prcp-gate-controller` with Kubebuilder; a `ReleaseGate` CRD (spec: service, environment, PRCP endpoint; status: decision, conditions, `observedGeneration`, last evaluated); the reconcile asks PRCP's API for the GateDecision and writes status; the controller never decides, `decide()` stays in Python [KB (Tutorial: Building CronJob, as the worked example), KIND]")], deps=["OP3", "K6a", "A2"])
unit("OP5", "6.10", [(7.0, "Correct controller behaviour: idempotent reconcile, conditions, requeue with backoff on UNKNOWN or a PRCP error (UNKNOWN never promotes), a finalizer that deregisters the gate in PRCP on delete, Events recorded [KB]")], deps=["OP4"])
unit("OP6", "6.10", [(8.0, "Tests: envtest integration tests against a fake PRCP (`httptest`): create gives PASS in status; PRCP down gives UNKNOWN and a requeue; delete runs the finalizer; a spec change moves `observedGeneration`; table-driven unit tests for the HTTP client [KB (Writing tests, envtest)]")], deps=["OP5"])
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

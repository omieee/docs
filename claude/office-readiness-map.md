# Office readiness map: every Go and Kubernetes idea for a year of platform work

**Version 1, Oct 27 2026, written by Claude for Om.** Status: new recommendation, office time only, zero plan hours. Used with `claude/office-task-protocol.md`. Generic on purpose: the assistant helping on an office task uses this map by itself; Om does not ask a coach which topics a task needs.

**How the assistant uses it, on every task**
1. List the ideas on the task's code path, using the numbers below.
2. For each idea, check its plan unit. **Unit already closed** (Om's log, or ask him): no lesson; one 2-minute recall question, then apply it. **Unit not closed yet:** a short lesson now, in office time: one idea, one tiny example Om types and runs in his own `learning-go-sandbox`, then the exact office line where it appears; 10-30 minutes; logged as "seen at work, not proven".
3. Teach in tier order, and within a tier in number order. Never teach an idea before the ones it rests on have at least been seen (for example 8 pointers before 27 client calls).
4. An idea not in this map: name it in the after-merge handoff line; the Phase 1 coach adds it here, once.
5. A lesson at work never replaces the plan unit or its proof. The unit still teaches and proves it on its own date.

Dates are the v3.8 week map (section 14); a unit closes at its proof, near its last week.

## Tier 1. Reading and changing Go (any office Go task)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 1 | Packages, imports, exported names (capital letter) | G1, done Oct 2026 |
| 2 | Functions, two return values, `if err != nil` | G1, then G4 (Dec 7-Jan 10) |
| 3 | Variables, `:=`, zero values | G1, done |
| 4 | Slices, `append`, aliasing | G2 (Nov 2-22) |
| 5 | Maps | G5 (Jan 4-24) |
| 6 | Structs and struct tags (`json:"spec"`) | G3 (Nov 16-Dec 13) |
| 7 | Methods and receivers | G3 |
| 8 | Interfaces, implicit satisfaction | G3 |
| 9 | Pointers, nil, `&` and `*`, optional pointer fields | G4 (Dec 7-Jan 10) |
| 10 | Errors: wrapping with `%w`, `errors.Is` and `errors.As` | G4 |
| 11 | `defer`, closing response bodies and files | G4 |
| 12 | `context.Context`: passing it, cancellation, timeouts | G7 (Feb 8-Mar 14) |
| 13 | Modules: `go.mod`, `go.sum`, `replace` lines | G1, plus the office on-ramp (F5) |

## Tier 2. Tests and the repo's own checks (any change that has tests)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 14 | `go test`, table-driven tests, `t.Run` | G1, then G6 (Jan 18-Feb 14) |
| 15 | Fakes through interfaces, dependency injection, a fake clock | G6 |
| 16 | `httptest` for HTTP code | G6 |
| 17 | `go test -race`, the repo's Makefile test target, coverage | G7 and A2 (May 3-30 2027) |
| 18 | The assertion library the repo uses | Not in the plan: office lesson at first use |
| 19 | Lint warnings from the repo's linter config | Not in the plan: office lesson at first use, fix the cause, never a blanket ignore |

## Tier 3. Kubernetes objects (any platform task)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 20 | Pods, Deployments, `kubectl get`, `describe`, `logs`, events | K1 (Oct 26-Nov 22) |
| 21 | Control-plane parts, the chain after `kubectl apply`, what a controller is | K2 (Nov 16-Dec 13) |
| 22 | Jobs, probes, requests and limits, rollout and undo | K3 (Dec 14-Jan 24) |
| 23 | Services, DNS, NetworkPolicy | K4 (Jan 18-Feb 14) |
| 24 | ConfigMap, Secret, ServiceAccount, Role and RoleBinding | K5 (Feb 15-Mar 7) |
| 25 | Debugging a broken workload from evidence | K7a (Mar 8-May 23) |

## Tier 4. Controllers (operator tasks)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 26 | The reconcile loop: desired vs actual, one change per round, idempotent | K2 in concept; OP1 (Aug 9-Sep 5 2027) |
| 27 | Client calls: Get, List, Create, Update, Patch, and the status update | OP4 (Oct 11-Nov 14 2027) |
| 28 | The reconcile result: requeue, retry after an error | OP1, OP5 (Nov 8-28 2027) |
| 29 | `resourceVersion` and update conflicts | OP1 |
| 30 | `generation`, `observedGeneration`, conditions | OP1, OP5 |
| 31 | Owner references and garbage collection | OP1, OP2 (Aug 30-Sep 19 2027) |
| 32 | Finalizers and deletion | OP1, OP5 |
| 33 | Watches, predicates, owned objects | OP1, OP2 |
| 34 | CRD Go types, markers, generated code (deepcopy, CRD YAML, RBAC) | OP4, OP7 (Dec 20 2027-Jan 16 2028) |
| 35 | envtest, and what it cannot prove | OP6 (Nov 29-Dec 26 2027) |
| 36 | Leader election | OP7 |

## Tier 5. Concurrency (only when the code path has it)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 37 | Goroutines, channels, `select` | G7 (Feb 8-Mar 14) |
| 38 | `sync.Mutex`, `WaitGroup`, the race detector | G7 |
| 39 | `errgroup`, bounded work | A2 (May 3-30 2027) |
| 40 | Goroutine leaks, clean shutdown | A4, A5 (Jun 14-Jul 25 2027) |

## Tier 6. HTTP, CLI and delivery (when the task calls services or ships something)

| # | Idea | Taught in the plan |
| --- | --- | --- |
| 41 | HTTP clients, timeouts, JSON, pagination of an API | A1 (Mar 8-Apr 4), A3 (May 31-Jun 20 2027) |
| 42 | Structured logs and metrics | A4 (Jun 14-Jul 4 2027) |
| 43 | Container images and the CI pipeline | C1 (Jun 28-Jul 25), A6 (Jul 26-Aug 15 2027) |
| 44 | The CLI framework the repo uses | Not in the plan: office lesson at first use |
| 45 | Helm charts, values, upgrade and rollback | Not in the plan (v3.9 F4 pending): office lesson at first use |

## What Om can do alone, and when

| By | Units closed | Office work Om can mostly own | Still needs help |
| --- | --- | --- | --- |
| Nov 22 2026 | G2, K1 | Read loops and slices; read-only `kubectl` checks | Almost every code change |
| Jan 10 2027 | G3, G4, K2 | Read most reconcile code; small changes to structs, pointers and errors | Tests, concurrency, controller API calls |
| Mar 14 2027 | G5-G7, K3-K5 | Table tests and fakes; RBAC and config fixes; simple goroutine code | Controller mechanics (Tier 4) |
| Aug 15 2027 | A1-A6, C1 | HTTP clients, bounded concurrency, logs and metrics, CI | Controller mechanics |
| Jan 16 2028 | OP1-OP7 | A controller feature end to end | Helm, unless F4 is approved |

**The weak spot, said plainly:** from January to August 2027, Tier 4 (controllers) comes only from office lessons, because OP1 starts Aug 9 2027. If controller work at the office turns out to be regular, the Nov 15 batch can move OP1 earlier (see F5 in `claude/plan-drafts/2026-10-27-v3.9-candidates-cdp-handoff.md`).

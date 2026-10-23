## 14. Week map from Oct 1

Seventy-four weeks, Oct 1 2026 to Feb 27 2028, 820.75 scheduled hours (v3.7: one week added before Gate B). W0 to W2 show what was done, and W3 is the current week. From W4 the map is built by a script from section 6 in lanes: a Python and PRCP lane every week, Go, Kubernetes, LLD and HLD lanes running in parallel at 1-2.5 hours a week, a stories lane when due, plus the fixed lines (DSA, machine coding practice, campaign, proofs and the weekly close). Where no unit keeps a watched track alive, the script places a retrieval rep (section 6.12). The checker confirms every week fits its cap (12, or 7 in light weeks), every unit's hours match section 6, DSA totals 144.25, no unit starts before the units it depends on, and no watched track breaks the continuity rule. The proof column names the units that close that week; each unit's proof is in section 6.

**How to use a row.** Work runs left to right within a week, DSA first each day. Watch the bracketed video first (bedside time is ideal), then read the docs as the authority, then build at the desk. A unit's proof is due in the week it ends. DSA problems are default picks from the NeetCode roadmap; swap any you have already solved. Each week's DSA hours cover the due colds first, under the 45-minute daily cap (section 6.6). The campaign line is real time inside the 12 hours; an unused campaign hour moves to the next unit in the row. When real weeks slip, the unfinished work moves forward in row order at the Sunday close, and the coach checks the continuity record before choosing the next block.

**Resource key (checked 2026-09-25; v3.6 and v3.7 additions checked 2026-10-23). Docs are lookup only; see section 6.**

| Key | Resource | Use |
| --- | --- | --- |
| NC | [NeetCode course and roadmap](https://neetcode.io/roadmap) | Lesson before every DSA family |
| FCC-Go | [freeCodeCamp and Boot.dev Go course](https://www.freecodecamp.org/news/go-programming-video-course/) (Lane Wagner, 2023; chapters with timestamps) | Go video, by chapter |
| LGWT | [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests) | Primary Go text, chapters as named |
| PIKE | [Rob Pike, Go Concurrency Patterns](https://www.youtube.com/watch?v=f6kdp27TYZs) ([slides](https://go.dev/talks/2012/concurrency.slide)) | Concurrency video |
| GO-SLICES, GO-ERRORS | [Go Slices: usage and internals](https://go.dev/blog/slices-intro), [Working with Errors in Go 1.13](https://go.dev/blog/go1.13-errors) | Official deep reads |
| GO-CONTEXT, GO-PIPELINES | [Go blog: context](https://go.dev/blog/context), [pipelines](https://go.dev/blog/pipelines) | Cancellation and fan-out |
| GO-PPROF, GO-SLOG | [Profiling Go programs](https://go.dev/blog/pprof), [Structured logging with slog](https://go.dev/blog/slog) | Leak lab, logging |
| EFFGO, ERRGROUP, CLIENTGO | [Effective Go](https://go.dev/doc/effective_go), [errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup), [client_golang](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus) | Idiom and packages |
| KK | [KodeKloud](https://kodekloud.com/) (owned): CKA course by Mumshad Mannambeth, lectures plus in-browser lab clusters with auto-checked practice tests; its 2025 updates include Custom Resource Definition, Custom Controllers and Operator Framework lessons | Main Kubernetes video and labs; only the lessons each week names |
| KK-OPS | [KodeKloud, Kubernetes Operators](https://kodekloud.com/courses/kubernetes-operators) (about 5 hours of video: Kubebuilder, controller-runtime, status, events, finalizers) | Only if it is live in Om's subscription; check first (v3.6) |
| KB | [The Kubebuilder Book](https://book.kubebuilder.io/): Architecture, Quick Start, [Tutorial: Building CronJob](https://book.kubebuilder.io/cronjob-tutorial/cronjob-tutorial.html), the envtest reference | Controller worked example (v3.6) |
| SAMPLE-CTRL | [kubernetes/sample-controller](https://github.com/kubernetes/sample-controller): a client-go controller for a `Foo` resource that creates Deployments; README and `docs/controller-client-go.md` | Operator 1 to read (v3.6) |
| ARGO-RO | [Argo Rollouts: Analysis and Progressive Delivery](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/) and its source on GitHub (`argoproj/argo-rollouts`, the analysis controller) | Operator 2 to read (v3.6) |
| CLIENTGO-K8S | [controller-runtime](https://pkg.go.dev/sigs.k8s.io/controller-runtime) and [client-go](https://pkg.go.dev/k8s.io/client-go) package docs | Lookup for 6.10 (v3.6) |
| NANA-K8S | [TechWorld with Nana, Kubernetes full course](https://www.youtube.com/watch?v=X48VuDVv0do) | Fallback if a KodeKloud lesson does not click |
| NANA-DOCKER | Docker Crash Course for Absolute Beginners and Docker Compose in 1h, on [TechWorld with Nana](https://www.youtube.com/c/techworldwithnana) | Docker video |
| KIND | [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/) | Local cluster |
| K8S | [Kubernetes Concepts](https://kubernetes.io/docs/concepts/), [Debug tasks](https://kubernetes.io/docs/tasks/debug/) | Authority, pages as named |
| LEARNK8S | [Visual guide to troubleshooting Kubernetes deployments](https://learnk8s.io/troubleshooting-deployments) | Debugging map |
| AWS-CPE | AWS Skill Builder, "AWS Cloud Practitioner Essentials" (free, beginner, [skillbuilder.aws](https://skillbuilder.aws)) | AWS foundations video (v3.6) |
| EKSWS | [Amazon EKS Workshop](https://www.eksworkshop.com/), maintained by AWS: Intro and Fundamentals modules | Hands-on EKS (v3.6) |
| AWS-FREE | [AWS Free Tier, Jul 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/): up to $200 in credits on a 6-month free plan | Cost rules for 6.11 (v3.6) |
| TF-TUT | [HashiCorp tutorials: Get Started - AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started), then the Modules and State tutorials | Primary Terraform text (v3.6) |
| FCC-TF | [freeCodeCamp: Learn Terraform and AWS by Building a Dev Environment](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) (Derek Morgan, 2022, about 2 hours; no modules section) | Terraform video, by chapter (v3.6) |
| TF-AWS-EKS | [terraform-aws-modules/eks](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest) | EKS module for CL3 (v3.6) |
| GH-OIDC | [GitHub Docs: Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws) | CI without static keys (v3.6) |
| PG | [PostgreSQL docs](https://www.postgresql.org/docs/current/) | Authority, chapters as named |
| CMU | CMU Database Group YouTube channel, 15-445 Fall 2024 lectures, by title | Database internals video |
| TS-ISO | [Tech School: isolation levels in Postgres](https://dev.to/techschoolguru/understand-isolation-levels-read-phenomena-in-mysql-postgres-c2e) | Hands-on isolation demo |
| SQLBOLT | [SQLBolt](https://sqlbolt.com/) lessons, plus its [subqueries and set-operations topics](https://sqlbolt.com/topics) | SQL concepts before each pgexercises section |
| PG-TUT | PostgreSQL tutorial, [Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html) | Window-functions lesson |
| UTIL | [Use The Index, Luke](https://use-the-index-luke.com/sql) | Indexing |
| PGEX | [pgexercises](https://pgexercises.com/) | SQL practice, 81 exercises |
| PSY, SQLA, ALEMBIC | [psycopg 3](https://www.psycopg.org/psycopg3/docs/), [SQLAlchemy 2.0 tutorial](https://docs.sqlalchemy.org/en/20/tutorial/), [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | Driver, ORM, migrations |
| HN | Hussein Nasser's YouTube channel, searched by topic | Database and network intuition |
| BEAZ | [David Beazley, Python Concurrency From the Ground Up](https://pyvideo.org/pycon-us-2015/python-concurrency-from-the-ground-up-live.html) | Python concurrency video |
| PYDOCS | [Python docs](https://docs.python.org/3/): asyncio, data model, threading, queue, profile | Authority |
| MCODING, ARJAN | mCoding and ArjanCodes YouTube channels | Python internals, design |
| RP | [Real Python](https://realpython.com/) free written tutorials, by the title each week row names (titles checked 2026-10-05; skip the paid video courses) | First read for Y3 and Y8 topics |
| FLUENT | *Fluent Python*, 2nd edition, Luciano Ramalho (O'Reilly, 2022), chapters as each week row names them (section 6.9 trigger met Oct 5) | Second pass for Y3 and Y8, named chapters only |
| MYPY | [mypy docs](https://mypy.readthedocs.io/en/stable/): Getting started; Using mypy with an existing codebase (checked 2026-10-05) | Y1 |
| PYTEST, HYP | [pytest](https://docs.pytest.org/), [Hypothesis](https://hypothesis.readthedocs.io/) | Test depth |
| PCC | *Python Crash Course*, 3rd edition (Eric Matthes), chapter 11 "Testing Your Code"; Om owns it | pytest basics, first read |
| DOCKER, GHA | [Docker docs](https://docs.docker.com/), [GitHub Actions docs](https://docs.github.com/actions) | Authority |
| PROM, USE | [Prometheus instrumentation](https://prometheus.io/docs/practices/instrumentation/), [USE method](https://www.brendangregg.com/usemethod.html) | Metrics |
| SRE | [Google SRE book](https://sre.google/sre-book/table-of-contents/), chapters 6, 21, 22, 23 | Monitoring, overload, consensus |
| HI, HI-YT | [Hello Interview](https://www.hellointerview.com/) Core Concepts and Key Technologies; its YouTube mock walkthroughs | Design course |
| KLEP | [Martin Kleppmann, Distributed Systems lectures](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB), [lecture notes](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf) | Distributed systems video |
| PRIMER | [system-design-primer](https://github.com/donnemartin/system-design-primer) | Gap filler |
| WAT, ALLD, RG | [workat.tech machine coding](https://workat.tech/machine-coding), [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) (its problem list includes Parking Lot and Elevator System, checked 2026-10-23), [Refactoring.Guru](https://refactoring.guru/design-patterns) | LLD practice and patterns |
| OSTEP, HPBN | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/), [High Performance Browser Networking](https://hpbn.co/) | OS, concurrency, networking |
| GRPC, OWASP | [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/), [OWASP API Security Top 10, 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | RPC, API security |
| INTERDB | [The Internals of PostgreSQL](https://www.interdb.jp/pg), Hironobu Suzuki (covers v14 and earlier; the core ideas hold) | Main text for MVCC, VACUUM, WAL, replication |
| GOBYEX | [Go by Example](https://gobyexample.com/) (linked from go.dev) | "How do I do X" instead of package docs |
| GO100 | [100 Go Mistakes](https://100go.co/) (free site for the book) | The classic Go traps with examples |
| RP-ASYNC | [Real Python: asyncio walkthrough](https://realpython.com/async-python/) (about 40 minutes) | Main text for asyncio |
| K8SAF | [Kubernetes Failure Stories](https://k8s.af/) | Real postmortems |
| JVNS, MWDNS | [Julia Evans' blog](https://jvns.ca/), [Mess With DNS](https://messwithdns.net/) | Networking explained plainly; a real DNS server to break |
| BBG | ByteByteGo on YouTube | Short visual design refreshers |
| ARDAN | Ardan Labs blog: [Scheduling in Go, parts I-III](https://www.ardanlabs.com/blog/2018/08/scheduling-in-go-part2.html), Garbage Collection in Go parts I-III, and its Kubernetes CPU and memory limits articles for Go | Go scheduler and GC at interview level |
| VEGETA | `vegeta` HTTP load generator (the older `hey` is unmaintained) | O1 load experiment |
| Peers | A real engineer who interrupts | Human mocks |
| PEER | [Exponent peer mock interviews, data structures and algorithms](https://www.aced.io/practice/data-structures-and-algorithms-mock-interviews) (tryexponent.com redirects here; hour-long sessions, partners take turns as interviewer and interviewee; checked 2026-10-23), or any engineer Om does not work with | Human live-coding mock (v3.7) |


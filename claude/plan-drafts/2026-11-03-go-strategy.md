# Go strategy proposal (Claude, Nov 3 2026)

Status: PROPOSAL, not approved, not plan content. Written so it is not forgotten; it goes into the section 9 change for Go once Om says yes. Nov 15 batch item B12.

## 1. The problem (evidence)

- The v3.8 G units follow Learn Go with Tests (LGWT) chapter order: Hello World, Integers, Iteration (G1); Arrays and slices (G2); Structs, methods and interfaces (G3); Pointers and errors (G4); Maps (G5). Checked Nov 3 in LGWT's SUMMARY.md.
- Each unit also cites freeCodeCamp/Boot.dev chapters, and that course has another order: 1 Variables, 2 Constants and Formatting, 3 Conditionals, 4 Functions, 5 Structs, 6 Interfaces, 7 Errors, 8 Loops, 9 Slices, 10 Maps, 11 Pointers, 12 Packages and Modules, 13 Channels, 14 Mutexes, 15 Generics, 16 Enums, 17 Quiz (boot.dev course page, Nov 3).
- Result on Nov 3: Boot.dev Ch 9 lessons 11-13 needed interfaces, a function as an input, the `strings` package and runes, none taught (Claude coach error, 16:12).
- Same bug class found while checking: G3 teaches value vs pointer receivers before G4 teaches pointers.

## 2. Resource check (Nov 3)

| Resource | Content against the s6.2 depth bar | Presentation | Verdict |
| --- | --- | --- | --- |
| Boot.dev Learn Go (paid, owned) | 148 lessons, 17 chapters, a "comprehensive introduction". No chapter on writing tests or on `context`, which G6, G7 and A1-A5 need | Interactive, code checked in the browser; Om solved Ch 9 lessons 11-12 alone | Good first contact, too shallow to be the spine |
| Boot.dev Learn HTTP Clients in Go | Chapters: Why HTTP, JSON, DNS, URIs, Headers, Methods, Paths, HTTPS, Errors, cURL; page names no timeouts, `context` or retries (A1, A3 need all three) | Interactive | Not needed |
| Learning Go 2e, Bodner (owned) | 16 chapters in dependency order: types, composite types, control, functions, pointers, types/methods/interfaces, generics, errors, modules, tooling, concurrency, standard library, context, writing tests. Covers every G unit plus the context and testing Boot.dev lacks | Book (text) | MUST-HAVE: the spine and the order |
| LGWT (free) | Test-first practice; also Dependency Injection, Mocking, Concurrency, Select, Sync, Context | Text plus typed code and tests | Keep, for tests after each topic |
| Concurrency in Go, Cox-Buday (owned) | Concurrency patterns in depth | Book | Keep for G7, A2, A5 depth |
| Exercism Go | Concept list has no goroutines, channels, context, testing, error wrapping or generics (listed as planned) | Interactive | Not enough |
| Let's Go Further, Edwards ($59.95, Go 1.27, Oct 2026) | Building API servers; intermediate to advanced, needs Go basics first. The agent is an HTTP client | Book | Not Phase 1; recheck after the JD harvest |
| Ardan Labs Ultimate Go (bundle $419 with BF2026 in Nov, regular $699, one year, 123+ h) | Lessons not checked by Claude; 123 h is more than the whole Go budget (68.5 h) | Video, real teacher | Not recommended until its lessons are checked |

## 3. The strategy

1. **One spine for order: Learning Go 2e chapter order.** Every G unit is re-mapped to its chapters. A unit never starts before the chapters it depends on.
2. **Per topic, in this order:** (a) Boot.dev chapter, if one exists, for hands-on first contact; (b) the Learning Go chapter for depth, only the sections the unit names; (c) the LGWT chapter for writing the tests; (d) the agent use step in PRCP's `agent/` folder.
3. **Taught list.** `claude/taught/go.md` lists every Go concept taught, with date and source. Before Om opens any lesson, the coach reads the lesson, compares it with the list, and says stop or skip before Om starts. Never "paste it and I will explain".
4. **All tracks.** The same check for every track's resources. Before Nov 15: audit Kubernetes (KodeKloud order), Python and psycopg, DSA lessons and LLD for the same mismatch, and report.
5. **Checker.** A `check_plan.py` rule: a unit may not cite a resource chapter before earlier units cover the chapters it depends on.
6. **Hours.** Sized from each chapter's pages and Om's measured Boot.dev pace (Nov 2-3: 13 lessons in about 195 minutes elapsed, teaching included, about 15 minutes a lesson). Every addition names what moves.

## 4. Proposed sequence (to be sized)

Chapter titles are from O'Reilly's table of contents, checked Nov 3; section contents are not checked yet.

| Step | Learning Go 2e | Boot.dev Learn Go | LGWT | Plan unit |
| --- | --- | --- | --- | --- |
| 1 | Ch 2-4 types, composite types, control (section list to be checked in Om's copy) | Ch 1-3, 8, 9 (done), 10 | Arrays and slices | G1, G2 |
| 2 | Ch 5 functions (functions as values) | Ch 4 (6 lessons left) | - | new |
| 3 | Ch 6 pointers | Ch 11 | - | G4 part, moved before G3 |
| 4 | Ch 7 types, methods, interfaces, embedding | Ch 5 (5 left), 6 | Structs, methods and interfaces | G3 |
| 5 | Ch 9 errors | Ch 7 | Pointers and errors | G4 |
| 6 | Ch 8 generics | Ch 15 | Maps | G5 |
| 7 | Ch 10-11 modules and tooling | Ch 12 | - | G1 leftovers |
| 8 | Ch 15 writing tests | - | Dependency Injection, Mocking | G6 |
| 9 | Ch 12 concurrency, Ch 14 context | Ch 13, 14 | Concurrency, Select, Sync, Context | G7 (plus Concurrency in Go) |
| 10 | Ch 13 standard library (net/http, slog) | - | - | A1, A4 |

## 5. Open for Om

- Yes or no to the spine and the per-topic order.
- Is Learning Go 2e on paper only, or also on Kindle (bedside reading)?
- Yes or no: fix Go now under s9 trigger 1 (untaught prerequisite blocking this week's work), the other 11 batch items on Nov 15.

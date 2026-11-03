# Go appendix, Nov 4 to Nov 15 2026 (approved amendment)

- Status: APPROVED by Om, Nov 3 2026 16:45 IST: "Yes to all" (the Go strategy in `2026-11-03-go-strategy.md`) and "create an appendix ... for now just cover what is from tomorrow till 15th". This is an approved amendment kept outside the plan file. It is folded into v3.9 at the right weeks on Nov 15; `plan/Phase1_Master_Plan_v3.8.md` is not edited before then.
- Scope: the Go lane only, Nov 4-15 (rest of W5, all of W6). Every other line of the W5 and W6 rows stays as v3.8 has it.
- Rule for every step: before Om opens any material, the coach reads it, checks every concept it uses against `claude/taught/go.md`, and says stop or skip before Om starts. After each step, the coach adds what was taught to that file.

## Steps, in order

Section lists for Learning Go chapters 2 and 3 are from O'Reilly's pages for the 2nd edition, read Nov 3 20:59.

| # | Step | Where | Box | Before it can start |
| --- | --- | --- | --- | --- |
| A | Learning Go 2e, chapter 2, all sections (checked Nov 3 against the taught list: nothing assumed that is not taught): predeclared types, zero value, literals, booleans, numeric types, a taste of strings and runes, explicit type conversion, untyped literals, `var` vs `:=`, `const`, typed and untyped constants, unused variables, naming | Bedside, Kindle | 0.75h | None |
| B | Learning Go 2e, chapter 3, from "Arrays" to "Strings and Runes and Bytes" (arrays, slices, `len`, `append`, capacity, `make`, emptying a slice, declaring, slicing, `copy`, array and slice conversion, strings, runes and bytes). The maps sections wait for Boot.dev Ch 10 (Boot.dev first, per the strategy); the structs sections wait for G3 | Bedside, Kindle | 0.5h | A done |
| C | Start `go-notes.md` in `learning-go-sandbox`: a slice is not a Python list copy; `'a'` is a rune, `"a"` is a string; Go does not mix `int` and `float64`. Then chapter 2's exercises, typed and run; the coach checks them against the taught list first | Desk | 0.5h | A and B done |
| D | One file from a blank page with `t *testing.T` and a `strings.Builder` (the plan's G2 line; both slipped on Oct 24). Shown next to a pytest test first, then Om types it | Desk | 0.25h | None (both taught in G1 and RR1) |
| E | Learn Go with Tests, "Arrays and slices", in `learning-go-sandbox`, in two sittings. It uses `t.Run` and `t.Helper` (G1) and variadic functions (Boot.dev Ch 9 lesson 6). New, and explained by the chapter itself: `slices.Equal` and `go test -cover` | Desk | 1.5h | C and D done |
| F | Agent use step: start the Go module in PRCP's `agent/` folder (module path as in s6.2), the probe targets as a slice, and a test on what `append` to a copy does | Desk | 1h | E done; the coach checks first that Om has made a module before (G1) |
| G | G2 proof (s6.2): a test proving two slices share a backing array, explained cold, plus the three section 7 questions | Desk | 0.5h | F done |

Total: 5h. Order of days: A and B in W5 (bedside fits Diwali week; Wed Nov 4 is an office day), C to G in W6 around the W6 row's other lines. Om picks the days.

## Hours

- Available for Go: 4.25h. G2's box is 3.5h (W5 2h, W6 1h, and W7's 0.5h pulled into W6); the Nov 2-3 Go time was charged to contingency at Om's figure (`phase1-log.md`, W5 row), so the box is unspent in the records. Plus 0.75h freed in W5: Y7a 0.25h (closed early, Oct 30) and the 0.5h campaign line (Om is not applying now, so it moves as the row rule says).
- Needed: 5h. The 0.75h gap is charged to contingency only if it is used (plan BUG B12), so no other track moves before Nov 15.

## Not in this window (v3.9 decides order and weeks on Nov 15)

- Boot.dev Ch 4 Functions (lessons 12-17) with Learning Go chapter 5; Boot.dev Ch 8 Loops with Learning Go chapter 4.
- Pointers (Boot.dev Ch 11, Learning Go chapter 6) before G3, so value and pointer receivers are taught after pointers.
- G3 onward, rebuilt on Learning Go's chapter order, with Go in Action 2e sections 8.5.5, 8.6, 9.2.2 and 11.3 where the strategy file names them.

## Coach work before Nov 15 (not Om's study time)

- Audit the other tracks for the same mismatch (Kubernetes on KodeKloud's order, Python and psycopg, the DSA lessons, LLD); report in `claude/outbox.md` and the Nov 15 batch by Sat Nov 14.
- Draft the `check_plan.py` rule: no unit may cite a resource chapter before earlier units cover what that chapter depends on.

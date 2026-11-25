# Go: what Om has been taught

Purpose: before Om opens any Go lesson, chapter or exercise, the coach checks every concept it uses against this list and says stop or skip before he starts (Go strategy, approved Nov 3 2026 16:45). Add a line after every step. "Seen" means used once with help; it is not yet a topic Om can be tested on.

## Taught

| Concept | Source | Date | Evidence |
| --- | --- | --- | --- |
| `go mod init`, `go test`, `go vet`, `gofmt`, `package main` vs a library package | G1, LGWT Hello World, Integers, Iteration | Oct 5-18 | `learning-go-sandbox` `g1/`, PR #2 |
| Functions, `if`, `switch`, `const`, the basic `for` loop | G1, LGWT | Oct 5-18 | `g1/` |
| `t.Run` subtests, `t.Helper`, `testing.TB`, Example and Benchmark functions | G1, LGWT | Oct 5-18 | `g1/`, `rr/` |
| `strings.Builder` | RR1, LGWT Iteration | Oct 24 | `rr/repeat.go`; slipped from a blank page, still on the G2 list |
| Variables, constants and formatting, conditionals | Boot.dev Ch 1-3 | done before Phase 1, date not known | Om's Boot.dev progress (Nov 2 screenshot); retention not checked |
| Functions lessons 1-11, Structs lessons 1-5 | Boot.dev Ch 4, Ch 5 | done before Phase 1, date not known | Om's Boot.dev progress; retention not checked |
| Arrays `[N]T` vs slices `[]T`, slicing, `make`, `len` and `cap`, variadic `...T`, `append` (store the result), `range`, a slice of slices | Boot.dev Ch 9 lessons 1-9 | Nov 2 | Om's screenshots, all passed |
| Two slices sharing one array (append surprises) | Boot.dev Ch 9 lesson 10 | Nov 3 | Om's screenshot, question 3 right |
| A string as a slice of bytes; comparing a character with `'A'` and `'Z'` | Boot.dev Ch 9 lesson 12 | Nov 3 | passed, written alone |
| Predeclared types and the zero value; literals (integer, float, rune, string); booleans; numeric types; a first look at strings and runes; explicit type conversion (no automatic `int` to `float64`); untyped literals; `var` vs `:=`; `const`, typed and untyped constants; unused variables; naming | Learning Go 2e ch 2 (appendix step A) | Nov 3 | read at bedside [90m], Om: done 23:09; 'literal' unclear, taught 23:12 (a value written straight in the code; literals are untyped, so `var f float64 = 42` works but `var f float64 = i` with `i int` fails, both run on Go 1.24); exercises not yet typed (step C) |
| Test names start `Test` plus a capital letter (`Testtwo` fails to build, `TwoTest` never runs); test files end `_test.go` (opposite of pytest); `t *testing.T` is the running test's handle; `go test -count=1` skips the cached result | Chat, Om's questions | Nov 25 | PRCP PR #12 `agent/targets_test.go`; Claude ran each naming case on Go 1.27.0 |
| `append` to a copy (`b := a`) leaves `a`'s length and items unchanged; each slice keeps its own length | G2 step F | Nov 25 | PRCP PR #12 `5b2d5f9`, prediction and why right |
| `slices.Equal`, `slices.Contains` | LGWT Arrays and slices, step F | Nov 16, Nov 25 | learning-go-sandbox PR #7, PRCP PR #12 |

## Seen once, not yet taught as a topic

| Concept | Where | Date | Full topic |
| --- | --- | --- | --- |
| An interface as a list of required methods; calling `msg.Type()` | Boot.dev Ch 9 lesson 11 | Nov 3 | G3 |
| A function passed as an input and called | Boot.dev Ch 9 lesson 13 | Nov 3 | Boot.dev Ch 4, Learning Go ch 5 |
| `range` gives a copy; write to `messages[i]` to change the element | Boot.dev Ch 9 lesson 13 | Nov 3 | G2 (step E) |
| A rune is one character in single quotes; a string uses double quotes | Boot.dev Ch 9 lesson 13 | Nov 3 | first look in Learning Go ch 2 (read Nov 3); full in ch 3 (step B) |
| `strings.Contains`, `strings.ToLower` | Boot.dev Ch 9 lesson 13 tip | Nov 3 | Learning Go ch 13 |

## Not taught yet

Pointers (the `*` in `*testing.T` seen once, Nov 25); methods and receivers; interfaces as a topic; embedding; error values and wrapping (`%w`, `errors.Is`, `errors.As`); `defer`, panic and recover; maps; generics; packages and modules beyond one module; goroutines, channels, `select`; `sync.Mutex`, `WaitGroup`; `context`; `httptest`; the rest of the `slices` package (Equal and Contains used); `go test -cover`.

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
| Predeclared types and the zero value; literals (integer, float, rune, string); booleans; numeric types; a first look at strings and runes; explicit type conversion (no automatic `int` to `float64`); untyped literals; `var` vs `:=`; `const`, typed and untyped constants; unused variables; naming | Learning Go 2e ch 2 (appendix step A) | Nov 3 | read at bedside, Om: done 23:09; exercises not yet typed (step C) |

## Seen once, not yet taught as a topic

| Concept | Where | Date | Full topic |
| --- | --- | --- | --- |
| An interface as a list of required methods; calling `msg.Type()` | Boot.dev Ch 9 lesson 11 | Nov 3 | G3 |
| A function passed as an input and called | Boot.dev Ch 9 lesson 13 | Nov 3 | Boot.dev Ch 4, Learning Go ch 5 |
| `range` gives a copy; write to `messages[i]` to change the element | Boot.dev Ch 9 lesson 13 | Nov 3 | G2 (step E) |
| A rune is one character in single quotes; a string uses double quotes | Boot.dev Ch 9 lesson 13 | Nov 3 | first look in Learning Go ch 2 (read Nov 3); full in ch 3 (step B) |
| `strings.Contains`, `strings.ToLower` | Boot.dev Ch 9 lesson 13 tip | Nov 3 | Learning Go ch 13 |

## Not taught yet

Pointers; methods and receivers; interfaces as a topic; embedding; error values and wrapping (`%w`, `errors.Is`, `errors.As`); `defer`, panic and recover; maps; generics; packages and modules beyond one module; goroutines, channels, `select`; `sync.Mutex`, `WaitGroup`; `context`; `httptest`; the `slices` package; `go test -cover`.

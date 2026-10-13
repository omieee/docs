# G1 Setup and basics, unit interview

- **Date:** 2026-10-13, 11:35-11:55 IST (W2, Tuesday)
- **Coach:** Claude (owner of G1; reviewed PR #2 from Oct 5)
- **Type:** unit proof per plan section 7: artifact, tests, paragraph from memory, three cold questions. Go is not covered by the Oct 6 DSA no-same-session-retry amendment, so section 7's teach-then-one-retry applies.
- **Mode:** written in chat, cold. Code closed, no notes, no AI.
- **Prerequisite check:** every question is about something Om built and fixed in PR #2: package main vs library (taught Oct 7, fixed Oct 11), `t.Helper` (Hello World chapter, used in `assertCorrectMessage`), Examples with `// Output:` (Integers chapter, used in `ExampleAdd` and `ExampleRepeat`).
- **Result:** G1 PASS. Interview 5/6, no open fail.

## Artifact evidence

- learning-go-sandbox PR #2, head 087baf3 (Go 1.27): `go build ./...` ok, `go vet ./g1/...` clean, `go test -race ./g1/...` ok, gofmt clean.
- Chapters: Hello World (names, languages, empty-name default, `t.Run`, `t.Helper`), Integers (`Add`, `ExampleAdd`), Iteration (`Repeat(ch, times)` with `strings.Builder`, `b.Loop` benchmark, `ExampleRepeat`).
- Planted bugs on the final head: helloworld English, French, empty-name default all caught; integers hardcoded and wrong-operator caught; iteration hardcoded output, input ignored, count ignored, off by one in both directions all caught.
- Fix history: sub1 `package main` without `main` deleted (2279bbf), dead `main` removed from helloworld (2279bbf), package renamed `integers` (2279bbf), English-branch test (67e388b), count parameter and second positive case with count 0 (1214abb, 087baf3).

## Transcript (questions as asked, Om's answers verbatim)

### Paragraph
What you built in G1 (Hello World, Integers, Iteration), what the Go test tooling gave you, and one thing you'd do differently now.

> In G1 i built three small programs
>
> 1. hello world: here we first wrote a test case that will check if "Hello World!" is printed or no.. there was no function so a then with same package name a function was created .. test passed then we added param to take name as input and uinstead of world it would say "Hello Om!".. then we added different langugare like spanish, french english use switch case to handle language.. I also implemented a t.Run to group many cases together and also the checking part was added a helper function which all other test runs used
> 2. integer: Same approch first test then code did basic addition and learnt how to add Examples and use of //Output
> 3. iteration: same approch first test and then code eventually reached wher user will give which character and how many times that shoulkd be repeted use intially the for loop to append to sthe string and return tested it's benchmark using testing.B and for b.loop() and then as taught moved the code to use Strings.builder and saw the benchmark improved

Mark: accepted. Test-first flow, `t.Run`, helper, Examples, benchmark and the `+=` to `strings.Builder` change (what was rejected and why) all covered. Wording slip: the Hello test checks the returned string, not what is printed; only Examples check printed output. "Do differently" not stated separately.

### Q1 Mechanism
In Go, what makes a package something you can run with `go run`, versus a library that other code imports? Why did `go build ./...` fail on your old `sub1` folder?

> Go looks for package main and main function to make it executable .. go build failed because if i remember either the function main was there and package main was not not there or vice versa not remembering correctly

Mark: **1/2.** Rule right. Specific failure not recalled, and "vice versa" would not fail the build. Correct answer: sub1 was `package main` with no `func main`, so the build fails with "function main is undeclared in the main package". A `func main` inside a non-main package compiles fine as an ordinary unused function; only `go run` refuses it.

Taught: the four-row table (package main or not, with or without `func main`, effect on `go build` and `go run`).

Retry, as asked: you create `cmd/greet/greet.go` with `package greet` and a `func main()` that prints "hello". What happens with `go build ./...`? With `go run ./cmd/greet`? What one-line change makes it runnable?

> 1. build will succed .. it is just a function main() unline any other function no one calls
> 2. run will fail as there is no main package
> 3. change package greet to package main

Retry correct. Item stays 1 (prompted).

### Q2 Mechanism
Your `assertCorrectMessage` helper calls `t.Helper()`. If you deleted that line and a test failed, what would change in the failure output?

> For each error it will show the linenumber of the the code after that t.Helper() .. it wont show the actual error linenumber where the error occured

Mark: **2/2.** Without `t.Helper()` every failure reports the `t.Errorf` line inside the helper instead of the calling test line, so you cannot tell which case failed.

### Q3 Failure
Someone writes `ExampleRepeat` but leaves out the `// Output:` comment. Does `go test` still check it? If `Repeat` were broken, what would they see?

> the result will not show up in go test -v .. No they would not see the test failing if Output line was not written

Mark: **2/2.** Without `// Output:` the example is compiled but never run, so a broken `Repeat` still passes.

## Verdict

**G1 PASS.** Artifact green (build, vet, race, gofmt), tests catch every planted bug, interview 5/6 with the one partial repaired. Hours: plan 3h, actual not logged.

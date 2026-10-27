# Office task protocol: learn while you fix

**Version 1, Oct 27 2026, written by Claude for Om.** Status: new recommendation, office time only, zero plan hours. It goes into v3.9 with F5 (`claude/plan-drafts/2026-10-27-v3.9-candidates-cdp-handoff.md`) if Om approves; until then it is Om's working rule for office tasks if he says yes.

**Why this exists.** Om may get an operator fix before the plan has taught structs, pointers or the reconcile loop (G2-G4 run Nov 2 to Jan 10, K2 Nov 16 to Dec 13, OP1 from Aug 2027). Teaching Go from zero under a deadline fails, and jumping between topics leaves nothing behind. So every AI that helps on an office task follows the same fixed order below.

**Who does what.**
- The CDP - Working assistant (it has the docs and the repos) runs the delivery help and the short lessons, in this order.
- A Phase 1 coach (Claude or ChatGPT) runs only the explain-back check and writes the office proof record (section 7). It never sees IBM code, only Om's own sanitized words.
- Only IBM-approved AI tools touch IBM code. Nothing from IBM code goes into any public repo.

**Two rules that never bend.**
1. Delivery and study stay separate. An office lesson does not replace any G, K or OP unit or its proof; a concept learned at work is logged as "seen at work, not proven" and is still taught and proven in its own unit.
2. Nothing goes into a PR that Om cannot explain line by line, except under the deadline valve (step E).

## Step A. Triage (about 15 min, read only)

The assistant explains what the ticket asks and shows the code path it touches. No code is written. Om writes three lines in his own words: what is broken, which function it lives in, and what "fixed" will look like.

## Step B. Concept list from the code path (about 10 min)

The assistant lists only the Go and Kubernetes ideas that appear on that path, in the order of the kit below, at most five. Everything else in the file is written down as "not today". It then asks Om which ones he already knows, and starts from his answer.

## Step C. The lessons, in this fixed order, only those on the list

One idea, one tiny example that Om types and runs in his own `learning-go-sandbox` (his own code, never IBM code), then the exact line in the office code where the idea appears. Next idea only when Om says it is clear. If he is lost, go back one level and change the format; never add more. The assistant names the exact beginner chapter (the plan's LGWT, FCC-Go or Kubebuilder book) and checks it the same day.

| # | Idea | Why it shows up in operator code | Tiny example Om runs | Box |
| --- | --- | --- | --- | --- |
| 1 | Functions, two return values, `if err != nil` | Almost every call returns a value and an error | A function that returns `(int, error)`, called twice, once failing | 20m |
| 2 | Structs and struct tags | The custom resource is a Go struct; tags like `json:"spec"` map YAML fields to Go fields | A small struct with tags, printed as JSON | 20m |
| 3 | Pointers and nil | `Get(ctx, key, &obj)` fills your variable through a pointer; optional fields like `*int32` can be nil | Change a struct through a pointer and through a copy, and see which one changes; a nil check | 25m |
| 4 | Methods and receivers | The controller is a method on a struct: `func (r *XReconciler) Reconcile(...)` | A pointer-receiver method that changes the struct next to a value-receiver one that does not | 15m |
| 5 | Errors and the reconcile result | Returning an error means "try again later"; returning nil means this round is done | Wrap an error with `%w` and find it again with `errors.Is` | 15m |
| 6 | `context.Context` | Passed into every call so work can be cancelled | Pass `ctx` through two functions and cancel it | 10m |
| 7 | The reconcile loop | Read the object, compare desired with actual, make one change, write status, return | On a fake object, run the same reconcile twice: the second run must change nothing (that is what idempotent means) | 30m |

About 2h15m in total, taught once, on the first task; from the second task only the new ideas. Not in the kit: channels, goroutines, `select`, generics, informer internals. A typical reconcile function uses none of them, because the framework runs the workers; they are taught only if the actual code path contains them, and otherwise wait for G7 and OP1.

## Step D. The fix, in this order

1. Om writes the approach and one option he rejected; the assistant critiques it, it does not choose.
2. Om lists the test cases from the ticket (normal, edge, failure) before the assistant drafts any test.
3. The assistant may draft code; Om types the core logic himself where he can and walks every line.
4. Om runs the tests and the end-to-end check himself; the assistant helps read the output.
5. Om writes the PR description in his own words.

## Step E. Deadline valve

If the deadline is truly hard (incident, manager escalation), ship with full AI help; keeping the job wins. Mark the task "AI-assisted, not owned" in the handoff, and do steps C and F within the week.

## Step F. After the merge (about 15 min)

Om sends the Phase 1 coach one sanitized line, no IBM code, paths or names:

`OFFICE | ticket: safe id or "internal" | ideas seen: 1, 3, 7 | I wrote: ... | AI wrote: ... | rejected option: ... | tests and one failure case: ... | owned or AI-assisted | ask: explain-back`

The Phase 1 coach then runs a 10-minute explain-back (what changed, why, one failure case, the rejected option), writes the office proof record, logs each idea as "seen at work, not proven" against its unit (for example pointers against G4), and gives no unit PASS for it.

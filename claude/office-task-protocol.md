# Office task protocol: learn while you fix

**Version 1.1, Oct 27 2026, written by Claude for Om** (1.1: the fixed 7-idea kit is replaced by the full map). Status: new recommendation, office time only, zero plan hours. It goes into v3.9 with F5 (`claude/plan-drafts/2026-10-27-v3.9-candidates-cdp-handoff.md`) if Om approves; until then it is Om's working rule for office tasks if he says yes.

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

## Step B. Ideas on the code path, from the map (about 10 min)

The assistant lists the ideas the code path uses, by their numbers in `claude/office-readiness-map.md` (45 ideas in 6 tiers, each tied to the plan unit and date that teaches it). Everything else in the file is written down as "not today". It asks Om which ones he already knows, and starts from his answer.

## Step C. Lessons, only for ideas whose plan unit has not closed

The map's five rules decide this, so no coach is needed per task: a closed unit gets a 2-minute recall question; an open one gets a short lesson in tier order (one idea, one tiny example Om types and runs in his own `learning-go-sandbox`, then the exact office line; 10-30 minutes). If Om is lost, go back one level and change the format; never add more. The assistant names the exact beginner chapter from the plan's resources (LGWT, FCC-Go, the Kubebuilder book) and checks it the same day. For a first operator fix this is usually ideas 2, 6, 7, 9, 10, 12, 26 and 28, about two hours; channels and goroutines (37-38) only if the code path has them.

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

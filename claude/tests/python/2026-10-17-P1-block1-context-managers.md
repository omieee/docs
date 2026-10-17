# P1 prerequisite Block 1: context managers, unit interview

Coach: Claude · Date: 2026-10-17 · Week: W2 · Mode: written, cold (no notes, no running code, no AI)
Prerequisite check: studied Oct 14 (Real Python "Python's with Statement" parts 1-4, Real Python YouTube video), Tx exercise coded Oct 15-16.
Artifact: learning-python-sandbox PR #1 7b450d4: fresh clone 4 green, ruff clean, planted bugs 5/5 caught (42be54a had 1/3).

## Questions as asked (11:45 IST)

Q1. Take `with NewTx() as events:` where the body raises `IndexError`. Step by step, what does Python do from the `with` line until the error leaves the block? Name which methods get called, in what order, what ends up in `events`, and what `__exit__` receives.

Q2. Now `NewTx(swallow=True)`, and the body raises `IndexError`. Is the `IndexError` raised at all, yes or no? What exactly does returning `True` from `__exit__` do? And in a real database transaction wrapper, what goes wrong if `__exit__` always returns `True`?

Q3. `def save(): with NewTx() as events: return "done"`. The body leaves by `return`. Does `__exit__` run? If yes, what three values does it receive, and does it write COMMIT or ROLLBACK?

## Answers verbatim (11:51 IST)

> 1.: When with is called first the __enter__ runs and if there is return type we can assign that to the as clause. then till we are in with loop we work with it and ass soon as we left indent we come out of with and __exit_ gets run in that we check if any error occured and take necessary steps.. Suppose for example:
> (code) with pytest.raises(IndexError): with NewTx() as events: events[20000]  # This will raise the Index error and in our case will add rollback anbd propagate the error to outter level where we are using pytest to catcj the Index error / assert 2 == len(events) # and that is why we are checking it here / assert events == ["BEGIN", "ROLLBACK"]
>
> 2.: Index error as such will not get triggered that we can catch.. what happens is it will fail for sure as 2000 index is not there .. if we print we will still see those IndexError gets printed but not an Error that can bve catched is propagated
>
> 3. Exit will run and it will commit because we are returning "done" .. doesn't look to me any error happened

## Scores

- Q1 mechanism 1/2: order right (__enter__, its return bound by `as`, body, __exit__ on leaving), ROLLBACK and propagation right, final events right. Missing: what __exit__ receives (exc_type, exc, tb). Wording: `with` is not a loop; the body runs once.
- Q2 failure 1/2: right that the error does not leave the block. Wrong claim: "we will still see IndexError printed" (a suppressed error prints nothing unless __exit__ prints it). "Raised at all" muddled ("not triggered" vs "fail for sure"): it is raised, then handed to __exit__ and discarded. Danger of always-True not answered. Local FAIL on the wrong claim.
- Q3 transfer 1/2: __exit__ runs, COMMIT right, reason "no error" right. Missing the three values (None, None, None).
- Total 3/6. Gap seen twice: what __exit__ receives. Second gap: suppression is silent.

## Taught on the spot

Ran demo (Peek class printing its three arguments, returning True): normal finish -> None | None | None; IndexError -> <class 'IndexError'> | IndexError('list index out of range') | <traceback object>, and no traceback on screen, the line after the block runs; return -> None | None | None. Danger: an always-True DB wrapper rolls back and hides the error, the caller believes the save worked, nothing in the logs.

## Retry (fresh wording, same mechanisms)

Class Quiet: __enter__ returns "x"; __exit__ returns `exc_type == KeyError`. Block 1 body `{}["missing"]` then print("A"); block 2 body `[][0]` then print("B"). (a) What does Python pass into __exit__ in block 1? (b) Does "A" print, and does anything about the KeyError show on screen? (c) Does "B" print? If not, what happens instead?
Key (verified by running): (a) KeyError class, the KeyError object, a traceback object. (b) A prints; nothing about KeyError shows. (c) B does not print: __exit__ returns False, IndexError propagates, traceback shown, program stops.

## Correction 2026-10-17 12:05 IST (Claude scoring error)

Om challenged the "suppressed error prints nothing" point with his own Tx run (return True): the four lines after "----" came from his own print() calls in __exit__; Python printed no "Traceback" block and "Hello World" ran. Re-reading Q2: "if we print we will still see those IndexError gets printed" is conditional (if __exit__ prints it), which is correct. The "wrong claim" and the local FAIL on Q2 are withdrawn. Q2 stays 1/2 only because the always-True danger was not answered. Total still 3/6. Shown with a run: Tx with the prints removed and return True prints nothing about the error; with return False Python prints the Traceback and stops before "Hello World". Retry unchanged.

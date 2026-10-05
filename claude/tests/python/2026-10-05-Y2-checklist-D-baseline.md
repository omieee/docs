# Y2 Checklist D baseline

- **Date:** 2026-10-05 (W1, carried from W0)
- **Coach:** Claude
- **Mode:** written, cold. No notes, no AI, no running code. Labelled written (section 7: spoken preferred).
- **Purpose:** diagnostic gap list (section 6.1 Y2). Not graded PASS/FAIL per item.
- **Result:** 0 solid, 6 shaky, 13 missing.

| # | Item | Om's answer (summary) | Mark | Correct answer |
|---|---|---|---|---|
| 1 | Mutable vs immutable | Definition right. Named `str` and `int` as mutable. Both snippets right, with right reasons | shaky | Mutable: list, dict, set. Immutable: int, str, tuple. Snippet 1 prints `[1, 2, 3]`: `a` and `b` name one list. Snippet 2 prints `(1, 2)`: `y + (3,)` builds a new tuple and rebinds `y` only |
| 2 | Hashability, `__eq__`, `__hash__` | Don't know | missing | Hashable: has a hash that never changes and can be compared with `__eq__`. Needed for dict keys and set members. Line 3 raises `TypeError: unhashable type: 'list'`. Rule: `a == b` must imply `hash(a) == hash(b)` |
| 3 | Shallow vs deep copy | Shallow "references the value", deep makes a fresh copy. Both outputs right | shaky | Shallow copy: new outer container, same inner objects. Deep copy: copies all the way down. `b` is `[[1, 2, 99], [3, 4]]`, `c` is `[[1, 2], [3, 4]]` |
| 4 | list, dict, set complexity | 5 of 6 right. `x in set` given as O(n). Why set is faster: not sure | shaky | O(n), O(1) average, O(1) average, O(1) amortized, O(n), O(1) vs O(n). Sets and dicts are hash tables: hash the value, jump to its slot. A list scans every item |
| 5 | Iterator vs iterable | Don't know | missing | Iterable can hand out an iterator (`__iter__`), e.g. a list. Iterator has `__next__`, remembers its position and gets used up. A list is iterable, not an iterator. Prints `1`, `[2, 3]`, `[]` |
| 6 | Generators | "4", rest don't know | missing | A function with `yield`. Calling it runs no code; each `next()` runs to the next `yield`. Values come one at a time, lazily. Prints `start`, `making 0`, `0` |
| 7 | Decorators | "Makes a function do something else". Output given as `hi OM` | missing | A function that takes a function and returns a new one, usually wrapping it. `@shout` means `greet = shout(greet)`. Prints `HI OM`: `.upper()` applies to the whole returned string |
| 8 | Context managers | Don't know (first time seen) | missing | Object with `__enter__` and `__exit__`. `with` guarantees `__exit__` runs when the block ends: normally, by `return`, or by exception. Prints `enter`, `inside`, `exit`; `return False` does not suppress, so `ValueError` propagates and `after` never prints |
| 9 | Exceptions | Output right (`try`, `key`, `finally`). `finally` right. `else` unknown | shaky | `else` runs only when the `try` body raised nothing. `finally` always runs |
| 10 | dataclass vs class | "A class that only holds variables". `frozen` guessed right. All 3 outputs wrong (`False`, `True`, `(1,2)`) | shaky | `@dataclass` generates `__init__`, `__repr__` and `__eq__` from the fields. `frozen=True` makes field assignment raise `FrozenInstanceError` and generates `__hash__`. Prints `True`, `False` (plain class compares identity), `P(x=1, y=2)` |
| 11 | Typing | Output `ab` right, with the right reason (hints not enforced). `str \| None` right. mypy unknown | shaky | mypy is a static type checker: it reports both arguments as incompatible type `str`, expected `int`, without running the code |
| 12 | GIL | Don't know | missing | A CPython lock that lets one thread run Python bytecode at a time. Yes, the total can be under 2,000,000: `counter += 1` is load, add, store, and a thread switch between them loses updates. The GIL protects the interpreter, not your read-modify-write. It may not show on every run or version; nothing guarantees it |
| 13 | Thread vs process vs asyncio | Process "a task with many threads" (partly right). Thread vague. asyncio unknown. No picks | missing | Thread: runs inside a process, shares its memory. Process: own memory, can hold many threads. asyncio: one thread runs many tasks, switching at `await` while they wait on I/O. Picks: (1) asyncio (threads also work), I/O-bound; (2) processes, CPU-bound and the GIL; (3) threads, blocking I/O releases the GIL while waiting |
| 14 | Async cancellation and timeouts | Don't know | missing | Cancel raises `CancelledError` inside the task at its current `await`. A timeout (`asyncio.timeout`, `wait_for`) cancels the inner task and raises `TimeoutError` to the caller. Clean up in `finally` or `async with`; do not swallow `CancelledError` |
| 15 | pytest fixtures | Don't know | missing | A function pytest runs to set up what a test names as a parameter; reusable, with teardown. Code before `yield` is setup, the yielded value goes to the test, code after `yield` runs after the test even if it fails. Prints `open`, `test conn`, `close` |
| 16 | Property-based testing | Don't know | missing | An example test checks one input. A property test (Hypothesis) generates many inputs, checks a rule that must always hold, and shrinks a failure to the smallest case. Sort: same length, non-decreasing order, same items, sorting twice equals sorting once |
| 17 | Refcount and cyclic GC | Don't know | missing | CPython frees an object when its reference count hits zero. After `del`, the two lists still point at each other, so each count stays 1. The cyclic garbage collector finds such groups and frees them |
| 18 | MRO and `super()` | Don't know | missing | MRO: the order Python searches classes for a method. `D`'s MRO is D, B, C, A, object. `super()` means the next class in that order, not "my parent". Prints `D`, `B`, `C`, `A` |
| 19 | ABC vs Protocol | Don't know | missing | ABC is nominal: a class counts only if it inherits (or is registered). Protocol is structural: a class counts if it has the methods, checked by type checkers; runtime `isinstance` needs `@runtime_checkable`. Duck: (1) no, (2) yes |

## Blocking current PRCP work (moved into 1a, taught in P1 hours)

- 8 Context managers: psycopg uses `with` for connections and transactions.
- 15 pytest fixtures: P1 rolls back one transaction per test.
- 10 dataclass equality and repr: P1 tests compare returned rows as dataclasses.

## Deferred to their units

- Y1 (W9): mypy (11).
- Y3 (W18, W20, W33-W34): 1, 2, 3, 6, 7, 18, 19, and the rest of 10.
- Y4 (W24-W26): 13 (asyncio part), 14.
- Y5 (W30-W31): 12, 13 (threads vs processes).
- Y6 (W31): 16, plus fixture depth.
- No unit names these yet: 4 (complexity), 5 (iterators), 9 (`else`), 17 (refcount and GC). Flagged as a GAP for the next plan revision.

## Triggers

- Section 6.9: 5 or more data-model items shaky or missing (1, 2, 5, 8, 17, 18 at least). The *Fluent Python* 2nd edition trigger is met. No week row names it yet.

## Retries after teaching

(added below as they happen)

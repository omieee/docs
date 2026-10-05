# Y2 Checklist D baseline

- **Date:** 2026-10-05 (W1, carried from W0)
- **Coach:** Claude
- **Mode:** written, cold. No notes, no AI, no running code. Labelled written (section 7: spoken preferred).
- **Purpose:** diagnostic gap list (section 6.1 Y2). Not graded PASS/FAIL per item.
- **Result:** 0 solid, 6 shaky, 13 missing.

## Rules as stated at the start

> No notes, no AI, no running code. Answer in your own words. "Don't know" is a fine answer. I won't teach during the run. I can give one neutral nudge if an answer is unclear. Gaps that block P1 get taught at the end, and the full gap list comes then too.

## Transcript (questions as asked, Om's answers verbatim)

### Q1: mutable vs immutable

What is the difference between a mutable and an immutable object in Python? Give one example of each.

Then say what each snippet prints, and why:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

```python
x = (1, 2)
y = x
y = y + (3,)
print(x)
```

**Om:**
```text
Mutable objects are the objects whose value cna change like str, int immutable are the once whose value can't change like tupple

print(a) = [1,2,3] because b = a is b is actually refrensing the values so a, b both are pointing to same and either of them can change the values

print(x) = (1,2) it's tupple and valus can't change when y is create a totally new memory is allocated for that
```

Coach reply: "Q1: shaky. Right: the definition, and both snippets with the right reasons. Wrong: one example." (Marks shown only here; Om then asked for no marks until the end.)

### Q2: hashability, `__eq__` and `__hash__`

What does it mean for an object to be "hashable"?

What happens on line 3 here, and why?

```python
d = {}
d[(1, 2)] = "ok"
d[[1, 2]] = "?"
```

Last part: if `a == b` is True, what must be true about `hash(a)` and `hash(b)`?

**Om:**
```text
IDK / IANS
```

### Q3: shallow vs deep copy

What is the difference between a shallow copy and a deep copy?

What do the two prints show, and why?

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0].append(99)
print(b)
print(c)
```

**Om:**
```text
shallow copy means the value is refrenced deep  copy means value is actually copied and restured in different plave and than tagged to a new variable a fresh copy is made

print(b) = [[1, 2,99], [3, 4]]
print(c) = [[1, 2], [3, 4]]
```

### Q4: list, dict and set complexity

Give the typical time complexity for each operation:

1. `x in my_list`
2. `x in my_set`
3. `my_dict[key]`
4. `my_list.append(x)`
5. `my_list.insert(0, x)`
6. `my_list.pop()` vs `my_list.pop(0)`

Then: why is `x in my_set` faster than `x in my_list`?

**Om:**
```text
O(n)
O(n)
O(1)
O(1)
O(n)
o(1) O(n)
Not Sure
```

### Q5: iterator vs iterable

What is the difference between an iterable and an iterator? Is a list an iterator?

What do the three prints show, and why?

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))
print(list(it))
print(list(it))
```

**Om:**
```text
IDK
```

### Q6: generators

What is a generator, and how is it different from a function that builds and returns a list?

What does this print, in order, and why?

```python
def count_up(n):
    for i in range(n):
        print("making", i)
        yield i

g = count_up(3)
print("start")
print(next(g))
```

**Om:**
```text
4, IDK
```

### Q7: decorators

What is a decorator?

What does this print, and what does the `@shout` line do? Write it without the `@` symbol.

```python
def shout(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@shout
def greet(name):
    return "hi " + name

print(greet("om"))
```

**Om:**
```text
A decorator is a thing that makes a function do something else
```

Coach nudge: "Two parts still open: what it prints, and the version without `@`. Answer them, or say "don't know"."

**Om:**
```text
I think it will print "hi OM"
```

### Q8: context managers

What is a context manager? What does a `with` block guarantee?

What does this print, in order? Does `"after"` print?

```python
class Demo:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("exit")
        return False

with Demo():
    print("inside")
    raise ValueError("boom")

print("after")
```

**Om:**
```text
I have seen this first time in my life IDK
```

Coach reply: "Noted. That one is P1-blocking, so I'll teach it at the end."

### Q9: exceptions

What does this print, in order?

```python
def f():
    try:
        print("try")
        raise KeyError("k")
    except ValueError:
        print("value")
    except KeyError:
        print("key")
    else:
        print("else")
    finally:
        print("finally")

f()
```

Then two short ones:
- When does `else` run?
- When does `finally` run?

**Om:**
```text
try key finally
```

Coach nudge: "The two short ones are still open: when does `else` run, and when does `finally` run? Answer them, or say "don't know"."

**Om:**
```text
else -: not sure i would be just guessing
finally: everytime regardless
```

### Q10: dataclass vs plain class

What does `@dataclass` give you that a plain class doesn't? What does `frozen=True` add? You use it in PRCP.

What do the three prints show?

```python
from dataclasses import dataclass

@dataclass
class P:
    x: int
    y: int

class Q:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(P(1, 2) == P(1, 2))
print(Q(1, 2) == Q(1, 2))
print(P(1, 2))
```

**Om:**
```text
false
true
(1,2)
```

Coach nudge: "First part still open: what does `@dataclass` give you, and what does `frozen=True` add? Answer it, or say "don't know"."

**Om:**
```text
@dataclass is a class that only holds variables .. frozen may be the values cant change further (i can junk of)
```

### Q11: typing

What does this print when run with plain `python`, and why? What would `mypy` say about it?

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("a", "b"))
```

Last part: what does the hint `name: str | None` mean?

**Om:**
```text
ab

name can be a string or None
```

Coach nudge: "Two parts still open: why it prints `"ab"`, and what `mypy` would say. Answer them, or say "don't know"."

**Om:**
```text
python a: int is a hint only it doesn't force compiler to take as int so eventually str a + str b is str ab
what is mypy
```

Coach reply: "Noted as don't know. In one line: mypy is a separate tool that reads your type hints and reports mismatches without running the code. More at the end."

### Q12: the GIL

What is the GIL?

Two threads each run `counter += 1` a million times on the same global `counter`, with no lock. Can the final value be less than 2,000,000? Why or why not, given the GIL?

**Om:**
```text
IDK
```

### Q13: thread vs process vs asyncio

In one sentence each: what is a thread, a process, and asyncio?

Then pick one for each job, and say why:
1. Call 200 HTTP endpoints and wait for all the responses.
2. Run a pure-Python number-crunching loop across 8 CPU cores.
3. Call a blocking library (no async support) 50 times in parallel.

**Om:**
```text
I can guess :

thread is programming language riunning thread which cpu cores can use
process is a task that can have many threads
asynio i have heard don't know
```

Coach nudge: "The three picks are still open. Answer them, or say "don't know"."

**Om:**
```text
IDK
```

### Q14: async cancellation and timeouts

This builds on asyncio, so "don't know" is fine.

In asyncio, what happens to a running task when it is cancelled, or when a timeout around it expires? What should your code do when that happens?

**Om:**
```text
IDK
```

### Q15: pytest fixtures

What is a pytest fixture, and why use one instead of setup code inside each test?

Running `pytest -s`, what prints, in order?

```python
import pytest

@pytest.fixture
def db():
    print("open")
    yield "conn"
    print("close")

def test_a(db):
    print("test", db)
```

**Om:**
```text
IDK
```

### Q16: property-based testing

How is a property-based test different from an example test like `assert add(2, 3) == 5`?

Give one property you could check for a function that sorts a list.

**Om:**
```text
IDK
```

### Q17: reference counting and garbage collection

How does Python decide when to free an object's memory?

After the `del` line, why might plain reference counting fail to free these two lists, and what does Python do about it?

```python
a = []
b = [a]
a.append(b)
del a, b
```

**Om:**
```text
IDK
```

### Q18: MRO and `super()`

What does MRO mean in Python?

What does this print, in order?

```python
class A:
    def hi(self):
        print("A")

class B(A):
    def hi(self):
        print("B")
        super().hi()

class C(A):
    def hi(self):
        print("C")
        super().hi()

class D(B, C):
    def hi(self):
        print("D")
        super().hi()

D().hi()
```

**Om:**
```text
IDK
```

### Q19: ABC vs Protocol

Both describe an interface. What is the difference between an abstract base class (`abc.ABC`) and a `typing.Protocol`?

Concretely: a class `Duck` has a `quack()` method but inherits from nothing. Does it count as a `Quacker` when:
1. `Quacker` is an ABC with an abstract `quack()`?
2. `Quacker` is a Protocol with `quack()`?

**Om:**
```text
IDK
```

## Coach marks (Claude)

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

## Blocking current PRCP work (moved into 1a, taught at the start of the first P1 session, in P1 hours)

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

## Process notes

- Right after the test, in the next message, Claude started a context-manager lesson with a retry question. Om rejected it as an unwanted context switch: a baseline only records where he stands. Lesson stopped, retry not taken, nothing scored from it.
- Second opinion requested by Om: ChatGPT to review these marks against the verbatim answers and record its view in `chatgpt/`.

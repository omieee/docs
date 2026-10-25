# Y3 generators, first part: teaching and part check (Claude)

- Plan content: W4 row, Y3 1h "Generators, first part: what `yield` does, how a generator pauses and resumes, so `yield` fixtures make sense" (v3.8), done early on Sun Oct 25 (W3's last day), like P1's hour and the Go rep. Not a unit close: Y3 runs to W36; this part's use step is the psycopg rollback fixture in P1 (W5-W8).
- Ask-first (Om, 11:32): never used `yield` before the Oct 23 pytest fixture.
- Video: Real Python, "Generators in Python" (youtube.com/watch?v=1t_NUJFh33Y, 2020, Python 3.7, live code in VS Code), 0:00-7:11 only. Checked by chapter list and code frames at 1:15, 3:10 and 6:40; the transcript would not load in the browser. First pick (Corey Schafer 2015, Python 2) was rejected by Om: coach error, logged.
- Warm-up (W4 trial, two questions on the last Python session, dataclass equality): HELD. Om: plain class has no own `__eq__`, so two objects at different locations give False; `__eq__` (from @dataclass) checks the values.
- Step 1 (calling a generator function does not run it; each next() runs to the next yield and pauses): Om's prediction had the order right and the reason right ("the functions is not invoked yet, it only gives the generator object"); missed the printed values 1 and 2 and the StopIteration on the third next(). Shown the real output.
- Step 2 (for calls next() and stops quietly): output right; reason half right (the generator's while ends, "behaves like break"); taught: the generator still raises StopIteration, the for loop catches it. Om: "clear and nicely taught".
- Time: 11:20-11:52 active [32m]; 11:10-11:20 waiting on Claude's video search (elapsed, of which [3m coach error] for the Python 2 video). Box 1h, inside.

## Questions as asked and answers verbatim (written, from memory, no code run, no notes, no AI)

**Q1 (how it works).** In your own words: what does `next(g)` do each time it is called, and from which line does the generator start running the next time?

> next(g) runs till next yield is reached.. and next time it runs after the yield line

Score 2/2. Runs to the next yield and pauses; resumes after that yield line. (That yield hands the value out is shown in his Q2 answer.)

**Q2 (trace).** Write the exact output, line by line:
```python
def letters():
    print("A")
    yield "x"
    print("B")
    yield "y"
    print("C")

g = letters()
print("made")
print(next(g))
print(next(g))
```

> made , A, x, B, y

Score 2/2. Exact, and C correctly not printed (no third next()).

**Q3 (use it somewhere new).** The Oct 23 fixture (`print("SETUP")`, `yield 5`, `print("TEARDOWN")`): explain what pytest must be doing so that SETUP runs before the test, the test gets 5, and TEARDOWN runs after the test.

> I guess what is happening is we pass the fixture as param toa test case that invoks the next() so the fixture yields that values that is till yiled line and thos setup happens and once the test ends next is called so that line after yield gets triggered and teardown happens

Neutral question (rule 9, one part could be read two ways): "Who calls next() here: the code inside your test function, or pytest itself?" Om: "pytest itself".

Score 2/2. next() once: SETUP runs, 5 is handed to the test; after the test, next() again: TEARDOWN runs. Note, not marked: after TEARDOWN the generator ends with StopIteration, which pytest catches, like a for loop.

**Total 6/6. Part check PASS.** Tonight: Real Python "How to Use Generators and yield in Python", only "Example 2: Generating an Infinite Sequence" and "Understanding the Python Yield Statement" (bedside reading, optional time logged).

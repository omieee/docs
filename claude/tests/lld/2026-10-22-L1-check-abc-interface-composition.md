# L1 check: abstract class, interface vs abstract class, composition

- Date: 2026-10-22 (Thu), W3. Coach: Claude. Label: L1 part check (section 7 cold questions, written in chat). L1 as a unit closes in W7 (s14), so this is not the unit close.
- Taught today: Bro Code "Python Object Oriented Programming Full Course" (IbMDCwVm63M), abstract classes 35:31-42:33 and composition 1:14:41-1:22:02 (transcripts read by Claude first); Claude's plain-words piece on interface vs abstract class (Printable vs Shape.describe). Practice: learning-python-sandbox PR #3 (merged 3dabb89) and PR #4 `f10b0a2`, Claude fresh run 24 passed, ruff clean.
- Minutes: [45-50m] (Om) for the hour, plus this check.

## Questions and answers (verbatim; one joke word left out because the repo is public)

**Q1.** In your own words, what is the difference between an interface and an abstract class in Python? What does a child class get from each one?

Om: "Interface is only the skeleton and no code is there .. where as abstract class also makes the same promice like Interface that every function within it should be implemented .. but abstract class can have other function which are not abstractmethod and those gets to the child class. Python doesnot support interface keywork .. abstract is implemented fy ABC"

Score 2/2. Interface: only the promise, no code; abstract class: the same promise plus normal methods the child inherits; no `interface` keyword, ABC is used.

**Q2.** A teammate writes `class Circle(Shape)` with an `__init__` and a method named `get_area()` instead of `area()`. What happens? Does the error come when Python reads the `class Circle` line, or when someone writes `Circle(5)`? Why?

Om: "Error will come when python reads class Circle and it will find that my [word left out] friend has not implented the area() .. this is because in python all abstatct method should be implemented in child class"

Score 1/2. Right: it fails because `area()` is not implemented and `get_area()` does not count. Wrong: the class line runs fine; the `TypeError` comes at `Circle(5)`, when an object is created. Rule 9: the answer picks one of the two offered options clearly, so no neutral question was needed.

Taught on the spot (after scoring): Python builds the class without complaint, because a child that leaves an abstract method empty is simply another abstract class, which is legal (for example Shape, then an abstract Polygon, then Square). The check runs only when someone tries to create an object. The early warning seen in Bro Code's video at the class line comes from the editor, not from Python.

Retry (fresh wording, same mechanism), asked 22:23: `Vehicle(ABC)` with abstract `go()`, `class Bike(Vehicle): pass`, then `print("A")`, `b = Bike()`, `print("B")`. What gets printed before the program stops, and on which line does it stop?

Om (22:24): "A will be printed / Then python wil compalain because we are creating bike obkect now"

Retry correct: "A" only, stops at `b = Bike()` (object creation). Repair landed; Q2 stays 1/2 as recorded.

**Q3.** In your code, is a `Car` an `Engine`, or does it have an `Engine`? Point to the exact line in your code that makes it so. And who creates the `Engine` object: the person who creates the car, or the `Car` itself?

Om: "Car != Engine .. In composition car "owns" an Engine and this line does that ```self.engine = Engine(horse_power)```"

Score 2/2 (rule 9, generous reading). Has-a / owns, right line. Who creates it was not said in words, but the quoted line sits in `Car.__init__`, so the Car creates its own Engine; note given to say it out loud next time.

## Result

- 5/6. One mechanism miss (Q2, when the abstract check runs), taught on the spot, fresh retry correct. Today's L1 topics (abstract class, interface vs abstract class, composition) checked. L1 stays open until W7 per the plan.

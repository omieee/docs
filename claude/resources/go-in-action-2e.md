# Go in Action, Second Edition: contents and unit map

Owned by Om (Kindle, ASIN B0GKPY9767). Joel Holmes, Andy Walker, William Kennedy. Manning, Sept 29 2026.
Contents transcribed from Om's screenshots, 2026-10-06 15:16-15:19 IST. The screenshots run on with no visible gaps; check the Kindle if a section looks missing.

**Status: new recommendation, not plan content.** Zero hours added. Learn Go with Tests stays the primary text for G1-G7 because every Go proof is tests. This book is the second pass, like Fluent Python for Python: read the mapped sections after the LGWT chapter, or when LGWT does not click. Never cover to cover. Closed during cold checks and the Gate A Go practical, like every resource. Goes into the section 14 resource key (proposed key GIA) at the next plan revision, Om approving.

## Unit map

| Unit | Sections | Note |
| --- | --- | --- |
| G1 Setup and basics | 2.2.3, 2.3, 2.4.2-2.4.10, 2.5.2, 8.1-8.3 | toolchain, modules, build, run, gofmt, package and import, scope, for loops, go doc, test files and go test |
| G2 Slices | 4.1.5, 4.1.8, 4.2 (4.2.4, 4.2.5, 4.2.6, 4.2.9 first) | arrays as values, append growth and surprises, slice expressions, nil vs empty |
| G3 Types | 3.6, 5.1, 5.2.1, 5.4, 5.5, 5.6 | structs, named types, embedding, methods, interfaces |
| G4 Pointers and errors | 3.7, 5.3, chapter 7 (7.7, 7.8, 7.10, 7.12 first) | pointers, sentinel errors, errors.As, panic and recover. Nil-interface trap: not visible in the contents, use GO100 |
| G5 Maps and generics | 4.3, 6.1, 6.2, 6.5.4 | generics basics only. Concurrent map writes: not visible in the contents, use GO100 |
| G6 Design for tests | 8.4, 8.5 (8.5.5 table-driven), 8.6 | test life cycle, table-driven tests, faking dependencies with an HTTP server |
| G7 Concurrency basics | 1.4, 9.1-9.4, 9.6 | WaitGroup, mutexes, context, channels. 9.5 Workers is a hand-built pool: sandbox only (plan 6.2) |
| A1 Sequential agent | 10.4, 10.5.1 | os and JSON config only; net/http timeouts are not in this book |
| A2 Bounded concurrency | 9.2.2, 9.3, 9.5.2 | errgroup, context cancellation, fan-out and fan-in |
| A3-A6 | none | no matching chapter; keep the plan's resources |
| Skip in Phase 1 | 3.3, 10.5.2, 10.7, 11.2-11.3, appendix A, appendix B | complex numbers, XML, regexp, multi-module workspaces; appendices are AI features, out of scope (plan section 1) |

## Contents

**1 Go is the solution**
- 1.1 The problems Go was built to solve
- 1.2 Fast compilation and type safety: 1.2.1 Development speed · 1.2.2 Type safety
- 1.3 Efficient execution
- 1.4 Concurrency built in: 1.4.1 Goroutines · 1.4.2 Channels and context · 1.4.3 A request's life cycle
- 1.5 Simplicity by design
- 1.6 World-class tooling
- 1.7 What this book covers

**2 Diving into Go**
- 2.1 Goal: A program to count words
- 2.2 What you need first: 2.2.1 A code editor · 2.2.2 Git · 2.2.3 The Go toolchain · 2.2.4 Terminal access
- 2.3 Creating your project root: 2.3.1 Creating a directory · 2.3.2 Initializing the project module
- 2.4 The first iteration: Counting spaces: 2.4.1 Creating main.go · 2.4.2 Building the program with go build · 2.4.3 Running the program with go run · 2.4.4 Formatting your code with gofmt · 2.4.5 Package declarations · 2.4.6 Import declarations · 2.4.7 Blocks and scope · 2.4.8 Variable declaration · 2.4.9 Comments · 2.4.10 Basic for loops · 2.4.11 Calling functions in other packages
- 2.5 A better way to split the string: 2.5.1 Introducing package strings · 2.5.2 Using go doc to view package documentation · 2.5.3 Multiple imports in an import directive · 2.5.4 Slices and len
- 2.6 Reading from a file: 2.6.1 Using the os package to interact with the filesystem · 2.6.2 Multiple return values · 2.6.3 Basic error handling and the log package · 2.6.4 Counting the words in the loaded file · 2.6.5 Running the program on a file
- 2.7 Specifying the file: 2.7.1 Getting program arguments from os.Args · 2.7.2 Avoiding a panic by using len · 2.7.3 Running your program with arguments
- 2.8 A more efficient method: 2.8.1 Using go doc to learn more about types · 2.8.2 Files and I/O interfaces · 2.8.3 Integrating the scanner loop · 2.8.4 Function types for modifying behavior
- 2.9 Reading multiple files

**3 Primitive types and operators**
- 3.1 Integer types: 3.1.1 Choosing an integer type
- 3.2 Floating-point number types: 3.2.1 Special floating-point values · 3.2.2 Choosing a floating-point type
- 3.3 Complex number types
- 3.4 Mathematical operators
- 3.5 The bool type: 3.5.1 Boolean functions
- 3.6 Struct types: 3.6.1 Structs as types
- 3.7 Pointer types: 3.7.1 Dereferencing pointers · 3.7.2 Creating pointers with new and literals
- 3.8 The string type: 3.8.1 Interpreted strings · 3.8.2 Raw string values · 3.8.3 String operations · 3.8.4 len() and Unicode characters · 3.8.5 Iterating Unicode strings using a range loop · 3.8.6 The rune type · 3.8.7 Converting a string to a slice of runes

**4 Collection types**
- 4.1 Arrays: 4.1.1 Declaring arrays · 4.1.2 Array type and length · 4.1.3 Working with array elements · 4.1.4 Iterating over arrays with for · 4.1.5 Arrays as values · 4.1.6 Multidimensional arrays · 4.1.7 Passing arrays to functions · 4.1.8 The problem with arrays
- 4.2 Slices: 4.2.1 Declaring slices with slice literals · 4.2.2 Declaring slices with make · 4.2.3 Nil slices · 4.2.4 Growing slices with append · 4.2.5 Avoiding append surprises · 4.2.6 Slice expressions · 4.2.7 Copying slices with copy · 4.2.8 Avoiding runtime panics when accessing slice values · 4.2.9 Nil slices versus empty slices
- 4.3 Maps: 4.3.1 Declaring maps · 4.3.2 Setting and accessing map values · 4.3.3 Removing values from maps · 4.3.4 Getting the number of values in a map · 4.3.5 Iterating over maps · 4.3.6 Passing maps to functions · 4.3.7 Key and value types

**5 Working with types**
- 5.1 Modeling a domain with types: 5.1.1 Named types · 5.1.2 Structs
- 5.2 Extending types: 5.2.1 Type embedding · 5.2.2 Complex types
- 5.3 Pointer types
- 5.4 Methods and behavior
- 5.5 Interfaces
- 5.6 Checking types: 5.6.1 Type composition and wrapping · 5.6.2 Example: Putting it all together

**6 Generics**
- 6.1 Typed parameters in generics: 6.1.1 Using interface constraints · 6.1.2 Defining custom constraints · 6.1.3 Using underlying types with tilde (~) · 6.1.4 Summary of type constraints
- 6.2 Implementing generic functions
- 6.3 Implementing generic interfaces
- 6.4 Multiple type parameters
- 6.5 Limitations and considerations: 6.5.1 Performance considerations · 6.5.2 Limitations of Go generics · 6.5.3 Common gotchas · 6.5.4 When to use generics · 6.5.5 Backward compatibility
- 6.6 Standard library support: 6.6.1 The constraints package · 6.6.2 The slices and maps packages · 6.6.3 The cmp package
- 6.7 Just getting started

**7 Errors in Go**
- 7.1 Go errors are values
- 7.2 The Go error type
- 7.3 Generating new errors
- 7.4 Handling errors
- 7.5 Logging errors
- 7.6 Annotating error logs with formatting
- 7.7 Sentinel errors
- 7.8 Identifying different types of errors
- 7.9 Creating a custom error type
- 7.10 Getting the underlying error with errors.As
- 7.11 An unexpected error journey
- 7.12 Don't panic: 7.12.1 Using Panic and Recover in your code

**8 Testing and tooling**
- 8.1 Test files and functions
- 8.2 Running tests with go test
- 8.3 Test functions
- 8.4 Test life cycle
- 8.5 Test-driven design: A calculator with a twist: 8.5.1 Black-box testing · 8.5.2 Writing tests for error conditions · 8.5.3 Writing good test logs · 8.5.4 Choosing testing targets · 8.5.5 Table-driven testing · 8.5.6 Implementation and initial testing · 8.5.7 Code coverage
- 8.6 Simulating dependencies with an HTTP server
- 8.7 Beyond unit tests: 8.7.1 Benchmark testing · 8.7.2 Fuzz testing

**9 Concurrency**
- 9.1 When to use concurrency
- 9.2 Sync package: 9.2.1 Wait groups · 9.2.2 Error Groups · 9.2.3 Mutexes
- 9.3 Adding some context
- 9.4 Channels
- 9.5 Concurrency patterns: 9.5.1 Workers · 9.5.2 Fan-out and fan-in
- 9.6 Helpful concurrency tips: 9.6.1 Best practices for Go concurrency · 9.6.2 When to use concurrency in Go · 9.6.3 When not to use concurrency in Go

**10 The standard library**
- 10.1 The fmt package · 10.2 The flag package · 10.3 The io package · 10.4 The os package
- 10.5 The encoding package: 10.5.1 JSON processing · 10.5.2 XML processing
- 10.6 The bufio package · 10.7 The regexp package · 10.8 The strings package · 10.9 The strconv package · 10.10 Scratching the surface

**11 Working with larger projects**
- 11.1 Modules: 11.1.1 Packages · 11.1.2 Domain module: Shared domain model
- 11.2 Versioning modules
- 11.3 Workspaces: 11.3.1 Understanding workspaces · 11.3.2 API module: REST service · 11.3.3 Worker module: Background feed fetcher · 11.3.4 Testing the complete system · 11.3.5 Versioning independent modules · 11.3.6 Workspace benefits demonstrated

**Appendix A Vector search with storage**
- A.1 Docker Compose setup: A.1.1 Installing Docker · A.1.2 Docker Compose configuration
- A.2 Extending the storage module: A.2.1 Installing dependencies · A.2.2 Implementing the Qdrant client · A.2.3 Search wrapper implementation · A.2.4 Overriding AddArticles for embedding · A.2.5 Implementing semantic search
- A.3 Using vector search: A.3.1 Worker integration · A.3.2 API usage · A.3.3 Running the complete system

**Appendix B LLM-powered summarization**
- B.1 LLM technologies: B.1.1 Ollama: Running models locally · B.1.2 LangChain: A consistent interface for LLMs
- B.2 Infrastructure setup
- B.3 Creating the summary module: B.3.1 Configuration and initialization · B.3.2 The Summarize method · B.3.3 Building the prompt
- B.4 Wiring it into the API: B.4.1 What the handler needs · B.4.2 The summary handler · B.4.3 Updating the API
- B.5 End-to-end test
- B.6 What to try next

**Index**

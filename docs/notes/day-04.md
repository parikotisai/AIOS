# Day 4 — Build a Reusable Tree Explorer + Preview Future Code Shapes

**Curriculum doc:** `docs/curriculum/01-days-1-to-5.md` (Day 4 block)

## Objective

Turn `explore_ast.py` from a fixed script into an interactive tool
(type any code, see its tree), then use it to preview three code
shapes coming in later days: `if/else`, `while`, and `def`.

## Concepts & definitions

- **`while True:`** — a loop that repeats its body forever, until
  something inside says stop. Analogy: a cashier's shift — keep
  serving the next customer, again and again, until told to go home.
- **`input("...")`** — pauses the program and waits for you to type
  one line. Whatever you type comes back as text (a string).
- **`break`** — the exit door of a loop. The moment Python hits
  `break`, it jumps out of the loop and continues below it.

- **`Expr` node** — a line that is just a value by itself, with
  nothing stored anywhere. `x = 5` → `Assign`; a lone `5` → `Expr`.
- **`==` vs `=`** — one `=` stores a value; two `==` asks "are these
  equal?" Classic beginner error to mix them up.

## Q&A log

- **Q: Explain the nested-loop upgrade line by line.**
  A: Walked through it with the cashier analogy — outer loop = one
  customer (snippet) per trip; `lines = []` = fresh empty basket each
  customer (inside the outer loop so old lines don't leak into the
  next snippet); inner loop = scan items (one `input()` line per
  trip; pasting feeds lines one at a time); empty line → inner
  `break` (done scanning, customer still there); `lines == ["quit"]`
  → outer `break` (shift over); `"\n".join` glues the basket back
  into the original multi-line text; then the Day-3 parse+dump pair.
  Key idea: **`break` exits only the loop it is directly inside** —
  the two `break`s here exit different loops.
- Check-question asked: why must `lines = []` be inside the outer
  loop? (answer pending)

- **Q: Do I have to memorise these topics or just understand them?**
  A: Understand only. Never memorize node names (`Compare`, `Gt`,
  `orelse`...) or tree layouts — that's the tree-explorer tool's job,
  and it's why we built it. Ideas worth owning (code-as-tree, an if
  has condition/then/else, Store=written vs Load=read) stick through
  use, not flashcards. Syntax like `while True`/`input()`/`break`
  gets learned by typing it many times, not by memorizing. The real
  test is "can you explain it in your own words."

### Part 2 preview #1: if/else — WORKS

- Multi-line tool upgrade succeeded; pasted the 4-line if/else and
  got the first `If` tree.
- **`If` node = 3 parts:** `test` (the condition), `body` (runs if
  true), `orelse` (runs otherwise — `else` literally becomes
  `orelse`).
- **`Compare` node** mirrors `x > 3` left-to-right: `left` =
  `Name('x', Load())`, `ops=[Gt()]` (Gt = greater than),
  `comparators=[Constant(3)]`.
- Bonus discovery: Enter on an empty basket → `ast.parse("")` →
  `Module(body=[])` — an empty tree, harmless and correct.
- Prediction exercise given: if with no else — what does `orelse`
  become? (curriculum answer: empty list `[]`)

### Check answers

- `lines = []` inside the loop: Sai described the flow (starts
  empty, inner loop appends) — half credit; sharpened the *why*:
  it's a **reset once per round**. If it lived above the loop,
  snippet 2 would inherit snippet 1's lines (`["x = 5", "y = 2"]`
  parsed together). Where you create something decides when it
  resets — same idea returns with Day 5's `variables = {}`.
- `orelse` prediction: **correct** — no else → `orelse=[]`, empty
  list. "Nothing to do otherwise", not an error.

### Part 2 previews #2 and #3 — done

- `while x > 0: x = x - 1` → Sai: "everything looks same as If."
  Correct — and that IS the lesson: same `test` + `body` shape
  (even an empty `orelse=[]`). The tree can't say "this loops"; the
  difference lives in the **evaluator**: If runs `body` once
  (maybe), While re-checks `test` and re-runs `body` until false.
  Tree = recipe, evaluator = cook.
- `def add(a, b): return a + b` → Sai found `a`/`b` inside `args`
  (as `arg(arg='a')`, `arg(arg='b')`). `body` = one `Return` holding
  a **`BinOp`** (`left=Name('a',Load())`, `op=Add()`,
  `right=Name('b',Load())`) — `BinOp` is the next node the tracer
  learns to evaluate (Day 6). A `FunctionDef` only *defines* —
  nothing runs (same describing-vs-cooking lesson as Bug #1).
- Ignorable clutter in `FunctionDef`: `posonlyargs`, `kw_defaults`,
  `decorator_list`, `type_params` — fancy-feature slots, all empty.

## What we built / ran

- Rewrote `backend/explore_ast.py` as an interactive loop:
  `while True:` → `input()` → `quit` check with `break` →
  `ast.parse` + `ast.dump`. Sai typed it all.
- Verified: `quit` exits cleanly.
- Sai's own experiments: typed `sai` → `Expr(value=Name(id='sai',
  ctx=Load()))` (a name being read); typed `1` →
  `Expr(value=Constant(value=1))` (a bare value).

### Bug #1 (great one): pasted the if/else into the FILE, not the prompt

- Symptom: after typing `quit`, crash — `NameError: name 'x' is not
  defined` at line 10 (`if x > 3:`).
- Cause: the preview snippet was pasted into `explore_ast.py` itself,
  after the loop. When `quit` broke the loop, Python kept executing
  the file and RAN the if/else for real — and `x` doesn't exist.
- **Lesson: code in the file = instructions (Python runs them). Code
  typed into the prompt = data (ast.parse only describes it).**
  Recipe analogy: the tool *reads* the recipe; the file *cooks* it.
- Proof from earlier: typing `rama` at the prompt gave no error even
  though no variable `rama` exists — because it was only described,
  never run.
- **NameError** — Python's way of saying "you used a name I've never
  heard of."
- Fix: deleted the pasted lines from the file; paste into the running
  tool's prompt instead.

### Bug #2 (planned surprise): pasting multi-line code into `input()`

- Symptom: pasting the 4-line if/else crashed with
  `IndentationError: expected an indented block after 'if' statement`.
- Cause: **`input()` reads exactly ONE line.** Only `if x > 3:`
  reached `ast.parse` — an `if` with no body. `ast.parse` never runs
  code, but it still demands complete grammar.
- **IndentationError** — "you promised indented lines after that
  colon, and there aren't any."
- Fix: upgrade the tool to collect lines until an empty line, then
  `"\n".join` them and parse the whole snippet. Real-engineering
  moment: the one-liner design outgrew its requirements.

### New concepts from the upgrade

- **list (`[]`)** — a container holding items in order (empty
  shopping basket).
- **`.append(x)`** — add one item to the end of the list.
- **`"\n".join(lines)`** — glue list items into one text with a
  newline (`\n` = "press Enter") between each: `["a","b"]` → `"a\nb"`.
- **Nested loop** — a loop inside a loop. Outer = one round per
  snippet (cashier per customer); inner = collect that snippet's
  lines (scan one customer's items). `break` only exits the loop
  it is directly inside.

## Check-your-understanding

- Why `lines = []` inside the outer loop? → reset per snippet
  (answered; sharpened with the two-snippet failure example).
- `orelse` with no else? → `[]` (correct on first prediction).
- While vs If tree? → same shape; the behavior difference is the
  evaluator's job (correct).
- Where are `a`, `b` in a `FunctionDef`? → in `args`; `body` is a
  `Return` with `BinOp` (correct, completed together).
- **Day's "done when" met:** pointed at condition vs. result in all
  three preview trees without looking at the doc.

## Wrap-up

- **Summary:** upgraded `explore_ast.py` from a fixed script into an
  interactive, multi-line tree explorer; used it to preview `If`,
  `While`, and `FunctionDef` trees ahead of Days 8–16. Two real bugs
  became the day's best lessons.
- **What Sai learned:** `while True` / `input()` / `break`; nested
  loops (a `break` exits only its own loop); lists, `.append`,
  `"\n".join`; code-in-file (runs) vs code-as-data (described);
  `input()` is one-line-only; `If` = test/body/orelse;
  `Compare`/`Gt`; While ≡ If in tree shape, differs at evaluation;
  `FunctionDef` = name/args/body; first sighting of `Return` and
  `BinOp`; `NameError`, `IndentationError`; understand-don't-memorize
  (the tool exists so node names never need memorizing).
- **What we built:** the interactive multi-line AST explorer
  (`backend/explore_ast.py`) — a tool that stays useful for the
  whole project.
- **Homework:** for the recording, explain aloud without notes: the
  two bugs and what each taught, and why While looking identical to
  If matters. Optionally explore 2–3 snippets of your own in the
  tool (e.g. a call with two arguments, a nested if).
- **Suggested commit:**
  `day-04: interactive multi-line AST explorer + if/while/def previews`
  then `git tag -a day-04 -m "Day 4: reusable tree explorer + control-flow previews"`
  and `git push --follow-tags`.
- **Prep for tomorrow (Day 5):** first evaluator (`tracer.py`) — the
  "cook" that actually executes what the tree describes, starting
  with plain assignment only. Today's recipe-vs-cook distinction is
  the exact foundation, and Day 5's `variables = {}` question will
  rhyme with today's `lines = []`.

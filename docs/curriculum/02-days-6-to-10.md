# Days 6–10 — Arithmetic, if/else, and Starting Loops

**Where you stand:** a working skeleton (backend and frontend talking), you've seen how `ast.parse` turns code into a tree, and your evaluator can handle plain assignment.

---

### Days 6–7 — Arithmetic, plus real data types
- Extend your evaluator to handle `+ - * /` inside an assignment (e.g. `y = x + 3`).
- Same extension, same evaluator: add strings (`ast.Constant` already covers this — confirm it), lists (`ast.List`), dicts (`ast.Dict`), and indexing (`ast.Subscript`, e.g. `x[0]` or `d["key"]`) as value types `eval_expr` can produce and `changed`/`variables` can store. This is the "not just numbers" scope item — it's the same kind of node-type extension as arithmetic, just more node types in one pass.
- Each evaluated line still appends one step object to the trace.
- **Done when:** `x = 5\ny = x + 3\nprint(y)` produces a correct 3-step trace with the right final value, **and** a snippet using a string, a list, and indexing (e.g. `names = ["a", "b"]\nfirst = names[0]`) traces correctly too.

### Days 8–9 — if / else, with comparison and boolean operators named
- Extend the evaluator to handle conditions — it needs to evaluate the condition, then walk only the branch that applies.
- The condition is a `Compare` node (`>`, `<`, `==`, etc.) or a `BoolOp` node (`and`/`or`) — handle both explicitly in `eval_expr`, not just as a side effect of getting `if` working.
- Test both branches, not just the one that happens to be true first.
- **Done when:** a program with if/else produces the correct branch in its trace, verified for both branches, **and** a condition combining a comparison with `and`/`or` (e.g. `if x > 0 and y < 10:`) evaluates correctly.

### Day 10 — Start while loops
- Begin extending the evaluator to handle `while`. Get a single-iteration loop working first — don't aim for full correctness yet.
- **Done when:** a while loop that should run exactly once produces a trace with the loop body appearing exactly once.

---

**Carries into Doc 03:** finishing while loops (multi-iteration), then starting function calls.

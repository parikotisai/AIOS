# Days 1–5 — Skeleton, Reading Code as a Tree, First Evaluator

**Where you stand:** nothing built yet — this is the start. Full lesson, full code, nothing assumed.

---

## Day 1–2 — Skeleton: backend and frontend talking

Three words, before any code:

- **Backend** — a program that just sits and waits. When someone asks it something, it answers. Nothing more.
- **Endpoint** — one specific address the backend listens on. `/trace` is an address, like a door with a name on it.
- **JSON** — a very organized way of writing data as text, so two different programs (your Python backend, your JavaScript frontend) can pass information to each other and both understand it.

The entire goal of Day 1–2: prove your backend (one program) and your frontend (a separate program) can talk to each other. Nothing about the actual tracer yet — that starts Day 5.

### Setup
```bash
mkdir code-visualizer && cd code-visualizer
mkdir backend frontend

cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install fastapi uvicorn
```

### `backend/main.py` — every line explained

```python
# Bring in a toolkit for building something that can "listen" for requests.
# Without this line, Python has no idea what "FastAPI" even means.
from fastapi import FastAPI

# A second toolkit, for one specific browser safety rule — explained below.
from fastapi.middleware.cors import CORSMiddleware

# This creates your actual backend program. Right now it's empty —
# an app with nothing attached to it yet. Everything below attaches to it.
app = FastAPI()

# Browsers have a rule: a page running at one address (your React app)
# is normally BLOCKED from fetching data from a different address
# (your backend). This block tells the browser "it's fine, allow it."
# Skip this, and your frontend's request gets silently blocked — it'll
# look like your code is broken when really this permission is missing.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow requests from anywhere (fine for now, on your own machine)
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/trace") means: "when someone visits /trace, run the
# function directly below me." That function is named get_trace —
# you could name it anything.
@app.get("/trace")
def get_trace():
    # This is what gets sent back: a Python list of dictionaries.
    # A dictionary is just labeled data, e.g. "step" is labeled 1.
    # FastAPI automatically turns this into JSON before sending it —
    # you don't have to convert it yourself.
    return [
        {"step": 1, "line": 1, "event": "assign", "changed": {"x": 5}, "variables": {"x": 5}},
        {"step": 2, "line": 2, "event": "assign", "changed": {"y": 8}, "variables": {"x": 5, "y": 8}},
        {"step": 3, "line": 3, "event": "print", "changed": {}, "variables": {"x": 5, "y": 8}},
    ]
```

Run it: `uvicorn main:app --reload`
- `uvicorn` is the program that keeps this running and listening.
- `main:app` means "look in main.py, run the thing called app."
- `--reload` means "restart yourself automatically whenever I save a change."

Open `http://127.0.0.1:8000/trace` in your browser — you should see that JSON, raw, as text.

### Frontend setup
```bash
cd ../frontend
npm create vite@latest . -- --template react
npm install
```

### `frontend/src/App.jsx` — every line explained

```jsx
// Bringing in two tools from React.
// useState = "remember a value, and redraw the screen when it changes"
// useEffect = "run this code automatically when the page first loads"
import { useEffect, useState } from 'react'

function App() {
  // Creates a variable called `trace`, starting out empty (null).
  // `setTrace` is the only way you're allowed to change it — and
  // doing so automatically redraws the screen with the new value.
  const [trace, setTrace] = useState(null)

  useEffect(() => {
    // Visit your backend's /trace address...
    fetch('http://127.0.0.1:8000/trace')
      // ...wait for the reply, turn it from JSON back into normal data...
      .then(res => res.json())
      // ...and save it into `trace`.
      .then(data => setTrace(data))
  }, [])   // empty [] means: only do this once, when the page first appears

  // Show whatever is currently in `trace`, formatted to be readable.
  // Before the fetch finishes, trace is still null — you'll see nothing
  // for a split second, then the real data appears.
  return <pre>{JSON.stringify(trace, null, 2)}</pre>
}

export default App
```

Run it: `npm run dev`, open the URL it prints (usually `http://localhost:5173`).

**Done when:** those 3 fake steps appear on your screen — fetched from your own backend, not hardcoded in React.

---

## Day 3 — Reading code as a tree

Your tracer eventually needs to look at code like `x = 5` and understand its *structure* — not just read it as text, but know "this is an assignment, the name is x, the value is 5." Python has a built-in tool that does exactly this: the `ast` module (ast = **A**bstract **S**yntax **T**ree — don't worry about the name, just think "the structure of the code, as data").

### `explore_ast.py`

```python
import ast

def show_tree(code):
    print(f"\n--- Code: {code} ---")
    tree = ast.parse(code)          # turns the text into a tree
    print(ast.dump(tree, indent=2)) # prints that tree so you can see it

show_tree("x = 5")
show_tree("y = x + 3")
show_tree("print(y)")
```

Run it: `python explore_ast.py`

For `x = 5`, you'll see something like:
```
Module(body=[
  Assign(
    targets=[Name(id='x', ctx=Store())],
    value=Constant(value=5))],
  type_ignores=[])
```

Read it out loud like this:
- `Module` — the whole file/snippet.
- `body=[...]` — the list of lines/statements inside it. Just one here.
- `Assign` — this line is an assignment.
- `targets=[Name(id='x', ...)]` — the thing being assigned *to* is a variable named `x`. It's a list because Python allows `x = y = 5`.
- `ctx=Store()` — "Store" means this name is being **written to** (as opposed to read from).
- `value=Constant(value=5)` — the thing being assigned is a plain, literal value: `5`.

For `y = x + 3`, you'll additionally see a `BinOp` (binary operation) — `left=Name('x', Load())`, `op=Add()`, `right=Constant(3)`. Notice `x` here has `ctx=Load()`, not `Store()` — because this time you're *reading* `x`, not writing to it. That Store vs. Load distinction is exactly how the tree tells "being assigned" apart from "being used."

For `print(y)` you'll see a `Call` node — a function is being called, with `y` passed in as an argument.

**Done when:** you can look at any one of these three trees and explain, out loud, in your own words, what it represents — without looking back at this doc.

---

## Day 4 — Build a reusable tree explorer, then preview what's coming

Today has two parts: turn yesterday's script into a permanent tool, then use it to look ahead at code shapes you'll need in later days — `if/else` (Day 8–9), `while` (Day 10–12), and functions (Day 13–16). Seeing these now, before you need them, means Day 8 won't be the first time you've seen an `If` node.

### Part 1 — Upgrade `explore_ast.py` into a tool you'll keep using

Replace the fixed `show_tree(...)` calls with this, so you can type in any code, any time, for the rest of the project:

```python
import ast

while True:
    code = input("\nEnter Python code (or 'quit'): ")
    if code == "quit":
        break
    tree = ast.parse(code)
    print(ast.dump(tree, indent=2))
```

Run it, and keep this file around — whenever a later day introduces something new, paste it in here first to see its shape before you write code for it.

### Part 2 — Preview 3 constructs you'll need soon

Paste each of these in, one at a time. Before reading the explanation below each one, try to answer for yourself: *which part is the condition, and which part runs as a result?*

**If / else:**
```python
if x > 3:
    y = 1
else:
    y = 2
```
You'll see an `If` node with three parts: `test` (the condition — a `Compare` node here, `Gt()` meaning "greater than"), `body` (the statements that run if `test` is true), and `orelse` (the statements that run otherwise — this is literally what "else" becomes). If there were no `else` in your code, `orelse` would just be an empty list.

**While:**
```python
while x > 0:
    x = x - 1
```
A `While` node — same shape as `If`: a `test` and a `body`. The difference from `If` isn't in the tree structure, it's in what your evaluator *does* with it later: `If` runs `body` once (maybe); `While` will need to re-check `test` and re-run `body` until it's false.

**Function definition:**
```python
def add(a, b):
    return a + b
```
A `FunctionDef` node: `name` ('add'), `args` (the parameter list — `a` and `b`), and `body` (the statements inside — here, a `Return` node holding `a + b`). Notice this just *defines* the function — nothing runs yet. A separate line like `add(2, 3)` would produce the `Call` node you already saw with `print(y)` on Day 3, but with `add` as the function and `[2, 3]` as the arguments.

**Done when:** for each of the three trees above, you can point to which part is "the condition" and which part is "what happens as a result" — without looking back at this doc. You don't need to remember the exact node names yet (`Compare`, `Gt`, etc.) — that's what your tree-explorer tool is for, going forward.

---

## Day 5 — Start the evaluator

An "evaluator" is just the piece of code that actually *does* what the tree describes, instead of just describing it. Today it only needs to handle plain assignment (`x = 5`) — nothing else yet.

### `tracer.py`

```python
import ast

# Holds the current value of every variable — like a scratchpad
# that updates as the "program" runs.
variables = {}

# Collects one entry for every step that happens.
trace = []

def eval_expr(node):
    """
    Given a piece of the tree that represents a VALUE (like `5` or `x`),
    figure out what that value actually is.
    """
    if isinstance(node, ast.Constant):
        # A literal number, e.g. the 5 in `x = 5`
        return node.value
    elif isinstance(node, ast.Name):
        # A variable being READ, e.g. the x in `y = x`
        return variables[node.id]
    else:
        # Anything else (arithmetic, function calls...) isn't supported
        # yet — that's Day 6+. Fail loudly instead of silently.
        raise Exception(f"Don't know how to evaluate this yet: {node}")

def run_statement(node, line_number):
    """
    Given one line of the program, actually do it, and record what happened.
    """
    if isinstance(node, ast.Assign):
        var_name = node.targets[0].id      # who's being assigned to, e.g. 'x'
        value = eval_expr(node.value)      # what it's being set to
        variables[var_name] = value

        trace.append({
            "step": len(trace) + 1,
            "line": line_number,
            "event": "assign",
            "changed": {var_name: value},
            # IMPORTANT: dict(variables) makes a COPY. If you stored
            # `variables` directly here, every past step would silently
            # change whenever a LATER line updates a variable — because
            # dictionaries in Python are shared by reference, not copied
            # automatically. This is a real, common bug — not a maybe.
            "variables": dict(variables),
        })
    else:
        raise Exception(f"Don't know how to run this yet: {node}")

# --- Try it ---
code = "x = 5\ny = 3"
tree = ast.parse(code)

for line_number, statement in enumerate(tree.body, start=1):
    run_statement(statement, line_number)

import json
print(json.dumps(trace, indent=2))
```

Run it: `python tracer.py`

**Done when:** running the two-line program above prints a trace with exactly 2 steps — step 1 shows `x: 5`, step 2 shows both `x: 5` and `y: 3` in `variables`. If step 1 also shows `y`, or shows the wrong value, that's the copy-vs-reference bug above — go find where you accidentally stored `variables` instead of `dict(variables)`.

---

**Carries into Doc 02:** extending `eval_expr` to handle `+ - * /` (a new node type, `BinOp`), and extending `run_statement` to handle `if`/`else`.

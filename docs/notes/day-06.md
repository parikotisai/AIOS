# Day 6 — Arithmetic in the Evaluator (+ - * /)

**Date:** 2026-08-18 (curriculum Day 6 — Day 5 closed 2026-08-13; curriculum days
are units of work, not calendar days)
**Curriculum doc:** `docs/curriculum/02-days-6-to-10.md` (Days 6–7 block)
**SDET overlay:** `docs/curriculum/sdet-overlay-v1.md` (Days 6–7 block)

## Objective

- **Build:** the evaluator learns arithmetic — `y = x + 3` traces with the right value.
- **SDET:** design test inputs systematically (equivalence partitioning, boundary values) instead of randomly; first real pytest file.

## Concepts & definitions

- **Regression test** — a check that runs every time and catches an old bug if it
  sneaks back. The Day 5 `assert` on the snapshot is one; it fired today.
- **Equivalence partitioning (SDET)** — inputs the code treats identically form one
  class; test ONE representative per class, not fifty. Sai derived this unprompted:
  "we don't need both `2 + 3` and `4 + 5`, both are BinOp/Add."
- **BinOp** — the AST node for "math between two sides": holds `left`, `op`, `right`.
  Left/right are themselves expressions → `eval_expr` calls itself (first recursion!).

## Q&A log

- **Q (Sai):** "I need a quick refresh session of this AST and code once so that I can feel confident."
  **A:** Refresher given — the evaluator is 3 jobs: translate (`ast.parse`: text → objects, like `JSON.parse`), decide-what-a-value-is (`eval_expr`), and do-the-line + log-it (`run_statement` appending to `trace`). Behavior-first walkthrough of `x = 5\ny = 3`.
- **Q (Sai):** "Is it considering 3 and 3.0 as same?"
  **A:** Equal in VALUE (`3 == 3.0` → True), different in TYPE (`int` vs `float`) —
  which is why JSON prints them differently. `3 == "3"` is False (number vs text).
  SDET nugget: `assert z == 3.0` checks the amount, not the container — a stricter
  test adds `isinstance(z, float)` when the displayed type matters. Value equality vs
  type equality; revisit when testing frontend display.
- **Q (Sai):** during the typing drill — "explain the Name case and the BinOp case in a
  simpler analogy."
  **A:** Name = phone contacts: "Amma" is a label, not a number; the phone looks up the
  entry and dials what's SAVED there (`variables[node.id]`). BinOp = a support ticket
  that's two tickets stapled together: split it, drop each half back into the SAME
  queue (eval_expr calls itself), combine the two answers with the operator. The inner
  calls land in the simpler cases — that's why BinOp was cheap to add.
- Homework progress: pytest installed ✓. Typing drill (3 spaced rounds in
  `practice_day6.py`) replaces the paper blank-page rewrite.
- **Memory card for the whole program** (built for the typing drill; reworded Day 6
  evening — Sai asked to drop the invented chants, plain step names instead):
  file = 5 blocks: **Setup → eval_expr → run_statement → Run the program → Asserts**.
  `eval_expr` = 4 cases in order: **Constant** (return its value) · **Name** (look it
  up in `variables`) · **BinOp** (evaluate left, evaluate right, apply the operator;
  unknown operator → raise) · **anything else → raise**.
  `run_statement` for Assign = 4 steps: **get the name → get the value → store it →
  record the step** (append the 5-key dict, `variables` as a `dict()` copy).
  Corrections during drill: inner calls of BinOp land in the NAME case (recursion =
  outer door delegates, inner doors answer); it's `ast.Mult`, not `ast.Mul`.
- **Round 1 of typing drill (practice_day6.py):** structure fully recalled from memory
  (5 blocks, both chants, frozen copy, enumerate start=1). 4 bugs at 3 locations, found
  via guided hunt: `{'...'}` set-braces instead of a string · stray space after `\n`
  (= IndentationError) · `isinstance(node, ...)` instead of `node.op` relapse (same as
  morning bug — reps working as intended) · `{"var_name": val}` quoted-key bug (silent,
  wrong `changed` output). New concepts en route: `{}` around a value makes a SET;
  quoted vs unquoted dict keys.
- **Round 1 COMPLETE (verified green):** Sai fixed all bugs from tracebacks (plus a
  self-fixed stray-quote SyntaxError and a value-vs-dict assert shape mix-up:
  `trace[1]["variables"]["y"]` is `4`, not `{"y": 4}` — make both sides of `==` the
  same shape). Wrote 5 asserts including one on `changed` after learning the day's
  biggest testing lesson: **a green suite was blind to the quoted-key bug because no
  assert ever checked `changed` — tests only protect what they actually check.**
  Chose their own operator set (Add + Pow, 8**4=4096) — creative variation, good sign.
- Morale evidence banked: entire evaluator typed from memory, 6 own-code bugs fixed
  solo or with hints only. "Can't write code" is measurably untrue after one rep.
- **Round 2 (practice_tracer1.py, same evening):** typed solo, all four operators —
  **zero bugs on review** (Round 1 had six). Pending to close the round: predict
  step values on paper (incl. what `5/3` produces), run, add asserts, and name the
  self-reported 30% not-yet-owned lines for tomorrow's targeted warm-up.
- Round 2 ran green (5/3 → 1.6666666666666667 float observed). Sai named their 30%:
  **run_statement**. Retaught via one-line-flow table (`z = x + y` through every line).
  Key clarifications: `targets` is a LIST because Python allows `a = b = 5` (take
  `[0]`, then `.id` = name as text) · `node.value` is still the un-computed structure —
  run_statement coordinates, eval_expr computes (division of labor) · `len(trace)+1` =
  the list numbering itself. Verification pending: 3 concrete questions on `x = 5` +
  asserts to close Round 2.
- run_statement check: Q1 ✓ ("x") · Q3 ✓ (0+1=1, reasoned correctly) · Q2 located a
  real confusion: Sai thought "four cases" meant the four OPERATORS. Retaught as a
  two-level tree: outer four cases = Name/Constant/BinOp/else-raise; the operator
  check is a SUB-decision nested inside the BinOp case only. Re-check pending on
  `y = 3` and `z = x + y` (two-level question).
- **Q (Sai):** "What about the left-side x — case 1 right?" **A:** No — the left side
  NEVER visits eval_expr. Right side = a value to compute (`eval_expr(node.value)`);
  left side = a destination label (`targets[0].id`, plain text used as dict key).
  Proof from own code: at line 1 `variables` is empty — if left-x used case 1 it would
  KeyError, but the program runs. Case 1 = a name being READ (right side). Python tags
  these Load vs Store in the tree (optional explorer peek). Check upgraded: for
  `z = x + y`, how many eval_expr calls total, and does z ever visit? (expect: 3 calls
  — BinOp, x, y; z never).
- z-is-a-label ✓ landed. Call-counting missed ("once") → retaught as an indented call
  log (3 calls: run_statement's + two self-calls for left/right), then made EMPIRICAL:
  Sai instruments eval_expr with a trace print (`print("eval_expr called with:", node)`),
  predicts 14 total calls for the 6-line program (1+1+3+3+3+3), runs, counts, removes
  the probe. New concept: **instrumentation** — add a probe, observe, remove.
- Print experiment: Sai counted **14** — matches prediction; recursion now seen, not
  just believed (plain lines = 1 call, math lines = 3).
- **Round 2 CLOSED (verified):** green trace + silent asserts (z==8, z==1.666...,
  changed check). Round 1: 6 bugs → Round 2: 0 bugs.
- **Morale flag at day close:** "feeling like I am missing something, little lost,
  don't know why." Offered 4-way self-diagnosis: (a) no big-picture map · (b) can't
  tell how much was me vs hints · (c) vocabulary piling up faster than it settles ·
  (d) doesn't feel like real coding. **Sai chose (b):** "felt like I understood but
  while typing am getting lost." Reframed as recognition vs recall (two skills, not
  one broken one); evidence: 6 bugs → 0 bugs in one day. Techniques given: say the
  step aloud before typing · recall steps not characters · write the step as an
  English comment when stuck. **Day 7 MUST open with Round 3: blank page, zero hints,
  Claude silent — the unaided win.**
- **Feedback for Day 7+:** Sai wants practical web-app-flavored examples. Agreed:
  realistic test data (price/qty/total, users list) within each day's scope, plus
  regular re-anchoring that the evaluator IS the web app's engine (wired to /trace
  Days 17–18; toy snippets = user inputs, not the app).
- **Sai found a real gap** while asking about `a = b = 5` ("what about b? targets[1]?"):
  yes, `targets[1]` is `b` — and our evaluator silently assigns only `a`, dropping `b`
  with no error. Same silent-failure class as the bare-else bug. Logged as a Day 7
  test case: input `a = b = 5` · class: negative (unsupported feature) · expected:
  loud raise · actual today: silent partial trace. Fix planned: multi-target guard in
  `run_statement` + pytest negative test.

## What we built / ran

- Session start: noticed `backend/tracer.py` was still in its Day 5 "bug demo" state
  (`"variables": variables` live-link active, snapshot line commented out) — the
  `assert` at the bottom fails when run. First task: confirm the red, restore the fix,
  confirm green. This is a live example of why regression checks exist.
- Sai ran `python tracer.py` → `AssertionError: step 1 snapshot is wrong` (step 1's
  variables showed `{x: 5, y: 3}` instead of `{x: 5}` — the live-link bug). Fixed by
  restoring `dict(variables)`, re-ran → correct trace, assert silent. **Regression test
  demonstrated live.**
- Sai typed the `BinOp` branch (from a fill-in-the-blanks skeleton). First run crashed:
  `AttributeError: 'builtin_function_or_method' object has no attribute 'expr'` —
  typo `eval.expr` instead of `eval_expr`. Debugging lesson: the dot made Python find
  the BUILT-IN `eval` and reach inside it for `.expr`. Dot = "reach inside a thing";
  underscore = just part of a name. Sai guided to spot it from the traceback, not handed
  the fix.
- Second bug: step 3 showed `z: null` instead of `11`. Root cause (two stacked bugs):
  (1) `isinstance(node, ast.Add)` checked the whole BinOp package instead of the
  `node.op` field — always False; (2) the inner `else`/raise was omitted, so instead of
  crashing loudly the function fell off the end and returned `None` (JSON `null`).
  **Lesson: silent wrong answers are worse than loud crashes — this is why
  crash-don't-guess and asserts exist.** Solution shown after hints exhausted (per
  escalation rules); Sai owes explain-back + solo implementation of Sub/Mult/Div.

- All 4 operators implemented by Sai solo (Add explicit fix, then Sub/Mult/Div with no
  skeleton). Ran two data sets (x=5,y=6 and x=15,y=5) — all values correct. Sai updated
  the Day 5 regression assert to match new data unprompted.
- Observation: `15 / 5` → `3.0` not `3` — Python's `/` ALWAYS returns a float, even on
  even division. (Overlay's "division edge cases" item.)
- **Code review finding:** division was implemented as the bare `else` — so unsupported
  operators (`%`, `**`) would silently compute division instead of crashing. Same
  silent-failure disease as the null bug, one level down. Sai asked to predict the
  `x ** y` behavior, then fix: explicit `ast.Div` elif + loud `raise` in else.
- Sai predicted `x ** y` would compute the power — actually the old `else` would have
  silently returned `15/5 = 3.0`. After the fix, `x ** y` correctly crashes loudly
  (`Exception: Wrong operation`). Polish suggested: print `node.op` (names `Pow`), not
  the whole BinOp object — a good error message names the suspect.
- Name-branch check closed: Sai correctly answered `eval_expr(Name 'y')` → `5` via
  `variables[node.id]` lookup (contacts-list model).

## SDET section

- **Test scenarios identified (by Sai, before coding):**
  - Happy path: `x = 5\ny = 6\nz = x + y`
  - Negative: division by zero (`x/0`) — spotted `/` as the dangerous operator
  - Negative: `x = sai` (undefined name) / string + number mixing
  - Negative (accidental find, kept!): missing newline → `y=4 z=x+y` = SyntaxError class
  - Equivalence insight: one test per operator class; `2+3` vs `4+5` adds nothing
- **Test cases written (as asserts in tracer.py):**
  - step 1 snapshot == `{"x": 15}` (Day 5 regression, data updated)
  - step 3 `z == 20` (addition)
  - step 6 `z == 3.0` (division — float result asserted deliberately)
- **Test results:** all 3 green (silence after trace). Along the way the asserts caught:
  wrong test data (y=6 → z=21, AssertionError fired correctly) and a broken test
  (`trace[6]` → IndexError — off-by-one, step N lives at `trace[N-1]`).
- **Bugs found & fixed this session (4):** typo `eval.expr` (AttributeError, decoded
  from traceback) · `isinstance(node, ast.Add)` instead of `node.op` (silent `null`) ·
  bare-`else` division swallowing unsupported operators (`x ** y` would return
  division's answer — fixed to explicit `ast.Div` + loud raise) · assert off-by-one.
- **Key lesson:** when a test fails, the bug can be in the code, the test DATA, or the
  TEST itself — Sai hit all three variants in one session and diagnosed each from the
  error type (AssertionError vs IndexError vs AttributeError).
- **Regression considerations:** the 3 asserts run on every `python tracer.py`; they
  move into a real pytest file at the start of Day 7.
- **Interview takeaway:** equivalence partitioning (named, derived by Sai);
  "0/1/many-style" input classes for operators; silent failure vs loud failure.
- **Parked for Day 7:** pytest install + first `test_tracer.py`; the "assert that a
  crash happens" test (`pytest.raises`) for unsupported operators and `x/0`;
  strings/lists/dicts/indexing; `print(y)` in the trace.

## Check-your-understanding (as they happened)

- Predict step 2 of `a = 2; b = a` → ✓ correct (`changed {b:2}`, both vars shown)
- Which branch handles `b = a`? → missed twice ("the if"), closed on 4th pass:
  `ast.Name` branch = look up `variables[node.id]` and return it; verified with
  concrete value ("it gets 5"). Mastery: got there, needs recall practice.
- Explain-back of the `.op` bug → ✓ own words ("node will give whole block so it
  didn't fire")
- `x ** y` prediction → ✗ predicted power would compute; learned: the evaluator only
  knows what we taught it; old code would have silently divided.

## Concepts noted

- Python `/` ALWAYS returns float (`15/5 → 3.0`), even on even division.
- `null` in JSON = Python `None`; a function that ends without `return` returns None.
- Dot vs underscore: `.` reaches inside an object; `_` is just part of a name.
- Step N of the trace lives at `trace[N-1]` (steps count from 1, lists from 0).
- A good error message names the suspect (`node.op` → "Pow", not the BinOp object).

## Wrap-up

- **Built:** evaluator handles `+ - * /` via `ast.BinOp` (first recursive use of
  `eval_expr`); unsupported operators fail loudly naming the operator; 3 regression
  asserts guard it all.
- **Learned:** equivalence partitioning · silent vs loud failure · code/data/test as
  three distinct failure sources · float division · trace[N-1] indexing.
- **Homework:** (1) `pip install pytest` in the venv (just install, nothing else);
  (2) on paper, blank-page rewrite of the whole `BinOp` elif from memory — writing
  recall is the muscle in training; (3) on paper, a test-input table for `eval_expr`:
  columns = snippet · class (happy/negative/boundary) · expected result-or-error —
  aim for ~8 rows; it becomes tomorrow's pytest file.
- **Commit:** `day-06: evaluator arithmetic (+ - * /) with regression asserts`
  then `git tag -a day-06 -m "Day 6: evaluator arithmetic"` and
  `git push --follow-tags`.
- **Tomorrow (Day 7) — order agreed with Sai at Day 6 close:**
  1. **Full recap of Days 1–6 first**, pin by pin, in WEB APP terms only (browser →
     server → request → response → code text → tree → trace), examples in
     price/cart/users flavor — no x/y/z. Sai asked for this explicitly to "get back."
  2. **Round 3: blank page, all reference files closed, Claude silent.** Honest
     measurement — Sai admitted Rounds 1–2 leaned on peeking at earlier examples.
     Bugs are fine; it's a measurement, not a judgment.
  3. Then the Day 7 build: pytest for real (`test_tracer.py`, `pytest.raises` for
     division-by-zero and unsupported operators — Sai's parked instinct), the
     `a = b = 5` multi-target guard + negative test (Sai's own find), strings, lists,
     dicts, indexing, `print` in the trace → completes the Days 6–7 done-when.
  - Language rule reinforced by Sai: **plain terms completely** — no invented
    mnemonics, no jargon like "instrument/probe" without a plain-word intro.

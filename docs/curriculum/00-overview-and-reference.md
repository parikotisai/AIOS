# Code Visualizer — Overview & Reference

Keep this one open in a tab. The other 9 docs assume you can glance back here.

## The project
A tool that runs real Python code and animates it step by step — one build that carries full-stack, test automation, and AI engineering, in that order, across 45 days. Extended to 60 days with a fourth phase (AIOS Integration) that turns the finished evaluator's agent loop into a multi-tool AIOS. Full day map: `60-day-master-syllabus.md`.

## The stack
- **Backend:** Python (FastAPI or Flask)
- **Frontend:** React
- Code is parsed with Python's own `ast` module. You write the evaluator that walks that tree and actually runs it, step by step, yourself — that's where the real learning is.

## The 10 documents
| Doc | Covers | Phase |
|---|---|---|
| 00 | This file — overview & schema | — |
| 01 | Days 1–5 | 1: Full Stack |
| 02 | Days 6–10 | 1: Full Stack |
| 03 | Days 11–15 | 1: Full Stack |
| 04 | Days 16–20 | 1: Full Stack |
| 05 | Days 21–25 | 2: Playwright |
| 06 | Days 26–30 | 2: Playwright |
| 07 | Days 31–35 | 3: AI Engineering |
| 08 | Days 36–40 | 3: AI Engineering |
| 09 | Days 41–45 | 3: AI Engineering |
| 10 | Days 46–60 | 4: AIOS Integration |

## The step schema (the core data structure of the whole project)
Every step your tracer records is one small object:

```
step        → order number (1, 2, 3...)
line        → which line just ran (for highlighting)
event       → "assign" / "call" / "return" / "loop_check" / "condition" / "print"
changed     → which variable changed, and its new value
variables   → full snapshot of everything in scope right now
call_stack  → active function calls, each with its own local variables
```

A matrix is just a variable holding a list of lists. A queue is just a list being popped from the front. Neither needs new tracer logic — only new drawing logic, later. Get this schema right, and the rest of the project is just extending it.

## Ground rules
- **~3 focused hours/day.** Same 45-day structure as before, but each day now carries real depth instead of the bare minimum to prove a concept — see "Scope" below. Fell behind? Slide the calendar, don't skip the block — the order matters more than the dates.
- **Separate project.** Different repo from your `lms-*` work, no production risk. Whether any of it ever feeds into BytesferLMS is a decision for after Day 45, not before.
- **"Done when" is the real gate.** Each block below has one. Moving on with a broken checkpoint just compounds confusion later — don't.

## Scope — job-ready depth, not just exposure
Beyond the original plan, each phase now goes deeper:
- **Phase 1:** strings/lists/dicts/indexing (not just numbers), `for` loops, comparison/boolean operators, real error handling in the tracer itself, a real code editor on the frontend, and a live deployment — not just localhost.
- **Phase 2:** Page Object Model, data-driven tests across many snippets, deliberate edge-case tests, cross-browser config.
- **Phase 3:** structured (JSON) AI output, a basic eval suite that scores AI-generated code against your evaluator, and a real agent loop — AI generates code, your evaluator runs it, errors get fed back for the AI to self-correct and retry.

Doc 01 (Days 1–5) stays as written — it's foundational setup and doesn't need deepening. The added depth shows up starting Doc 02, written against your real code once you're there.

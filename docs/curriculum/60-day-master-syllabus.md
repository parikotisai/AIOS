# AIOS via Code Visualizer — 60-Day Master Syllabus
### Single reference doc. Days 1–45 summarize Docs 00–09 (your existing files — not rewritten here). Days 46–60 are the full new Phase 4 content (Doc 10).

---

## 1. The 60-Day Map

| Days | Phase | Focus | Full detail lives in |
|---|---|---|---|
| 1–5 | 1: Full Stack | Foundational setup (kept as-is, no deepening needed) | Doc 01 |
| 6–10 | 1: Full Stack | Full stack continued | Doc 02 |
| 11–15 | 1: Full Stack | Full stack continued | Doc 03 |
| 16–20 | 1: Full Stack | Full stack continued, live deployment | Doc 04 |
| 21–25 | 2: Playwright | Test automation | Doc 05 |
| 26–30 | 2: Playwright | Test automation continued | Doc 06 |
| 31–35 | 3: AI Engineering | Structured output, eval suite | Doc 07 |
| 36–40 | 3: AI Engineering | AI engineering continued | Doc 08 |
| 41–45 | 3: AI Engineering | Agent loop (code-only) | Doc 09 |
| 46–50 | 4: AIOS Integration | Tool registry, MCP, browser | Doc 10 |
| 51–55 | 4: AIOS Integration | Email, docs, RAG, checkpointing | Doc 10 |
| 56–60 | 4: AIOS Integration | Orchestration, safety, capstone | Doc 10 |

---

## 2. Days 1–45 (existing docs — summary only)

**I have not seen Docs 01–09's actual day-by-day content** — only the scope description from Doc 00. What follows is that scope, faithfully, not invented detail. Treat Docs 01–09 as the source of truth for exact daily topics.

**Phase 1 — Full Stack (Days 1–20).** Backend in Python (FastAPI or Flask), React frontend, an AST-based step tracer you write yourself (the step schema: `step / line / event / changed / variables / call_stack`), a real code editor, live deployment (not just localhost). Depth beyond the original plan: strings/lists/dicts/indexing, `for` loops, comparison/boolean operators, real error handling in the tracer itself.

**Phase 2 — Playwright (Days 21–30).** Page Object Model, data-driven tests across many snippets, deliberate edge-case tests, cross-browser config.

**Phase 3 — AI Engineering (Days 31–45).** Structured (JSON) AI output, a basic eval suite scoring AI-generated code against your own evaluator, and a real agent loop: AI generates code, your evaluator runs it, errors feed back for the AI to self-correct and retry.

---

## 3. Days 46–60 (new — Phase 4: AIOS Integration)

### Block A — Days 46–50: Tools, MCP, Browser
| Day | Topic | Done when |
|---|---|---|
| 46 | Tool abstraction, MCP-shaped. Code-evaluator becomes the first registered tool. Read-tool vs act-tool split decided here, as architecture — not later. | Registry works; Phase 3 tests still pass unmodified |
| 47 | Your own MCP server (Python `mcp` SDK) exposing AIOS's tools + consuming one external MCP server (filesystem or GitHub) | Claude Desktop can call your tool; your agent can call an external one |
| 48 | Planner/router with loop guards (max iterations, max tool calls) and a spend cap, built in from day one. Tracer schema extended to log `tool_call → result → retry` | A task with no matching tool fails safely instead of looping |
| 49 | Browser tool via Playwright (reuse Phase 2). High-level task tools preferred over low-level click primitives | Planner correctly routes a "find X on this page" task to the browser tool |
| 50 | Multi-step browser tasks, session persistence. Mini project: "morning scout" digest across 2–3 sites | Digest runs end to end unattended |

### Block B — Days 51–55: Email, Docs, RAG, Checkpointing
| Day | Topic | Done when |
|---|---|---|
| 51 | Email + Calendar tools, real OAuth 2.0 flow. Read/search = read-tool. Draft (never auto-send) = act-tool | Agent drafts a reply; it sits unsent |
| 52 | One generic approval gate every act-tool routes through. Document tool (Drive API), reusing Day 51's OAuth | Every act-tool built so far requires the same approval step |
| 53 | RAG foundations — embeddings + plain-Python vector store (list/dict or SQLite, cosine similarity — no LangChain) | Embed 10 docs, retrieve top 3 for a query, explain the ranking |
| 54 | Research tool — web search + Day 53 retrieval, synthesized into structured JSON | All 6 tools (code, MCP, browser, email/calendar, docs, research) independently callable |
| 55 | Checkpointing — persist orchestrator state to file/SQLite. The kill test: kill mid-run, restart | Resumes exactly where it died, not from scratch |

### Block C — Days 56–60: Orchestration, Safety, Capstone
| Day | Topic | Done when |
|---|---|---|
| 56 | Business automation = orchestration on top of Day 55's checkpointing, not a new tool | One instruction → correct 3-step plan across 3 tools; survives a mid-workflow kill |
| 57 | Safety audit — prompt injection against the full tool set; answer "what's the blast radius if compromised today" | Injected instruction not obeyed; blast-radius answer in under a minute |
| 58–59 | Capstone: research → draft email → save doc → approve → send. Day 59 is deliberate debug/integration buffer | Runs unattended except the one approval step |
| 60 | Demo & wrap — full multi-agent trace visualized live in your tracer UI, recorded | You can watch, step by step, what ran, what changed, where it retried |

---

## 4. What v1.2 had that this plan intentionally drops

| v1.2 topic | Why it's cut here |
|---|---|
| JWT / multi-user auth | Personal, single-user tool — add later only if you expose this beyond yourself |
| Cross-provider structured output (4 LLM providers) | Unneeded for personal use on one provider |
| Dedicated prompt-registry + A/B eval day | Folded in as an ongoing practice, not a calendar day |
| Separate weekly architecture-review days | Folded into the existing per-day "done when" gates |
| LangGraph specifically as a named framework | Checkpointing concept is covered (Day 55) in plain Python instead — matches your existing preference for plain Python over heavy frameworks. Fine to swap in LangGraph later if you want the named-framework line on a resume |

Everything else from v1.2's actual dedicated days — MCP, RAG, the kill test, loop guards, OAuth, read/act tool separation, drafts-don't-send, browser tool design — is now in Block A–C above.

---

## 5. V2.0 (the execution handbook) — status

**Reusable as-is:** the mechanism — six paste-ready generation prompts (journal + git log → devlog/LMS lesson/LinkedIn/X/shorts), the two cadence modes, the BytesferLMS course-slot mapping. None of that is day-specific; it works over any day count.

**Needs rebuilding, not reuse:** the Day Map itself — the money-moment/video-title/talking-points entry for each of the old 34 days. Those don't correspond to this curriculum's days anymore. That's a separate follow-up task once this syllabus is locked, not something to do now.

---

## 6. Repo housekeeping (from earlier)

```
docs/
  curriculum/        ← active source of truth: this file + Docs 00–10
  archive/
    30-day-ai-agent-engineering-bootcamp-v1.2.md
    aios-engineering-bootcamp-v2-execution-handbook.md
    code-visualizer-45-day-roadmap.md   ← superseded by Docs 01–09; different day-groupings, don't keep active
```
Update `CLAUDE.md`'s Source of Truth section to point at `docs/curriculum/` once these are in place.

---

## 7. Verified against Doc 00's Scope (2026-08-04)

Docs 01–09 were checked line-by-line against Doc 00's promised Scope section and Doc 10's assumptions. Three real gaps were found and closed: Phase 1 had no live deployment step and no string/list/dict/indexing evaluator work; Phase 2 had no Page Object Model, data-driven tests, or cross-browser CI; Phase 3 had no structured output, no self-correct retry loop, and no eval suite — despite Doc 10 assuming that loop already existed. All three are now fixed directly in Docs 02, 04, 05, 06, 08, 09. Docs 01, 03, and 07 needed no content changes, only a recap-line update in Doc 03 and Doc 09, and a transition-line update in Doc 08, to stay consistent with what upstream days now cover.

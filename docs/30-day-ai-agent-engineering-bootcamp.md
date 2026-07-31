# The 30-Day AI Agent Engineering Bootcamp
### From basic Python to a production-grade, multi-agent AI Operating System

> **Version 1.2 — FINAL technical curriculum (source of truth).**
> Changelog: **v1.0** — original 30-day curriculum (Weeks 1–4 + capstone).
> **v1.1** — review feedback integrated via Appendix D (CS-foundations micro-lessons, database design depth, design patterns named in place, cost-optimization thread, model selection, weekly architecture reviews + code reading, daily debugging drill).
> **v1.2** — Week 5 frontend track added (Days 31–34: React + TypeScript + Tailwind + Vite, building the AIOS web UI); Appendix D8 corrected accordingly.
> Companion document: *AIOS Engineering Bootcamp V2.0 — Execution Handbook* (build-in-public workflow; extends this file, never modifies it).

---

## 0. How This Bootcamp Works

**Who this is for:** A builder with basic Python, real software-testing experience, and 3–4 focused hours per day. Your QA background is not a footnote — it is your unfair advantage. Most self-taught AI engineers ship agents they cannot verify. You already think in terms of "how do I prove this works?" This bootcamp weaponizes that.

**The one rule:** Every claim an AI system makes must be verifiable by a test. An agent saying "done" is not done. A passing test is done. This principle appears on Day 6 and never leaves.

**Daily rhythm (3–4 hours):**

```
┌─────────────────────────────────────────────────┐
│ 0:00–0:45  LEARN    Read/watch, apply the       │
│                     17-step teaching framework   │
│ 0:45–2:45  BUILD    Practical coding + mini     │
│                     project (hands on keyboard)  │
│ 2:45–3:15  VERIFY   Write tests, run quiz,      │
│                     debug what broke             │
│ 3:15–3:30  COMMIT   Git commit + 3-line journal │
│                     (what/why/what confused me)  │
└─────────────────────────────────────────────────┘
```

**How to apply the 17-step teaching framework:** This document is the *map* — the what, why, and in what order. For each topic listed on a given day, run the full framework (What is it → Why → Problem it solves → Analogy → Internals → Diagram → Smallest example → Line-by-line → Exercise → Mini project → Mistakes → Debugging → Industry usage → Interview → Summary → Quiz → Challenge) as a study session with your AI tutor of choice. The curriculum tells you exactly which concepts to feed into that framework and in what sequence, so nothing is introduced before its prerequisites.

**One repository for 30 days.** You build a single monorepo called `aios/` (your AI Operating System). Every day adds to it. By Day 30 it is a portfolio piece, a product seed, and your interview talking-track — not 30 disconnected scripts.

**Prerequisite chain (LEGO principle):**

```
Python fundamentals ──► Type hints ──► Pydantic ──► Structured outputs
        │                                  │              │
        ▼                                  ▼              ▼
   HTTP/JSON ──► REST ──► Async ──► LLM API calls ──► Tool calling ──► Agent loop
                                        │                                  │
                                        ▼                                  ▼
                            Embeddings ──► Vector DB ──► RAG ──► Memory ──► LangGraph
                                                                              │
                                                                              ▼
                                              FastAPI ──► MCP ──► Multi-agent ──► CAPSTONE
```

Nothing on the right is taught before everything on its left.

---

## 1. The 2026 Stack — and WHY Each Choice Over Alternatives

| Layer | Choice | Rejected alternatives & why |
|---|---|---|
| Python tooling | **uv** (env + packages + lockfile) | pip+venv (slow, no lockfile discipline), Poetry (slower resolver, being displaced). uv is Rust-fast, one tool for everything, industry default by 2026. |
| Lint/format | **ruff** | black+flake8+isort (three tools doing what one does faster). |
| Testing | **pytest** | unittest (verbose, less ecosystem). pytest fixtures map directly onto dependency injection thinking. |
| HTTP client | **httpx** | requests (no async support — a dealbreaker for agents making parallel LLM calls). |
| Validation | **Pydantic v2** | dataclasses/attrs (no runtime validation of untrusted LLM output — the #1 source of agent bugs). Pydantic is also the schema language of FastAPI, structured outputs, and most agent frameworks — one skill, four uses. |
| API framework | **FastAPI** | Flask (sync-first, manual validation), Django (batteries you don't need for an API-first agent backend). FastAPI is async-native, Pydantic-native, auto-documents itself. |
| Agent framework | **LangGraph** | CrewAI (opinionated, hides the loop — bad for learning WHY), AutoGen (conversation-centric, weaker persistence). LangGraph gives you explicit state machines, checkpointing (pause/resume agents), and human-in-the-loop — the three things production agents actually need. Crucially: you build a raw agent loop from scratch FIRST (Day 10), so LangGraph is a convenience, not a mystery. |
| Tool protocol | **MCP** | Bespoke per-provider tool wiring. MCP is the open standard (Anthropic-originated, adopted by OpenAI/Google in 2025) — write a tool server once, use it from any model, Claude Desktop, or your own agents. |
| Providers | **Claude + Gemini + OpenAI-compatible + Ollama** | Single-provider lock-in. You build a provider-router abstraction so switching is a config change. Ollama teaches you what "local model" actually means (weights, quantization, VRAM). |
| Vector DB | **Qdrant** (+ pgvector awareness) | Pinecone (closed, can't self-host — wrong for an "OS" you own), Chroma (fine for toys, weaker production story). Qdrant: open source, Docker-first, hybrid search built in. You also learn pgvector so you know when "just use Postgres" is the right call. |
| Databases | **SQLite → PostgreSQL, Redis** | Starting with Postgres adds ops friction on Day 1. SQLite teaches SQL with zero setup; you migrate to Postgres in Week 4 and *feel* why (concurrency, types, production). Redis for queues/cache/rate-limits. |
| Browser automation | **Playwright** | Selenium (flaky waits, older architecture). Playwright auto-waits, has codegen, and is what you already trust from testing. |
| Containers | **Docker + Compose** | Bare-metal deploys (non-reproducible), Kubernetes (massive overkill for a solo founder — learn it when you have the problem it solves). |
| CI/CD | **GitHub Actions** | Jenkins (self-hosted maintenance burden). Actions lives where your code lives. |
| LLM observability | **Langfuse** (self-hosted) + **structlog** | LangSmith (excellent but closed/hosted). Langfuse is open source — consistent with owning your OS. structlog because print-debugging agents is how you lose weekends. |

---

# WEEK 1 — FOUNDATIONS (Days 1–7)
### Theme: "A professional Python workshop, then first contact with LLMs"

**Week 1 architecture — what exists by Day 7:**

```
┌──────────────────────────────────────────────────────┐
│                    aios/ (repo)                      │
│                                                      │
│  ┌────────────┐   ┌──────────────┐   ┌───────────┐   │
│  │  CLI chat   │──►│ LLM client   │──►│ Provider  │   │
│  │  (Day 7)    │   │ (httpx,async)│   │ APIs      │   │
│  └────────────┘   └──────┬───────┘   └───────────┘   │
│                          │                            │
│  ┌───────────────────────▼────────────────────────┐  │
│  │ config (env vars) · logging · error handling   │  │
│  │ type hints everywhere · pytest suite · ruff    │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

**Repo structure established Day 1 (grows all month):**

```
aios/
├── pyproject.toml          # uv-managed project + ruff config
├── uv.lock
├── .env.example            # documented env vars (never commit .env)
├── .gitignore
├── README.md
├── src/aios/
│   ├── __init__.py
│   ├── config.py           # Day 5
│   ├── logging.py          # Day 5
│   └── llm/                # Day 7
├── tests/
└── docs/journal.md         # daily 3-line log
```

---

## Day 1 — Professional Environment: uv, Git, GitHub
**Duration:** 3.5h (Learn 1h / Build 2h / Verify+commit 0.5h)
**Objectives:** Explain what a virtual environment isolates and why; initialize a uv project; use git init/add/commit/branch/merge; push to GitHub with SSH; write a .gitignore that protects secrets.
**Topics:** interpreters vs environments, uv (init, add, sync, lock), semantic versioning, git's object model (working tree → staging → commits as snapshots), branches as pointers, remotes, SSH keys.
**Reading (45–60m):** uv docs "Projects" section; git internals explainer (commits/branches/HEAD).
**Practical:** Create `aios/` with uv; make 5 commits across 2 branches; deliberately create and resolve a merge conflict; push to GitHub.
**Mini project:** "Repo bootstrap" — the exact structure above, plus a `Makefile`/justfile with `setup`, `lint`, `test` targets.
**Homework:** Write `docs/journal.md` entry #1; read your git log and explain each commit hash's parent.
**Quiz (self-test):** (1) What problem do lockfiles solve that requirements.txt doesn't? (2) What does a branch literally point to? (3) Why is `.env` in .gitignore but `.env.example` committed?
**Interview expectation:** "Walk me through what happens when you run `git commit`." "Why virtual environments at all?"
**Common mistakes:** committing `.venv/`; using `git add .` blindly; HTTPS remotes then fighting auth daily.
**Git milestone:** `day-01: project bootstrap with uv, structure, CI-ready layout`

## Day 2 — Modern Python: Type Hints, Errors, Pydantic Foundations
**Duration:** 3.5h
**Objectives:** Annotate any function fully (including generics, Optional, unions); explain what type hints do and do NOT do at runtime; design exception hierarchies; validate untrusted data with Pydantic v2.
**Topics:** type hints as contracts, `mypy`-style checking vs runtime, dataclasses, why dataclasses fail on untrusted input, Pydantic models, field validators, `model_validate` / `model_dump`, custom exceptions, try/except/else/finally, EAFP vs LBYL, exception chaining (`raise ... from`).
**Why now:** Every LLM response you'll ever parse is untrusted input. Pydantic on Day 2 means every later day validates instead of hopes.
**Practical:** Build `schemas.py` with a `ChatMessage`, `ToolCall`, `AgentConfig` model set — the actual schemas your OS will use for weeks.
**Mini project:** "Config validator" — load a JSON config, validate with Pydantic, produce human-readable errors for 5 deliberately broken configs.
**Homework:** Type-annotate Day 1's Makefile helper script; run `ruff check` clean.
**Quiz:** (1) Difference between a dataclass and a Pydantic model receiving `{"age": "25"}`? (2) When does a type hint cause a runtime error? (3) Why `raise NewError from original`?
**Interview:** "How do you handle malformed data from an external API?"
**Common mistakes:** `except Exception: pass`; mutable default arguments; validating at every layer instead of at the boundary.
**Git milestone:** `day-02: typed schemas + exception hierarchy`

## Day 3 — JSON, HTTP, and REST from the Wire Up
**Duration:** 3.5h
**Objectives:** Read/write JSON fluently (including edge cases: unicode, numbers, nesting); explain an HTTP request byte-by-byte; use verbs/status codes/headers correctly; consume a real REST API with httpx.
**Topics:** JSON grammar and its Python mapping, serialization pitfalls (datetimes, Decimals), HTTP anatomy (request line, headers, body), methods, status code classes (2xx/4xx/5xx and what each MEANS for retry logic), headers that matter for AI APIs (`Authorization`, `Content-Type`, rate-limit headers), REST resource design, pagination, idempotency.
**Analogy anchor:** HTTP as postal mail — envelope (headers), letter (body), return address, delivery receipts (status codes).
**Practical:** Use httpx (sync, for now) against a public REST API; handle 404s, timeouts, and retries with exponential backoff — by hand, so you understand what retry libraries do.
**Mini project:** "API explorer CLI" — fetch, paginate, and pretty-print any REST endpoint; save responses to disk as JSON.
**Quiz:** (1) Which status codes are safe to retry and why? (2) Why is PUT idempotent but POST not? (3) What breaks when you `json.dumps` a datetime?
**Interview:** "Design the retry policy for a flaky third-party API."
**Common mistakes:** retrying 4xx errors; ignoring rate-limit headers; string-concatenating URLs.
**Git milestone:** `day-03: http client with retries + backoff`

## Day 4 — Async Programming (the Agent Engineer's Superpower)
**Duration:** 4h — this is the hardest foundation day; budget for it.
**Objectives:** Explain the event loop, coroutines, and awaitables; convert sync httpx code to async; run N API calls concurrently with `asyncio.gather` and `TaskGroup`; know when async does NOT help (CPU-bound work).
**Topics:** blocking vs non-blocking IO, the event loop as a single-threaded scheduler, `async def` / `await`, tasks vs coroutines, `gather` vs `TaskGroup` (structured concurrency), timeouts and cancellation, semaphores for rate limiting, async context managers.
**Why now:** An orchestrator querying 3 agents, or a RAG system embedding 500 chunks, is either async or unusably slow. Every framework you'll touch (FastAPI, LangGraph, MCP SDKs) is async-native.
**Visual anchor:**
```
SYNC:   req1 ████████ req2 ████████ req3 ████████   (24s)
ASYNC:  req1 ████████
        req2 ████████                                (8s)
        req3 ████████
```
**Practical:** Rewrite Day 3's client as `AsyncClient`; fetch 20 URLs concurrently with a semaphore capping at 5; add per-request timeout + cancellation handling.
**Mini project:** "Concurrent fetcher" — CLI that measures sync vs async wall-time on the same workload and prints the speedup.
**Quiz:** (1) Why doesn't async speed up a pure-math loop? (2) What happens to sibling tasks when one task in a TaskGroup raises? (3) What does `await` actually yield control to?
**Interview:** "Explain the difference between concurrency and parallelism, and where asyncio sits."
**Common mistakes:** calling blocking code (`time.sleep`, sync DB drivers) inside async functions; forgetting to await; unbounded `gather` hammering an API into 429s.
**Git milestone:** `day-04: async client with semaphore + structured concurrency`

## Day 5 — Configuration, Secrets, and Logging Like Production
**Duration:** 3h
**Objectives:** Centralize config with pydantic-settings; manage secrets via env vars; replace all prints with structured logging; explain log levels and when each is used.
**Topics:** 12-factor config, `.env` files and loading order, pydantic-settings (typed, validated config — Pydantic payoff #2), API-key hygiene (rotation, least privilege, never in git history), structlog: structured key-value logs, processors, contextvars for request/agent IDs, log levels (DEBUG/INFO/WARNING/ERROR) with concrete rules.
**Practical:** Build `config.py` (single `Settings` object) and `logging.py` (structlog setup) — these two files serve the entire OS from now on.
**Mini project:** Retrofit Days 3–4 code: zero prints, all logs structured, secrets from env, one command flips DEBUG on.
**Quiz:** (1) Why env vars over a config.json for secrets? (2) What's the difference between a log at WARNING vs ERROR — operationally? (3) What is structured logging FOR (hint: grep vs query)?
**Interview:** "You leaked an API key to GitHub. Walk me through the next 10 minutes."
**Common mistakes:** logging secrets; f-string logging that serializes huge objects at DEBUG even when disabled; one giant God-config.
**Git milestone:** `day-05: typed settings + structured logging`

## Day 6 — Testing: Your Home-Field Advantage
**Duration:** 3.5h
**Objectives:** Write pytest tests with fixtures/parametrize; mock HTTP and LLM calls (respx / monkeypatch); measure coverage meaningfully; articulate the test pyramid FOR AI SYSTEMS (deterministic unit tests → contract tests → LLM evals).
**Topics:** pytest discovery, fixtures as dependency injection, parametrize, mocking boundaries (mock the wire, not your own logic), async tests (`pytest-asyncio`), coverage and its limits, and the key mental shift: LLM outputs are non-deterministic, so you test *contracts* (schema validity, tool-call shape, behavioral evals) rather than exact strings. This becomes full evals on Day 25.
**Practical:** Test suite for Days 2–5 code: schema validation cases, retry logic (mocked 500s then 200), async concurrency behavior, config loading.
**Mini project:** "The lying function" — write a function with 3 subtle bugs, then write the tests that catch each; document your reasoning. (You'll recognize this exercise: it's test design, your craft.)
**Quiz:** (1) Why mock httpx rather than your own retry wrapper? (2) What can 100% coverage still miss? (3) How do you test something non-deterministic?
**Interview:** "How would you test an AI agent?" — you will have a real answer by Day 25; today you have the framework.
**Common mistakes:** testing implementation instead of behavior; brittle exact-string asserts on LLM output; no async test config, silently passing coroutines.
**Git milestone:** `day-06: test suite + CI-ready pytest config`

## Day 7 — First Contact: LLM APIs, Tokens, Context Windows
**Duration:** 4h
**Objectives:** Explain what an LLM does at inference (next-token prediction, sampling); define tokens and count them; explain context windows and their cost/latency/truncation consequences; call Claude, Gemini, an OpenAI-compatible endpoint, and Ollama through ONE common interface you design; stream responses.
**Topics:** what a model file actually is (weights), tokenization (why "strawberry" trips models), temperature/top-p intuitively, context window as working memory (analogy: a desk of fixed size — new papers push old ones off), system vs user vs assistant roles, message arrays as *the* API shape, streaming (SSE), pricing math per token, Ollama: pulling a model, quantization in one paragraph, local vs API trade-offs.
**Practical:** Build `src/aios/llm/` — a `Provider` protocol (abstract interface) + Claude, Gemini, OpenAI-compatible, and Ollama implementations + a router that picks by config. Async, typed, logged, tested with mocks. **This abstraction is the heart of your OS.**
**Mini project:** **Week 1 deliverable — CLI chatbot**: multi-turn conversation, streaming output, `/model` command to hot-swap providers mid-conversation, token count + cost printed per turn.
**Quiz:** (1) Why does the API take the FULL message history every call? (2) What happens when history exceeds the context window? (3) Why can the same prompt give different answers at temperature 0.9?
**Interview:** "Explain tokens to a PM." "API model vs local model — when each?"
**Common mistakes:** treating the API as stateful; ignoring max_tokens; building against one provider's SDK shape everywhere (lock-in).
**Git milestone:** `day-07: provider router + streaming CLI chat (WEEK 1 COMPLETE)`

---

# WEEK 2 — AI FUNDAMENTALS (Days 8–14)
### Theme: "From chatbot to capable system: structure, tools, knowledge, memory"

**Week 2 architecture — what exists by Day 14:**

```
┌────────────────────────────────────────────────────────────┐
│                      CLI Research Agent                     │
│                                                             │
│   ┌──────────┐    ┌─────────────────────────────────────┐  │
│   │  Agent   │───►│           TOOL REGISTRY              │  │
│   │  Loop    │    │  web_search · read_file · calculator │  │
│   │ (Day 10) │◄───│  rag_search (Day 12)                 │  │
│   └────┬─────┘    └─────────────────────────────────────┘  │
│        │                                                    │
│   ┌────▼─────┐   ┌───────────┐   ┌──────────────────────┐  │
│   │ Provider │   │  MEMORY    │   │   RAG PIPELINE       │  │
│   │ Router   │   │ short-term │   │ chunk→embed→Qdrant   │  │
│   │ (Week 1) │   │ long-term  │   │ →hybrid→rerank       │  │
│   └──────────┘   │ (SQLite)   │   └──────────────────────┘  │
│                  └───────────┘                              │
└────────────────────────────────────────────────────────────┘
```

## Day 8 — Prompt Engineering as Engineering
**Duration:** 3h
**Objectives:** Structure prompts with role/context/task/constraints/format; use few-shot examples deliberately; use XML/markdown delimiters; design system prompts as specifications; version and test prompts like code.
**Topics:** why prompts work (conditioning the distribution), system-prompt design, few-shot vs zero-shot and when examples hurt, chain-of-thought and when models do it natively, delimiters and injection-resistance basics, prompt files in the repo (`prompts/` directory, versioned, with changelog) — prompts are code.
**Practical:** Build a prompt registry: prompts as versioned files loaded by name, with variables. Write 3 iterations of one extraction prompt; measure accuracy against 20 hand-labeled cases (mini-eval — seed of Day 25).
**Mini project:** "Prompt A/B harness" — run two prompt versions over a test set, score, report which wins.
**Quiz:** (1) Why do delimiters reduce prompt injection risk? (2) When do few-shot examples backfire? (3) Why version prompts?
**Interview:** "How do you know your prompt change made things better?"
**Common mistakes:** prompts hardcoded in Python strings; "improving" prompts with no eval; kitchen-sink system prompts.
**Git milestone:** `day-08: prompt registry + A/B harness`

## Day 9 — Structured Outputs: Making LLMs Speak Machine
**Duration:** 3h
**Objectives:** Force schema-conforming JSON from every provider (native structured-output modes + tool-based extraction); validate with Pydantic; design repair-and-retry loops for invalid output.
**Topics:** why free-text parsing is a dead end, JSON mode vs schema-constrained decoding vs tool-call extraction (three mechanisms, when each), Pydantic → JSON Schema (payoff #3), handling refusals and partials, the validate→repair→retry pattern with capped attempts.
**Practical:** `structured.py`: `async def extract(text, schema: type[BaseModel]) -> BaseModel` that works across all four providers, with retry-on-invalid + logging of failure modes.
**Mini project:** "Universal extractor" — feed messy inputs (emails, job posts, receipts) and extract typed objects; test with 15 cases including adversarial ones.
**Quiz:** (1) Why is asking nicely for JSON not enough? (2) What does constrained decoding constrain? (3) Where does the validated boundary sit in your architecture?
**Interview:** "Design a pipeline that turns 10,000 messy PDFs' text into database rows."
**Common mistakes:** regex-parsing JSON out of prose; unbounded retry loops; schemas with vague field descriptions (descriptions ARE prompt engineering).
**Git milestone:** `day-09: cross-provider structured extraction`

## Day 10 — Tool Calling and the Agent Loop, From Scratch
**Duration:** 4h — the most important day of the month.
**Objectives:** Explain function/tool calling end-to-end (schema → model emits call → you execute → result returns to model); build a tool registry with auto-generated schemas from typed Python functions; implement the core agent loop by hand; add loop guards.
**Topics:** what the model actually outputs (a structured request, not execution — the model never runs anything, YOU do), tool schemas from function signatures + docstrings, parallel tool calls, the loop: `while model wants tools: execute → append results → call again`, termination conditions, max-iteration guards, error-as-tool-result (feeding failures back so the model self-corrects), tool design principles (few, well-described, typed).
**Visual anchor:**
```
 ┌────────► MODEL ─────────┐
 │    "call web_search"    │
 │                         ▼
 RESULTS ◄──── YOUR CODE executes tool
 (appended       (the model only ASKS)
  to history)
```
**Practical:** Build `tools/registry.py` (decorator: `@tool` turns a typed function into a registered, schema'd tool) and `agent/loop.py` (provider-agnostic agent loop). Tools today: calculator, read_file, list_dir, web_search.
**Mini project:** "First real agent" — answers questions requiring 2–3 chained tool calls; logs every step; hard-stops at 10 iterations.
**Quiz:** (1) Who executes tools, and why does that matter for safety? (2) Why feed errors back instead of raising? (3) What are three distinct loop-termination conditions?
**Interview:** "Whiteboard the agent loop." — This is THE agent-engineering interview question in 2026.
**Common mistakes:** vague tool descriptions (the model picks tools by description!); no iteration cap (hello, $40 infinite loop); swallowing tool errors.
**Git milestone:** `day-10: tool registry + handwritten agent loop`

## Day 11 — Embeddings and Vector Databases (Qdrant)
**Duration:** 3.5h
**Objectives:** Explain embeddings as coordinates in meaning-space; compute and compare them (cosine similarity); stand up Qdrant in Docker (your first container — gentle Docker preview); create collections, upsert, and query with metadata filters.
**Topics:** embedding models vs chat models, dimensionality, cosine similarity with a 2D visual, semantic vs keyword search and why you eventually want both, Qdrant concepts (collections, points, payloads, filters), batch embedding (async — Day 4 payoff), chunk IDs and idempotent upserts.
**Visual anchor:**
```
        "puppy" •  • "dog"
                       • "wolf"
   meaning-space
        "car" •   • "truck"          distance ≈ meaning
```
**Practical:** `docker run qdrant`; embed 200 sentences; build similarity search with filters; verify "closest neighbors" match intuition on 10 spot checks.
**Mini project:** "Semantic notes search" — index your own `docs/journal.md` entries + any markdown notes; query in natural language.
**Quiz:** (1) Why can't you use a chat model's output as an embedding? (2) What does cosine similarity ignore that dot product doesn't? (3) Why store payload/metadata alongside vectors?
**Interview:** "When is keyword search better than vector search?" (Trick question setup for Day 12: hybrid.)
**Common mistakes:** mixing embedding models within one collection; embedding whole documents as single vectors; ignoring filters and post-filtering in Python.
**Git milestone:** `day-11: qdrant integration + semantic search`

## Day 12 — RAG: A Production Pipeline, Not a Demo
**Duration:** 4h
**Objectives:** Build the full pipeline: load → chunk → embed → index → retrieve (hybrid) → rerank → generate with citations; explain every stage's failure modes; evaluate retrieval quality with hit-rate metrics.
**Topics:** why RAG exists (knowledge cutoff, private data, hallucination reduction, cost vs fine-tuning), chunking strategies (fixed/recursive/semantic) and why chunk size is THE hyperparameter, overlap, hybrid retrieval (dense + keyword/BM25) and fusion, cross-encoder reranking (why a second, slower model re-scores the top-k), prompt assembly with citations, retrieval evals (hit@k on a gold set), when RAG is the WRONG tool.
**Practical:** `rag/` module: ingest a folder of PDFs/markdown (10+ docs), hybrid search in Qdrant, rerank, answer with inline citations. Build a 15-question gold set and measure hit@5 before/after reranking.
**Mini project:** "Docs oracle" — point it at real documentation (e.g., FastAPI's docs) and interrogate it; every answer cites chunks.
**Quiz:** (1) Symptom of chunks-too-large vs chunks-too-small? (2) Why does hybrid beat pure-dense on part numbers, names, and codes? (3) What does the reranker see that the retriever didn't?
**Interview:** "Your RAG system gives wrong answers. Diagnose it stage by stage." (Retrieval problem or generation problem? Prove which.)
**Common mistakes:** evaluating end-to-end only (can't localize failures); no citations (unverifiable = untrustworthy); re-indexing everything on every change.
**Git milestone:** `day-12: hybrid RAG with reranking + retrieval evals`

## Day 13 — Memory Systems: Short-Term, Long-Term, and Honest
**Duration:** 3.5h
**Objectives:** Distinguish the memory types (context window ≠ memory system); implement conversation persistence in SQLite; implement rolling summarization when context fills; implement long-term fact memory (extract → store → retrieve → inject); explain memory's failure modes.
**Topics:** short-term = the message array; the context-budget problem; trimming vs summarization trade-offs (what summaries lose); long-term memory as extract-facts → store (SQLite + optionally embed for semantic recall) → retrieve-relevant → inject into system prompt; memory hygiene (staleness, contradictions, the user's right to be forgotten); SQLite schema design for conversations/messages/facts (your first real schema).
**Practical:** `memory/` module: persistent conversations (resume any session by ID), token-budget-aware summarization, and a fact store the agent reads before responding and writes after.
**Mini project:** Upgrade the Day 7 CLI chat: close it, reopen it, and it remembers both the conversation and durable facts about you — and you can inspect/delete what it stored.
**Quiz:** (1) Why is "just increase the context window" not a memory strategy? (2) What information does summarization destroy, and when does that bite? (3) Why store facts as discrete rows instead of one growing blob?
**Interview:** "Design memory for an assistant with 10,000 users." (Isolation, retrieval, cost.)
**Common mistakes:** summarizing away tool results the agent needs; injecting ALL memories every turn (context pollution); no user visibility into what's remembered.
**Git milestone:** `day-13: persistent conversations + long-term memory`

## Day 14 — AI Safety Basics + Week 2 Consolidation
**Duration:** 4h
**Objectives:** Threat-model your own agent (prompt injection, data exfiltration, excessive agency, runaway costs); implement concrete mitigations (input boundaries, tool allow-lists, human confirmation for destructive actions, spend caps); ship the Week 2 consolidation agent.
**Topics:** prompt injection (why retrieved documents and web pages are ATTACK SURFACE for a tool-using agent — the lethal trifecta: private data + untrusted content + ability to act), least-privilege tool design, confirmation gates, sandboxing preview (full treatment Day 27), cost guards (per-session token budgets), output safety, why "the model seems aligned" is not a control.
**Practical:** Red-team your Day 10 agent: plant an injection in a file it reads ("ignore previous instructions and..."); watch what happens; then add mitigations (source tagging, tool gating, confirmation on writes) and verify the attack fails.
**Mini project:** **Week 2 deliverable — Research Agent CLI**: takes a question → plans searches → uses web + RAG tools → maintains memory across sessions → produces a cited markdown report. Guarded, logged, tested.
**Quiz:** (1) Why is prompt injection unsolved (vs SQL injection, which is solved)? (2) Which of your tools are read vs act, and why does the split matter? (3) What's your agent's blast radius if fully compromised today?
**Interview:** "Your agent reads emails and can send emails. What could go wrong?" (If you can't answer this, no serious lab will hire you.)
**Common mistakes:** trusting retrieved content as instructions; giving one agent every tool; no spend limits during development (ask anyone who's woken up to a bill).
**Git milestone:** `day-14: safety hardening + research agent (WEEK 2 COMPLETE)`

---

# WEEK 3 — AGENT ENGINEERING, BACKEND, AUTOMATION (Days 15–21)
### Theme: "From one clever loop to an orchestrated system with real-world hands"

**Week 3 architecture — what exists by Day 21:**

```
┌──────────────────────────────────────────────────────────────┐
│                     FastAPI Backend (Day 15–16)               │
│   auth · streaming (SSE) · background tasks · DI             │
└───────────────┬──────────────────────────────────────────────┘
                │
     ┌──────────▼──────────┐
     │  LangGraph runtime  │  state graphs · checkpoints ·
     │     (Day 17–18)     │  human-in-the-loop · retries
     └──────────┬──────────┘
                │ orchestrates
   ┌────────────┼────────────────┬───────────────┐
   ▼            ▼                ▼               ▼
 Planner     Research         Browser         Comms
 agent       agent (RAG)      agent           agent
                              (Playwright,    (Gmail/Calendar,
                               Day 20)         Day 21)
                │
                ▼
     ┌─────────────────────┐
     │  MCP servers (Day 19)│  filesystem · github · custom
     └─────────────────────┘
```

## Day 15 — FastAPI + Pydantic + Dependency Injection
**Duration:** 3.5h
**Objectives:** Build a typed, auto-documented API; explain ASGI and why FastAPI is async-native; use dependency injection for config/DB/LLM clients; structure routers for a growing app.
**Topics:** ASGI vs WSGI in one diagram, path/query/body params, response models (Pydantic payoff #4), `Depends()` — DI as "declare what you need, the framework wires it" (analogy: restaurant orders, not grocery shopping), dependency overrides in tests (this is why DI exists), lifespan events for startup/shutdown of clients, router organization, OpenAPI docs for free.
**Practical:** `api/` package: `/chat` (non-streaming first), `/conversations`, `/health`; all Week-2 components injected as dependencies; tests using `TestClient` with mocked LLM dependency.
**Mini project:** Your CLI now talks to your API instead of calling the LLM directly — clean client/server split.
**Quiz:** (1) Why does DI make testing dramatically easier? (2) What does a response_model do to extra fields? (3) Why must dependencies holding connections use lifespan/yield?
**Interview:** "How do you swap a real LLM for a fake one in tests without touching endpoint code?"
**Common mistakes:** business logic inside endpoint functions; creating an httpx client per request; sync endpoint functions that block the event loop.
**Git milestone:** `day-15: fastapi backend with DI + tests`

## Day 16 — Auth, Streaming, and Background Tasks
**Duration:** 3.5h
**Objectives:** Protect endpoints with API-key auth, then JWT (issue/verify/expire); stream agent output over SSE; run long jobs in the background with status polling.
**Topics:** authN vs authZ, API keys vs JWTs (stateless sessions, claims, expiry, why you never roll your own crypto — `pyjwt`/passlib do it), hashing vs encryption, SSE vs WebSockets (why SSE wins for token streaming: simpler, HTTP-native, auto-reconnect), FastAPI `StreamingResponse`, `BackgroundTasks` vs a real queue (preview of Redis, Day 22), job-status pattern (submit → 202 + job_id → poll).
**Practical:** `/chat/stream` streaming real agent tokens over SSE; `/jobs` endpoint pair for a slow research task; JWT-protected routes with a login stub.
**Mini project:** Terminal client that logs in, streams a response live, and polls a background research job to completion.
**Quiz:** (1) What's inside a JWT and why can the server trust it without a DB lookup? (2) When do you need WebSockets instead of SSE? (3) Why is `BackgroundTasks` unsuitable for jobs that must survive a restart?
**Interview:** "Design streaming chat for a web client, including reconnects."
**Common mistakes:** JWTs with no expiry; secrets in JWT payloads (they're readable!); background tasks doing CPU-heavy work in the request process.
**Git milestone:** `day-16: auth + SSE streaming + background jobs`

## Day 17 — LangGraph: Agents as State Machines
**Duration:** 4h
**Objectives:** Model an agent as a graph (state, nodes, edges, conditional routing); rebuild Day 10's loop in LangGraph and articulate exactly what you gained; use checkpointing to pause/resume; add human-in-the-loop interrupts.
**Topics:** why graphs — your handwritten loop can't express "if plan fails, replan; if 3 failures, escalate to human" without spaghetti; state schemas (typed — Pydantic payoff #5), nodes as functions, conditional edges, cycles, checkpointers (every step persisted → resume after crash, time-travel debugging), `interrupt` for human approval (this is how the Day 14 confirmation gate becomes first-class), streaming graph events.
**Why LangGraph and not the loop forever:** you keep the loop's understanding but gain durability, observability, and interrupts — the three production requirements. You are not learning magic; you already built the engine on Day 10.
**Practical:** Port the research agent to LangGraph: plan → search → synthesize → cite, with a conditional "needs more research?" cycle and a checkpoint DB. Kill the process mid-run; resume it.
**Mini project:** Add a human gate: before the agent writes any file, execution pauses; you approve/deny via an API call.
**Quiz:** (1) What exactly does a checkpointer persist? (2) Conditional edge vs putting the if-statement inside a node — why does the difference matter for observability? (3) How does an interrupt differ from just stopping?
**Interview:** "Why do production agent systems use graph/state-machine runtimes instead of while-loops?"
**Common mistakes:** monster do-everything nodes (invisible to tracing); mutating state instead of returning updates; skipping checkpointing "for now."
**Git milestone:** `day-17: research agent on langgraph + checkpoints + human gate`

## Day 18 — Planning, Reflection, and Multi-Agent Orchestration
**Duration:** 4h
**Objectives:** Implement plan-then-execute with dynamic replanning; implement reflection (a critic pass that scores work against explicit criteria before it ships); design an orchestrator–specialist architecture; know when multi-agent is over-engineering.
**Topics:** why one agent degrades as scope grows (context pollution, tool confusion, no separation of concerns), planner patterns (structured plan objects — Pydantic payoff #6 — not prose plans), executor feedback → replanning, reflection/critic loops and their cost (every reflection is another LLM call: worth it for reports, absurd for a calculator), orchestrator–worker topology vs peer handoffs, shared state design between agents, and the honesty section: most "multi-agent" products are one agent with good tools — you'll build multi-agent because your OS genuinely has distinct domains (research/browser/comms/code), each needing different tools, prompts, and permissions.
**Practical:** LangGraph supergraph: Orchestrator routes to {Researcher, Writer, Critic}. Critic scores drafts against a rubric; below threshold → revision cycle (max 2). All state checkpointed.
**Mini project:** "Report factory" — request a topic via API; watch plan → research → draft → critique → revise → final flow through structured logs.
**Quiz:** (1) What breaks when 2 agents can write the same state key? (2) Why must plans be structured objects? (3) Give a case where adding a second agent made a system worse.
**Interview:** "When would you NOT use multi-agent architecture?" (Strong candidates argue against complexity.)
**Common mistakes:** agents chatting in prose instead of passing typed state; unbounded reflection loops; orchestrator doing work itself instead of routing.
**Git milestone:** `day-18: orchestrator + critic with bounded reflection`

## Day 19 — MCP: The USB Port for AI Tools
**Duration:** 3.5h
**Objectives:** Explain MCP's architecture (host/client/server; tools, resources, prompts); consume existing MCP servers from your agents; build your own MCP server exposing your OS's tools; connect it to Claude Desktop/Code as proof of interoperability.
**Topics:** the M×N integration problem MCP solves (every app × every tool → protocol in the middle; analogy: USB replaced a drawer of proprietary cables), transports (stdio vs streamable HTTP — when each), tool/resource/prompt primitives, the official Python SDK (`FastMCP`-style decorators), security model (an MCP server runs with YOUR permissions — Day 14 thinking applies: allow-lists, read-only defaults), why this beats hand-wiring: your Day 10 registry served one app; an MCP server serves every MCP client on earth.
**Practical:** (1) Wire a filesystem MCP server into your LangGraph agents. (2) Build `aios-mcp`: your memory store, RAG search, and report generator exposed as MCP tools. (3) Connect it to Claude Desktop and use YOUR tools from a product you didn't write — the moment MCP clicks.
**Mini project:** GitHub-via-MCP: agent lists your repos' open issues and drafts triage comments (read-only today; write scopes come Day 21).
**Quiz:** (1) What's the difference between a tool and a resource in MCP? (2) Why does stdio transport imply local trust? (3) What did you gain over the Day 10 registry, concretely?
**Interview:** "Explain MCP to an engineer who's never heard of it, in 90 seconds."
**Common mistakes:** MCP servers with god permissions; tools with undocumented side effects; assuming every MCP server you find is safe to install (it's arbitrary code).
**Git milestone:** `day-19: aios mcp server + external mcp consumption`

## Day 20 — Playwright: Giving Your Agents Eyes and Hands
**Duration:** 4h
**Objectives:** Drive a real browser from async Python (navigate, locate, click, type, extract, screenshot); write selectors that survive redesigns; wrap browser capabilities as safe agent tools; handle auth sessions and downloads.
**Topics:** Playwright architecture (browser server ↔ your script over websocket — why it's fast and reliable), auto-waiting (the reason your test experience says "Selenium flakes, Playwright doesn't"), locator strategy hierarchy (role/text > test-id > CSS >> XPath), persistent contexts for logged-in sessions, headless vs headed, tracing for debugging, and the agent-integration decision: high-level task tools ("search_flights(origin, dest)") vs low-level primitives ("click(selector)") — start high-level and reliable; low-level agentic browsing is powerful but failure-prone, and you'll gate it accordingly. Ethics/ToS: rate limits, robots.txt, no credential harvesting.
**Practical:** `browser/` module with tools: `fetch_page_text`, `screenshot`, `fill_form`, `extract_table`, plus one site-specific high-level tool of your choice. Session persistence so a login survives restarts.
**Mini project:** "Morning scout" — agent visits 3 sites you actually check daily, extracts what matters, produces one digest. (First taste of the capstone's daily-briefing feature.)
**Quiz:** (1) Why does auto-waiting eliminate `sleep(5)` hacks? (2) Why prefer role/text locators over CSS chains? (3) Why are high-level browser tools more agent-reliable than click-level control?
**Interview:** "Design browser automation that doesn't break when the site ships a redesign."
**Common mistakes:** brittle selectors; ignoring `networkidle`/load states; letting an LLM click arbitrary elements on authenticated sites without gates.
**Git milestone:** `day-20: browser toolset + morning scout`

## Day 21 — Real-World APIs: Gmail, Calendar, GitHub, Files, Terminal
**Duration:** 4h
**Objectives:** Complete OAuth 2.0 for Google APIs and explain each step of the flow; build read/draft (not auto-send) email tools; build calendar query/create tools; build GitHub automation with a PAT; wrap filesystem and shell access with strict sandboxes.
**Topics:** OAuth 2.0 properly (consent → auth code → token exchange → refresh tokens; analogy: hotel key-card, not the master key — scoped, expiring, revocable), scopes as least-privilege, Gmail API (query syntax, MIME parsing, drafts-first policy: the agent DRAFTS, you SEND — the single most important safety decision in this bootcamp), Calendar API (events, free/busy), GitHub REST (issues, PRs) building on Day 19's MCP work, filesystem tools with path-allowlist jail, terminal tools with command allow-lists + timeouts + no-shell-injection argument passing.
**Practical:** `integrations/` package: gmail (search/read/draft), calendar (today/create), github (issues/PR comments), files (jailed), shell (allow-listed). Every write-capable tool routes through the Day 17 human gate.
**Mini project:** "Inbox triage" — agent reads unread email, classifies (urgent/action/FYI/noise), drafts replies for the top 3, and presents everything for your approval. Nothing sends itself.
**Quiz:** (1) Why refresh tokens — why not one eternal token? (2) Why drafts-only for an email agent? (3) How does argument-array subprocess execution prevent shell injection?
**Interview:** "Design an email assistant a security team would approve."
**Common mistakes:** requesting broad OAuth scopes "to be safe" (backwards!); tokens committed to git; `shell=True` with model-generated strings (never).
**Git milestone:** `day-21: gmail/calendar/github/files/shell tools, gated (WEEK 3 COMPLETE)`

---

# WEEK 4 — PRODUCTION + CAPSTONE (Days 22–30)
### Theme: "Make it real: persistence, containers, CI, observability — then ship the OS"

## Day 22 — PostgreSQL + Redis: The Production Data Layer
**Duration:** 3.5h
**Objectives:** Migrate the SQLite persistence layer to PostgreSQL (async); explain what Postgres buys you (concurrency, types, JSONB, durability); use Redis for caching, rate limiting, and a real task queue; know what belongs in which store.
**Topics:** SQLite vs Postgres honestly (when SQLite is actually fine), asyncpg/SQLAlchemy-async basics, migrations with Alembic (schema change discipline), JSONB for tool-call payloads, connection pooling, Redis data structures (strings/hashes/sorted sets) mapped to real uses: LLM response cache, sliding-window rate limiter, job queue (replacing Day 16's in-process BackgroundTasks with something restart-proof), TTLs. Data-placement rule of thumb: Postgres = truth, Redis = speed, Qdrant = meaning.
**Practical:** Docker-compose file for postgres+redis+qdrant (compose taught properly tomorrow — today you use it); migrate conversations/messages/facts to Postgres via Alembic; add Redis caching to embeddings and a rate limiter to `/chat`.
**Mini project:** Job queue v2 — research jobs survive an API restart mid-run (checkpoints in Postgres, queue in Redis). Kill it, restart it, watch it finish.
**Quiz:** (1) What concurrency problem does Postgres solve that SQLite has? (2) Why cache embeddings but not chat completions (usually)? (3) What happens to Redis data on restart, and when is that acceptable?
**Interview:** "Which datastore for: chat history, session cache, semantic search, rate limits — and why?"
**Common mistakes:** sync DB drivers in async endpoints (event-loop poison); schema changes without migrations; Redis as the only copy of anything important.
**Git milestone:** `day-22: postgres + redis data layer with migrations`

## Day 23 — Docker & Compose: Reproducible Everything
**Duration:** 3.5h
**Objectives:** Explain images vs containers vs layers; write an optimized multi-stage Dockerfile for the API (uv-based, small, cached, non-root); compose the full stack (api, postgres, redis, qdrant, langfuse) with networks, volumes, healthchecks; debug inside containers.
**Topics:** containers vs VMs (namespaces + cgroups, one diagram), layer caching and why dependency-install order matters, multi-stage builds, `.dockerignore`, non-root users, env injection at runtime (Day 5 payoff — your 12-factor config drops in unchanged), compose services/networks/volumes/depends_on+healthchecks, dev hot-reload via bind mounts vs prod images.
**Practical:** `docker compose up` brings up your ENTIRE OS from zero on any machine. Prove it: wipe local state, clone fresh, one command, working system.
**Mini project:** "New laptop test" — a README quickstart that takes a stranger from git-clone to chatting with your OS in under 5 minutes. (This becomes your capstone's onboarding.)
**Quiz:** (1) Why does copying `pyproject.toml` before source code speed rebuilds? (2) Volume vs bind mount? (3) What does a healthcheck change about `depends_on`?
**Interview:** "Your image is 2.4GB. Walk me through shrinking it."
**Common mistakes:** secrets baked into images; `latest` tags everywhere; running as root; ignoring healthchecks so the API races the database at startup.
**Git milestone:** `day-23: full stack containerized, one-command boot`

## Day 24 — CI/CD with GitHub Actions
**Duration:** 3h
**Objectives:** Build a pipeline that lints, type-checks, tests, and builds the image on every push; gate merges on green; manage secrets in CI; add a smoke-eval job for prompts (the AI-native twist).
**Topics:** workflow anatomy (triggers/jobs/steps/matrix), caching uv deps for fast runs, service containers for Postgres/Redis in tests, branch protection + PR discipline (yes, solo devs benefit: PRs are where CI gates and where you'll run AI code review), GitHub Secrets, image publish to GHCR, deploy job patterns (SSH-pull-restart for a VPS — honest, simple, sufficient), and CI for AI systems: a cheap eval subset (Day 8's harness) runs on prompt changes, failing the build if quality regresses.
**Practical:** `.github/workflows/ci.yml`: ruff → mypy → pytest (with services) → docker build → (on tag) push to GHCR. Branch protection on. Break the build on purpose; fix it.
**Mini project:** Deployment target — a VPS or free tier of a container host: push a tag, watch your OS go live on the public internet with HTTPS.
**Quiz:** (1) Why cache dependencies but never secrets? (2) What do service containers replace from your local setup? (3) Why run evals in CI only on prompt/model changes?
**Interview:** "Design CI for a system whose tests include non-deterministic LLM calls."
**Common mistakes:** tests green locally, red in CI (env drift — Docker solves this, use it); secrets echoed into logs; deploys with no rollback path (keep the previous image tag).
**Git milestone:** `day-24: full ci/cd, deployed`

## Day 25 — Observability & Evals: Seeing Inside the Machine
**Duration:** 3.5h
**Objectives:** Instrument every LLM call, tool call, and agent step with Langfuse tracing; correlate structured logs with trace IDs; track cost/latency/error dashboards; build a real eval suite (the Day 6 promise, delivered) and score your agents nightly.
**Topics:** traces/spans/generations, why agent debugging without traces is archaeology, cost attribution per feature/agent, structlog↔trace correlation via contextvars (Day 5 payoff), eval taxonomy — deterministic checks (schema-valid? cited sources exist? tool args well-formed?), golden-set grading, LLM-as-judge (uses, biases, and why you calibrate the judge against your own labels), regression evals as the AI version of regression tests (your QA instincts, translated), simple alerting (error-rate and daily-spend thresholds).
**Practical:** Langfuse (self-hosted, already in compose) wired through the provider router — every generation traced with session/user/agent metadata. Build a 30-case eval set for the research agent; score baseline; change a prompt; measure the delta — now you IMPROVE with evidence, not vibes.
**Mini project:** "Nightly report card" — scheduled GitHub Action runs the eval suite and posts scores + spend to your inbox (drafted by your own email tool, naturally).
**Quiz:** (1) Trace vs log — what question does each answer? (2) Three known biases of LLM-as-judge? (3) Why must eval sets contain known-hard and adversarial cases?
**Interview:** "Your agent 'got worse' after a model upgrade. Prove it, localize it, fix it."
**Common mistakes:** tracing only failures (you need baselines); eval sets of 5 easy cases (noise); measuring quality without measuring cost (a 2% gain for 3× spend is usually a loss).
**Git milestone:** `day-25: tracing + eval suite + nightly report`

---

## THE CAPSTONE — Days 26–30: "AIOS Mission Control"

A production-grade personal AI Operating System. Everything below already exists in your repo as parts; the capstone is assembly, hardening, and polish — by design. (And deliberately: this architecture is the seed of a real product — a multi-agent Mission Control is exactly the kind of system you can later point at business automation for clients.)

**Capstone architecture:**

```
┌────────────────────────────────────────────────────────────────────┐
│                          AIOS MISSION CONTROL                       │
│                                                                     │
│  ┌───────────────┐        ┌──────────────────────────────────────┐ │
│  │   Clients      │  SSE   │           FastAPI Gateway             │ │
│  │ web UI (min.)  │◄──────►│  JWT auth · rate limits · streaming  │ │
│  │ CLI · MCP      │        │  job submission · approval endpoints │ │
│  └───────────────┘        └───────────────┬──────────────────────┘ │
│                                           │                         │
│                          ┌────────────────▼─────────────────┐      │
│                          │      ORCHESTRATOR (LangGraph)     │      │
│                          │ intent → plan → route → monitor   │      │
│                          │ checkpoints · human gates · retry │      │
│                          └───┬─────┬─────┬─────┬─────┬──────┘      │
│                              │     │     │     │     │             │
│        ┌─────────┐ ┌────────▼┐ ┌──▼───┐ ┌▼─────┐ ┌──▼─────┐       │
│        │ MEMORY  │ │Research │ │Browser│ │Comms │ │ Coder  │       │
│        │ agent-  │ │ agent   │ │agent  │ │agent │ │ agent  │       │
│        │ shared  │ │ RAG+web │ │Play-  │ │gmail/│ │ write+ │       │
│        │ (facts+ │ │ +cite   │ │wright │ │cal,  │ │ run in │       │
│        │ convos) │ └─────────┘ └──────┘ │drafts│ │sandbox │       │
│        └─────────┘                      └──────┘ └────────┘       │
│                                           │                         │
│  ┌────────────────────────────────────────▼────────────────────┐  │
│  │ Providers: Claude · Gemini · OpenAI-compat · Ollama (router) │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │ Postgres (truth) · Redis (queue/cache) · Qdrant (meaning)    │  │
│  │ Langfuse (traces) · structlog · Docker Compose · CI/CD       │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

**Capstone folder structure (final form):**

```
aios/
├── src/aios/
│   ├── api/            # gateway: routes, auth, sse, jobs, approvals
│   ├── orchestrator/   # supergraph, routing, plans, gates
│   ├── agents/         # research/ browser/ comms/ coder/ (prompt+tools+graph each)
│   ├── llm/            # provider router (4 providers)
│   ├── tools/          # registry + shared tools
│   ├── integrations/   # gmail, calendar, github
│   ├── browser/        # playwright toolset
│   ├── rag/            # ingest, hybrid retrieve, rerank
│   ├── memory/         # conversations, facts, summaries
│   ├── sandbox/        # code execution jail
│   ├── mcp_server/     # aios exposed via MCP
│   ├── evals/          # golden sets, judges, runners
│   ├── config.py · logging.py · schemas.py
├── prompts/            # versioned prompt files
├── tests/              # unit + integration + eval smoke
├── migrations/         # alembic
├── docker/ · docker-compose.yml
├── .github/workflows/
└── docs/               # architecture.md, runbook.md, journal.md
```

## Day 26 — Capstone I: Core Assembly
**Duration:** 4h
**Objectives:** Stand up the gateway + orchestrator skeleton; wire intent classification (chat vs task vs question-about-memory); route simple chat through memory + provider router end-to-end with streaming; define the capstone's typed state schema and approval flow as contracts FIRST.
**Deliverable:** Natural streamed chat with persistent memory, model hot-swap, and full tracing — through the production stack (compose, Postgres, Langfuse), not the Week-1 CLI path.
**Verify:** Integration test: new conversation → 3 turns → restart stack → resume conversation → memory intact.
**Common mistakes:** rebuilding components instead of importing them; skipping the state-schema design and paying for it on Day 27.
**Git milestone:** `day-26: capstone core — gateway + orchestrator + memory chat`

## Day 27 — Capstone II: The Specialist Agents + Safe Code Execution
**Duration:** 4h
**Objectives:** Mount Research (RAG+web+citations), Coder (generate → execute in sandbox → read results → fix → repeat), and the reflection Critic into the orchestrator; build the sandbox properly.
**Sandbox (the day's deep topic):** why `exec()` is never the answer; layered containment — dedicated Docker container per execution: no network, read-only base FS + tmpfs workdir, CPU/memory/time limits, non-root, output-size caps; the generate→run→observe→fix loop is what makes a coding agent feel magical, and the sandbox is what makes it survivable.
**Deliverable:** "Analyze this CSV and chart the trend" → plan → code → sandboxed run → self-correct on error → chart + explanation returned. Research questions produce cited reports.
**Verify:** Adversarial tests: agent-written code attempting network calls, file escape, and infinite loops — all contained, all logged.
**Git milestone:** `day-27: capstone agents — research + coder + sandbox`

## Day 28 — Capstone III: Hands on the World (Browser, Email, Files, MCP)
**Duration:** 4h
**Objectives:** Mount Browser and Comms agents; route every side-effecting action through the approval gate with a clean approval UX (pending-actions endpoint + minimal web view); expose the whole OS as an MCP server; add scheduled autonomy (the morning briefing).
**Deliverable:** "Check my inbox, draft replies to anything urgent, and add the mentioned meeting to my calendar" → triage → drafts → calendar proposal → ONE approval screen → executed. Cron job produces a daily briefing (calendar + inbox summary + morning-scout digest) in your inbox as a draft.
**Verify:** Injection red-team round 2: malicious instructions planted in an email and a webpage; confirm the gate + source-tagging hold. (Day 14's lesson, now at full system scale.)
**Git milestone:** `day-28: capstone automation — browser/comms/mcp + approvals`

## Day 29 — Capstone IV: Hardening, Evals, Documentation
**Duration:** 4h
**Objectives:** Full eval pass across agents (routing accuracy, citation validity, draft quality via calibrated judge, sandbox containment); load-test the gateway; finish `architecture.md` (diagrams + every technology's WHY — you have 29 days of reasons) and `runbook.md` (start, stop, backup, rotate keys, common failures); cut test-coverage gaps on the critical path; tag `v1.0`.
**Deliverable:** Green CI, green evals, a README quickstart a stranger can follow, and docs that would pass an engineering-org review.
**Interview framing:** This day IS the interview prep — every hardening decision is a story for "tell me about a system you built."
**Git milestone:** `day-29: v1.0 — hardened, evaluated, documented`

## Day 30 — Ship, Demo, and the Road Past Day 30
**Duration:** 3h
**Objectives:** Deploy v1.0 via the Day 24 pipeline; record a 5-minute demo (the artifact that outlives the month — script it: problem → architecture → live flows → safety story); write the retrospective (what you'd redesign — the highest-signal interview material there is); commit the roadmap-forward.
**Roadmap past Day 30 (so momentum survives contact with Monday):**
- **Weeks 5–6:** voice interface; proper web UI; more MCP integrations (WhatsApp Business API is an obvious one for your market); fine-grained per-agent permissions.
- **Weeks 7–8:** eval-driven prompt optimization; cheaper model routing by task difficulty; multi-user tenancy — the step that turns AIOS from personal OS into sellable product.
- **Continuous:** one new eval case per bug forever (regression discipline); monthly dependency + model upgrades gated by the eval suite.
**Git milestone:** `day-30: shipped. AIOS v1.0 live.` 🏁

---

## Appendix A — Cross-Cutting Software Engineering (woven through, not bolted on)

| Practice | Where it lives in the 30 days |
|---|---|
| Clean code | Enforced by ruff from Day 1; naming/function-size review every VERIFY block |
| Project structure | Established Day 1, stress-tested by growth every single day |
| SOLID | DI (Day 15) = Dependency Inversion; Provider protocol (Day 7) = Liskov/Interface Segregation; tool modules (Day 10) = Single Responsibility; discussed explicitly in those lessons |
| Testing | Days 6, 25, and every day's VERIFY block; evals as testing's AI-native extension |
| Documentation | README (Day 23), architecture + runbook (Day 29), journal daily |
| Version control | Daily milestones; branching from Day 1; PR + protected main from Day 24 |
| Code review | From Day 24: self-review via PR diffs + AI review pass before merge, with the rule that YOU must be able to explain every line you merge |

## Appendix B — Interview Preparation Index

By Day 30 you have first-hand, code-backed answers to the questions that actually get asked for AI/agent engineering roles:
1. Whiteboard the agent loop (Day 10) — the canonical question
2. Diagnose a failing RAG system stage-by-stage (Day 12)
3. Design memory for a multi-user assistant (Day 13)
4. What could go wrong with an email-capable agent, and your mitigations (Days 14, 21, 28)
5. Why a graph runtime over a while-loop (Day 17)
6. When NOT to go multi-agent (Day 18)
7. Explain MCP in 90 seconds (Day 19)
8. Test/eval a non-deterministic system (Days 6, 24, 25)
9. Datastore selection rationale (Day 22)
10. "Tell me about a system you built" → AIOS, with tradeoffs and a retro (Days 29–30)

## Appendix C — Rules of Engagement (read weekly)

1. **Tests are ground truth.** An agent's claim of completion is a hypothesis; a passing check is a fact.
2. **Type the boundaries.** Every piece of data crossing a boundary (API, LLM, tool, DB) passes through a Pydantic model.
3. **Draft, don't send.** Side effects require human approval until an eval history earns autonomy.
4. **No unexplained lines.** If AI helped write it and you can't explain it, you don't merge it.
5. **Budget everything.** Iteration caps, token caps, timeouts, spend alerts — before you need them.
6. **Ship daily.** A committed imperfect thing beats an uncommitted perfect plan. The journal keeps you honest.

---

# Appendix D — v1.1 Integration: Review Feedback, Mapped to Days

This appendix integrates external review feedback without breaking the 3–4 hr/day budget. Rule: each addition is a 15–30 minute slot inside an existing day, anchored to the moment the concept becomes *necessary* — or it's explicitly deferred past Day 30. Nothing gets a floating "study this someday" status.

## D1. CS foundations — woven in as micro-lessons (15–30 min each)

| Micro-topic | Day | Anchor (why here) |
|---|---|---|
| Variables in memory, stack vs heap, mutability | 2 | Explains mutable-default-arg bug and why Pydantic copies data |
| Processes, filesystem model | 1 | What `uv run` and your shell actually do |
| Serialization (bytes ↔ objects) | 3 | JSON is one serialization; explains the datetime problem from first principles |
| DNS, TCP/IP, TLS handshake (one diagram each) | 3 | What happens before your httpx request has a connection |
| CPU vs RAM, threads vs processes vs event loop | 4 | THE prerequisite for understanding why async helps IO and not math |
| Caching fundamentals (hit/miss/invalidation/TTL) | 11 → 22 | First taste with embedding reuse; formalized with Redis |
| Big-O, just enough | 11 + 22 | Why vector search uses ANN indexes (not linear scan); why DB indexes exist |
| Networking ports, localhost, 0.0.0.0 | 15 + 23 | The #1 source of "it works locally, not in Docker" confusion |

## D2. Database design — expanded inside Days 13 and 22

- **Day 13 (+20 min):** primary/foreign keys, normalization by intuition (design conversations→messages→facts, spot the redundancy, fix it), when denormalizing is fine.
- **Day 22 (+30 min):** indexes (and their write cost), transactions, ACID, isolation levels in plain language (what two concurrent agents writing memory can corrupt without them), `EXPLAIN ANALYZE` on one slow query before and after adding an index. Quiz addition: "Your messages table hit 1M rows and queries got slow — walk through your diagnosis."

## D3. Design patterns — named where you already built them

You build these patterns anyway; v1.1 makes you *name* them (interviews care):
- **Strategy + Adapter** → the provider router (Day 7). **Factory** → tool registry (Day 10). **Repository** → memory store (Day 13). **Dependency Injection** → FastAPI Depends (Day 15). **Observer** → SSE/event streaming (Day 16). Each day's LEARN block gains a 10-minute "the pattern you just used, formally" segment.

## D4. Cost optimization — consolidated into a named thread

Already present in pieces; now explicit: token budgeting (Day 7 cost-per-turn), embedding cache (Day 22), **provider-level prompt caching** (added Day 25 — cache-aware system-prompt layout can cut input cost dramatically; this is a 2026 must-know), batching embeddings (Day 11), model routing by task difficulty with the eval suite as referee (Day 25 + post-30). Day 25's report card gains a cost-per-feature line.

## D5. Model selection — added to Day 7 (+15 min)

Trade-off discussion, not brand loyalty: frontier reasoning vs multimodal strength vs tool-use reliability vs local/private/offline — and the honest answer: **your evals on your tasks decide, not benchmarks or vibes.** The provider router exists precisely so this stays a config decision.

## D6. Weekly rituals — added to Days 7, 14, 21, 29 (30 min each)

1. **Architecture review:** "What breaks at 100 users? 1,000? 100,000?" Write the answer in `docs/architecture.md`. Early weeks the honest answer is "everything, and that's fine" — the value is knowing *which part fails first.*
2. **Code reading:** one high-quality codebase excerpt per week — W1: httpx retry/transport internals; W2: the MCP Python SDK server module (before Day 19 — read it, then build with it); W3: a LangGraph checkpointer implementation; W4: FastAPI's dependency-resolution code. Deliverable: 5 bullet notes in the journal — "one thing I'll steal, one thing I don't understand yet."

## D7. Daily debugging drill — amends the VERIFY block

VERIFY now includes: reproduce **2–3 planted bugs** for the day's topic (each day's Common Mistakes list is the menu), observe the actual failure, fix it, write one line on the root cause. Ten minutes a day; the payoff is that production failures look familiar instead of terrifying.

## D8. Deliberately NOT added (scope discipline)

- **Frontend/React module** — NOT skipped after all (v1.2 correction): prior React exposure turned out to be AI-assisted vibe coding, not hands-on fluency. Frontend gets a proper dedicated track as **Days 31–34** (see Week 5 below) rather than being squeezed into the core 30, so the prerequisite chain and daily budget stay intact. Within the core 30: Day 16 keeps its 15-min client-side-SSE segment, and Day 28's approval UI is built as deliberately minimal server-rendered HTML — ugly on purpose, replaced properly in Week 5.
- **Full system-design module** (microservices, load balancers, horizontal scaling) — deferred post-30. The weekly D6 reviews build the muscle; the deep material belongs when a real product hits real load. One exception pulled in: **reverse proxy** (Caddy) lands in Day 24 because HTTPS deployment genuinely needs it.
- **Kubernetes** — stays out, as v1.0 already decided. Compose until scale demands otherwise.

**Net budget impact:** ≈ +25 min/day average, absorbed by trimming each day's LEARN block to its essentials (the micro-lessons *replace* generic reading time, not extend the day).

---

# WEEK 5 — THE FRONTEND TRACK (Days 31–34, v1.2)
### Theme: "Learn React and Tailwind for real — by building the face of your own OS"

**Why these 4 days exist:** The products you've shipped so far used React via AI-assisted vibe coding — the code exists, but the mental model doesn't. That's exactly the gap Rule 4 (Appendix C) forbids: *no unexplained lines.* This track fixes it the same way the rest of the bootcamp works — you don't study React in the abstract, you build the real AIOS web UI against your own API, and by the end you can also read, debug, and maintain the React code already running in your Bytesfer products.

**Why AFTER Day 30, not inside the core 30:** (1) The frontend consumes the API — auth, SSE, jobs, approvals must exist first, and by Day 31 they all do. (2) React has its own prerequisite chain (JS mental model → components → state → effects → streaming); wedging it mid-stream would break both chains. (3) The core month stays achievable at 3–4 hrs/day.

**Stack and WHY:** **Vite + React + TypeScript + Tailwind CSS v4.** Vite over Create-React-App (dead) and over Next.js (a full-stack framework — wrong tool when FastAPI is already your backend; learn Next.js later if SEO/SSR ever matters). TypeScript because you just spent 30 days learning that typed boundaries prevent bugs — the frontend deserves the same. Tailwind over hand-rolled CSS (utility classes keep styling co-located and consistent) and over component libraries like MUI (they hide the CSS you're here to learn — you can adopt shadcn/ui *after* you understand what it generates). TanStack Query arrives Day 33 only after you've felt the pain it solves by hand.

**Week 5 architecture — what exists by Day 34:**

```
┌─────────────────────────────────────────────────────────┐
│                 AIOS Web UI (Vite + React + TS)          │
│                                                          │
│  ┌──────────┐  ┌────────────┐  ┌─────────────────────┐  │
│  │  Login    │  │ Chat view  │  │ Mission Control      │  │
│  │  (JWT)    │  │ streaming  │  │ dashboard:           │  │
│  │           │  │ tokens via │  │ jobs · approvals ·   │  │
│  └──────────┘  │ SSE        │  │ memory inspector     │  │
│                └────────────┘  └─────────────────────┘  │
│         Tailwind styling · TanStack Query · fetch        │
└───────────────────────────┬─────────────────────────────┘
                            │ HTTPS (Caddy, Day 24 setup)
                ┌───────────▼───────────┐
                │   FastAPI Gateway      │  (unchanged —
                │   + CORS config        │   one new middleware)
                └───────────────────────┘
```

**Folder addition:**

```
aios/
├── web/
│   ├── index.html · vite.config.ts · tailwind config (v4: in CSS)
│   ├── src/
│   │   ├── main.tsx · App.tsx
│   │   ├── api/          # typed client: auth, chat, jobs, approvals
│   │   ├── components/   # MessageList, Composer, ApprovalCard, JobRow
│   │   ├── pages/        # Login, Chat, Dashboard
│   │   └── hooks/        # useStream, useAuth
│   └── Dockerfile        # build → static files → served by Caddy
```

## Day 31 — JavaScript/TypeScript Essentials + React Mental Model + First Tailwind
**Duration:** 3.5–4h
**Objectives:** Understand what the browser actually runs (DOM, events, the JS event loop — you already know event loops from Day 4; same concept, different runtime); read modern JS/TS fluently (const/let, arrow functions, destructuring, spread, template literals, promises/async-await, modules, interfaces/types); explain React's core model (UI = f(state): components as functions, props down, JSX as syntax not magic, re-rendering); apply Tailwind utilities for layout, spacing, color, typography.
**Topics:** npm vs uv (same job, different ecosystem), Vite dev server and what "bundling" means, JSX → `createElement` (see the compiled output once, demystify forever), component composition, props typing with TS, Tailwind's utility-first philosophy and why it beats "one giant CSS file" for solo maintainers, flexbox via Tailwind (`flex`, `gap`, `justify-*`, `items-*`).
**Practical:** Scaffold `web/` with Vite; build the static chat layout — header, scrollable message list, composer — as pure components with hardcoded messages, styled entirely with Tailwind, fully typed.
**Mini project:** A `MessageBubble` component that renders user vs assistant vs tool-call messages differently based on typed props — the same `ChatMessage` schema from Day 2, now as a TS interface (one contract, both ends of the wire).
**Quiz:** (1) What triggers a React re-render? (2) What does JSX compile into? (3) Why must props be treated as read-only?
**Common mistakes:** mutating props; writing CSS files out of Tailwind habit-avoidance; `any` everywhere (TS with `any` is JS with extra steps).
**Git milestone:** `day-31: web scaffold + static chat UI in typed react + tailwind`

## Day 32 — State, Effects, and Talking to Your API (incl. CORS + Auth)
**Duration:** 4h
**Objectives:** Manage state with `useState` (and know when state should live in a parent — lifting state up); fetch data with `useEffect` correctly and explain why effects are for *synchronizing with external systems*, not "run code on load"; wire real login against your Day 16 JWT endpoint; store/attach tokens sanely; fix CORS with understanding rather than copy-paste.
**Topics:** state vs props vs derived values, controlled inputs (the composer), lists and keys (and why index-as-key corrupts UIs), effect dependency arrays and cleanup functions, race conditions in fetch-on-type (ignore-stale-response pattern), CORS from first principles (browser same-origin policy → preflight → FastAPI CORSMiddleware — 20 min that saves you the classic day of confusion), JWT storage trade-offs (memory + refresh vs localStorage; XSS is why this is a debate at all), a typed `api/` client module with one place for base-URL/auth/error handling.
**Practical:** Login page → token → authenticated fetch of conversation list → render → create new conversation → send message (non-streaming) → response appears. Logout clears state.
**Mini project:** "Memory inspector" page: list the facts your OS stores about you (Day 13's transparency endpoint), with delete buttons — your right-to-be-forgotten feature, now user-facing.
**Quiz:** (1) Why does the effect dependency array exist and what breaks with a missing dep? (2) What is a preflight request and what triggers it? (3) Why is index-as-key dangerous for a reordering list?
**Common mistakes:** infinite effect loops (setting state that's in the dep array); fetching in effects without cleanup; sprinkling fetch calls through components instead of one API module.
**Git milestone:** `day-32: auth flow + live API integration + memory inspector`

## Day 33 — Streaming UI: SSE on the Client, TanStack Query, Real Chat
**Duration:** 4h
**Objectives:** Consume your Day 16 SSE endpoint and render tokens as they arrive; build a `useStream` hook (auth-header-capable fetch-stream reading, since native `EventSource` can't send Authorization headers — the practical detail everyone hits); handle reconnects, aborts (user hits stop), and errors mid-stream; adopt TanStack Query for the non-streaming data and articulate exactly which pain it removed from Day 32's hand-rolled code.
**Topics:** ReadableStream + TextDecoder parsing of SSE frames, accumulating partial tokens into state without re-render storms (batching), optimistic UI (user message appears instantly), AbortController, auto-scroll behavior, TanStack Query (queries, mutations, invalidation, caching) as the industry-standard answer to "server state is not client state," loading/error/empty states as first-class design.
**Practical:** The chat page becomes real: streamed responses, stop button, conversation switcher (Query-cached), markdown rendering of assistant output with code blocks.
**Mini project:** Live job monitor — Day 22's background jobs rendered as a status list that polls via Query and shows plan → step progress from checkpoint data.
**Quiz:** (1) Why fetch-streams instead of EventSource here? (2) What does Query's cache invalidation replace from yesterday's code? (3) Why does naive per-token `setState` hurt, and what's the fix?
**Common mistakes:** appending to state inside a tight stream loop without batching; forgetting AbortController (zombie streams); using Query for the streaming call itself (wrong tool — streams are imperative).
**Git milestone:** `day-33: streaming chat + tanstack query + job monitor`

## Day 34 — Mission Control Dashboard, Polish, Ship
**Duration:** 4h
**Objectives:** Replace Day 28's deliberately-ugly approval page with the real thing (pending actions as cards: what the agent wants to do, arguments, source context, approve/deny → mutation → refresh); assemble the dashboard (jobs, approvals, memory, daily-briefing view); add client-side routing; make it responsive (mobile-first Tailwind — consistent with your mobile-responsive-web product philosophy); build for production and serve behind Caddy via the existing compose + CI pipeline.
**Topics:** React Router (routes, layouts, protected routes tied to auth), responsive Tailwind (`sm:` `md:` breakpoints), dark mode with Tailwind in 20 minutes (because it's your OS and it should look like it), `vite build` output and what a production bundle is, serving static files behind the Day 24 reverse proxy, adding the web build to CI.
**Practical + deliverable:** **AIOS UI v1 live over HTTPS**: login → chat with streaming → approve a real pending email draft from your phone. That last sentence is the demo.
**Verify:** Lighthouse pass for obvious performance/accessibility misses; the Day 23 "new laptop test" updated — one compose command now boots backend AND frontend.
**Quiz:** (1) What does a protected route actually check, and where can it be bypassed (hint: client-side checks are UX, the API is the security)? (2) What's in `dist/` after a build? (3) Why mobile-first breakpoints?
**Common mistakes:** treating client-side route guards as security; shipping the dev server to production; desktop-only layouts.
**Git milestone:** `day-34: AIOS web UI v1 shipped (WEEK 5 COMPLETE)` 🏁

**After Day 34 — closing the vibe-coding loop:** spend one session opening your existing Bytesfer product's React codebase and reading it with your new eyes: identify the state flows, find one bug or smell, fix it yourself, and explain the fix in your journal. That's the moment "vibe-coded" becomes "mine."

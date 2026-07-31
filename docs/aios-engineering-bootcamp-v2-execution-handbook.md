# AIOS Engineering Bootcamp Version 2.0
### Learn • Build • Record • Teach • Ship
#### The Execution Handbook — companion to Curriculum v1.2

---

## 0. What This Document Is (and Is Not)

**V1.2 is the technical curriculum. It is final. This document does not modify, reorder, or restate it.** Every day referenced below (Days 1–34) means "that day exactly as specified in v1.2."

**V2.0 is the execution handbook**: how each v1.2 day becomes, in one workflow, (a) an engineering session, (b) a recorded devlog, (c) an LMS lesson, (d) a LinkedIn post + X thread, (e) shorts material, and (f) GitHub artifacts.

**The authenticity constraint, honored honestly:** You asked for real engineering, not fake polished tutorials. That means the *outputs of the session* — the reflection, what broke, how you fixed it, the actual commit messages — cannot be pre-written in this document. Pre-scripted "failures" ARE fake tutorials. So V2.0 splits every day into two halves:

1. **Pre-plannable (written here):** the day's content angle, video title, the "money moment" to make sure the camera captures, talking points, which mistakes to keep in the edit, shorts seeds.
2. **Session-derived (produced by you, daily, via templates + prompts in §3–4):** reflection, YouTube description/chapters, LMS lesson body, LinkedIn post, X thread, PR description. Budget: ~45 minutes, most of it AI-assisted from your own journal + recording.

**The strategic frame (why this whole thing is worth an extra hour a day for you specifically):**
- Every daily LMS lesson lands as a module in **your own product** — the AI Bootcamp course slot that already exists in BytesferLMS. You are not creating course content *about* the journey; the journey **is** the course, dogfooded through your own platform. When institutes ask "who wrote your AI track?", the answer is a 34-day public receipt.
- The videos are **Channel A** (AI engineering, monetized through BytesferLMS) — the channel your existing strategy already says to launch first. This bootcamp is its launch content: 34 days of episodes, pre-sequenced.
- LinkedIn (your primary channel) gets the professional build-log; X gets the technical thread. Same session, four surfaces, zero separate work.

---

## 1. The One Workflow

```
        LEARN ──► BUILD ──► RECORD           (same 3–4 hrs — recording is
          │         │      (simultaneous)     passive; you build on camera)
          │         ▼
          │      REFLECT  (15 min — journal answers, §3.1)
          │         ▼
          │      PUBLISH  (30–45 min — derive all deliverables, §3.2)
          │         ▼
          │       TEACH   (LMS lesson auto-derived; audience learns WITH you)
          │         ▼
          └──── IMPROVE ──► SHIP  (tomorrow's session opens with yesterday's lesson)
```

**Honest time math.** v1.2 costs 3–4 hrs/day. Recording adds ~0 (screen + mic run while you work). The publishing pipeline adds **45–60 min/day**. Total: 4–5 hrs/day. With a day job, that is the edge of sustainable — so V2.0 defines two cadence modes and you pick per week, guilt-free:

- **Mode A — Daily Raw Devlog (recommended for Weeks 1–2):** publish every day, minimal editing (trim dead air, add chapters, done). Raw is the brand: "watch someone actually become an AI engineer." Upload target: same night or next morning.
- **Mode B — Record Daily, Publish 3×/week:** every session recorded, but only the 3 strongest become edited videos; the rest feed shorts + posts. LinkedIn + X still ship daily (they take 10 min from the template). Switch to Mode B any week the day job spikes — recording never stops, only editing effort flexes.

**Non-negotiables either mode:** daily git milestone (v1.2 already requires it), daily journal reflection, daily LinkedIn post. Those three cost <25 min combined and are the compounding assets.

---

## 2. The Recording System

**Setup (one-time, before Day 1):** OBS (screen + webcam bubble + mic), a fixed scene layout, a `RECORDING` checklist note on screen edge, and a hotkey to drop a marker (in OBS: chapter marker hotkey) — every time something breaks or surprises you, **hit the marker**. Markers are how you find shorts and "keep this mistake" moments without re-watching 3 hours.

**Session structure (every day, ~10 seconds of discipline each):**

| Segment | Length | What it is |
|---|---|---|
| Opening | 30–60s | "Day N of building my AI Operating System in public. Yesterday: X. Today: Y." One sentence each. |
| Objective | 1 min | Read the day's objective from v1.2 in your own words. What exists in AIOS by tonight. |
| Recap bridge | 1 min | How yesterday's piece connects — point at the architecture diagram, touch the actual file. |
| Architecture | 2–5 min | Whiteboard/excalidraw BEFORE coding: what you're about to build and why here. |
| Build | bulk | Code with the mic on. Think aloud (below). Documentation reading ON camera. |
| Debug | as it happens | Never pause recording when something breaks. Say "okay, this is broken, let's find out why." These segments outperform everything else. |
| Test | 5–15 min | Run the day's tests / VERIFY drill on camera. Green is the payoff shot. |
| Reflection | 3–5 min | Answer the §3.1 questions to camera, unedited, tired. This is the LMS lesson's soul. |
| Closing | 30s | "Tomorrow: Z. Code's on GitHub, lesson's on BytesferLMS. Day N done." |

**Estimated recording durations:** raw = your session (3–4h). Published Mode A: 20–45 min (trim only). Published Mode B: 15–25 min edited. Capstone days (26–30) and Day 10 justify longer cuts.

**Thinking aloud — the skill that makes the channel:** narrate *decisions*, not keystrokes. Not "now I'm typing async def" but "I'm making this async because tomorrow three agents call it concurrently." When you don't know something, say the actual sentence: "I don't know what this error means. Let's read it properly." That sentence is why people will subscribe: the positioning is *I am becoming an AI engineer*, not *I already am one*. You're a trainer by background — this is training, done honestly, one day ahead of the student instead of ten years.

**KEEP THESE — never edit out (the authenticity manifesto):**
1. Reading documentation (scrolling, squinting, finding the right section)
2. Every red traceback and the moment of confusion after it
3. Wrong assumptions said aloud, then discovered wrong
4. The v1.2 daily debugging drill (reproducing planted bugs is *content by design*)
5. Architecture changes mid-day ("this design is wrong, here's why, redrawing it")
6. Failed experiments and dead ends — say the cost: "that was 40 minutes; here's what it taught me"
7. Searching (Google/Stack Overflow/asking an AI) — including evaluating whether the answer is right
8. Tests failing before they pass; git mistakes and their fixes (wrong branch, bad rebase — gold)
9. Cost surprises ("that loop just spent ₹X in tokens")
10. The tired end-of-day reflection, verbatim

**Cut freely:** long silent typing, waiting on installs/builds (timelapse them), repeated identical errors after the lesson's been learned once.

---

## 3. The Post-Session Pipeline (45–60 min, template-driven)

### 3.1 Reflect (15 min, journal — the source of truth for everything else)

Answer in `docs/journal.md`, every day, in this exact order:
1. What did I learn? (concept, not activity)
2. What surprised me?
3. What broke?
4. How did I fix it? (the actual path, including wrong turns)
5. What would I redesign?
6. What is tomorrow's challenge, and what am I unsure about?

Plus two production lines: **timestamped markers list** (from OBS hotkey) and **today's money moment — did I capture it?** (If not: 5-minute re-record of just that demo. The money moment is the one clip the day cannot ship without.)

### 3.2 Publish (30–45 min — derive, don't write from scratch)

Everything below is generated FROM the journal + git log + the day's v1.2 block, using the paste-ready prompts in §4. Order of operations:

1. **GitHub (5 min):** milestone commit (v1.2 defines it) → push → PR from day branch with description (prompt §4.5) → merge. Tag on capstone days. README's progress table gains one row.
2. **YouTube metadata (10 min):** title (pre-planned, §6) + description/chapters/tags via prompt §4.1. Upload (Mode A) or queue (Mode B).
3. **LMS lesson (10 min):** prompt §4.2 turns journal + code refs into a BytesferLMS-format lesson. Publish to the AI Bootcamp course as Module N. Where your product supports it, attach the day's video and the repo permalink. (Later, per your existing plan, internal review agents can approve these before publish.)
4. **LinkedIn (7 min):** prompt §4.3. Post same evening — engineering log tone, never marketing.
5. **X thread (5 min):** prompt §4.4. 5–8 tweets, technical.
6. **Shorts (batch weekly, not daily):** Sunday, pull the week's markers, cut 5–10 shorts from the seed list (§6) + whatever genuinely happened. Shorts are byproduct, never a daily obligation.

---

## 4. Reusable Generation Prompts + Templates (paste-ready)

Use any capable model. Always paste three inputs: **(a)** today's v1.2 day block, **(b)** today's journal entry, **(c)** `git log --oneline` for the day. The prompts forbid invention — deliverables may only contain what actually happened.

### 4.1 YouTube metadata
```text
You are my devlog editor. Using ONLY the attached curriculum day, journal entry,
and git log (do not invent events), produce:
1. FINAL TITLE — under 60 chars, curiosity + honesty, no clickbait lies.
   Base title: "<pre-planned title from the Day Map>". Improve only if the
   session's real events beat it.
2. SEO TITLE variant (search-intent phrasing).
3. DESCRIPTION — 3 short paragraphs: what I built into AIOS today, what broke
   and what it taught, links block (GitHub repo + day tag, BytesferLMS lesson,
   LinkedIn, X). Include the day's tech keywords naturally.
4. CHAPTERS — from these timestamps: <paste markers>. Chapter names describe
   the engineering event ("First agent loop run", "Debugging the 429s").
5. TAGS — 15, mixed head/long-tail.
6. THUMBNAIL IDEA — one frame, one emotion, max 4 words of text, based on the
   day's money moment.
7. PINNED COMMENT — one genuine question to viewers about today's design
   decision (not "smash subscribe").
8. CTA line for the outro — send viewers to the BytesferLMS lesson to do the
   exercises, and to the repo to read the code.
Playlist: "Building AIOS — 34-Day AI Engineering Bootcamp".
```

### 4.2 LMS lesson (BytesferLMS AI Bootcamp format)
```text
Turn today's session into a self-paced lesson for my LMS. Inputs attached:
curriculum day, journal, git log, key code file paths. Do not invent content;
where the curriculum lists a concept I did not reach today, mark it
"covered in Day N". Produce:
- Lesson title (Module N: <topic>)
- Learning objectives (3–5, measurable: "explain…", "implement…", "debug…")
- Concept explanation (600–900 words, my teaching framework: what/why/problem/
  analogy/internals/diagram-in-text/smallest-example)
- Worked example referencing the actual repo files (permalinks to today's tag)
- 3 exercises (in-editor runnable where possible: Python for backend days,
  JS/TS for Days 31–34)
- Quiz: 5 MCQs with answer key + one-line why-wrong per distractor
- Assignment: tonight's homework from the curriculum, restated as a rubric
- Challenge: the curriculum's challenge project
- Resources: only links I actually used today (from journal)
- Estimated lesson duration
- Certificate criteria: quiz ≥80% + assignment repo link submitted
Tone: learner-to-learner ("here's what confused me and how I got past it"),
not lecturer-to-student.
```

### 4.3 LinkedIn build log
```text
Write my daily build-in-public post from the attached journal + git log.
Rules: engineering log, not marketing. No hooks like "I did X so you don't
have to". Structure: Day N/34 header line → what now exists in AIOS (2–3
lines, concrete) → the day's real problem and how I solved it (the meat,
4–6 lines, technical) → one lesson stated plainly → one architecture note
or diagram-as-text if the day had one → link to repo + video. 
Under 1300 chars. First person. No emojis beyond ▸ or →. End with the same
question as the video's pinned comment.
```

### 4.4 X (Twitter) thread
```text
From the attached journal + git log, write a 5–8 tweet technical thread.
T1: Day N/34 + the single most interesting thing that happened (specific).
T2–T6: the technical narrative — decision, why, what broke, the fix, with
one short code/log snippet screenshot slot marked [IMG]. T7: lesson in one
sentence. T8: links (repo, video, LMS lesson). No engagement-bait, no
"🧵👇", no invented drama.
```

### 4.5 PR description + release notes
```text
From the attached git log and journal: 
1. PR title = the day's milestone message.
2. PR description: What / Why / How verified (tests run, drill bugs fixed) /
   Screenshots-or-logs slots / Follow-ups (from "what would I redesign").
3. README progress-table row: Day N | topic | what shipped | link to video+lesson.
4. On tag days only: release notes (features, fixes, known issues — from
   journal, no invention).
```

### 4.6 Weekly & monthly review prompts — see §7.

---

## 5. How to Read the Day Map

Each entry below extends one v1.2 day. Format:
- **Title** — pre-planned video title (playlist-consistent: "Day N — …"; refine with §4.1 if reality beats the plan).
- **Money moment** — the one demo the recording MUST capture; it is the thumbnail, the short, and the proof.
- **Talk** — talking points (bullets, not a script) to hit while coding.
- **Keep** — day-specific mistakes/segments that must survive the edit (on top of the §2 manifesto).
- **Shorts** — seeds (30–60s each); cut only the ones that actually happened well.

Objectives, build goals, folder changes, git commits, quizzes, exercises: **already defined per day in v1.2** — the pipeline pulls them from there. They are not restated here (V2.0 extends, it does not duplicate).

---

## 6. THE DAY MAP (Days 1–34)

### Week 1 — Foundations (arc: "a professional workshop rises from an empty folder")

**Day 1 — "I'm building my own JARVIS. Day 1: the professional setup"**
Money moment: empty folder → structured repo → first push visible on GitHub.
Talk: why one repo for 34 days; uv vs pip in one sentence + live speed demo; a commit is a snapshot, a branch is a pointer; why .env never enters git.
Keep: SSH key fumbling; the deliberate merge conflict and its resolution, unhurried.
Shorts: the 34-day challenge announcement (this is the channel trailer) · uv vs pip install race · "what a git commit actually is" whiteboard · the .gitignore that saves your API keys.

**Day 2 — "Type hints and Pydantic: why AI engineers can't skip this"**
Money moment: Pydantic rejecting garbage input with a beautiful error while a dataclass swallowed it silently.
Talk: hints are contracts not enforcement; LLM output = untrusted input, always; stack vs heap micro-lesson while explaining mutability.
Keep: the mutable-default-argument bug reproduced live; any mypy/ruff complaint you didn't expect.
Shorts: dataclass vs Pydantic fed `"age": "25"` · the mutable default bug in 45s · "every LLM response is untrusted input".

**Day 3 — "HTTP from the wire up (what really happens before your API call)"**
Money moment: hand-rolled retry with exponential backoff surviving simulated 500s on screen.
Talk: DNS→TCP→TLS in three tiny diagrams; status-code classes as retry policy; serialization is older than JSON.
Keep: the datetime JSON serialization failure; reading rate-limit headers for the first time.
Shorts: which status codes you may retry (and the one you never) · what happens when you hit Enter on a URL · the datetime that broke json.dumps.

**Day 4 — "Async Python finally clicked (agent engineering's superpower)"**
Money moment: the sync-vs-async wall-clock race — same 20 requests, timer on screen.
Talk: event loop = single-threaded scheduler; IO-bound vs CPU-bound honestly; semaphores as politeness enforced.
Keep: the first forgotten `await` and its cryptic warning; blocking-call-inside-async demonstrated and felt.
Shorts: 24s → 8s race clip · concurrency vs parallelism in one kitchen analogy · the semaphore that prevents 429s · "why async does nothing for math".

**Day 5 — "Config, secrets, and logs: the unglamorous day that saves the project"**
Money moment: one env flag flips DEBUG and the structured logs light up with context.
Talk: 12-factor in plain words; the API-key-in-git horror genre; print vs structlog = grep vs query.
Keep: retrofitting Days 3–4 code — refactoring on camera is rare content; any secret you almost logged.
Shorts: "your API key is in your git history" · print() vs structured logs side-by-side · rotating a leaked key in 60s.

**Day 6 — "I'm a tester learning AI engineering — today those worlds met"**
Money moment: mocked 500-then-200 sequence proving the retry logic, tests green.
Talk: your QA background as the throughline; mock the wire, not your logic; the question that runs the rest of the series: how do you test something non-deterministic?
Keep: the "lying function" exercise end-to-end; a test that passed for the wrong reason.
Shorts: "how do you test an AI?" (part 1 of a recurring series) · the 100% coverage lie · fixture = dependency injection you already use.

**Day 7 — "My code talked to 4 different AIs today (Claude, Gemini, GPT, local)"**
Money moment: `/model` hot-swap mid-conversation in the CLI, streaming, cost printed per turn.
Talk: tokens and the desk-sized context window; the API is stateless — you send the whole history every time; model selection = trade-offs decided by evals, not vibes; Week-1 architecture review (what breaks at 100 users? everything — which part first?).
Keep: first Ollama pull and the wait (timelapse); the first time the full-history-resend truly lands.
Shorts: what a token is (tokenizer on screen) · same prompt, two different answers — why · the context-window desk analogy · running an LLM on my own laptop · what the API really receives (the message array).

### Week 2 — AI Fundamentals (arc: "the chatbot grows hands, knowledge, and memory")

**Day 8 — "Prompts are code (I built an A/B harness to prove it)"**
Money moment: two prompt versions scored on 20 labeled cases; a winner, by numbers.
Talk: prompts versioned in the repo with a changelog; delimiters and why they resist injection; when few-shot examples hurt.
Keep: your first prompt losing to your second; hand-labeling cases (tedium is honest).
Shorts: "stop editing prompts by vibes" · delimiters vs injection demo · the few-shot example that backfired.

**Day 9 — "Forcing an LLM to speak machine (structured outputs)"**
Money moment: a messy real email → validated typed object, across two different providers.
Talk: three mechanisms (JSON mode / constrained decoding / tool-extraction) and when each; validate→repair→retry with a cap; schema field descriptions ARE prompt engineering.
Keep: an invalid output caught by Pydantic and repaired on retry — the whole loop, live.
Shorts: never regex JSON out of prose again · the repair-retry loop animated · one schema, four providers.

**Day 10 — "I built an AI agent from scratch. No framework." ⭐ flagship**
Money moment: the loop's first autonomous run — model requests tool, code executes, result returns, model continues, answer lands. Logs scrolling. Let it breathe on camera.
Talk: the model never executes anything — it only asks; the while-loop everyone wraps in mystique; errors fed back as results; iteration caps or bankruptcy.
Keep: EVERYTHING today. First malformed tool call. The loop that didn't terminate. This is the series' signature video.
Shorts: the agent loop in 60 seconds (whiteboard) · "who actually runs the tools?" · the $40 infinite loop cautionary tale · error-as-feedback: agents that fix themselves · first autonomous run reaction clip.

**Day 11 — "Meaning as coordinates: embeddings + my first vector DB"**
Money moment: nearest-neighbors of a word appearing, and they make sense; Qdrant running in Docker.
Talk: chat models vs embedding models; cosine similarity on a 2D sketch; first Docker container as a gentle preview; caching fundamentals via embedding reuse.
Keep: a neighbor result that surprises you (they always do); first `docker run` friction.
Shorts: "puppy is near dog is near wolf" visualization · semantic vs keyword search · why you never embed a whole book as one vector.

**Day 12 — "RAG done properly (hybrid search + reranking, with receipts)"**
Money moment: hit@5 measured before and after reranking — the number moves on screen.
Talk: chunk size is THE hyperparameter; why hybrid wins on names and part numbers; the reranker sees what the retriever can't; localize failures per stage or debug forever.
Keep: a retrieval that fails, and the stage-by-stage diagnosis; building the gold set by hand.
Shorts: RAG in 60 seconds · chunks too big vs too small — the symptoms · "is it retrieval or generation?" the one diagnostic question.

**Day 13 — "My AI finally remembers me (memory systems + first real schema)"**
Money moment: close the CLI, reopen, it greets the conversation AND recalls a fact from yesterday.
Talk: context window ≠ memory system; what summarization destroys; normalization by intuition while designing conversations→messages→facts; the user's right to see and delete what's stored.
Keep: the schema redesign moment (first drafts are always wrong); a summary that lost something important.
Shorts: "bigger context window" is not a memory strategy · what the summary forgot · show me what you know about me (transparency demo).

**Day 14 — "I hacked my own AI agent (prompt injection, live)"**
Money moment: the planted injection succeeding — the agent obeys the malicious file. Then the mitigations land, the attack repeats, and fails. Before/after, same attack.
Talk: the lethal trifecta (private data + untrusted content + ability to act); read tools vs act tools; drafts-don't-send as a design philosophy; Week-2 architecture review; Week-2 consolidation: the research agent ships.
Keep: the successful attack in full — the uncomfortable part is the value; the mitigation being designed on the whiteboard.
Shorts: prompt injection demo (the clip that travels) · "why is this unsolved when SQL injection is solved?" · the lethal trifecta in 45s · read vs act: sorting my agent's tools.

### Week 3 — Agents, Backend, Automation (arc: "one clever loop becomes an orchestrated system with hands")

**Day 15 — "FastAPI: my agent gets a real backend"**
Money moment: the auto-generated /docs page — every endpoint, typed, interactive, for free.
Talk: DI as the restaurant order (declare needs, kitchen wires it); why DI = testability (swap the LLM for a fake without touching endpoints); ports/localhost micro-lesson; the Strategy/Adapter pattern you built on Day 7, now named.
Keep: the first 422 validation error and reading it properly; TestClient with an overridden dependency working first try (or not).
Shorts: interactive API docs for free · swap a real LLM for a fake in one line (DI) · sync endpoint blocks the whole event loop — demo.

**Day 16 — "Streaming, JWT auth, and background jobs (the backend grows up)"**
Money moment: tokens streaming live over SSE into the terminal client, behind a JWT login.
Talk: what's literally inside a JWT (decode one on screen) and why the server trusts it statelessly; SSE vs WebSockets — and the client-side view (reconnects, buffering); submit → 202 + job_id → poll; Observer pattern, named.
Keep: the first CORS-shaped or auth-shaped 401 confusion; decoding a JWT by hand.
Shorts: I decoded a JWT on camera (they're readable!) · SSE vs WebSockets in 45s · "why can't the server just remember me?" — stateless auth.

**Day 17 — "Why production agents are state machines (LangGraph + the kill test)"**
Money moment: kill the process mid-run; restart; the agent resumes from its checkpoint exactly where it died.
Talk: what the Day-10 while-loop cannot express; checkpoints = durability + time-travel debugging; interrupts make human approval first-class; you already built the engine — this is the transmission.
Keep: porting pains (the loop resisting graph shape); the first successful resume reaction.
Shorts: the kill test (crash it, resume it) · agents as state machines whiteboard · human-in-the-loop: my agent asks permission now.

**Day 18 — "Two agents argued and my report got better (orchestration + critic)"**
Money moment: the Critic rejecting a draft against the rubric, forcing a revision cycle, and the revised draft scoring higher.
Talk: when multi-agent is over-engineering (say it plainly); plans as typed objects, never prose; reflection costs a full LLM call — spend it where quality pays; orchestrator routes, it does not work.
Keep: state-schema collisions between agents; a reflection loop that wanted to run forever until you capped it.
Shorts: my AI critic rejected my AI writer's draft · "when NOT to use multi-agent" (the contrarian short) · plans are objects, not paragraphs.

**Day 19 — "MCP: I plugged MY tools into Claude Desktop"**
Money moment: your own memory/RAG tools appearing and working inside Claude Desktop — a product you didn't write, using your code.
Talk: the M×N problem and the USB analogy; tools vs resources vs prompts; an MCP server runs with YOUR permissions — treat installs like installing software, because it is; weekly code-reading payoff (you read the SDK before building on it).
Keep: transport confusion (stdio vs HTTP) if it bites; the Claude-Desktop-sees-my-tools reaction.
Shorts: my tools inside Claude Desktop (the wow clip) · MCP is USB for AI · "would you pip install a random MCP server?" — the trust talk.

**Day 20 — "My agent browses the web now (Playwright, from a tester's hands)"**
Money moment: the morning-scout digest — three real sites visited, one clean summary produced.
Talk: why Playwright doesn't flake (auto-wait) — your testing past vouching on camera; locator hierarchy (role/text > test-id > CSS >> XPath); high-level task tools vs letting an LLM click anything; ethics: rate limits, ToS, no credential games.
Keep: a selector that broke and the sturdier one that replaced it; watching the browser drive itself the first time.
Shorts: my AI reads three sites before I wake up · why role-based locators survive redesigns · "should an LLM be allowed to click anything?".

**Day 21 — "My AI reads my inbox (and is not allowed to send anything)"**
Money moment: inbox triage — real unread mail classified, top replies drafted, everything waiting on YOUR approval. Nothing sends itself.
Talk: OAuth as the hotel key-card (scoped, expiring, revocable); drafts-only as the bootcamp's most important safety decision; shell tools with allow-lists and argument arrays — `shell=True` never; Week-3 architecture review.
Keep: the OAuth consent dance in full (everyone fumbles it once); the first drafted reply and your genuine reaction to its quality.
Shorts: my agent drafts, only I send · OAuth explained with a hotel key-card · the one subprocess mistake that's an injection hole.

### Week 4 — Production + Capstone (arc: "the system becomes real, then becomes ONE thing")

**Day 22 — "The job that survived a server crash (Postgres + Redis)"**
Money moment: research job running → kill the API → restart → the job resumes from Redis queue + Postgres checkpoints and finishes.
Talk: SQLite vs Postgres honestly (SQLite wasn't wrong, it was right until now); Postgres = truth, Redis = speed, Qdrant = meaning; transactions/ACID via "two agents writing memory at once"; EXPLAIN before/after an index — the number drops on screen.
Keep: the Alembic migration written and run live; the crash-and-resume demo raw, first take.
Shorts: I killed my server mid-job and it finished anyway · the three-database rule (truth/speed/meaning) · one index, query time before/after.

**Day 23 — "One command boots my entire AI OS (Docker Compose)"**
Money moment: wipe local state → fresh `git clone` → `docker compose up` → chatting with AIOS. The new-laptop test, on camera.
Talk: containers vs VMs in one diagram; layer caching (why pyproject.toml copies first); non-root, healthchecks, and why the API must wait for Postgres; the image-size shrink as a mini-story.
Keep: the first compose race condition (API up before DB); the 2GB image and its diet.
Shorts: fresh laptop → running AI OS in one command · why your Docker build is slow (layer order) · 2.4GB → 300MB image shrink.

**Day 24 — "Push a tag, watch it deploy (CI/CD for an AI system)"**
Money moment: `git push --tags` → Actions pipeline runs (lint → types → tests → build) → the live URL updates. HTTPS via Caddy.
Talk: CI for non-deterministic systems — the smoke-eval job that fails builds on prompt regressions; branch protection for a solo dev (yes, really — it's where CI gates live); rollback = the previous image tag, kept warm; reverse proxy micro-lesson.
Keep: the deliberately broken build and its fix; the first deploy to the public internet — full reaction.
Shorts: my CI runs AI quality checks, not just tests · deploying by pushing a tag · "solo devs don't need PRs" — wrong, here's why.

**Day 25 — "Seeing inside the machine (traces + the eval suite)"**
Money moment: a full agent run as a Langfuse trace waterfall — every LLM call, tool call, token count, rupee cost, laid bare. Then: a prompt change measured against 30 eval cases, verdict by numbers.
Talk: debugging agents without traces is archaeology; LLM-as-judge and its biases (calibrate against your own labels); evals = regression testing's AI-native form — the Day-6 question, finally answered in full; prompt caching layout cutting input cost; cost-per-feature honesty.
Keep: the trace that exposes a call you didn't know was happening (there's always one); the eval that fails and is RIGHT to fail.
Shorts: what one agent request actually costs (trace on screen) · "how do you test an AI?" part 2 — evals · the LLM judge that grades my agents nightly.

**Day 26 — "Capstone begins: assembling AIOS from 25 days of parts"**
Money moment: streamed chat through the FULL production stack (compose, Postgres, gateway, tracing) — then restart everything and resume the same conversation, memory intact.
Talk: assembly, not rebuilding — every import today was built on a numbered day (say which, on camera); intent routing (chat vs task); the state schema designed FIRST and why Day 27 depends on it.
Keep: integration friction — two modules that never met before disagreeing; the schema whiteboard session in full.
Shorts: 25 days of parts becoming one system (montage over architecture diagram) · the restart-and-remember demo · "assemble, don't rebuild".

**Day 27 — "My AI writes code, runs it in a cage, and fixes its own bugs"**
Money moment: "analyze this CSV and chart the trend" → generated code fails → agent reads the error → fixes it → chart appears. The self-correction loop, uncut. Plus: agent-written escape attempts (network call, file escape, infinite loop) all dying against the sandbox.
Talk: why `exec()` is never the answer; the containment layers one by one; the generate→run→observe→fix loop is the magic AND the risk — the sandbox is why you're allowed to enjoy it.
Keep: every sandbox escape attempt and its containment log; the first successful self-correction, unedited.
Shorts: my AI fixed its own bug (the loop, uncut) · I let my AI try to escape its sandbox · why exec() on AI code ends careers.

**Day 28 — "One approval screen runs my digital life (and survives an attack)"**
Money moment: "check my inbox, draft urgent replies, calendar the meeting" → triage → drafts → calendar proposal → ONE approval screen → executed. Then injection red-team round 2: malicious email instructions hit the gate and die.
Talk: every side-effect through the gate — autonomy is earned by eval history, not granted by optimism; the OS exposed via MCP (your assistant available inside other tools); the scheduled morning briefing as first taste of true autonomy.
Keep: round-2 attack in full, mirror of Day 14 at system scale; the deliberately ugly approval page (own it on camera — "Week 5 fixes this properly").
Shorts: one approval screen, three automations · attacking my own AI, round 2 · my AI briefs me every morning (cron + drafts).

**Day 29 — "Hardening day: evals green, docs written, v1.0 tagged"**
Money moment: the wall of green — CI passing, eval suite passing, coverage on the critical path — and the `v1.0` tag pushed.
Talk: runbook thinking (start, stop, backup, rotate, common failures); architecture.md as 29 days of WHY, written down; Week-4/system-wide architecture review (100/1k/100k users — with real answers now); every hardening choice is an interview story — say them aloud.
Keep: an eval gap found today and closed today; writing docs on camera (nobody shows this; you should).
Shorts: what a runbook is and why grown-up systems have one · my system's honest answer to "what breaks at 1,000 users" · tagging v1.0 — the click.

**Day 30 — "AIOS v1.0 is LIVE (30-day monthly review)"**
Money moment: the Day-24 pipeline deploying v1.0 + the scripted 5-minute demo: problem → architecture → live flows → safety story.
Talk: the monthly review ON CAMERA — this video doubles as the §7.2 written review: skills gained (AI concepts, software engineering, and honestly, what's still shaky), portfolio value, interview readiness, GitHub/YouTube/LMS output totals; the retro ("what I'd redesign" — highest-signal content of the series); the road past Day 30.
Keep: the retro, fully honest — including anything that still embarrasses you about the codebase.
Shorts: 30 days, one AI OS — the montage · 3 things I'd redesign · "am I an AI engineer now?" (the honest answer).

### Week 5 — Frontend Track (arc: "the vibe coder learns React for real, on camera")

**Day 31 — "Confession: I shipped React apps without knowing React. Day 1 of fixing that."**
Money moment: the confession itself (this is the week's hook and one of the series' most human clips) + first fully-typed component tree rendering the static chat UI.
Talk: vibe coding got products shipped and left a debt — name it without shame; UI = f(state) as the one idea; JSX compiled output shown once, demystified forever; Tailwind utilities while laying out the chat shell; same event-loop concept as Day 4, new runtime.
Keep: the confession unedited; TS errors and reading them properly (they're a curriculum, not an obstacle); first flexbox fight.
Shorts: "I shipped React apps without knowing React" (the honest hook — will travel) · JSX is just function calls · UI = f(state) in 45s · Tailwind: why classes in HTML isn't the crime you think.

**Day 32 — "My React app logs into MY backend (state, effects, CORS pain)"**
Money moment: login page → JWT from your own Day-16 endpoint → real conversation list renders. And the CORS error arriving on schedule, then defeated with understanding.
Talk: state vs props vs derived; effects synchronize with external systems — they are not "on load" hooks; the dependency array honestly; index-as-key corruption demo; JWT storage trade-offs said plainly; the typed api/ module = one door to the backend.
Keep: the CORS preflight error IN FULL — from red console to CORSMiddleware to understanding why; the first infinite effect loop (a rite of passage).
Shorts: CORS finally explained (the eternal-demand short) · the index-as-key bug, demonstrated · infinite useEffect loop — why it happens · memory inspector: my AI shows what it knows about me.

**Day 33 — "Streaming AI tokens into the browser (the hook EventSource can't write)"**
Money moment: assistant tokens streaming live into the chat UI, markdown rendering as they land, stop button aborting mid-stream.
Talk: why native EventSource can't send auth headers and what to do instead (fetch streams + TextDecoder); batching token updates or re-render storms; optimistic UI; then TanStack Query arrives and you name exactly which hand-written pain from yesterday it deletes.
Keep: the re-render storm BEFORE the batching fix (show the jank); the AbortController zombie-stream bug if it bites.
Shorts: streaming AI into the browser (the visual) · EventSource's dirty secret (no auth headers) · the setState-per-token mistake · "server state is not client state" — why Query exists.

**Day 34 — "I approved my AI's email from my phone (AIOS UI ships)"**
Money moment: the phone. Login on mobile → pending approval card → the agent's drafted email → tap approve → it executes. Filmed on the phone, over the shoulder.
Talk: client-side route guards are UX — the API is the security (say it twice); mobile-first Tailwind matching your product philosophy; vite build → static files → Caddy → the same one-command compose boots backend AND frontend; dark mode because it's YOUR OS.
Keep: the Lighthouse findings and the fixes; the updated new-laptop test end-to-end; the phone clip raw, first take if possible.
Shorts: approving my AI's email from my phone (series finale clip) · client route guards aren't security · one command now boots everything · dark mode in 20 minutes.
**Plus (per v1.2):** schedule the "closing the vibe-coding loop" session — opening the real Bytesfer product codebase with new eyes, fixing one real bug — as a bonus episode. Arguably the most valuable video of the series for other vibe-coders, which in 2026 is a very large audience.

---

## 7. Weekly & Monthly Reviews

### 7.1 Weekly review (publish on Days 7, 14, 21, 29, 34 — as video segment + written post)
Generation prompt (paste-ready; attach the week's journal entries + `git log` + repo stats):
```text
From the attached week of journals and git history (no invention), produce my
weekly review: 1) Engineering lessons (top 5, concrete). 2) Architecture
evolution — what the diagram looked like Monday vs today, and what forced each
change. 3) Repository growth — modules added, test count, LOC (report, don't
worship). 4) Technical debt honestly listed with a paydown plan. 5) Future
improvements queued. 6) Best bugs fixed — top 3 with root causes. 7) Most
important commits — 5, with why they mattered. Format: one LinkedIn-ready
post + one expanded README/docs section.
```

### 7.2 Monthly review (Day 30; second edition after Day 34)
Covered on camera per the Day-30 entry; written version generated with:
```text
From 30 days of journals, git history, and the eval-suite history, produce the
monthly review: skills learned (AI engineering / software engineering /
and after Day 34, React) each rated honestly [solid / working / shaky];
concepts mastered vs merely met; portfolio value (what AIOS demonstrates to an
employer or client, in their words); interview readiness against the Appendix-B
question list — which I can answer from experience now; GitHub growth; content
totals (videos, LMS lessons, posts, shorts); what I'd redesign; the next-90-days
plan. No inflation: "shaky" stays "shaky".
```

---

## 8. Channel, Playlist, and Distribution Strategy

- **YouTube = Channel A** (per your existing dual-channel plan — Channel A launches first, and this series IS the launch). Playlist: **"Building AIOS — 34-Day AI Engineering Bootcamp."** Naming: `Day N — <title>`. The Day-1 short doubles as the channel trailer.
- **BytesferLMS**: each lesson publishes as `AI Bootcamp → Module N`, with video embed + repo permalink + runnable exercises. By Day 34 the AI Bootcamp course slot holds 34 real modules — inventory for the B2C track and proof-of-curriculum for institute (B2B) conversations. Certificate criteria per lesson (§4.2) roll up into a course certificate.
- **LinkedIn** (primary channel): the daily build log, evenings, plus the weekly review. Consistency beats reach for 34 days; the compounding is the point.
- **X**: daily thread; flagship days (10, 14, 17, 19, 27, 28, 34) deserve extra care — those are the discovery vehicles.
- **Shorts/Reels**: batch-cut Sundays from OBS markers; cross-post YouTube Shorts ↔ Instagram Reels unchanged. Seeds in §6 are a menu, not a quota — 150+ seeds exist across the map; cut the ones reality blessed.
- **Cross-linking discipline:** every artifact links the other three (video ↔ LMS lesson ↔ repo tag ↔ post). The funnel is: short → video → LMS lesson → BytesferLMS signup. That last hop is the business.

---

## 9. Final Deliverables (Definition of Done for V2.0)

By end of Day 34, all of the following exist and interlink:
- ✅ AIOS v1 — backend, multi-agent system, React frontend — deployed, Dockerized, CI/CD'd, documented (v1.2's deliverables, untouched)
- ✅ GitHub: 34 milestone commits/PRs, tagged releases, progress README, architecture docs
- ✅ 34 devlog videos (Mode A) or full recordings + ≥15 edited videos (Mode B), in one playlist
- ✅ 34 LMS lessons live in BytesferLMS's AI Bootcamp course, each with objectives, exercises, quiz, assignment, certificate criteria
- ✅ 34 LinkedIn build logs + 5 weekly reviews + 1 monthly review (2 after Day 34)
- ✅ 34 X threads
- ✅ 150+ shorts seeds banked; ≥25 shorts published
- ✅ One workflow, no separate work: every deliverable derived from the session's journal + recording + git log

**The identity output, which is the real deliverable:** a public, timestamped, verifiable record that you designed, built, secured, evaluated, deployed, and taught a production multi-agent system — start to finish, mistakes included. That record is simultaneously a portfolio, a channel, a course catalog, and the most credible sales asset Bytesfer's training business can own.

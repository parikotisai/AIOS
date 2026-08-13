# SDET Overlay v1 — Days 5–60 + Post-60 Job-Readiness Track

**Version:** v1.0 — 2026-08-13
**Status:** ACTIVE overlay. This document does not replace anything.

---

## 1. Purpose

Make Sai genuinely job-ready for an SDET / QA Automation / AI-SDET role
by layering professional testing skills onto the existing 60-day AIOS
curriculum — without changing what gets built.

Three connected outcomes this overlay serves:

1. **SDET career** — job-ready within the 100-day learning program.
2. **Code Visualizer** — finished as a real, tested product (future
   BytesferLMS integration).
3. **AIOS/JARVIS** — the eventual AI engineering capstone, tested like
   a professional AI system.

## 2. Relationship with the existing AIOS curriculum

- `docs/curriculum/60-day-master-syllabus.md` + Docs 00–10 remain the
  **build source of truth** — WHAT WE BUILD. Unchanged.
- This overlay is the **learning/testing source of truth** — WHAT SAI
  LEARNS AND PRACTICES AS AN SDET ALONGSIDE THE BUILD.
- Days 1–4 are complete and are NOT retrofitted. The overlay begins at
  **Day 5**.
- Day numbers here always refer to the existing AIOS day numbers.
  Nothing is renumbered, reordered, or removed.
- The SDET layer normally takes **~30–45 focused minutes** inside the
  existing ~3 focused hours/day. It attaches to the day's real build
  work — it is not a separate lecture track.
- If this overlay ever appears to conflict with an AIOS curriculum doc,
  the AIOS doc wins for build content; this overlay wins for testing
  practice; and the conflict gets reported, not silently resolved.

## 3. SDET learning principles

1. **Test thinking before implementation.** Before building a feature:
   what is the expected behavior? What could go wrong? Happy paths,
   negative paths, edge cases, boundaries, risks — then build.
2. **The evaluator is the laboratory.** Every feature Sai builds is
   also the system under test. Nothing artificial is imported just to
   have something to test.
3. **Progressive tooling.** pytest, Playwright, CI, etc. are introduced
   only when the build genuinely needs them, one small piece at a time.
   Never the whole framework in one day.
4. **Tests must prove themselves.** A test that cannot fail is not a
   test. Regularly break the code on purpose and watch the suite go red.
5. **Why before how.** Every technique (parameterization, POM,
   fixtures, schema validation) is learned with its motivating problem
   first. Memorized commands don't survive interviews.
6. **Everything becomes portfolio evidence.** Test suites, eval
   results, kill tests, and injection audits are recorded as artifacts
   a hiring manager can be shown.
7. **Sai writes the tests.** Claude teaches, reviews, and challenges;
   Sai types. Per the AI Assistance principle in CLAUDE.md.

### The standard SDET workflow (Day 5 onward, for every meaningful feature)

1. Understand the feature → 2. expected behavior → 3. what could go
wrong → 4. happy paths → 5. negative paths → 6. edge cases →
7. boundaries → 8. equivalence classes (where useful) → 9. risks →
10. expected results → 11. implement → 12. test → 13. automate what's
worth automating → 14. run regression → 15. debug failures →
16. explain what was tested and why.

Not every day exercises all 16 steps — but the order of thinking never
changes.

---

## 4. Days 5–16 overlay — Python Evaluator + SDET Foundation

The evaluator (`tracer.py` → backend) is the first serious software
component. It is the SDET laboratory for this whole phase.

### Day 5 — First evaluator + first test thinking

- **Existing AIOS focus:** evaluator handles plain assignment
  (`x = 5`); trace steps with copied variable snapshots.
- **SDET objective:** understand what software testing *is*.
- **Concepts:** expected vs actual · assertion · test scenario vs test
  case · happy path vs negative path · why the copy-vs-reference bug in
  Doc 01 is exactly what a test exists to catch · pytest introduced
  *conceptually only* (a program that runs your assertions and reports
  red/green).
- **Practical activity:** before running `tracer.py`, write down on
  paper: for input `x = 5\ny = 3`, what exactly should the trace
  contain? (expected result first, run second). Then ask: what inputs
  would break today's evaluator? (`y = x` before x exists; empty code;
  `x = 5 + 3` — unsupported until Day 6).
- **Expected artifacts:** a written expected-vs-actual table for the
  two-line program; a list of at least 3 "what could go wrong" inputs;
  the smallest useful test when appropriate (even a plain `assert` in a
  script counts today).
- **Done when:** Sai can explain, unprompted: the difference between a
  test scenario ("assignment updates variables") and a test case
  ("input `x = 5`, expect step 1 variables == `{'x': 5}`"), and why the
  Day 5 curriculum's snapshot-copy check is really a regression test.
- **Interview relevance:** "What is testing?" / "Expected vs actual" —
  the first question of every QA interview.

### Days 6–7 — Arithmetic + data types

- **Existing AIOS focus:** evaluator handles `+ - * /`, strings, lists,
  dicts, indexing.
- **SDET objective:** design test inputs systematically instead of
  randomly.
- **Concepts:** positive/negative cases per node type · **equivalence
  partitioning** (all "simple additions" behave alike — test one per
  class, not fifty) · **boundary-value thinking** (0, negative numbers,
  empty string, empty list, index 0, last index, index out of range,
  missing dict key) · division edge cases (÷ by zero, non-integer
  results) · pytest for real now: a test file, `assert`, running the
  suite — parameterization when the same test repeats over many inputs
  naturally invites it.
- **Practical activity:** build a test-input table for `eval_expr`:
  columns = input snippet, class (happy/negative/boundary), expected
  result or expected error. Then implement the highest-value rows as
  pytest tests against the evaluator.
- **Expected artifacts:** first real pytest file(s) for the evaluator;
  the input-design table in the day's notes.
- **Done when:** the suite passes; at least one test asserts an
  *error* is raised (negative path); Sai can explain why testing
  `2 + 3` and `4 + 5` both adds no value but `x[len(x)]` does.
- **Interview relevance:** equivalence partitioning and BVA are asked
  by name in nearly every manual + automation interview.

### Days 8–9 — if/else, comparisons, boolean operators

- **Existing AIOS focus:** evaluator handles `Compare`, `BoolOp`,
  if/else branch walking.
- **SDET objective:** branch-oriented test design.
- **Concepts:** true branch vs false branch — both must be tested ·
  branch coverage as an idea (every branch executed at least once by
  some test) · boundary cases on comparisons (`x > 3`: test 2, 3, 4 —
  the boundary and both sides) · truth tables for `and`/`or` · negative
  cases (comparing incompatible things).
- **Practical activity:** for `if x > 3:` write the 3-value boundary
  test set before implementing; for `x > 0 and y < 10` enumerate the
  four true/false combinations and pick the minimum set that exercises
  both operators.
- **Expected artifacts:** pytest tests covering both branches of an
  if/else, at least one boundary triple, at least one `and`/`or` combo.
- **Done when:** deliberately inverting one comparison operator in the
  evaluator makes at least one test fail (proof the branch tests bite).
- **Interview relevance:** "How would you test an if condition?" and
  decision/branch coverage questions.

### Day 10 — while loops (single iteration)

- **Existing AIOS focus:** while loop runs exactly once correctly.
- **SDET objective:** loop-oriented test design.
- **Concepts:** the classic loop test set — **zero iterations, one
  iteration, many iterations** · termination behavior · the
  infinite-loop risk (what should an evaluator do about `while True:`?
  — a genuine design/risk conversation, foreshadowing Day 48's loop
  guards) · regression tests: everything from Days 5–9 must still pass.
- **Practical activity:** write the zero-iteration test (condition
  false on entry — body must never appear in the trace) and the
  one-iteration test; note the many-iteration test as a known gap that
  Days 11–12 will close.
- **Expected artifacts:** loop tests in pytest; a noted risk entry
  about infinite loops in the day's notes.
- **Done when:** zero- and one-iteration tests pass; full suite from
  earlier days still green.
- **Interview relevance:** "How do you test a loop?" — the 0/1/many
  answer is expected verbatim.

### Days 11–12 — Multi-iteration loops

- **Existing AIOS focus:** loops fully correct across N iterations.
- **SDET objective:** regression protection + test organization.
- **Concepts:** loop boundary tests (exactly N, N−1, N+1 expectations
  in the trace) · why repeated execution amplifies state bugs (the
  snapshot-copy bug from Day 5 would be catastrophic here) · organizing
  a growing pytest suite: file naming, one behavior per test,
  arrange-act-assert shape, descriptive test names as documentation ·
  what a **regression suite** is and why it runs on every change.
- **Practical activity:** the 5-iteration loop test from the
  curriculum's done-when, written as a test first; reorganize test
  files if they have become a pile.
- **Expected artifacts:** a tidy, named test suite that covers
  assignment, arithmetic, data types, if/else, and loops; all green.
- **Done when:** Sai can point at the suite and say which tests are
  the regression safety net for which evaluator feature.
- **Interview relevance:** "What is regression testing and when do you
  run it?" · test naming/organization comes up in automation code
  reviews at interviews.

### Days 13–16 — Function calls, call stack, recursion

- **Existing AIOS focus:** frames pushed/popped, local variables,
  return values; Day 16 recursion checkpoint (the hardest checkpoint in
  Phase 1).
- **SDET objective:** testing stateful, structurally complex behavior;
  first fixtures; error-handling tests.
- **Concepts:** testing call/return events and `call_stack` contents ·
  local vs global variable assertions · recursion tests as the ultimate
  regression test (factorial(3): assert exact push/pop order) · pytest
  **fixtures** where justified (e.g. a helper that runs code through
  the evaluator and returns the trace — used by nearly every test now)
  · parameterized tests across many snippets · negative testing for
  whatever error handling the curriculum introduces here (calling an
  undefined function, wrong argument count).
- **Practical activity:** before implementing frames, answer as a
  tester: "what would prove the call stack is wrong?" (same variable
  name `n` at two levels showing the wrong value is the classic). Turn
  those answers into tests as the feature lands.
- **Expected artifacts:** structured pytest suite with a shared
  run-the-evaluator helper/fixture; recursion trace test; at least two
  negative tests; everything earlier still green.
- **Done when:** the recursive factorial test asserts the full
  push/pop sequence and passes; breaking frame-pop logic on purpose
  turns it red.
- **Interview relevance:** fixtures and parameterization are the two
  pytest features every Python-SDET interview probes; "how would you
  test recursive code" is a strong differentiator answer.

---

## 5. Days 17–20 overlay — API, UI, and Deployment Testing

### Days 17–18 — Real backend wiring → API testing begins

- **Existing AIOS focus:** `/trace` accepts real code via POST, returns
  the JSON trace; syntax errors return a clear error, not a crash.
- **SDET objective:** professional API testing fundamentals.
- **Concepts:** HTTP request/response anatomy · GET vs POST (and why
  `/trace` becomes POST) · status codes (200 vs 4xx vs 5xx — what
  *should* bad code return?) · request validation · response
  validation · JSON structure/schema validation (every step must have
  `step/line/event/changed/variables` — the project's own schema is the
  contract) · positive API tests · negative API tests: malformed
  request body, empty body, empty code string, invalid Python,
  unsupported-feature code, very large snippet (boundary) · API
  regression suite.
- **Practical activity:** using the project's natural tooling (e.g.
  FastAPI's test client / `requests`-style calls — no unrelated tools),
  build an API test suite that mirrors the pytest evaluator suite but
  through the HTTP boundary.
- **Expected artifacts:** API test suite: ≥5 positive cases (assign,
  if/else, while, function call, recursion) and ≥4 negative cases
  (malformed JSON, empty code, syntax error, unsupported feature), each
  asserting both status code and body shape.
- **Done when:** invalid Python returns a controlled error response
  (asserted by a test), and the server provably never 500s on bad user
  code.
- **Interview relevance:** status codes, GET vs POST, and "how do you
  test an API negatively" are guaranteed interview questions.

### Days 19–20 — Real frontend + live deployment → test strategy begins

- **Existing AIOS focus:** real React UI (editor, Run, step controls,
  variables panel, line highlight) + public deployment.
- **SDET objective:** think in test strategy, not just test cases.
- **Concepts:** **smoke testing** (the 5-minute "is it fundamentally
  alive" pass) vs regression testing · **critical user journeys** (type
  code → Run → step through → see variables: the journey that must
  never break) · test data thinking (which snippets make good standing
  test data and why) · basic test strategy (what gets tested manually
  now, what gets automated in Phase 2, and why UI automation waits for
  Playwright) · basic defect reporting: title, steps to reproduce,
  expected, actual, severity — practiced on any real bug found today ·
  **environment differences** (localhost vs deployed: CORS, URLs, cold
  starts) · deployment smoke test: the short checklist run against the
  public URL after every deploy.
- **Practical activity:** write a manual smoke-test checklist
  (5–8 steps) and execute it against localhost AND the deployed URL;
  log any real bug found as a proper defect report in the notes.
- **Expected artifacts:** smoke checklist in the day's notes (it
  becomes the Phase 2 automation backlog); at least one practice defect
  report; a one-paragraph test strategy for the app as it stands.
- **Done when:** the deployed app passes the smoke checklist, and Sai
  can explain which checklist items should become automated tests and
  which are not worth automating.
- **Interview relevance:** smoke vs sanity vs regression, defect
  report structure, and "how do you decide what to automate" — all
  core interview material.

---

## 6. Days 21–30 overlay — Playwright / Core SDET Automation

This is the major SDET automation phase. Everything here is directly
job-oriented: the WHY of each technique matters more than the command.

### Days 21–22 — First Playwright test

- **Existing AIOS focus:** install Playwright; page-load test passes.
- **SDET objective:** understand what UI automation actually is.
- **Concepts:** browser / context / page (the three-level model) ·
  locators (role/text/test-id — and why brittle CSS selectors are a
  known failure mode) · web-first assertions (auto-waiting: why
  Playwright asserts differ from plain asserts) · test structure ·
  headless vs headed · running and reading test output.
- **Expected artifacts:** the page-load test, written by Sai, with each
  line explainable.
- **Done when:** `npx playwright test` passes AND Sai can explain what
  a locator is and why auto-waiting exists (the flakiness problem it
  solves).
- **Interview relevance:** "Explain Playwright's architecture" and
  "why Playwright over Selenium" openers.

### Days 23–24 — Page Object Model

- **Existing AIOS focus:** `CodeVisualizerPage` class; test uses only
  page-object methods; breaking Run makes the test fail.
- **SDET objective:** maintainable automation architecture.
- **Concepts:** Page Object Model — the problem it solves (UI change =
  one class edit, not fifty test edits) · encapsulation of selectors ·
  actions vs assertions placement · test isolation (each test starts
  from a clean page; no test depends on another) · fixtures in
  Playwright (setup/teardown of the page object).
- **Practical activity:** the deliberate-defect ritual: break the Run
  button, watch red; fix, watch green. This ritual now becomes standard
  for every automated suite.
- **Expected artifacts:** `CodeVisualizerPage`; a test file with zero
  raw selectors; notes on which selectors were chosen and why.
- **Done when:** the curriculum's done-when passes AND Sai can defend
  POM to a skeptic ("why not just put selectors in the test?").
- **Interview relevance:** POM is the single most-asked automation
  design question.

### Days 25–26 — Correctness test → data-driven testing

- **Existing AIOS focus:** UI correctness test (`y = 8` shown), then
  generalized over a list of `(code, expected)` pairs including edge
  cases.
- **SDET objective:** data-driven testing done properly.
- **Concepts:** parameterization/data-driven structure · choosing test
  data as equivalence classes (normal, string/list, edge: empty list,
  non-integer division, always-false branch) · positive + negative +
  edge in one table · one-line cost of adding a case as the measure of
  good design.
- **Expected artifacts:** the data-driven suite; the case table
  documented in notes with each case's class labeled.
- **Done when:** curriculum done-when passes AND every case in the
  table can be justified ("what bug would this case catch that the
  others wouldn't?").
- **Interview relevance:** data-driven frameworks and test-data design
  are standard mid-level SDET questions.

### Day 27 — Backend-only tests + the test pyramid

- **Existing AIOS focus:** ≥5 direct `/trace` tests, no browser.
- **SDET objective:** layering — where each kind of test belongs.
- **Concepts:** the test pyramid (many fast API/unit tests, fewer UI
  tests) · speed/stability/cost trade-offs · when a UI test is the
  wrong tool · API + UI covering the same behavior at different layers
  on purpose.
- **Expected artifacts:** the backend suite; a short notes entry
  mapping the project's tests onto the pyramid.
- **Done when:** Sai can answer: "the arithmetic logic is already
  API-tested — why keep any UI test for it at all?" (answer: the UI
  test covers wiring/display, not arithmetic).
- **Interview relevance:** the test pyramid is a guaranteed strategy
  question.

### Day 28 — Prove the tests work (mutation thinking)

- **Existing AIOS focus:** deliberately break the evaluator; suite
  must go red.
- **SDET objective:** test effectiveness over test count.
- **Concepts:** deliberate defect seeding (informal mutation testing) ·
  silent-pass as the worst failure mode of a test suite · debugging a
  failing test: read the error, reproduce, isolate — screenshots and
  traces (`--trace on`) where useful · flaky vs genuinely failing.
- **Expected artifacts:** notes recording each seeded defect, which
  test caught it, and any defect NO test caught (each of those becomes
  a new test).
- **Done when:** at least 3 different seeded defects each turn some
  test red; any uncaught defect has a new test written for it.
- **Interview relevance:** "How do you know your tests are any good?"
  — this day is the answer.

### Days 29–30 — CI + cross-browser

- **Existing AIOS focus:** GitHub Actions on every push; Chromium +
  Firefox projects.
- **SDET objective:** automation that runs without a human.
- **Concepts:** CI concepts (trigger → job → steps → status) · CI as a
  quality gate (red = don't merge) · cross-browser reasoning (what
  actually differs between engines; what cross-browser bugs look like)
  · smoke vs regression suites in CI (fast subset per push vs full
  suite) · flaky tests in CI: detection, quarantine idea, why retries
  hide problems · reporters and artifacts (HTML report, traces on
  failure).
- **Expected artifacts:** the workflow file (written and explainable
  line by line); a green check on a real commit across 2 browsers;
  notes distinguishing this repo's smoke set from its full regression
  set.
- **Done when:** curriculum done-when passes AND Sai can explain what
  happens, step by step, from `git push` to green checkmark.
- **Interview relevance:** "Describe your CI pipeline" — every SDET
  interview, without exception.

---

## 7. Days 31–45 overlay — AI Engineering + AI-SDET

The existing AI Engineering curriculum remains the primary build. The
overlay turns its artifacts into explicit AI-testing skill and
portfolio evidence.

### Days 31–33 — First LLM API call

- **Existing AIOS focus:** send one trace step to an LLM; get a
  one-sentence explanation.
- **SDET objective:** understand why testing AI differs from testing
  code.
- **Concepts:** non-determinism (same input, different output — what
  does "expected result" even mean now?) · properties vs exact values
  (can't assert the sentence; CAN assert: non-empty, one sentence,
  mentions the changed variable, no code fences) · prompt as test
  input: positive prompts, negative/weird prompts (empty step, huge
  variables dict) · failure paths: API errors, timeouts — what should
  the app do?
- **Expected artifacts:** a written list of assertable properties for
  the explain feature; manual test log of ≥3 step types + ≥2 weird
  inputs.
- **Done when:** Sai can explain the shift from exact-match assertions
  to property-based assertions and why it's forced here.
- **Interview relevance:** "How do you test something
  non-deterministic?" — THE AI-SDET differentiator question.

### Days 34–36 — Explain button wiring

- **Existing AIOS focus:** button works for every step type in a full
  recursive trace.
- **SDET objective:** systematic coverage of AI-feature inputs.
- **Concepts:** input-space coverage by step type (assign, call,
  return, loop_check, condition, print) as equivalence classes ·
  hallucination-oriented checks (does the explanation mention variables
  that don't exist in the step?) · UI failure paths (API down mid-click
  → user sees what?).
- **Expected artifacts:** a per-step-type test log; automated checks
  where deterministic properties allow.
- **Done when:** every step type has been exercised and any
  wrong/hallucinated explanation is recorded as a defect with its
  input.
- **Interview relevance:** demonstrates AI test-coverage design by
  input class.

### Days 37–39 — Structured output generation

- **Existing AIOS focus:** "bubble sort" → JSON matching a Pydantic
  schema (`code`, `algorithm_name`, `uses_features`) → into the editor.
- **SDET objective:** structured output validation — the heart of
  AI-SDET.
- **Concepts:** JSON/schema validation as the assertable contract with
  an LLM · schema-validation failure as a first-class test case (not an
  exception to ignore) · prompt test cases: positive ("bubble sort"),
  negative ("delete my hard drive", empty string, non-algorithm
  request), edge (ambiguous: "sort") · `uses_features` cross-checked
  against what the evaluator actually supports (a machine-checkable
  honesty test of the AI's own claim) · retry/reject behavior on
  invalid JSON.
- **Expected artifacts:** schema-validation tests; a prompt test-case
  table (positive/negative/edge) with observed behavior; defect entries
  for any schema violation.
- **Done when:** curriculum done-when passes AND an invalid/hostile
  request provably cannot inject unvalidated content into the editor.
- **Interview relevance:** structured output + schema validation is
  the most concrete, demonstrable AI-testing skill on the market.

### Days 40–42 — Self-correct retry loop

- **Existing AIOS focus:** generate → run → fail → feed error back →
  retry; capped at 3; every attempt logged; uncorrectable input fails
  loudly.
- **SDET objective:** failure-path and retry-loop testing.
- **Concepts:** deliberately induced failure as a test technique (ask
  for a feature the evaluator doesn't support) · retry-cap boundary
  testing (succeeds on attempt 2; exhausts 3 and fails safely — both
  must be tested, per the curriculum's own done-when) · log assertions
  (the attempt log is itself an output to validate) · infinite-loop
  risk revisited (Day 10's lesson, now with money on the line — each
  retry costs tokens).
- **Expected artifacts:** tests/logged runs for: first-try success,
  success-on-retry-2, cap-exhausted safe failure, direct-editor bad
  input safe failure.
- **Done when:** all four paths demonstrated and recorded; Sai can
  explain why the cap is a boundary and what the boundary cases are
  (attempts 1, 3, and the never-allowed 4th).
- **Interview relevance:** retry/backoff/failure-path testing is asked
  for any system that calls external services — AI or not.

### Days 43–45 — Eval suite, polish, write-up

- **Existing AIOS focus:** 10–15 fixed algorithm requests through the
  full pipeline; score recorded in the README.
- **SDET objective:** evaluation datasets — AI testing as a
  discipline; portfolio framing.
- **Concepts:** **golden test cases** / evaluation dataset (the fixed
  request list IS one) · deterministic evaluation where possible (the
  evaluator running the generated code is a deterministic oracle — this
  architecture is exactly why the eval suite works) · scoring
  (pass@1 vs pass-after-retry) · **prompt regression testing** (change
  a prompt → rerun the eval suite → compare scores; a score drop is a
  regression) · honest reporting (the real number, not the flattering
  one).
- **Expected artifacts:** the eval suite results in the README as a
  real number; a notes entry framing the suite as AI-SDET portfolio
  evidence; the 3–4 interview sentences from the curriculum, extended
  with one sentence about how the system is *tested*.
- **Done when:** curriculum done-when passes AND Sai can explain, in
  interview language: "I built an evaluation dataset with a
  deterministic oracle and use it for prompt regression testing."
- **Interview relevance:** this is the centerpiece AI-SDET portfolio
  story. Rehearse it.

---

## 8. Days 46–60 overlay — AIOS/JARVIS + Agent Testing

The existing AIOS architecture and build sequence stay intact. The
overlay adds professional agent-testing practice around each day, and
frames the curriculum's built-in safety work (kill test, injection
audit) as deliberate AI-SDET portfolio evidence.

### Day 46 — Tool registry

- **SDET objective:** tool input/output validation; regression across
  refactors.
- **Overlay:** the curriculum's own gate ("Phase 3 tests still pass
  unmodified") *is* a regression test of a refactor — name it as such.
  Add: schema validation tests for the tool interface; a test that a
  read-tagged tool is queryable and an act-tagged tool is gated;
  negative test for registering a malformed tool.
- **Done when:** registry behavior is covered by tests and the
  read/act tag provably changes behavior.

### Day 47 — MCP server

- **SDET objective:** contract testing across a protocol boundary.
- **Overlay:** test your MCP tool with valid and invalid arguments
  from the outside; verify documented behavior matches actual behavior
  (that's a contract test); treat the curriculum's "common mistakes"
  list (god permissions, undocumented side effects) as a security
  review checklist and write the answers down.
- **Done when:** at least one negative test against your own MCP
  server exists, and the permissions question has a written answer.

### Day 48 — Planner/router + loop guards

- **SDET objective:** guard testing — limits are boundaries; boundaries
  get boundary tests.
- **Overlay:** tests for max-iterations trips, max-tool-calls trips,
  spend-cap trips, and the no-matching-tool safe failure (the day's own
  done-when). Router testing: known task → expected tool (a routing
  table is test data). The extended tracer schema
  (`tool_call → result → retry`) gets validation tests like the Phase 1
  step schema did.
- **Done when:** every guard has a test that trips it on purpose.

### Days 49–50 — Browser agent

- **SDET objective:** browser-agent testing; flakiness management at
  agent level.
- **Overlay:** Phase 2 skills reused against an agent: does the
  planner route browser-shaped tasks correctly (positive + negative)?
  What happens when the page changes or an element is missing (failure
  path)? For the morning-scout digest: define what "correct digest"
  means BEFORE running it (expected result first), and rerun-stability
  as a flakiness check.
- **Done when:** one failure-path browser test exists and the digest's
  correctness criteria were written before the first full run.

### Days 51–52 — Email/Calendar OAuth + approval gate

- **SDET objective:** security-critical path testing.
- **Overlay:** OAuth failure behavior (deny consent, expired token —
  what does the agent do?) · the draft-never-sends invariant tested
  deliberately (the highest-stakes negative test so far) · approval
  gate: every act-tool tested to require approval; attempt an act
  WITHOUT approval and assert it's blocked (the test that matters most)
  · blast-radius thinking introduced here, not Day 57.
- **Done when:** "no approval → no action" is demonstrated by test for
  every act-tool, and an OAuth failure path has been exercised.

### Days 53–54 — RAG + research tool

- **SDET objective:** retrieval testing.
- **Overlay:** retrieval quality as testable behavior: for a known
  10-doc corpus, queries with known-correct top results = golden
  retrieval cases · negative: query matching nothing (what should top-3
  even mean?) · research tool output is structured JSON → schema
  validation again · source-grounding check (does the synthesis cite
  retrieved docs, or hallucinate?).
- **Done when:** ≥3 golden retrieval cases pass and the research
  tool's output schema is validated by test.

### Day 55 — Checkpointing: the kill test

- **SDET objective:** kill-test methodology as a named, professional
  technique (chaos-style resilience testing).
- **Overlay:** the curriculum's kill test, made systematic: kill at
  *different* points (before/mid/after a tool call), verify resume from
  each · state-file corruption as a negative case (what if the
  checkpoint itself is damaged?) · record each kill point + outcome as
  a table — this table is portfolio evidence.
- **Done when:** resume verified from ≥3 distinct kill points, results
  tabled in notes.

### Days 56–60 — Orchestration, safety audit, capstone

- **SDET objective:** multi-tool orchestration testing; prompt
  injection testing; end-to-end regression.
- **Overlay:**
  - **Day 56:** workflow-level tests — correct 3-step plan for a known
    instruction (planning as assertable output); kill mid-workflow
    resume (Day 55 methodology at orchestration level).
  - **Day 57:** the prompt-injection audit run as a professional
    security test: a written test-case list of injection attempts
    (page-embedded, email-embedded, doc-embedded), each with expected
    behavior "not obeyed," each executed and recorded pass/fail; the
    blast-radius answer written down. This document is first-class
    AI-SDET portfolio evidence — treat it like a deliverable.
  - **Days 58–59:** capstone testing = full regression across every
    tool + the critical journey (research → draft → save → approve →
    send) with the approval gate proven again in situ; integration
    failure paths (curriculum: "multi-agent systems break *between*
    tools") get explicit attention.
  - **Day 60:** the recorded demo doubles as evidence; final regression
    pass across all suites (Phase 1–4) before recording.
- **Done when:** injection test cases are documented with results; the
  capstone passes its critical-journey test; all historical suites are
  green at Day 60.
- **Interview relevance:** kill tests, injection audits, approval-gate
  proofs, and loop-guard tests are exactly what "how would you test an
  AI agent?" wants — and almost no candidate has actually done them.

---

## 9. Post-60-Day SDET Job-Readiness Track

Runs AFTER Day 60. Detailed day-by-day scheduling is deliberately NOT
defined yet — it will be planned once the Day 1–60 overlay is
validated in practice. The track covers the major SDET competencies the
AIOS curriculum doesn't sufficiently cover, grouped into modules:

**Module A — Manual testing & test design fundamentals**
Manual testing fundamentals · SDLC/STLC · test scenarios, test cases,
test conditions · positive/negative testing · smoke vs sanity ·
regression · exploratory testing · risk-based testing · equivalence
partitioning & boundary-value analysis (formalized) · decision tables ·
state transition testing · pairwise testing · defect lifecycle ·
severity vs priority · test planning, test strategy, test estimation.
*(Much of this was practiced informally during Days 5–60; here it gets
the formal vocabulary and interview polish.)*

**Module B — Data & backend testing**
SQL · database testing · API automation (deepened beyond the project's
own API) · mocking/stubbing · test doubles · contract testing.

**Module C — Platform & DevOps**
Linux · Git/GitHub (formalized) · Docker · CI/CD beyond GitHub
Actions basics · cloud testing fundamentals.

**Module D — Specialized testing**
Performance testing (k6/JMeter awareness) · security testing & OWASP
fundamentals · accessibility testing · microservices testing ·
distributed-system testing fundamentals · Kafka/message-system testing
awareness · Selenium awareness/comparison (vs Playwright) · mobile
testing awareness.

**Module E — Engineering maturity**
Observability & log analysis · production debugging · flaky-test
management · automation framework architecture · SDET system design.

**Module F — Interview preparation**
DSA / Big-O for interviews · coding interview prep · SQL interview
prep · manual testing interview prep · automation interview prep · API
interview prep · AI-SDET interview prep · resume/project positioning
(Code Visualizer + AIOS as the portfolio spine) · portfolio
presentation · mock interviews.

---

## 10. SDET competency checklist

Track mastery level (0–6, per CLAUDE.md's Mastery Levels) against each
item. Target Level 5–6 for core items by end of the program.

**Test design:** expected vs actual · scenario vs case · happy/negative
paths · edge cases · boundary-value analysis · equivalence
partitioning · branch thinking · loop testing (0/1/many) · risk-based
prioritization.

**Python test automation:** pytest basics · parameterization ·
fixtures · test organization · negative testing · regression suites ·
deliberate defect seeding.

**API testing:** HTTP fundamentals · status codes · request/response
validation · JSON schema validation · negative API testing · API
regression.

**UI automation:** Playwright fundamentals · locators · web-first
assertions · POM · test isolation · data-driven testing · debugging
with traces/screenshots · flaky-test concepts · cross-browser.

**CI/CD:** GitHub Actions · CI gates · smoke vs regression suites in
CI · reading CI failures.

**AI-SDET:** property-based assertions for non-deterministic output ·
structured output/schema validation · prompt test design ·
hallucination checks · evaluation datasets & golden cases · scoring ·
prompt regression · retry/failure-path testing.

**Agent testing:** tool I/O validation · read vs act tools · router
testing · loop guards & spend caps · approval gates · OAuth failure
paths · retrieval testing · kill-test methodology · prompt injection
testing · blast-radius analysis · multi-tool regression.

**Process:** defect reporting · smoke checklists · test strategy ·
test data design · explaining what was tested and why.

---

## 11. Mastery expectations

- A concept counts as learned only when demonstrated (explain in own
  words, predict output, trace execution, write/modify code, catch a
  seeded defect) — per CLAUDE.md's Adaptive Mastery Mode.
- Core test-design and automation concepts target **Level 5–6**:
  Sai writes the tests independently and can explain, debug, and
  defend them.
- Awareness-tier topics (k6/JMeter, Kafka, mobile, Selenium
  comparison) target **Level 2–3** until the post-60 track deepens
  them.
- The calendar is a target, not a mastery substitute. A day's SDET
  layer that needs another session gets another session; the overlay
  slides with the curriculum's own "slide the calendar" rule.

## 12. Interview / job-readiness expectations

By the end of Day 60, Sai should be able to, out loud, without notes:

1. Explain the test pyramid using this project's own suites as the
   example.
2. Walk through the Playwright framework (POM, fixtures, data-driven,
   CI, cross-browser) as "a framework I built," not "a course I took."
3. Answer equivalence partitioning / BVA / loop testing questions with
   examples from the evaluator.
4. Describe the CI pipeline from push to green check.
5. Tell the AI-SDET story: schema-validated LLM output, a
   deterministic-oracle eval suite, prompt regression, capped
   self-correction — with real numbers from the README.
6. Tell the agent-testing story: loop guards, spend caps, approval
   gates, kill tests, prompt-injection audit, blast radius — with the
   Day 55/57 artifacts as proof.
7. Produce a defect report, a smoke checklist, and a test strategy for
   an unfamiliar app on request.

The post-60 track then closes the remaining gaps (SQL, performance,
security, formal vocabulary, mock interviews) to full job readiness
within the 100-day program.

---

*v1.0 — 2026-08-13 — initial overlay. Changes require a stamped
version bump, same convention as the curriculum docs.*

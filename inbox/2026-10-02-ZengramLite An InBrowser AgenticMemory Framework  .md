---
title: "Zengram-Lite: An In-Browser Agentic-Memory Framework - Semantic Knowledge, Session Tracking, and Token-Budgeted Context"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.00042
priority: low
status: unread
interest: medium
next_step: skim
---
# Zengram-Lite: An In-Browser Agentic-Memory Framework - Semantic Knowledge, Session Tracking, and Token-Budgeted Context
> 原文: [https://arxiv.org/abs/2610.00042](https://arxiv.org/abs/2610.00042)

arXiv:2610.00042v1 Announce Type: new
Abstract: AI agents increasingly run in the browser, and they need somewhere to keep what they learn. The client-side state of the art, however, is a vector index - nearest-neighbor search over embeddings - with the rest of an agent's memory left to application code: the conversation history is an array in localStorage, context management is hand-rolled truncation, and there is no shared notion of a fact's confidence, its provenance, or the session that produced it. We present zengram-lite, an agentic-memory framework compiled to a single ~2.95 MB gzipped WebAssembly artifact that runs entirely in a browser tab. It provides three tiers over one transactional store. The knowledge tier offers hybrid vector-and-full-text recall with a fact lifecycle - confidence that rises and falls as facts are confirmed or contradicted, importance that decays over time, supersession that treats a restated fact as an update, and scope namespacing. The session-tracking tier models the conversation itself as first-class data: sessions, turns, typed content parts, and tool calls with state and timing, all as queryable tables. The context-assembly tier turns that structure into a token-budgeted prompt through a six-phase assembly that packs system instructions, knowledge, and recent history under a caller's budget, and returns a stable fingerprint that signals when a prompt prefix can be reused. The bundle is a superset of the zeta-lite SQL engine - the same .wasm re-exports the full Postgres-compatible surface, MVCC snapshot isolation, and copy-on-write database branching - so memory inherits transactional consistency across all three tiers. Because the wasm surface is synchronous while the framework's canonical operations depend on an asynchronous LLM and embedder, zengram-lite exposes a bring-your-own-result seam that runs the framework's real code paths over results the application computes in JavaScript.

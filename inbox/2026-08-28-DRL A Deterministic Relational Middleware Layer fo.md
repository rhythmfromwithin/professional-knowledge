---
interest: medium
link: https://arxiv.org/abs/2608.26172
next_step: skim
priority: low
slack_ts: '1787986067.100509'
source: cs.DB - Databases
status: unread
title: 'DRL: A Deterministic Relational Middleware Layer for Transaction-Safe Enterprise
  NL2SQL Under Schema-Graph Scaling'
---
# DRL: A Deterministic Relational Middleware Layer for Transaction-Safe Enterprise NL2SQL Under Schema-Graph Scaling
> 原文: [https://arxiv.org/abs/2608.26172](https://arxiv.org/abs/2608.26172)

arXiv:2608.26172v1 Announce Type: new
Abstract: Deploying natural-language interfaces over enterprise OLTP catalogs fails at scale because semantic parsers collapse under schema-graph scaling, inflating context beyond stable LLM attention budgets. We present DRL (Deterministic Relational Middleware Layer), a safe pipeline interposing between front-ends and SQL backends. DRL comprises dynamic context pruning, relational AST typing, and transactional safeguard verification (EXPLAIN gating and NULL guards) to bound context and flag operational silent divergence (SDop). We evaluate DRL on PostgreSQL and MySQL, contributing (i) an OLTP schema-graph scaling model, (ii) a 1,000-pair Workload Verification Suite, (iii) baselines B0-B3, and (iv) an enterprise NL2SQL failure taxonomy. On PostgreSQL, schema-linked hints (B1) yield a 76% context reduction over naive full-catalog prompting (B0); DRL's dynamic router (B2) reaches a 92% reduction at pruning p95 = 0.58 ms and middleware p95 = 4.6 ms. GPT-4o, Claude Sonnet 4.5, and Gemini 2.5 Flash achieve 52.9%, 52.8%, and 52.1% execution match under a corrected evaluation harness; SDop flags 89-100% of false-positive EX-passing queries. GPT-4o failures are dominated by semantic/filter errors (254/471), while column hallucination is a minor factor (47/471). Crucially, a single regex defect in our evaluation post-processor silently suppressed accuracy and manufactured a false 4-10% cross-vendor gap that vanished when corrected, showing that benchmark code deserves the same scrutiny as the models it scores. DRL reframes enterprise NL2SQL as systems engineering - context bounding, verification, and plan-aware admission - not a leaderboard exercise.

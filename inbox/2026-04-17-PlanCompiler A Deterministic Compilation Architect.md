---
interest: medium
link: https://arxiv.org/abs/2604.13092
next_step: skim
priority: low
slack_ts: '1776482307.590369'
source: cs.SE - Software Engineering
status: unread
title: 'PlanCompiler: A Deterministic Compilation Architecture for Structured Multi-Step
  LLM Pipelines'
---
# PlanCompiler: A Deterministic Compilation Architecture for Structured Multi-Step LLM Pipelines
> 原文: [https://arxiv.org/abs/2604.13092](https://arxiv.org/abs/2604.13092)

arXiv:2604.13092v1 Announce Type: new
Abstract: Large language models (LLMs) remain brittle in multi-step structured workflows, where errors compound across sequential transformations, validation stages, and stateful operations such as SQL persistence. We present PlanCompiler, a compilation architecture for structured LLM pipelines that separates planning from execution through a typed node registry, static graph validation, and deterministic compilation. Instead of relying on autoregressive chaining at runtime, the system first produces a typed JSON plan over a fixed registry of primitives, validates that plan against explicit structural and type constraints, and compiles only validated plans into executable Python.
We evaluate the approach on a 300-task benchmark covering increasing workflow depth, SQL roundtrip persistence, and schema-themed stress tests. In this setting, PlanCompiler achieves 100% first-pass success on Sets A and B, 88% on Set C, 96% on Set D, 88% on schema-trap tasks, and 84% on SQL roundtrip tasks, outperforming direct free-form code-generation baselines from GPT-4.1 and Claude Sonnet on five of six benchmark sets and achieving 278/300 successes overall versus 202/300 and 187/300 for the two baselines, respectively. Across the full suite, planning cost is approximately \$0.356, compared with \$2.140 for GPT-4.1 and \$18.391 for Claude, while maintaining competitive end-to-end latency.
These results suggest that, for registry-constrained structured data workflows, deterministic compilation can improve first-pass reliability and cost efficiency relative to free-form code generation. Residual failures are concentrated in two narrow classes: late output-contract errors on aggregation tasks and early type mismatches at the SQLite persistence boundary, clarifying both the benefits and the current limits of the approach.

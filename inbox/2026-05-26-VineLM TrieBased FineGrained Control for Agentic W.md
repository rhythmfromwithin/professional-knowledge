---
title: "VineLM: Trie-Based Fine-Grained Control for Agentic Workflows"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.23914
priority: medium
status: unread
interest: medium
next_step: skim
---
# VineLM: Trie-Based Fine-Grained Control for Agentic Workflows
> 原文: [https://arxiv.org/abs/2605.23914](https://arxiv.org/abs/2605.23914)

arXiv:2605.23914v1 Announce Type: new
Abstract: Agentic workflows interleave configurable LLM stages with tool stages and often include retries or refinement loops. Existing workflow managers profile full workflow configurations offline and assign each request a static workflow-level plan that binds each configurable LLM stage to a single model, reuses that model across repeated loop iterations, and does not revisit those choices at runtime. We present VineLM, a workflow manager that enables fine-grained control by choosing the model for each stage invocation as execution unfolds under request-level objectives such as maximizing accuracy under cost or latency budgets. VineLM represents feasible executions as an annotated trie of model-choice prefixes and uses checkpointing and cascade profiling to estimate path accuracy, cost, and latency without exhaustively profiling every request on every path. At runtime, VineLM re-roots the trie after each stage invocation and replans over the remaining subtrie using the realized execution prefix and remaining latency budget. On NL2SQL and math reasoning workflows, VineLM improves the cost-latency-accuracy frontier over coarse workflow-level baselines, achieving up to 18% higher accuracy at the same per-request budget with its sparse profiling reducing offline profiling cost by 98-99.8% when compared to exhaustive profiling.

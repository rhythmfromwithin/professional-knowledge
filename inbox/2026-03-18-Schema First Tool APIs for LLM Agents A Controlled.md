---
title: "Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.13404
priority: low
status: unread
interest: medium
next_step: skim
---
# Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance
> 原文: [https://arxiv.org/abs/2603.13404](https://arxiv.org/abs/2603.13404)

arXiv:2603.13404v1 Announce Type: new
Abstract: Tool use has become central to modern LLM agents, yet interface design is rarely isolated as an experimental variable. This paper studies whether schema based tool contracts and structured validation diagnostics improve reliability under strict interaction budgets. We evaluate three conditions that preserve identical tool semantics and information content: free form documentation, JSON Schema specifications, and JSON Schema with structured diagnostics.
We implement a deterministic software engineering sandbox with logs, metrics, configurations, and repository tasks, and evaluate a fully crossed pilot with one open local model, three seeds, three interface conditions, and four budgets. We report end task success, interface misuse, execution failures, semantic misuse, recovery behavior, and overhead. In this pilot, success remains zero across conditions, while schema conditions reduce interface misuse but not semantic misuse. The evidence supports a precise interpretation that interface formalization improves contract adherence, but semantic action quality and timeout sensitive tasks remain dominant bottlenecks under constrained local inference.

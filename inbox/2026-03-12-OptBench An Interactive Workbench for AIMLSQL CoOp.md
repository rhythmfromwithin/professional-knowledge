---
title: "OptBench: An Interactive Workbench for AI/ML-SQL Co-Optimization[Extended Demonstration Proposal]"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.08880
priority: low
status: unread
interest: medium
next_step: skim
---
# OptBench: An Interactive Workbench for AI/ML-SQL Co-Optimization[Extended Demonstration Proposal]
> 原文: [https://arxiv.org/abs/2603.08880](https://arxiv.org/abs/2603.08880)

arXiv:2603.08880v1 Announce Type: new
Abstract: Database workloads are increasingly nesting artificial intelligence (AI) and machine learning (ML) pipelines and AI/ML model inferences with data processing, yielding hybrid SQL+AI/ML queries that mix relational operators with expensive, opaque AI/ML operators, often expressed as UDFs. These workloads are challenging to optimize because ML operators behave like black boxes, data-dependent effects such as sparsity, selectivity, and cardinalities can dominate runtime, domain experts often rely on practical heuristics that are difficult to develop with monolithic optimizers, and AI/ML operators introduce numerous co-optimization opportunities such as factorization, pushdown, ML-to-SQL conversion, and linear-algebra-to-relational-algebra rewrites, significantly enlarging the search space of equivalent execution plans. At the same time, research prototypes for SQL+ML optimization are difficult to evaluate fairly because they are typically developed on different platforms and evaluated using different queries.
We present OptBench, an interactive workbench for building and benchmarking query optimizers for hybrid SQL+AI/ML queries in a transparent, apples-to-apples manner. OptBench runs all optimizers on a unified backend using DuckDB and exposes an interactive web interface that allows users to (i) construct query optimizers by leveraging and extending abstracted logical plan rewrite actions, (ii) benchmark and compare different optimizer implementations over a suite of diverse queries while recording decision traces and latency, and (iii) visualize logical plans produced by different optimizers side-by-side. The system enables practitioners and researchers to prototype optimizer ideas, inspect plan transformations, and quantitatively compare optimizer designs on multimodal inference queries within a single workbench.

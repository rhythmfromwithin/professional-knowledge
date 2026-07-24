---
title: "Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.19679
priority: low
status: unread
interest: medium
next_step: skim
---
# Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting
> 原文: [https://arxiv.org/abs/2607.19679](https://arxiv.org/abs/2607.19679)

arXiv:2607.19679v1 Announce Type: new
Abstract: Materialized views (MVs) accelerate OLAP and data-warehouse workloads by precomputing reusable subexpressions, but practical MV-based query acceleration is a multi-stage pipeline: candidate enumeration, view selection under storage budgets, and query rewriting inside the optimizer. Existing evaluations typically study only parts of this pipeline and within a single system, leaving end-to-end trade-offs and cross-system behavior unclear.
In this paper, we benchmark MV-based query rewriting by jointly evaluating enumeration, selection, and rewriting with a modular evaluation framework and by using controlled ablations. We also introduce a cross-engine protocol allowing us to compare systems that expose only execution plans by contrasting native optimizer-level rewriting with portable SQL rewriting baselines when available. Across representative academic methods and modern open-source and commercial systems, we find strong interaction effects across stages and large variability in MV usage and realized savings. We identify recurring failure modes that explain performance regressions after rewriting. Our results highlight which pipeline stages most often limit performance and provide evidence to guide future MV enumeration, selection, and rewriting designs.

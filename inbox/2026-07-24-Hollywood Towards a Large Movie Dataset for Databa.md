---
title: "Hollywood: Towards a Large Movie Dataset for Database Benchmarking"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.19666
priority: low
status: unread
interest: medium
next_step: skim
---
# Hollywood: Towards a Large Movie Dataset for Database Benchmarking
> 原文: [https://arxiv.org/abs/2607.19666](https://arxiv.org/abs/2607.19666)

arXiv:2607.19666v1 Announce Type: new
Abstract: The IMDb real-world dataset of the JOB benchmark has been extensively used in the last decade as part of the research line on cardinality estimation, given its ability to stress test both traditional and learned estimators. However, unlike the synthetic TPC family, it does not come with a scale factor, being a simple dump. We introduce Hollywood, a synthetic IMDb-compatible benchmark generator that combines LLM-generated semantic dictionaries with deterministic temporal-graph-based relational data generation. We analyze a preliminary Hollywood-200K, which contains 200,000 primary movies, generated series and episode title rows, 19.7M IMDb-style rows, and 213 nonzero JOB-Light, JOB, and JOB-Complex queries. Experiments with two open systems demonstrate that Hollywood induces cardinality estimation errors comparable to or exceeding those observed on the original IMDb dataset. The release includes generation settings and prompt/LLM-output provenance together with adapted SQL and labels, enabling tests of whether cardinality estimators generalize beyond a fixed movie snapshot and distribution.

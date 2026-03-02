---
title: "CACTUSDB: Unlock Co-Optimization Opportunities for SQL and AI/ML Inferences"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2602.23469
priority: low
status: unread
---
# CACTUSDB: Unlock Co-Optimization Opportunities for SQL and AI/ML Inferences
> 原文: [https://arxiv.org/abs/2602.23469](https://arxiv.org/abs/2602.23469)

arXiv:2602.23469v1 Announce Type: new
Abstract: There is a growing demand for supporting inference queries that combine Structured Query Language (SQL) and Artificial Intelligence / Machine Learning (AI/ML) model inferences in database systems, to avoid data denormalization and transfer, facilitate management, and alleviate privacy concerns. Co-optimization techniques for executing inference queries in database systems without accuracy loss fall into four categories: (O1) Relational algebra optimization treating AI/ML models as black-box user-defined functions (UDFs); (O2) Factorized AI/ML inferences; (O3) Tensor-relational transformation; and (O4) General cross-optimization techniques. However, we found none of the existing database systems support all these techniques simultaneously, resulting in suboptimal performance. In this work, we identify two key challenges to address the above problem: (1) the difficulty of unifying all co-optimization techniques that involve disparate data and computation abstractions in one system; and (2) the lack of an optimizer that can effectively explore the exponential search space. To address these challenges, we present CactusDB, a novel system built atop Velox - a high-performance, UDF-centric database engine, open-sourced by Meta. CactusDB features a three-level Intermediate Representations (IR) that supports relational operators, expression operators, and ML functions to enable flexible optimization of arbitrary sub-computations. Additionally, we propose a novel Monte-Carlo Tree Search (MCTS)-based optimizer with query embedding, co-designed with our unique three-level IR, enabling shared and reusable optimization knowledge across different queries. Evaluation of 12 representative inference workloads and 2,000 randomly generated inference queries on well-known datasets, such as MovieLens and TPCx-AI, shows that CactusDB achieves up to 441 times speedup compared to alternative systems.

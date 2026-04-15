---
title: "Horrila: Cost-Based Placement of Semantic Operators in Hybrid Query Plans"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.09944
priority: low
status: unread
interest: medium
next_step: skim
---
# Horrila: Cost-Based Placement of Semantic Operators in Hybrid Query Plans
> 原文: [https://arxiv.org/abs/2604.09944](https://arxiv.org/abs/2604.09944)

arXiv:2604.09944v1 Announce Type: new
Abstract: Recent database systems have introduced semantic operators that leverage large language models (LLMs) to filter, join, and project over structured data using natural language predicates. In practice, these operators are combined with traditional relational operators, e.g., equi-joins, producing hybrid query plans whose execution cost depends on both expensive LLM calls and conventional database processing. A key optimization question is where to place each semantic operator relative to the relational operators in the plan: placing them earlier reduces the data that subsequent operators process, but requires more LLM calls; placing them later reduces LLM calls through deduplication, but forces relational operators to process larger intermediate data. Existing systems either ignore this placement question or apply simple heuristics without considering the full cost trade-off. We present Horrila, a plan-level optimizer for hybrid semantic-relational queries. Horrila reduces hybrid query planning to semantic filter placement via two equivalence-preserving rewrites. We prove that deferring all semantic filters to the latest possible position minimizes LLM invocations under function caching, but show that this can cause relational processing costs to dominate on complex multi-table queries. To balance LLM cost against relational cost, Horrila uses a dynamic-programming-based cost model that finds the placement minimizing their weighted sum. On 44 semantic SQL queries across five schemas and two benchmarks, Horrila achieves up to 1.5$\times$ speedup and 4.29$\times$ cost reduction while maintaining high output quality: an average F1 of 0.85 against the unoptimized baseline and 0.84 against human-annotated ground truth on SemBench. Overall, Horrila achieves a significant cost reduction while preserving the highest accuracy among six publicly available systems.

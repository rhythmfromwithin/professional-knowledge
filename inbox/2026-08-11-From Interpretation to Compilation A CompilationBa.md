---
title: "From Interpretation to Compilation: A Compilation-Based Execution Engine for Semantic Operator Systems"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.06677
priority: low
status: unread
interest: medium
next_step: skim
---
# From Interpretation to Compilation: A Compilation-Based Execution Engine for Semantic Operator Systems
> 原文: [https://arxiv.org/abs/2608.06677](https://arxiv.org/abs/2608.06677)

arXiv:2608.06677v1 Announce Type: new
Abstract: Semantic operators extend data processing with natural-language predicates. Existing semantic operator systems commonly execute these operators through interpretation-based execution: for every data item, an LLM interprets the operator predicate and directly produces the corresponding result. Although expressive, this design places expensive model invocations inside the data-processing loop, causing latency and monetary cost to scale with input cardinality.
We present SemBaker, a compilation-based execution engine for semantic operator systems. SemBaker acts as an external plugin rather than replacing a backend's native execution. For selected semantic filters, maps, and joins, it invokes an LLM once to generate a deterministic Python function and executes that function locally without per-item LLM calls. A cost-based optimizer routes each operator to native or compiled execution, while compilation overlaps pipeline execution. SemBaker supports Palimpzest, LOTUS, Nirvana, and DocETL through thin adapters. Across three 200-query QA workloads, SemBaker achieves average speedups of 4.8 to 6.3 times and average cost reductions of 5.4 to 10.7 times, with competitive processing quality.

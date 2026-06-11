---
interest: medium
link: https://arxiv.org/abs/2606.11789
next_step: skim
priority: low
slack_ts: '1781153113.751419'
source: cs.DB - Databases
status: unread
title: Efficient Graph Indexing for Interval-Aware Vector Search
---
# Efficient Graph Indexing for Interval-Aware Vector Search
> 原文: [https://arxiv.org/abs/2606.11789](https://arxiv.org/abs/2606.11789)

arXiv:2606.11789v1 Announce Type: new
Abstract: Interval-aware Approximate Nearest Neighbor (ANN) search arises in applications where each object is associated with a numeric value or interval, and queries must satisfy both vector-similarity and interval constraints. Existing methods are typically tailored to a single query semantics, such as interval-filtered ANN search, and therefore require multiple specialized indexes to support diverse workloads, leading to substantial indexing and memory overhead. To address this limitation, we propose the Unified Interval-aware Relative Neighborhood Graph (URNG), a unified graph framework for interval-aware ANN search. URNG preserves the monotonic searchability of relative-neighborhood-graph based ANN indexes while additionally ensuring structural heredity over query-induced subgraphs, enabling a single index to support multiple interval-aware query semantics. Building on this framework, we develop UG, a practical graph index that efficiently approximates URNG through unified interval-aware pruning and iterative repair, together with a query algorithm for interval-aware ANN search. Extensive experiments on 5 datasets show that UG consistently achieves a strong accuracy-efficiency trade-off across diverse interval-aware workloads while maintaining competitive index construction cost and memory usage.

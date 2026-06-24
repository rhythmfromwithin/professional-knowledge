---
interest: medium
link: https://arxiv.org/abs/2606.24204
next_step: skim
priority: low
slack_ts: '1782274340.361719'
source: cs.DB - Databases
status: unread
title: Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor
  Search
---
# Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor Search
> 原文: [https://arxiv.org/abs/2606.24204](https://arxiv.org/abs/2606.24204)

arXiv:2606.24204v1 Announce Type: new
Abstract: Approximate Nearest Neighbor Search (ANNS) is a core primitive for unstructured data retrieval. Real-world applications--such as temporal databases, financial data analysis, and retrieval-augmented generation--often require hybrid queries whose valid objects are constrained by continuous interval attributes, such as lifespans or price ranges. We study Interval-Predicate ANNS (IPANNS), where validity is determined by a predicate between an object interval and a query interval. Existing range-filtering ANNS (RFANNS) methods are designed for single-dimensional scalar filters, but interval predicates such as containment and overlap rely on two coupled endpoint constraints. Treating endpoints as independent scalar attributes can incur large intersection overhead, while containment-specific methods lack a generalized indexing abstraction. In this paper, we propose the Unified Dominance Graph (UDG), a graph-indexing framework for the closed two-bound conjunctive fragment of IPANNS. For a chosen interval predicate, UDG maps object and query endpoints into a normalized two-dimensional dominance space and builds a dominance-labeled graph over the transformed coordinates. Containment, overlap, and other supported endpoint-bound predicates therefore reuse the same construction and search algorithms after semantic mapping, while each UDG instance remains tied to its selected predicate. UDG compresses query-state-specific proximity graphs into one compact index. To improve graph search under restrictive interval filters, we add validity-preserving patch edges that provide routing choices when few objects remain valid. Extensive evaluations on standard benchmarks and real-world datasets show that UDG achieves stable query performance across multiple interval relations and workloads, significantly outperforming existing hybrid search baselines while maintaining low indexing overhead.

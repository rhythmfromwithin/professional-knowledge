---
interest: medium
link: https://arxiv.org/abs/2611.25416
next_step: skim
priority: low
slack_ts: '1795328175.526629'
source: cs.DB - Databases
status: unread
title: 'Standardized Tolerance for Adaptive Reuse and Repair: A Method for HNSW Migration
  Under Embedding Model Change Scenarios'
---
# Standardized Tolerance for Adaptive Reuse and Repair: A Method for HNSW Migration Under Embedding Model Change Scenarios
> 原文: [https://arxiv.org/abs/2611.25416](https://arxiv.org/abs/2611.25416)

arXiv:2611.25416v1 Announce Type: new
Abstract: When an embedding model changes, the same collection is re-encoded, and its vector index must be adapted to the new embedding space. Because the source and target vectors represent the same objects, suitable connections in the source index can be reused. We propose STARR (Standardized Tolerance for Adaptive Reuse and Repair) to migrate HNSW indexes after an embedding model change. STARR compares standardized edge lengths over the same source neighbor lists in both embedding spaces and uses the correlation between their distance profiles to set the allowable increase in standardized edge length. It reconnects affected vertices by searching the partially migrated graph and shares the resulting candidates with their neighbors. We bound edge rejection under local distance distortion, characterize migration work, and prove that a final repair pass makes every vertex reachable from the entry point at the base layer while respecting degree limits. Single-threaded experiments on MS MARCO, Wikipedia, and CC3M, each with one million objects, show that STARR achieves 5.25--44.54$\times$ construction speedups over Fresh and migrates faster than both DGM variants on all 15 selected transitions. Recall@10 remains within one percentage point of Fresh in 10 cases, and query throughput exceeds DGM-Local in 14 cases. Parameter sweeps on three transitions further demonstrate favorable migration-time--recall tradeoffs beyond the default settings. Across all 240 directed transitions among 16 MS MARCO models, STARR achieves a median construction speedup of 16.71$\times$ with a median recall loss of 1.0 percentage point.

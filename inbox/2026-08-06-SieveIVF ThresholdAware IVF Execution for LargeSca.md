---
title: "SieveIVF: Threshold-Aware IVF Execution for Large-Scale Training Data Deduplication"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.03199
priority: low
status: unread
interest: medium
next_step: skim
---
# SieveIVF: Threshold-Aware IVF Execution for Large-Scale Training Data Deduplication
> 原文: [https://arxiv.org/abs/2608.03199](https://arxiv.org/abs/2608.03199)

arXiv:2608.03199v1 Announce Type: new
Abstract: Embedding-based training data deduplication retrieves candidate duplicate edges above an application similarity threshold, but fixed-probe inverted-file (IVF) search ignores this predicate when giving every query the same partition budget. Across four Hunyuan workloads, qualifying neighbors appear early despite sharply varying search depths. We present SieveIVF, a threshold-aware IVF executor that stops after $W$ consecutive searches find no qualifying candidate. The systems challenge is to preserve partition-major batching when each query's remaining work depends on prior results. Continuous batching groups ready queries by partition. A lookahead scheduler layers on top, exposing only work committed by the stopping rule to increase concurrency without changing stopping decisions or returned results. We implement SieveIVF in Lance. At $W=8$, SieveIVF is $4.1$--$7.6\times$ faster than fixed-probe IVF on four 10M Hunyuan workloads and $6.1$--$8.4\times$ faster on two public 100M workloads under the same index and search parameters, with pooled filtered top-10 recall losses of $0.03$--$1.13$ percentage points on Hunyuan and $1.43$--$2.29$ percentage points on the public workloads. These results show how an application predicate can guide IVF work allocation without changing the index or bounded top-$k$ interface.

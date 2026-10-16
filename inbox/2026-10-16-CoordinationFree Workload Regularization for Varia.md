---
title: "Coordination-Free Workload Regularization for Variable-Cost Distributed Training"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.21162
priority: medium
status: unread
interest: medium
next_step: skim
---
# Coordination-Free Workload Regularization for Variable-Cost Distributed Training
> 原文: [https://arxiv.org/abs/2610.21162](https://arxiv.org/abs/2610.21162)

arXiv:2610.21162v1 Announce Type: new
Abstract: Synchronous data-parallel training usually assigns every rank the same number of records, even when record costs vary by orders of magnitude. For variable-length models, this converts input variation into idle time because each step waits for its most expensive rank-local batch. We present Batch Cost Lookahead (BCL), a coordination-free data-loading policy that buffers a bounded rank-local window and repartitions it into fixed-cardinality packs with balanced estimated cost. BCL preserves the trainer's record-count contract and requires neither cross-rank metadata exchange nor runtime modification. In simulation over public workload distributions, enabling BCL reduces per-rank estimated batch-cost variability by up to 82.8%. Across 13 NeMo-RL SFT corpora on eight H200 GPUs, rank-local BCL runs 1.050 to 1.167 times faster than pooled MFFD. Compiled H200 measurements on an internal sequence workload show speedups of 1.197 to 1.343 times over packed execution from one to four nodes. We also identify a memory-feasibility boundary: a p99 cap for high-variance or OOM-prone data bounds outliers before BCL balances the rest. These results show that substantial variable-cost imbalance can be removed at the data-loader boundary, while clarifying when data preparation or broader coordination is still necessary.

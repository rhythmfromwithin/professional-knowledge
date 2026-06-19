---
interest: medium
link: https://arxiv.org/abs/2606.19576
next_step: skim
priority: low
slack_ts: '1781847261.798789'
source: cs.DB - Databases
status: unread
title: 'REMOP: REmote-Memory-aware OPerator Optimization'
---
# REMOP: REmote-Memory-aware OPerator Optimization
> 原文: [https://arxiv.org/abs/2606.19576](https://arxiv.org/abs/2606.19576)

arXiv:2606.19576v1 Announce Type: new
Abstract: Remote and disaggregated memory tiers expand the effective memory capacity of analytical database engines, but they also reshape the cost structure of out-of-memory query processing. When an operator spills beyond local DRAM, moving pages to remote memory incurs both data-transfer time and a fixed round-trip latency per transfer. Classical operator analyses and buffer-allocation heuristics primarily target disk spilling by minimizing total I/O volume. Under remote memory, these strategies can be suboptimal because they may trigger excessive transfer rounds. We present REMOP, a remote-memory-aware operator optimization framework that uses transfer-round-aware intra-operator memory policies to improve out-of-memory execution under tight memory budgets. REMOP introduces the number of transfer rounds into the latency cost model and derives operator-specific buffer-partitioning strategies, instantiating the approach for blocked nested-loop join, external merge sort, and external hash join in DuckDB. Our evaluation on a two-node compute-memory testbed shows that REMOP reduces transfer rounds by up to 97% and operator runtime by up to 48% on spill-heavy microbenchmarks, and lowers the average runtime of spilling TPC-H and TPC-DS queries by 22.7% and 26.4% end-to-end.

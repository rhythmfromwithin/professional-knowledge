---
interest: medium
link: https://arxiv.org/abs/2607.00303
next_step: skim
priority: medium
slack_ts: '1782965365.971089'
source: cs.DC - Distributed Computing
status: unread
title: Promise-Future Synchronization for Cluster Asynchronous Many-Task Runtimes
  via MPI One-Sided Communication
---
# Promise-Future Synchronization for Cluster Asynchronous Many-Task Runtimes via MPI One-Sided Communication
> 原文: [https://arxiv.org/abs/2607.00303](https://arxiv.org/abs/2607.00303)

arXiv:2607.00303v1 Announce Type: new
Abstract: Asynchronous Many-Task (AMT) runtimes use futures as placeholders for values produced by other tasks. In the ItoyoriFBC AMT runtime, the existing future-only model binds each future to its producer at creation time and requires the number of tasks that read each future to be fixed at compile time. This prevents directly expressing algorithms that create dependencies dynamically. We extend ItoyoriFBC with an implementation of a promise-future model that lifts these limitations. Thereby, our ItoyoriFBC variant supports dynamic algorithms such as Hierarchical LU factorization (HLU). We experimentally evaluated our implementation using HLU on up to 16 nodes and observed near-ideal scaling with a 15.6x speedup.

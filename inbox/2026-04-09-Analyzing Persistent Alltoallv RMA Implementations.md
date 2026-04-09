---
interest: medium
link: https://arxiv.org/abs/2604.05099
next_step: skim
priority: medium
slack_ts: '1775703392.791589'
source: cs.DC - Distributed Computing
status: unread
title: Analyzing Persistent Alltoallv RMA Implementations for High-Performance MPI
  Communication
---
# Analyzing Persistent Alltoallv RMA Implementations for High-Performance MPI Communication
> 原文: [https://arxiv.org/abs/2604.05099](https://arxiv.org/abs/2604.05099)

arXiv:2604.05099v1 Announce Type: new
Abstract: Collective communication operations such as MPI\_Alltoallv are central to many HPC applications, particularly those with irregular message sizes. We design, implement, and evaluate persistent MPI RMA variants of Alltoallv based on fence and lock synchronization, separating a one time initialization phase from per iteration execution to enable reuse of communication metadata and window state across repeated epochs.
Our benchmarks tested on LLNL's Dane supercomputer show that the fence-persistent variant consistently outperforms the non-persistent baseline for large message sizes, achieving up to 44% reduction in runtime and improving scalability with increasing process counts; at 448 processes the runtime decreases from 2.49s to 1.54s (38% faster). We further evaluate the algorithms under irregular sparse communication patterns and compare fence- and lock-based designs, including hierarchical extensions.
Message-size sweeps and a break-even model demonstrate that persistence provides immediate payoff for messages greater or equal to 32,768 bytes, while smaller messages show limited benefit due to metadata amortization costs. These results indicate that persistent RMA Alltoallv is a practical approach for workloads with large messages, where removing repeated metadata processing leaves runtime dominated by data movement, as evidenced by the increasing time savings with message size, and they clarify the trade-offs between fence and lock synchronization on modern HPC systems.

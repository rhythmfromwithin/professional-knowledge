---
interest: medium
link: https://arxiv.org/abs/2604.08914
next_step: skim
priority: medium
slack_ts: '1776137321.417399'
source: cs.DC - Distributed Computing
status: unread
title: 'Finding Nemo-Nemo: CFT DAG-based Consensus in the WAN'
---
# Finding Nemo-Nemo: CFT DAG-based Consensus in the WAN
> 原文: [https://arxiv.org/abs/2604.08914](https://arxiv.org/abs/2604.08914)

arXiv:2604.08914v1 Announce Type: new
Abstract: This paper introduces Nemo-Nemo, a practical crash-fault tolerant (CFT) consensus protocol designed to outperform existing protocols in wide-area networks by bridging design principles from the CFT and Byzantine-fault tolerant (BFT) worlds. By structuring command propagation through a causally ordered DAG, Nemo-Nemo allows all consensus replicas to propose commands with a naturally self-regulating communication regime. By exploiting multi-leader architecture, Nemo-Nemo avoids the performance bottleneck inherent to single-leader protocols. By separating command dissemination from consensus logic, Nemo-Nemo handles challenging network conditions even when consensus commits are stalled. Moreover, leader proposals that miss a deadline are never dropped, but deterministically deferred and executed later, preserving throughput under transient network delays. And by enabling Nemo-Nemo to commit on a DAG in just two network hops, it matches the latency of existing CFT systems, while achieving significantly higher throughput. The result is a robust, deployable system: the first DAG-based CFT consensus protocol proven to exceed state-of-the-art wide-area network performance in both speed and resilience.

---
interest: medium
link: https://arxiv.org/abs/2604.27174
next_step: skim
priority: medium
slack_ts: '1777780643.685599'
source: cs.DC - Distributed Computing
status: unread
title: End-to-End and Phase-Level Performance Optimization for Hyperledger Fabric
---
# End-to-End and Phase-Level Performance Optimization for Hyperledger Fabric
> 原文: [https://arxiv.org/abs/2604.27174](https://arxiv.org/abs/2604.27174)

arXiv:2604.27174v1 Announce Type: new
Abstract: Hyperledger Fabric (HLF) is a modular, permissioned blockchain widely adopted in enterprise settings. Enhancing its throughput and latency remains challenging, as optimization decisions made in one phase of the transaction lifecycle can adversely affect other phases. In this work, we present a systematic, phase-level and end-to-end study of HLF optimizations along three fronts, combining production-grade testbed experiments with calibrated SimPy simulations. First, we introduce two novel optimization techniques that target commit-phase bottlenecks: block-level pipelining and strategic waiting. In pipelining, we overlap validation and private-data acquisition of successive blocks with state-consistency checks and ledger updates improving commit throughput by up to 1.9x. Strategic waiting coordinates commit progress by temporarily pausing fast leaders and boosting laggers to sustain endorsement parallelism, yielding up to a 1.2x higher throughput. Second, we conduct micro-benchmarking of three configuration levers: private-data dissemination, block-size selection, and endorsement peer selection. Our results reveal that: (i) Relaxed quorums for private-data dissemination significantly reduce latency in both endorsement and commit phases; (ii) Under light workloads, smaller blocks yield lower end-to-end latency, whereas, under heavy workloads, larger blocks are necessary to improve throughput and reduce latency; and (iii) Relaxed leader selection dramatically reduces dropped transactions and boosts endorsement throughput, with a modest increase in MVCC invalidations. Finally, we analyze the interplay among private-data dissemination, VSCC parallelization, and pipelined commits. Interestingly, the throughput gains over a serial commit path are maximized at a moderate level of parallelization. Together, our findings provide phase-aware and protocol-level refinements for optimizing HLF.

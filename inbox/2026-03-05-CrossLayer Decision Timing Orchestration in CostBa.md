---
interest: medium
link: https://arxiv.org/abs/2603.02253
next_step: skim
priority: low
slack_ts: '1773369795.263239'
source: cs.DB - Databases
status: unread
title: 'Cross-Layer Decision Timing Orchestration in Cost-Based Database Systems:
  Resolving Structural Temporal Misalignment'
---
# Cross-Layer Decision Timing Orchestration in Cost-Based Database Systems: Resolving Structural Temporal Misalignment
> 原文: [https://arxiv.org/abs/2603.02253](https://arxiv.org/abs/2603.02253)

arXiv:2603.02253v1 Announce Type: new
Abstract: This paper analyzes execution instability in traditional cost-based database management systems (DBMS) and identifies a structural timing misalignment between optimization and execution stages that contributes to tail-latency amplification. Beyond estimation accuracy and raw execution throughput, we argue that decision timing and the availability of runtime signals materially affect robustness under uncertainty.
In conventional DBMS architectures, the optimizer relies on historical statistics, the executor observes runtime data distributions and resource states, and accelerators impose up-front transfer costs and amortization constraints. This temporal asynchrony can lead to rigid early-bound decisions that fail under input-scale shifts or stale statistics.
We propose a cross-layer decision timing orchestration framework that shifts final decision authority from the compile-time optimizer to the runtime executor via selective late binding of operator-level choices. A Unified Risk Signal (URS) integrates optimizer uncertainty, execution-time observations, and accelerator cost signals without collapsing them into a single static cost model.
Experiments on a modified PostgreSQL prototype evaluate (i) input-scale shift, (ii) stale-statistics drift, and (iii) GPU offload break-even regimes using controlled microbenchmarks. The proposed orchestration improves execution stability, reducing P99 latency by up to 20x under severe estimation drift while maintaining comparable median latency.

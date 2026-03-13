---
interest: medium
link: https://arxiv.org/abs/2603.00357
next_step: skim
priority: medium
slack_ts: '1773369788.768759'
source: cs.DC - Distributed Computing
status: unread
title: 'SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM
  Pretraining Systems with 100k+ GPUs'
---
# SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs
> 原文: [https://arxiv.org/abs/2603.00357](https://arxiv.org/abs/2603.00357)

arXiv:2603.00357v1 Announce Type: new
Abstract: In large-scale LLM pre-training systems with 100k+ GPUs, failures become the norm rather than the exception, and restart costs can dominate wall-clock training time. However, existing fault-tolerance mechanisms are largely unprepared for this restart-dominant regime. To address this challenge, we propose SPARe - Stacked Parallelism with Adaptive Reordering - a fault-tolerance framework that masks node failures during gradient synchronization by stacking redundant data shards across parallelism groups and adaptively reordering execution. SPARe achieves availability comparable to traditional replication while maintaining near-constant computation overhead of only 2~3x, even under high redundancy where traditional replication would require linearly inflating overhead. We derive closed-form expressions for endurable failure count and computation overhead, validate them via SimGrid-based discrete-event simulation, and jointly optimize redundancy and checkpointing to minimize time-to-train. At extreme scale with up to 600k GPUs, SPARe reduces time-to-train by 40~50% compared to traditional replication.

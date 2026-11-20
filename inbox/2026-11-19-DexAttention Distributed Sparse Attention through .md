---
interest: medium
link: https://arxiv.org/abs/2611.23512
next_step: skim
priority: medium
slack_ts: '1795157496.068919'
source: cs.DC - Distributed Computing
status: unread
title: 'DexAttention: Distributed Sparse Attention through Rapid Online Planning and
  Persistent GPU Execution'
---
# DexAttention: Distributed Sparse Attention through Rapid Online Planning and Persistent GPU Execution
> 原文: [https://arxiv.org/abs/2611.23512](https://arxiv.org/abs/2611.23512)

arXiv:2611.23512v1 Announce Type: new
Abstract: Sparse attention reduces computation, but distributed execution may still transfer unnecessary data and incur substantial per-operation overhead. Mask-aware assignment and scheduling can reduce these costs, but replanning for dynamic masks must be cheaper than the execution time it saves. We present DexAttention, a distributed sparse attention system that co-designs fast online planning with persistent execution. Its assigner uses GPU-accelerated, topology-aware clustering to balance computational load and reduce communication. A lightweight greedy scheduler orders coarse communication and computation operations, while a persistent kernel on each GPU enforces fine-grained dependencies and dispatches ready tasks. This division keeps detailed synchronization out of planning while enabling overlap without repeated attention launches. The framework supports static and dynamic per-head masks across multiple attention compute kernels. On a four-node, 16-GPU cluster, DexAttention achieves a $1.39\times$ geometric-mean end-to-end training speedup over the fastest applicable baseline across 11 configurations. For dynamic video attention, it achieves $2.11$--$2.37\times$ speedups over Ring Attention including planning.

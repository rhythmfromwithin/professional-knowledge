---
interest: medium
link: https://arxiv.org/abs/2607.26316
next_step: skim
priority: medium
slack_ts: '1785728286.733129'
source: cs.DC - Distributed Computing
status: unread
title: 'Route-Block Membership Selects Packed-AWQ Arithmetic: A Controlled Single-Fixture
  Mechanism Study'
---
# Route-Block Membership Selects Packed-AWQ Arithmetic: A Controlled Single-Fixture Mechanism Study
> 原文: [https://arxiv.org/abs/2607.26316](https://arxiv.org/abs/2607.26316)

arXiv:2607.26316v1 Announce Type: new
Abstract: Mixture-of-experts (MoE) inference first aligns routed tokens into padded expert blocks, then executes packed quantized matrix multiplication over those blocks. This preprocessing is often treated as bookkeeping. In one pre-specified Qwen3-Coder AWQ layer-6 fixture on a pinned vLLM/Marlin build and RTX 3090 runtime, we show that the tested route-block interventions select exact packed arithmetic trajectories. Two fixed preconstruction histories produced distinct native alignments and exact trajectories. Injecting the opposite alignment transferred W13, activation, routed-W2, and final outputs. Permuting two routes within one block preserved each native trajectory, while exchanging two prior-data-selected routes across the boundary between expert-106 blocks 40 and 41 transferred the complete opposite trajectory. Source- and binary-derived schedule geometry maps those blocks to direct/full-K and split/global-reduction classes. Forcing a single-slice 200-block grid made W13 bitwise equal. Stable canonical construction made both histories converge to a third exact trajectory. The confirmatory cohort contains 70 valid cold processes and seven required perturbation rejections. This is a causal mechanism result for one fixture, not a prevalence, allocator, portability, or serving-impact claim.

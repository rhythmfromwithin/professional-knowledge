---
interest: medium
link: https://arxiv.org/abs/2604.14561
next_step: skim
priority: medium
slack_ts: '1776569842.577679'
source: cs.DC - Distributed Computing
status: unread
title: 'CoCoDiff: Optimizing Collective Communications for Distributed Diffusion Transformer
  Inference Under Ulysses Sequence Parallelism'
---
# CoCoDiff: Optimizing Collective Communications for Distributed Diffusion Transformer Inference Under Ulysses Sequence Parallelism
> 原文: [https://arxiv.org/abs/2604.14561](https://arxiv.org/abs/2604.14561)

arXiv:2604.14561v1 Announce Type: new
Abstract: Diffusion Transformers (DiTs) are increasingly adopted in scientific computing, yet growing model sizes and resolutions make distributed multi-GPU inference essential. Ulysses sequence parallelism scales DiT inference but introduces frequent all-to-all collectives that dominate latency. Overlapping these with computation is difficult due to tight data dependencies, large message volumes, and asymmetric interconnect bandwidths.
We introduce CoCoDiff, a distributed DiT inference engine exploiting two observations: (1) V requires only linear projection while Q/K need additional normalization and RoPE, creating opportunities to overlap V's communication with Q/K computation; (2) adjacent denoising steps produce similar tensors, yielding temporal redundancy. CoCoDiff introduces three mechanisms: Tile-Aware Parallel All-to-all (TAPA) decomposes collectives into topology-aligned phases; V-First scheduling hides V's communication behind Q/K computation; and V-Major selective communication transmits only active projections on slow interconnects. On the Aurora supercomputer with four DiT models across 1-8 nodes (up to 96 Intel GPU tiles), CoCoDiff achieves an average speedup of 3.6x, peaking at 8.4x.

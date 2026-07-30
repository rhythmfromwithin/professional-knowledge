---
title: "Representation Capacity-Matched QNN-SNN Twin Construction for Rate-Encoded SNNs"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2409.08290
priority: low
status: unread
interest: medium
next_step: skim
---
# Representation Capacity-Matched QNN-SNN Twin Construction for Rate-Encoded SNNs
> 原文: [https://arxiv.org/abs/2409.08290](https://arxiv.org/abs/2409.08290)

arXiv:2409.08290v5 Announce Type: replace
Abstract: Spiking Neural Networks (SNNs) promise higher energy efficiency over conventional Quantized Artificial Neural Networks (QNNs) due to their event-driven, spike-based computation. However, prevailing energy evaluations often oversimplify, focusing on computational aspects while neglecting critical overheads like comprehensive data movements and memory accesses. Such simplifications can lead to misleading conclusions regarding the true energy benefits of SNNs. This paper presents a rigorous re-evaluation. We establish a fair baseline by mapping rate-encoded SNNs with $T$ timesteps to capacity-matched QNNs with $\lceil \log\_2(T+1) \rceil$ bits. This ensures both models have comparable representational capacities, as well as similar hardware requirements, enabling meaningful energy comparisons. We introduce a detailed analytical energy model encompassing core computation and data movements. Using this model, we systematically explore a wide parameter space, including intrinsic network characteristics (SNN time window size, spike rate, QNN sparsity, model size, weight bit-level) and hardware characteristics (memory system and network-on-chip). Our analysis identifies specific operational regimes where SNNs genuinely offer superior energy efficiency. For example, under typical neuromorphic hardware conditions, SNNs with moderate time windows ($T = 5$) require an average spike rate ($s\_r$) below 5.7% to outperform equivalent QNNs These insights guide the design of truly energy-efficient neural network solutions.

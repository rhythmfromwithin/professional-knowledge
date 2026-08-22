---
title: "BASC : Behavior-Aligned Quantization and Pruning for Low-Bit Spiking Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.19239
priority: low
status: unread
interest: medium
next_step: skim
---
# BASC : Behavior-Aligned Quantization and Pruning for Low-Bit Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2608.19239](https://arxiv.org/abs/2608.19239)

arXiv:2608.19239v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) encode information through binary spikes and compute in an event-driven manner, offering an energy-efficient paradigm for machine intelligence. However, high-performance SNNs incur substantial memory and timestep-wise computation costs that hinder deployment on resource-constrained devices. Quantization and pruning provide complementary routes to reducing these costs, yet both make their decisions with local criteria that overlook temporal task feedback in quantization and inter-channel dependencies in pruning. Consequently, optimizing either criterion can still yield suboptimal compression performance. We refer to this discrepancy as criterion-behavior mismatch and propose Behavior-Aligned SNN Compression (BASC), a unified framework with two lightweight modules. For quantization, the scale is applied to synaptic current at every timestep and therefore shifts spike timing. Temporal-Behavior Scale Correction (TSC) makes the scale learnable under a temporal loss, allowing firing behavior to inform scale optimization. For pruning, channel importance depends on how channels jointly drive the membrane potential across the firing threshold. Boundary-Level Inter-Channel Correction (BIC) uses channelwise importance scores for initial selection and inter-channel information to re-evaluate only channels near the pruning threshold. Extensive experiments on static and neuromorphic benchmarks show that lower-bit BASC models match or outperform higher-bit baselines and retain this accuracy advantage after structured pruning, while further reducing model storage and synaptic operations.

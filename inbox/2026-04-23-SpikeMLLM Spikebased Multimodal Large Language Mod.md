---
title: "SpikeMLLM: Spike-based Multimodal Large Language Models via Modality-Specific Temporal Scales and Temporal Compression"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2604.18610
priority: low
status: unread
interest: medium
next_step: skim
---
# SpikeMLLM: Spike-based Multimodal Large Language Models via Modality-Specific Temporal Scales and Temporal Compression
> 原文: [https://arxiv.org/abs/2604.18610](https://arxiv.org/abs/2604.18610)

arXiv:2604.18610v1 Announce Type: new
Abstract: Multimodal Large Language Models (MLLMs) have achieved remarkable progress but incur substantial computational overhead and energy consumption during inference, limiting deployment in resource-constrained environments. Spiking Neural Networks (SNNs), with their sparse event-driven computation, offer inherent energy efficiency advantages on neuromorphic hardware, yet extending them to MLLMs faces two key challenges: heterogeneous modalities make uniform spike encoding insufficient, and high-resolution image inputs amplify timestep unfolding overhead. We propose SpikeMLLM, the first spike-based framework for MLLMs, which unifies existing ANN quantization methods in the spiking representation space and incorporates Modality-Specific Temporal Scales (MSTS) guided by Modality Evolution Discrepancy (MED) and Temporally Compressed LIF (TC-LIF) for timestep compression from T=L-1 to T=log2(L)-1. Experiments on four representative MLLMs across diverse multimodal benchmarks show that SpikeMLLM maintains near-lossless performance under aggressive timestep compression (Tv/Tt=3/4), with average gaps of only 0.72% and 1.19% relative to the FP16 baseline on InternVL2-8B and Qwen2VL-72B. We further develop a dedicated RTL accelerator tailored to the spike-driven datapath, observing 9.06x higher throughput and 25.8x better power efficiency relative to an FP16 GPU baseline under a deployment-oriented co-design setting, suggesting the promise of algorithm-hardware co-design for efficient multimodal intelligence.

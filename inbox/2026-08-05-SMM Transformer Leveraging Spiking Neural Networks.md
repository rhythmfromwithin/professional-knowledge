---
title: "SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.01622
priority: low
status: unread
interest: medium
next_step: skim
---
# SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks
> 原文: [https://arxiv.org/abs/2608.01622](https://arxiv.org/abs/2608.01622)

arXiv:2608.01622v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) enable event-driven computation with sparse activations, but building multimodal Transformers on SNNs is hindered by unstable training in deep spiking stacks and the mismatch between dense softmax attention and spike-based communication. We propose SMM Transformer, an SNN-based multimodal Transformer framework that combines (i)PLMP, a Parallel LIF with Multistage Learnable Parameters neuron and a tailored P-STBP algorithm for stable deep SNN training, (ii) SMSA, an attention-inspired spike-driven token-mixing module that replaces dense pairwise softmax attention with channel-wise spike co-activation and self-compensation, and (iii)SMoE, a spiking mixture-of-experts module for modality-aware fusion. Across visual and multimodal benchmarks, SMM Transformer achieves competitive accuracy compared to ANN baselines. Under a standard MAC/AC arithmetic model, SMSA reduces the estimated operator-level compute energy of the attention module by up to 97%, while whole-model profiling shows more moderate but consistent efficiency gains.

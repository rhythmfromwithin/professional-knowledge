---
interest: medium
link: https://arxiv.org/abs/2608.13952
next_step: skim
priority: low
slack_ts: '1787190023.411579'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Reducing ANN-SNN Conversion Error via Residual Membrane Potential Alignment
---
# Reducing ANN-SNN Conversion Error via Residual Membrane Potential Alignment
> 原文: [https://arxiv.org/abs/2608.13952](https://arxiv.org/abs/2608.13952)

arXiv:2608.13952v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) serve as core architectures for neuromorphic computing thanks to event-driven operation and ultra-low power consumption. Direct SNN training is hindered by non-differentiable spikes that induce vanishing gradients and unstable optimization. ANN-SNN conversion circumvents such issues by reusing well-trained ANN weights for low-latency, energy-efficient inference. Nevertheless, existing conversion schemes suffer from severe accuracy drops at small timesteps, large inference delays and cumulative quantization errors, even with marginal performance loss at large $T$. To address these limitations, we first analyze flaws of conventional conversion pipelines from residual membrane potential statistics and propose a novel conversion strategy combining dynamic initial potential tuning and feature enhancement. We then introduce a regularization loss $\mathcal{L}\_{\mathrm{RMPD}}$ to adapt initial potential of IF neurons and mitigate systematic truncation bias from boundary aggregation. A dedicated SCR-Conv2d competitive refinement layer with grouped convolution is further built to sharpen feature discrimination, eliminate redundant spikes and stabilize encoding under tiny time windows. Integrated with the state-of-the-art QCFS baseline, our approach delivers consistent low-latency performance gains and generalizes to ReLU CNNs, ANN Transformers, and multi-threshold SNN variants. Evaluations on CIFAR-10, CIFAR-100 and ImageNet verify prominent accuracy improvements at $T=2,4,8$, with negligible extra computation overhead. This work offers an effective conversion paradigm to facilitate real-world SNN deployment on neuromorphic chips.

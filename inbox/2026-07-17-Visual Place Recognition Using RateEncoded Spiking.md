---
title: "Visual Place Recognition Using Rate-Encoded Spiking Neural Networks with Discrete STDP Learning"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.13584
priority: low
status: unread
interest: medium
next_step: skim
---
# Visual Place Recognition Using Rate-Encoded Spiking Neural Networks with Discrete STDP Learning
> 原文: [https://arxiv.org/abs/2607.13584](https://arxiv.org/abs/2607.13584)

arXiv:2607.13584v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) trained through unsupervised Spike-Timing-Dependent Plasticity (STDP) have been explored as solutions to visual loop closure problems, driven by the prospect of efficient on-device inference on neuromorphic devices. State-of-the-art STDP-based models deliver high classification accuracy but fail to reach the high Recall at 100% Precision (R@100P) needed for reliable autonomous navigation. We present a discrete, tensor-native implementation of the STDP-based SNN-VPR pipeline using PyTorch with snnTorch and evaluate it on a 100-place Nordland dataset using 15 independently-trained networks. The contribution of three decisions in the implementation is investigated. First, we show how to perform neuron assignment with a closed-form, deterministic tensor pipeline and show that it provides significantly higher R@100P than a standard argmax procedure. However, some of this gain comes from implementation differences compared to prior continuous-time models, which we measure independently. Second, ablation in isolation shows that state reset after each query helps improve R@100P regardless of the way neurons are assigned. Third, velocity-compensated sliding window aggregation over k consecutive frames reaches R@100P = 100.00% at k = 5 for constant-velocity traversal and an additional 0.20 ms latency. Taken together, these findings show the impact of inference stage design decisions in STDP-based SNN-VPR on recall precision, although the separate contribution of each mechanism and implementation differences is only partially disentangled and needs further examination.

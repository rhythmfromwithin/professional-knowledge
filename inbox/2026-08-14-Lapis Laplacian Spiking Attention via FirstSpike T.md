---
title: "Lapis: Laplacian Spiking Attention via First-Spike Timing and Membrane Leakage"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.11865
priority: low
status: unread
interest: medium
next_step: skim
---
# Lapis: Laplacian Spiking Attention via First-Spike Timing and Membrane Leakage
> 原文: [https://arxiv.org/abs/2608.11865](https://arxiv.org/abs/2608.11865)

arXiv:2608.11865v1 Announce Type: new
Abstract: Self-attention has become central to spiking vision transformers, yet its query-key scoring is still largely inherited from dense networks. Existing spiking variants either simplify dot product scoring or replace it with discrete operators, but spike timing, the native variable of a spiking network, does not directly define how tokens are related. We propose Lapis, a spiking attention mechanism that scores each token pair by the L1 distance between its query and key first-spike latency vectors under time-to-first-spike coding, and maps this distance to an affinity through a Laplacian kernel. The kernel's exponential decay matches the impulse response of a leaky integrate-and-fire membrane, so the accumulated latency difference determines the decay of a membrane trace, while row normalization reduces to a bit shift under power-of-two rounding. Scoring therefore needs only subtraction, absolute value, and accumulation, and removes all multiplication between query and key channels. Under a matched backbone and training schedule, Lapis reaches 96.56% top-1 accuracy on CIFAR-10, within 0.53 points of dot-product scoring. On ImageNet-1K, it reduces the estimated arithmetic energy of the attention path by 14.5x relative to dense dot-product attention. The deployed 6-bit model attains 83.25% top-1 accuracy at an estimated arithmetic energy of 3.28mJ per image.

---
title: "Gradient-Free Training of Spiking Neural Networks via Low-Rank Evolution Strategies"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.30361
priority: low
status: unread
interest: medium
next_step: skim
---
# Gradient-Free Training of Spiking Neural Networks via Low-Rank Evolution Strategies
> 原文: [https://arxiv.org/abs/2605.30361](https://arxiv.org/abs/2605.30361)

arXiv:2605.30361v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) offer compelling energy efficiency on neuromorphic hardware, yet their training remains challenging because the discrete spike threshold is non-differentiable. Surrogate-gradient methods sidestep this by approximating the derivative, but they impose backpropagation infrastructure that is incompatible with on-chip learning. Evolution Strategies (\es) are a natural gradient-free alternative, yet their computational cost scales with the number of parameters, making them impractical for large weight matrices.
We present a method for training SNNs using EGGROLL, a low-rank factorisation of ES perturbations that reduces per-generation memory from $\mathcal{O}(mn)$ to $\mathcal{O}(r(m{+}n))$. Combining EGGROLL with a Leaky Integrate-and-Fire SNN on N-MNIST, we demonstrate that gradient-free training achieves 79.21% test accuracy while reducing per-generation wall-clock time by 2.23$\times$ relative to full-rank ES. Our results demonstrate EGGROLL is viable for SNN training, with a clear accuracy-speed tradeoff, compatible with training on neuromorphic hardware without surrogate gradients.

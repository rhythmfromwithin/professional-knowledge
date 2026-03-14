---
title: "Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.11676
priority: low
status: unread
interest: medium
next_step: skim
---
# Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2603.11676](https://arxiv.org/abs/2603.11676)

arXiv:2603.11676v1 Announce Type: new
Abstract: Although the temporal spike dynamics of spiking neural networks (SNNs) enable low-power temporal pattern capture capabilities, they also incur inherent inconsistencies that severely compromise representation. In this paper, we perform dual consistency optimization via Stable Spike to mitigate this problem, thereby improving the recognition performance of SNNs. With the hardware-friendly ``AND" bit operation, we efficiently decouple the stable spike skeleton from the multi-timestep spike maps, thereby capturing critical semantics while reducing inconsistencies from variable noise spikes. Enforcing the unstable spike maps to converge to the stable spike skeleton significantly improves the inherent consistency across timesteps. Furthermore, we inject amplitude-aware spike noise into the stable spike skeleton to diversify the representations while preserving consistent semantics. The SNN is encouraged to produce perturbation-consistent predictions, thereby contributing to generalization. Extensive experiments across multiple architectures and datasets validate the effectiveness and versatility of our method. In particular, our method significantly advances neuromorphic object recognition under ultra-low latency, improving accuracy by up to 8.33\%. This will help unlock the full power consumption and speed potential of SNNs.

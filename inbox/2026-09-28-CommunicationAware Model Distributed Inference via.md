---
title: "Communication-Aware Model Distributed Inference via Latent Representation Compression"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.30413
priority: medium
status: unread
interest: medium
next_step: skim
---
# Communication-Aware Model Distributed Inference via Latent Representation Compression
> 原文: [https://arxiv.org/abs/2609.30413](https://arxiv.org/abs/2609.30413)

arXiv:2609.30413v1 Announce Type: new
Abstract: We study optimization of distributed model inference over resource-constrained edge resources. We propose a framework that optimizes the trade-off between model accuracy and communication costs by controlling latent representation compression to meet strict Quality of Service (QoS) throughput targets. For settings with known channel state information (CSI), we derive a closed-form optimal solution for single tasks and reduce the multi-task problem to a convex optimization program characterized by a per-link water-filling strategy. We extend these to handle unpredictable environments via a stochastic dual descent algorithm that relies only on causal channel estimates. We provide Lyapunov-based proofs demonstrating that our approach strictly satisfies long-term delay constraints while achieving a bounded optimality gap. Our results offer a robust, scalable blueprint for maximizing the performance of pipelined AI tasks in dynamic, resource-constrained distributed systems. We verify the effectiveness of our proposed framework through simulations and experiments with real edge devices.

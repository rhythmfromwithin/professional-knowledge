---
interest: medium
link: https://arxiv.org/abs/2603.12354
next_step: skim
priority: medium
slack_ts: '1773974659.742399'
source: cs.CV - Computer Vision
status: unread
title: 'Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning
  and Dynamic Routing in Deep Networks'
---
# Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks
> 原文: [https://arxiv.org/abs/2603.12354](https://arxiv.org/abs/2603.12354)

arXiv:2603.12354v1 Announce Type: new
Abstract: Efficient deep learning traditionally relies on static heuristics like weight magnitude or activation awareness (e.g., Wanda, RIA). While successful in unstructured settings, we observe a critical limitation when applying these metrics to the structural pruning of deep vision networks. These contemporary metrics suffer from a magnitude bias, failing to preserve critical functional pathways. To overcome this, we propose a decoupled kinetic paradigm inspired by Alternating Gradient Flow (AGF), utilizing an absolute feature-space Taylor expansion to accurately capture the network's structural "kinetic utility". First, we uncover a topological phase transition at extreme sparsity, where AGF successfully preserves baseline functionality and exhibits topological implicit regularization, avoiding the collapse seen in models trained from scratch. Second, transitioning to architectures without strict structural priors, we reveal a phenomenon of Sparsity Bottleneck in Vision Transformers (ViTs). Through a gradient-magnitude decoupling analysis, we discover that dynamic signals suffer from signal compression in converged models, rendering them suboptimal for real-time routing. Finally, driven by these empirical constraints, we design a hybrid routing framework that decouples AGF-guided offline structural search from online execution via zero-cost physical priors. We validate our paradigm on large-scale benchmarks: under a 75% compression stress test on ImageNet-1K, AGF effectively avoids the structural collapse where traditional metrics aggressively fall below random sampling. Furthermore, when systematically deployed for dynamic inference on ImageNet-100, our hybrid approach achieves Pareto-optimal efficiency. It reduces the usage of the heavy expert by approximately 50% (achieving an estimated overall cost of 0.92$\times$) without sacrificing the full-model accuracy.

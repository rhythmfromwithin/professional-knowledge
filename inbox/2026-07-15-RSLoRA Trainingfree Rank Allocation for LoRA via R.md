---
interest: medium
link: https://arxiv.org/abs/2607.09757
next_step: skim
priority: medium
slack_ts: '1784172053.090209'
source: cs.CV - Computer Vision
status: unread
title: 'RSLoRA: Training-free Rank Allocation for LoRA via Representational Sensitivity
  Probing'
---
# RSLoRA: Training-free Rank Allocation for LoRA via Representational Sensitivity Probing
> 原文: [https://arxiv.org/abs/2607.09757](https://arxiv.org/abs/2607.09757)

arXiv:2607.09757v1 Announce Type: new
Abstract: Low-Rank Adaptation (LoRA) has become a cornerstone of parameter-efficient fine-tuning (PEFT); however, the conventional practice of uniform rank assignment ignores the functional heterogeneity of neural layers. Existing rank allocation methods typically struggle with a trade-off between computational intensity and heuristic simplicity: training-based methods suffer from prohibitive overhead, while pre-allocation methods fail to capture the dynamic task-specific representation manifold. In this paper, we propose RSLoRA (Representational Sensitivity LoRA), a training-free and gradient-free rank allocator driven by activation-space geometry. We identify a "sensitivity regime shift" across layers, observing that static weight analysis and local gradients are insufficient to reflect how updates reshape a model's internal representations. To address this, RSLoRA introduces a virtual representational probing mechanism. By simulating adaptation through structured low-rank noise and measuring the resulting manifold displacement by using Effective Rank and Frechet Distance, we identify high-sensitivity modules that require higher rank capacity. Our framework effectively bridges the gap between expert-crafted heuristics and actual representational impact. Extensive evaluations demonstrate that RSLoRA consistently outperforms state-of-the-art allocators (e.g., AdaLoRA, GoRA) across mainstream benchmarks. By eliminating the need for iterative training-time adjustments and backward gradients, RSLoRA provides a highly efficient, robust, and representation-aware solution for large-scale model adaptation.

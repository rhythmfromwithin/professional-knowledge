---
title: "Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.19893
priority: medium
status: unread
interest: medium
next_step: skim
---
# Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering
> 原文: [https://arxiv.org/abs/2607.19893](https://arxiv.org/abs/2607.19893)

arXiv:2607.19893v1 Announce Type: new
Abstract: Point-based neural rendering (PBNR) represents 3D scenes as explicit, trainable primitives and underpins high-quality reconstruction and emerging embodied AI and world-model pipelines. Unlike layer-structured neural networks, PBNR has primitive-indexed dependencies: each view reads and updates only a sparse, view-dependent subset of mutable scene state. As large scenes require distributed training and optimized renderers reduce per-view computation, global task- or iteration-level barriers increasingly place synchronization, rather than rendering, on the critical path. We present Odin, a distributed PBNR training system that replaces global barriers with primitive-level synchronization. Its ahead-of-time scheduler uses stable locality and phase order to identify low-conflict overlap windows, while the runtime validates primitive publication before later work observes mutable state. Odin provides a quality-first path that preserves synchronized-training visibility and a throughput-first path that uses overlap and gradient evidence to admit only small, low-impact delayed reads; structural changes and high-impact cases remain synchronized. Across four existing PBNR pipelines and 13 non-city scenes on 8 GPUs, Odin improves throughput by 1.22 times on average and hides 82% of critical-path wait while preserving reconstruction quality. In a MatrixCity mixed-parallel case study scaling to 64 GPUs, Odin improves throughput over Grendel by up to 1.89 times without changing renderer kernels, optimizers, training budgets, or model capacity.

---
title: "Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.04178
priority: medium
status: unread
interest: medium
next_step: skim
---
# Microbenchmark-Driven Analytical Performance Modeling Across Modern GPU Architectures
> 原文: [https://arxiv.org/abs/2605.04178](https://arxiv.org/abs/2605.04178)

arXiv:2605.04178v1 Announce Type: new
Abstract: Rapidly evolving GPU architectures featuring complex memory hierarchies, matrix units, and varied precision formats continue to widen the gap between theoretical peaks and achievable performance. We design and develop analytical performance models for NVIDIA Blackwell (B200) and AMD CDNA3 (MI300A) grounded in systematic microbenchmark characterization. For Blackwell, the model captures Tensor Memory (TMEM), asynchronous bulk copy (TMA), and 5th-generation tensor cores; for CDNA3, the model captures Infinity Cache hierarchy, VGPR constraints, and occupancy. Validation yields 1.31% MAE on B200 (21 kernels) and 0.09% on MI300A (27 kernels), while naive roofline baselines exceed 95% error on the same kernels. We further validate the models using Rodinia~3.1 and SPEChpc 2021 Tiny.The models are updated with HBM bandwidth, capacity, and cache parameters and applied to H200 (Hopper) and MI250X (CDNA2), indicating no major restructuring of the models are needed. All models and benchmarks will be released as open-source upon acceptance.

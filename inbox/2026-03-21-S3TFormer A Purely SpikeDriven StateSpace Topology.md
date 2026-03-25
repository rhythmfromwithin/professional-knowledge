---
interest: medium
link: https://arxiv.org/abs/2603.18062
next_step: skim
priority: medium
slack_ts: '1774407041.901329'
source: cs.CV - Computer Vision
status: unread
title: 'S3T-Former: A Purely Spike-Driven State-Space Topology Transformer for Skeleton
  Action Recognition'
---
# S3T-Former: A Purely Spike-Driven State-Space Topology Transformer for Skeleton Action Recognition
> 原文: [https://arxiv.org/abs/2603.18062](https://arxiv.org/abs/2603.18062)

arXiv:2603.18062v1 Announce Type: new
Abstract: Skeleton-based action recognition is crucial for multimedia applications but heavily relies on power-hungry Artificial Neural Networks (ANNs), limiting their deployment on resource-constrained edge devices. Spiking Neural Networks (SNNs) provide an energy-efficient alternative; however, existing spiking models for skeleton data often compromise the intrinsic sparsity of SNNs by resorting to dense matrix aggregations, heavy multimodal fusion modules, or non-sparse frequency domain transformations. Furthermore, they severely suffer from the short-term amnesia of spiking neurons. In this paper, we propose the Spiking State-Space Topology Transformer (S3T-Former), which, to the best of our knowledge, is the first purely spike-driven Transformer architecture specifically designed for energy-efficient skeleton action recognition. Rather than relying on heavy fusion overhead, we formulate a Multi-Stream Anatomical Spiking Embedding (M-ASE) that acts as a generalized kinematic differential operator, elegantly transforming multimodal skeleton features into heterogeneous, highly sparse event streams. To achieve true topological and temporal sparsity, we introduce Lateral Spiking Topology Routing (LSTR) for on-demand conditional spike propagation, and a Spiking State-Space (S3) Engine to systematically capture long-range temporal dynamics without non-sparse spectral workarounds. Extensive experiments on multiple large-scale datasets demonstrate that S3T-Former achieves highly competitive accuracy while theoretically reducing energy consumption compared to classic ANNs, establishing a new state-of-the-art for energy-efficient neuromorphic action recognition.

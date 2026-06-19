---
interest: medium
link: https://arxiv.org/abs/2606.18588
next_step: skim
priority: medium
slack_ts: '1781847254.856079'
source: cs.DC - Distributed Computing
status: unread
title: 'Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale
  Scene Reconstruction via Pixel-level Communication'
---
# Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication
> 原文: [https://arxiv.org/abs/2606.18588](https://arxiv.org/abs/2606.18588)

arXiv:2606.18588v1 Announce Type: new
Abstract: 3D Gaussian Splatting (3DGS) enables high-fidelity and real-time 3D scene reconstruction, but scaling training to large-scale scenes requires optimizing hundreds of millions of Gaussians across multiple GPUs. Existing distributed approaches either partition scenes into isolated regions, causing global inconsistency, or rely on global Gaussian-level exchanges, which lead to substantial growth in inter-GPU communication and quickly dominate iteration time.
We propose Splaxel, a communication-efficient distributed 3DGS training framework based on pixel-level local rendering and global composition. Instead of synchronizing Gaussians, each GPU renders its local subset and exchanges only partial pixel values, maintaining mathematical consistency while keeping communication cost stable as the scene size increases. Splaxel further reduces pixel-level redundancy through geometric and transmittance visibility prediction and improves GPU utilization via conflict-free camera-view consolidation. Evaluated on large-scale datasets with up to 120M Gaussians, Splaxel achieves up to 7.6$\times$ speedup over the state-of-the-art distributed 3DGS framework while preserving high reconstruction quality.

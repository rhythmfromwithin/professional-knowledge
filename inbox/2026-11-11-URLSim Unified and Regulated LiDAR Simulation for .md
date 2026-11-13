---
interest: medium
link: https://arxiv.org/abs/2611.12932
next_step: skim
priority: medium
slack_ts: '1794550328.086459'
source: cs.CV - Computer Vision
status: unread
title: 'URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction
  of Dynamic Driving Scenes'
---
# URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction of Dynamic Driving Scenes
> 原文: [https://arxiv.org/abs/2611.12932](https://arxiv.org/abs/2611.12932)

arXiv:2611.12932v1 Announce Type: new
Abstract: Reconstructing high-fidelity LiDAR simulation scenes from real-world driving logs is essential for cost-effective safety validation of autonomous driving systems. While simulators based on Neural Radiance Fields (NeRF) achieve realistic scene reconstruction, their large-scale adoption is limited by slow rendering speeds. Recent 3D Gaussian splatting (3DGS) approaches have improved rendering efficiency through explicit primitive representation and differentiable rasterization. However, existing 3DGS-based methods remain largely restricted to rigid vehicles and produce redundant primitives through unconstrained densification. To address these limitations, we propose URL-Sim, a unified and regulated dynamic LiDAR simulation framework. URL-Sim constructs a dynamic Gaussian scene graph that decouples the modeling of traffic participants, including vehicles, pedestrians, and cyclists, enabling accurate reconstruction of heterogeneous dynamic objects within a single framework. It further introduces a regulated Gaussian densification strategy that ranks primitives with multi-dimensional importance scores and allocates Gaussians to the most critical regions while keeping the total primitive count bounded. Experiments on the Waymo and KITTI-360 datasets demonstrate that URL-Sim achieves higher quantitative accuracy and visual quality than existing baselines under comparable primitive budgets, and accurately recovers the geometry and poses of diverse dynamic traffic participants.

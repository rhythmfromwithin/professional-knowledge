---
interest: medium
link: https://arxiv.org/abs/2608.12442
next_step: skim
priority: medium
slack_ts: '1786931065.993219'
source: cs.CV - Computer Vision
status: unread
title: 'MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis'
---
# MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis
> 原文: [https://arxiv.org/abs/2608.12442](https://arxiv.org/abs/2608.12442)

arXiv:2608.12442v1 Announce Type: new
Abstract: Differentiable rendering has advanced novel view synthesis (NVS), yet applying it to real-world driving remains difficult due to sparse capture viewpoints, dynamic objects, and limited multi-trajectory data. We introduce the Multi-View Multi-Vehicle (MV2) dataset and benchmark for evaluating NVS models under large viewpoint changes in dynamic urban scenes. MV2 features synchronized captures from a car, scooter, and drone, each following distinct yet synchronized trajectories. Training NVS methods on one vehicle's camera stream and testing on another enables evaluation under substantially larger viewpoint variations than existing single-trajectory datasets. All sequences are registered via Structure-from-Motion and camera poses verified using manual pixel-level correspondence annotations, yielding 50 high-quality scenes with 12000 images. Benchmarking recent NVS and camera pose estimation methods shows that NVS performance degrades with increasing viewpoint disparity, and that feed-forward pose estimators notably lag behind optimization-based approaches, highlighting MV2 as a rigorous testbed for NVS in driving. The dataset, benchmark protocol, and project resources are available at https://mv2-dataset.github.io/.

---
title: "FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.22868
priority: high
status: unread
interest: medium
next_step: skim
---
# FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence
> 原文: [https://arxiv.org/abs/2605.22868](https://arxiv.org/abs/2605.22868)

arXiv:2605.22868v1 Announce Type: new
Abstract: Autonomous systems and smart-industry deployments increasingly split computation across near-sensor, edge, and cloud resources, where tight energy, latency, and reliability budgets demand run-time adaptivity. In practice, deciding what to compute and transmit at each point is pivotal; yet as multimodal sensor suites (cameras, LiDAR/depth, etc.) proliferate at the edge, most prior approaches either (i) fuse modalities on powerful servers or (ii) apply uni-modal near-sensor filters that ignore cross-modal dependencies, leading to redundant transmissions or missed events. We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems. Lightweight near-sensor classifiers are trained via a three-step procedure: (i) a server-side fusion model learns the downstream task, (ii) filter-out-safe (FoS) labels quantify each modality's necessity relative to the fused decision, and (iii) an edge-side fusion model is compacted by injecting near-sensor predictions as auxiliary signals. The result is a run-time decision layer that jointly reduces compute and communication while scaling linearly with sensor count. On a dual-modality (RGB+Depth/LiDAR) setup with SynDrone, FusionSense sustains task quality at substantially higher data-reduction rates than uni-modal filters and delivers large end-to-end gains: up to 33x lower energy at 1% FoI prevalence, 11x at 10%, a 92.3% reduction in quality loss at a fixed 30% data reduction, and roughly 1.5x higher energy savings than the best prior filtering baseline.

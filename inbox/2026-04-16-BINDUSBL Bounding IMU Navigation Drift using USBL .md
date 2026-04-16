---
title: "BIND-USBL: Bounding IMU Navigation Drift using USBL in Heterogeneous ASV-AUV Teams"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.11861
priority: medium
status: unread
interest: medium
next_step: skim
---
# BIND-USBL: Bounding IMU Navigation Drift using USBL in Heterogeneous ASV-AUV Teams
> 原文: [https://arxiv.org/abs/2604.11861](https://arxiv.org/abs/2604.11861)

arXiv:2604.11861v1 Announce Type: new
Abstract: Accurate and continuous localization of Autonomous Underwater Vehicles (AUVs) in GPS-denied environments is a persistent challenge in marine robotics. In the absence of external position fixes, AUVs rely on inertial dead-reckoning, which accumulates unbounded drift due to sensor bias and noise. This paper presents BIND-USBL, a cooperative localization framework in which a fleet of Autonomous Surface Vessels (ASVs) equipped with Ultra-Short Baseline (USBL) acoustic positioning systems provides intermittent fixes to bound AUV dead-reckoning error. The key insight is that long-duration navigation failure is driven not by the accuracy of individual USBL measurements, but by the temporal sparsity and geometric availability of those fixes. BIND-USBL combines a multi-ASV formation model linking survey scale and anchor placement to acoustic coverage, a conflict-graph-based TDMA uplink scheduler for shared-channel servicing, and delayed fusion of received USBL updates with drift-prone dead reckoning. The framework is evaluated in the HoloOcean simulator using heterogeneous ASV-AUV teams executing lawnmower coverage missions. The results show that localization performance is shaped by the interaction of survey scale, acoustic coverage, team composition, and ASV-formation geometry. Further, the spatial-reuse scheduler improves per-AUV fix delivery rate without violating the no-collision constraint, while maintaining low end-to-end fix latency.

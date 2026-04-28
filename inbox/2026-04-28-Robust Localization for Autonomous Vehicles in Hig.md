---
title: "Robust Localization for Autonomous Vehicles in Highway Scenes"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.22040
priority: medium
status: unread
interest: medium
next_step: skim
---
# Robust Localization for Autonomous Vehicles in Highway Scenes
> 原文: [https://arxiv.org/abs/2604.22040](https://arxiv.org/abs/2604.22040)

arXiv:2604.22040v1 Announce Type: new
Abstract: Localization for autonomous vehicles on highways remains under-explored compared to urban roads, and state-of-the-art methods for urban scenes degrade when directly applied to highways. We identify key challenges including environment changes under information homogeneity, heavy occlusion, degraded GNSS signals, and stringent downstream requirements on accuracy and latency. We propose a robust localization system to address highway challenges, which uses a dual-likelihood LiDAR front end that decouples 3D geometric structures and 2D road-texture cues to handle environment changes; a Control-EKF further leverages steering and acceleration commands to reduce lag and improve closed-loop behavior. An automated offline mapping and ground-truth pipeline keep maps fresh at high cadence for optimal localization performance. To catalyze progress, we release a public dataset covering both urban roads and highways while focusing on representative challenging highway clips, totaling 163 km; benchmarking is standardized using product-oriented accuracy metrics and certified ground truth. Compared to Apollo and Autoware, our system performs similarly on urban roads but shows superior robustness on challenging highway scenarios. The system has been validated by more than one million kilometers of road testing.

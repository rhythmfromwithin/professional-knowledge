---
interest: medium
link: https://arxiv.org/abs/2605.26119
next_step: skim
priority: medium
slack_ts: '1780028376.799679'
source: cs.DC - Distributed Computing
status: unread
title: 'Edge AI Deployment Beyond Models: A BSP-Aware Systems Framework for Industrial
  Embedded Platforms'
---
# Edge AI Deployment Beyond Models: A BSP-Aware Systems Framework for Industrial Embedded Platforms
> 原文: [https://arxiv.org/abs/2605.26119](https://arxiv.org/abs/2605.26119)

arXiv:2605.26119v1 Announce Type: new
Abstract: Industrial Edge AI programs often begin with the model and only later confront the platform. That sequencing is attractive because it allows early demonstrations, but it breaks down when the deployment target is an embedded system with long product lifecycles, vendor-specific kernels, heterogeneous accelerators, safety constraints, and nontrivial I/O paths. In that environment, a model is only one component of a larger execution chain that begins at the sensor, traverses the board support package (BSP), and ends in a production service loop. This paper argues that robust Edge AI deployment must be treated as a systems problem rather than a late-stage application packaging exercise. The paper presents a BSP-aware framework for industrial embedded platforms organized around five layers: hardware, BSP/operating-system adaptation, runtime and acceleration, application/inference, and operations/validation. The discussion is grounded in vendor architecture documentation for Android, NXP i.MX, NVIDIA Jetson, ONNX Runtime, and TensorRT, and in systems literature on embedded AI benchmarking, device instability, and heterogeneous edge fleets. The result is a practical framework that connects low-level platform work to measurable deployment outcomes such as reproducibility, diagnosability, sustained throughput, and field reliability.

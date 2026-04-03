---
interest: medium
link: https://arxiv.org/abs/2603.28888
next_step: skim
priority: medium
slack_ts: '1775185061.491179'
source: cs.RO - Robotics
status: unread
title: 'A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility
  Study of VLMs for Low-Latency Anomaly Detection'
---
# A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility Study of VLMs for Low-Latency Anomaly Detection
> 原文: [https://arxiv.org/abs/2603.28888](https://arxiv.org/abs/2603.28888)

arXiv:2603.28888v1 Announce Type: new
Abstract: Semantic anomalies-context-dependent hazards that pixel-level detectors cannot reason about-pose a critical safety risk in autonomous driving. We propose a \emph{semantic observer layer}: a quantized vision-language model (VLM) running at 1--2\,Hz alongside the primary AV control loop, monitoring for semantic edge cases, and triggering fail-safe handoffs when detected. Using Nvidia Cosmos-Reason1-7B with NVFP4 quantization and FlashAttention2, we achieve ~500 ms inference a ~50x speedup over the unoptimized FP16 baseline (no quantization, standard PyTorch attention) on the same hardware--satisfying the observer timing budget. We benchmark accuracy, latency, and quantization behavior in static and video conditions, identify NF4 recall collapse (10.6%) as a hard deployment constraint, and a hazard analysis mapping performance metrics to safety goals. The results establish a pre-deployment feasibility case for the semantic observer architecture on embodied-AI AV platforms.

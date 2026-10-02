---
title: "STATERA: Hidden Mass Estimation via Zero-Shot Sim-to-Real Kinematics using Frozen Temporal Tubelets"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.00003
priority: medium
status: unread
interest: medium
next_step: skim
---
# STATERA: Hidden Mass Estimation via Zero-Shot Sim-to-Real Kinematics using Frozen Temporal Tubelets
> 原文: [https://arxiv.org/abs/2610.00003](https://arxiv.org/abs/2610.00003)

arXiv:2610.00003v1 Announce Type: new
Abstract: Vision models pretrained for frame-level appearance often struggle to infer hidden physical properties from motion. We study center-of-mass (CoM) localization for opaque, asymmetric rigid bodies from short monocular videos, where surface cues and point tracking are unreliable under self-occlusion. We propose STATERA, which adapts a pretrained video backbone (V-JEPA) with mostly frozen weights and a lightweight temporal tubelet mixer to predict per-frame CoM heatmaps and trajectories. To support this task, we introduce the HiddenMass Benchmark, comprising 50K MuJoCo trajectories and a 63-sequence real-world test set with physically calibrated CoM ground truth. In simulation, STATERA-50K-Sigma improves normalized CoM error from 41.7% (DINOv2) to 25.2%. In zero-shot sim-to-real transfer, we observe a fundamental trade-off in supervision: phase-aware targets can induce bimodal predictions, while phase-agnostic targets can collapse toward statistically safe centroids. Nevertheless, our phase-aware STATERA-50K-Crescent is the only evaluated method that demonstrates consistent movement toward the true hidden offset. While this leads to a monocular vector overshoot artifact that marginally increases absolute Euclidean error compared to a static geometric centroid, it improves physics capture from 2.6% to 41.0%. These results suggest that frozen temporal representations can better separate inertial dynamics from visual geometry for hidden-parameter estimation.

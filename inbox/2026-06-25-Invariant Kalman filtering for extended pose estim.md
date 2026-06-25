---
interest: medium
link: https://arxiv.org/abs/2606.25083
next_step: skim
priority: medium
slack_ts: '1782360763.583089'
source: cs.RO - Robotics
status: unread
title: Invariant Kalman filtering for extended pose estimation in multi-IMU articulated
  rigid-body systems
---
# Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems
> 原文: [https://arxiv.org/abs/2606.25083](https://arxiv.org/abs/2606.25083)

arXiv:2606.25083v1 Announce Type: new
Abstract: Accurate extended pose estimation (orientation, velocity, and position) for IMU-instrumented articulated rigid-body systems is a key challenge in robotics and human motion analysis. The invariant extended Kalman filter (IEKF) addresses this problem for a single rigid body with convergence guarantees and consistency under unobservability, but extending these properties to articulated systems is nontrivial: inter-body pose coupling prevents a direct application, and incorporating joint kinematic constraints within the invariant framework remains an open problem. To address this gap, we introduce the relative L-extended pose, a Lie group representation for kinematic-tree systems. With one IMU per body, it yields group-affine dynamics and allows joint constraints to be expressed in invariant form. We incorporate these constraints as noise-free pseudo-measurements within an iterated IEKF (IterIEKF), thereby preserving the convergence and consistency guarantees of invariant filtering. Validated on both a UR5e robot and a human leg, the proposed IterIEKF outperforms all EKF, IterEKF, and absolute-pose IterIEKF baselines. It converges faster, exhibits lower run-to-run variability, and consistently achieves the lowest RMSE, with reductions of at least 50% compared to the second-best filter across all scenarios considered in this work.

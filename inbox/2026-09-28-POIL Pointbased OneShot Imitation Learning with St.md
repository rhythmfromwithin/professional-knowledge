---
interest: medium
link: https://arxiv.org/abs/2609.30404
next_step: skim
priority: medium
slack_ts: '1790659454.073129'
source: cs.RO - Robotics
status: unread
title: 'POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems'
---
# POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems
> 原文: [https://arxiv.org/abs/2609.30404](https://arxiv.org/abs/2609.30404)

arXiv:2609.30404v1 Announce Type: new
Abstract: We present POIL, a point-based one-shot imitation learning framework with stable dynamical systems. While one-shot imitation avoids collecting extensive demonstrations, successful one-shot manipulation requires not only transferring a demonstrated trajectory to a novel object but also executing it robustly under changing scene conditions, grasp configurations, and external disturbances. POIL addresses both problems through a shared representation: a set of 3D points on the object's functional part, used jointly for trajectory transfer and closed-loop execution. The one-shot transfer from the demonstrated trajectory is enabled with point correspondences. POIL grounds the shared functional part with a multi-modal large language model, and transfers the trajectory across viewpoint, pose, and object category changes. During execution, multi-view tracking observes the same points online, and Point-set BCSDM drives them in closed loop by projecting per-point velocities onto a single rigid-body twist computed from the tracked points alone. This extends stable dynamical models from an SE(3) pose to a point set without requiring a known 3D model or pose estimator. We show that at the goal the controller becomes a gradient flow on the classical SO(3) potential, so its terminal phase inherits the almost-global convergence of that potential under a rigid-object assumption. Across simulation and real-robot experiments, POIL transfers a single demonstration across object category, grasp pose, and goal geometry, while recovering from external disturbances during execution. Project page: https://sangminkim-99.github.io/poil

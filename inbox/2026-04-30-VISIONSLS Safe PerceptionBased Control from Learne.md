---
interest: medium
link: https://arxiv.org/abs/2604.24894
next_step: skim
priority: medium
slack_ts: '1777692900.472599'
source: cs.RO - Robotics
status: unread
title: 'VISION-SLS: Safe Perception-Based Control from Learned Visual Representations
  via System Level Synthesis'
---
# VISION-SLS: Safe Perception-Based Control from Learned Visual Representations via System Level Synthesis
> 原文: [https://arxiv.org/abs/2604.24894](https://arxiv.org/abs/2604.24894)

arXiv:2604.24894v1 Announce Type: new
Abstract: We propose VISION-SLS, a method for nonlinear output-feedback control from high-resolution RGB images which provides robust constraint satisfaction guarantees under calibrated uncertainty bounds despite partial observability, sensor noise, and nonlinear dynamics. To enable scalability while retaining guarantees, we propose: (i) a learned low-dimensional observation map from pretrained visual features with state-dependent error bounds, and (ii) a causal affine time-varying output-feedback policy optimized via System Level Synthesis (SLS). We develop a scalable, novel solver for the resulting nonconvex program that leverages sequential convex programming coupled with efficient Riccati recursions. On two simulated visuomotor tasks (a 4D car and a 10D quadrotor) with >= 512 x 512 pixels and a 59D humanoid task with partial observability, our method enables safe, information-gathering behavior that reduces uncertainty while guaranteeing constraint satisfaction with empirically-calibrated error bounds. We also validate our method on hardware, safely controlling a ground vehicle from onboard images, outperforming baselines in safety rate and solve times. Together, these results show that learned visual abstractions coupled with an efficient solver make SLS-based safe visuomotor output-feedback practical at scale. The code implementation of our method is available at https://github.com/trustworthyrobotics/VISION-SLS.

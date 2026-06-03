---
title: "Fixed-Time Dynamic Landing of Quadrotors using Adaptive Unscented Kalman Filtering and Nonlinear Model Predictive Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.02658
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fixed-Time Dynamic Landing of Quadrotors using Adaptive Unscented Kalman Filtering and Nonlinear Model Predictive Control
> 原文: [https://arxiv.org/abs/2606.02658](https://arxiv.org/abs/2606.02658)

arXiv:2606.02658v1 Announce Type: new
Abstract: This paper introduces an estimation and control framework for dynamic landing of multi-rotor uncrewed aerial vehicles on moving platforms. The proposed method integrates nonlinear model predictive control with a real-time minimum-jerk trajectory planner that enforces a prescribed touchdown time, enabling consistent timing during the terminal descent. To enhance robustness in the presence of time-varying sensing quality, we utilize an adaptive unscented kalman filter that updates the process and measurement noise statistics online. In addition, we provide a reference feasibility analysis showing that minimum-jerk references induce bounded thrust and torque commands under standard tracking hypotheses. The proposed framework is evaluated in simulation and hardware experiments, and it is shown to achieve repeatable landings and improved platform velocity prediction accuracy relative to EKF/UKF-based methods.

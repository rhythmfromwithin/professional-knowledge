---
interest: medium
link: https://arxiv.org/abs/2607.01281
next_step: skim
priority: medium
slack_ts: '1783136980.593999'
source: cs.RO - Robotics
status: unread
title: 'WaveLander: A Generalizable Hierarchical Control Framework for UAV Landing
  on Wave-Disturbed Platforms via Reinforcement Learning'
---
# WaveLander: A Generalizable Hierarchical Control Framework for UAV Landing on Wave-Disturbed Platforms via Reinforcement Learning
> 原文: [https://arxiv.org/abs/2607.01281](https://arxiv.org/abs/2607.01281)

arXiv:2607.01281v1 Announce Type: new
Abstract: Autonomous landing of unmanned aerial vehicles (UAVs) on wave-disturbed marine platforms remains challenging due to stochastic platform motion, time-varying platform attitude, and uncertain touchdown conditions. Existing model-based methods often require accurate motion prediction and online optimization, while end-to-end learning approaches may suffer from high training complexity and limited interpretability. This paper presents WaveLander, a hierarchical control framework via reinforcement learning (RL) that decouples vertical landing decision-making from low-level flight stabilization. The RL policy maps a compact platform-relative observation to a scalar vertical velocity reference, while a conventional low-level flight controller maintains attitude stability and lateral tracking. This formulation reduces dynamic platform landing to a low-dimensional, timing-aware control problem and enables smooth landing behavior without explicit switching rules. Simulation results under randomized wave-induced platform motions show that WaveLander achieves robust landing performance and generalizes to unseen disturbance conditions, demonstrating the potential of hierarchical learning-based control for marine UAV recovery.

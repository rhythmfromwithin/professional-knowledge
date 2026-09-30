---
title: "Passive-Dynamic-Walking-Inspired Dynamics Guidance for Energy-Efficient Humanoid Locomotion"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.35935
priority: medium
status: unread
interest: medium
next_step: skim
---
# Passive-Dynamic-Walking-Inspired Dynamics Guidance for Energy-Efficient Humanoid Locomotion
> 原文: [https://arxiv.org/abs/2609.35935](https://arxiv.org/abs/2609.35935)

arXiv:2609.35935v1 Announce Type: new
Abstract: Learning energy-efficient humanoid locomotion requires discovering mechanically economical gait coordination, not merely reducing actuator effort. Reinforcement learning promotes efficiency through effort-related reward penalties, which guide the step-to-step mechanics of walking only indirectly. This article proposes a framework inspired by passive dynamic walking (PDW) that temporarily creates slope-equivalent conditions favorable to economical gait discovery and removes all PDW-specific guidance before nominal-dynamics optimization. During early training, a tilted-gravity field assists sagittal progression on flat collision geometry, complemented by curriculum-coupled reward terms. The core framework requires no reference trajectories, gait phases, or contact schedules. In a five-seed forward-locomotion study on a 29-DoF Unitree G1, the framework reduces mechanical cost of transport by 6.8-15.2% over commanded speeds of 0.5-2.0m/s without degrading velocity tracking. Mechanical-work decomposition attributes the reduction to positive actuator work, and reward-matched comparisons separate the guided regime's faster gait acquisition from the tilt's additional benefit to converged economy. The framework extends to unassisted omnidirectional locomotion, where its benefit persists once a walking-specific motion prior supplies kinematic coordination, the combination reducing speed-matched cost of transport by 18.7%. On hardware, forward cost of transport falls by 16.3% with the motion prior and by 4.5% without it, the latter within the trial-to-trial spread.

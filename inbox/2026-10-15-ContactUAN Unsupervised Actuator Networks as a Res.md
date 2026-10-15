---
interest: medium
link: https://arxiv.org/abs/2610.18991
next_step: skim
priority: medium
slack_ts: '1792037691.248149'
source: cs.RO - Robotics
status: unread
title: 'Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for
  Humanoid Control'
---
# Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control
> 原文: [https://arxiv.org/abs/2610.18991](https://arxiv.org/abs/2610.18991)

arXiv:2610.18991v1 Announce Type: new
Abstract: Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness to impacts. This failure can arise from actuator sim-to-real gaps because forces depend on actuator torques. We introduce Contact-UAN, a residual world model that preserves a simulator's physics priors while correcting actuator dynamics to align simulated rollouts with recorded hardware rollouts. For humanoid motion with contact, this requires contact-consistent replay: if hardware playback in simulation begins with misaligned contact wrenches, the residual model learns to correct reset artifacts rather than actuator discrepancies. Using only onboard proprioception, Contact-UAN infers the simulator-side stance-foot pose needed to initialize replay with consistent contact forces. We show that a UAN trained on 6.5 minutes of real-world walking data generalizes to tasks that benefit from accurate force and impulse regulation and produces policies that transfer seamlessly to the real world, yielding 20% lower running torque, 43% lower force-tracking error, extreme compliance, accurate impedance control, and dynamic, robust jumps.

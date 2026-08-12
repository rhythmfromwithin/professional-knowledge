---
interest: medium
link: https://arxiv.org/abs/2608.07546
next_step: skim
priority: medium
slack_ts: '1786501801.544359'
source: cs.RO - Robotics
status: unread
title: Generalizing deep reinforcement learning across cable-driven parallel robot
  configurations with actuator-level policies
---
# Generalizing deep reinforcement learning across cable-driven parallel robot configurations with actuator-level policies
> 原文: [https://arxiv.org/abs/2608.07546](https://arxiv.org/abs/2608.07546)

arXiv:2608.07546v1 Announce Type: new
Abstract: Cable-driven parallel robots (CDPRs) present diverse configurations and complex control challenges, which can be addressed by deep reinforcement learning (DRL) by learning their nonlinear dynamics. However, DRL methods often require extensive training time, and the resulting policies do not generalize well to different robot configurations or varying numbers of actuators. In this article, we introduce a novel DRL approach for controlling CDPRs that does not depend on the specific robot configuration. Our method trains an actuator-level policy that controls each motor to achieve its target cable length, in contrast to conventional DRL approaches that learn to control the entire robot to reach a desired end-effector position. To the best of our knowledge, this is the first work to apply DRL to control CDPRs using an actuator-level policy. This approach offers two main advantages: (i) a single shared policy can be applied to any CDPR configuration, regardless of actuator count, and (ii) reliance on inverse kinematics, avoiding the more challenging forward kinematics problem. Training is performed in simulation, and the learned policy is successfully transferred to a real CDPR. Experimental results show that the actuator-level policy (ALP) surpasses traditional reinforcement learning methods in both robustness and precision. We further control a real 8-motor CDPR with 3D motion using a policy trained on a simulated 4-motor planar CDPR operating in 2D. This illustrates that the proposed method is applicable to any CDPR configuration, independent of actuator number or placement.

---
title: "Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.02443
priority: medium
status: unread
interest: medium
next_step: skim
---
# Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control
> 原文: [https://arxiv.org/abs/2603.02443](https://arxiv.org/abs/2603.02443)

arXiv:2603.02443v1 Announce Type: new
Abstract: Simultaneous locomotion and manipulation enables robots to interact with their environment beyond the constraints of a fixed base. However, coordinating legged locomotion with arm manipulation, while considering safety and compliance during contact interaction remains challenging. To this end, we propose a whole-body controller that combines a model-based admittance control for the manipulator arm with a Reinforcement Learning (RL) policy for legged locomotion. The admittance controller maps external wrenches--such as those applied by a human during physical interaction--into desired end-effector velocities, allowing for compliant behavior. The velocities are tracked jointly by the arm and leg controllers, enabling a unified 6-DoF force response. The model-based design permits accurate force control and safety guarantees via a Reference Governor (RG), while robustness is further improved by a Kalman filter enhanced with neural networks for reliable base velocity estimation. We validate our approach in both simulation and hardware using the Unitree Go2 quadruped robot with a 6-DoF arm and wrist-mounted 6-DoF Force/Torque sensor. Results demonstrate accurate tracking of interaction-driven velocities, compliant behavior, and safe, reliable performance in dynamic settings.

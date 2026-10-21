---
interest: medium
link: https://arxiv.org/abs/2610.23872
next_step: skim
priority: medium
slack_ts: '1792556396.117949'
source: cs.RO - Robotics
status: unread
title: 'DUET: Decoupled Upper- and Lower-Body Execution for Task-Agnostic Humanoid
  Loco-Manipulation'
---
# DUET: Decoupled Upper- and Lower-Body Execution for Task-Agnostic Humanoid Loco-Manipulation
> 原文: [https://arxiv.org/abs/2610.23872](https://arxiv.org/abs/2610.23872)

arXiv:2610.23872v1 Announce Type: new
Abstract: Changing a humanoid robot's manipulation policy should not require retraining the controller that maintains the robot's balance. This study introduces DUET, a decoupled execution framework that enables locomotion and manipulation controllers to operate simultaneously by combining their commands only at the robot interface. A reinforcement-learning locomotion policy controls the 12 leg joints and a waist yaw joint, tracking planar velocity, turning rate, and pelvis height from deep crouching to upright standing on a 23-degree-of-freedom Unitree G1. The 10 arm joints are excluded from the action space, while their positions and velocities are included only as observations, so that any compatible manipulation policy that generates arm-joint targets can control the upper body, and the locomotion policy keeps the lower body stable without requiring shared training or direct coordination. This study demonstrates the modular approach on hardware by pairing the same locomotion checkpoint with two different vision-language-action models, GR00T N1.7 and pi0.5. In simulation evaluation, the locomotion controller kept the robot's lower body stable with no falls while tracking the commanded planar velocity, yaw rate, and pelvis height with errors of 0.186 m/s, 0.142 rad/s, and 0.016 m, respectively. Ablation studies identify the upper-body pose curriculum as the dominant component, and removing this training step reduces episode survival from 20.0 to 7.4 seconds and increases the fall rate to 6.06 per environment minute. Robustness tests show no falls under pushes of up to 1.0 m/s within the trained payload range, and no falls at twice the payload limit for pushes below 0.7 m/s. These results show that a manipulation policy can be exchanged without retraining, restarting, or otherwise touching the layer that keeps the robot upright.

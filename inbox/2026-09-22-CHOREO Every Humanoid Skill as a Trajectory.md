---
title: "CHOREO: Every Humanoid Skill as a Trajectory"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.22274
priority: medium
status: unread
interest: medium
next_step: skim
---
# CHOREO: Every Humanoid Skill as a Trajectory
> 原文: [https://arxiv.org/abs/2609.22274](https://arxiv.org/abs/2609.22274)

arXiv:2609.22274v1 Announce Type: new
Abstract: Recent advances in humanoid robotics have produced diverse skills through reinforcement learning, motion imitation, and generative modeling. Yet these capabilities remain siloed because they are built around incompatible representations, interfaces, and controllers. We present CHOREO, a framework for training-free composition of heterogeneous humanoid skills. Our key observation is that, regardless of how a skill is learned, it can ultimately be expressed as an executable motion trajectory. Based on this observation, CHOREO converts each capability into SkillMotion, a unified representation that combines motion states, contacts, semantics, and boundary conditions. Skills are composed through direct continuation, cubic Hermite blending, or validated bridge motions, without retraining source models or updating models at test time. On Unitree G1 in MuJoCo, CHOREO organizes 2,950 admitted SkillMotion assets derived from heterogeneous sources and achieves 95.4\% sequence success across 130 multi-action tasks, including 93.8\% success on eight-action sequences. These results demonstrate that executable trajectories provide a scalable interface for accumulating and composing pretrained humanoid capabilities.

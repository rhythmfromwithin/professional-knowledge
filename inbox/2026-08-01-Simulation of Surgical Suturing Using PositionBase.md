---
title: "Simulation of Surgical Suturing Using Position-Based Dynamics and the Material Point Method for Robot Reinforcement Learning"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.27494
priority: medium
status: unread
interest: medium
next_step: skim
---
# Simulation of Surgical Suturing Using Position-Based Dynamics and the Material Point Method for Robot Reinforcement Learning
> 原文: [https://arxiv.org/abs/2607.27494](https://arxiv.org/abs/2607.27494)

arXiv:2607.27494v1 Announce Type: new
Abstract: Recent advances in robotics research have created a strong demand for high-performance simulators. Surgical robotics simulation faces unique challenges due to the need to model diverse objects, such as rigid instruments, soft tissue, and fluids. While many studies simulate sutures or soft tissue independently, only a few have considered the complete soft-tissue suturing scenario, including the contact between sutures and deformable tissue during suture insertion. Building on previous work, this paper presents a novel suturing simulation environment using sutures modelled by position-based dynamics (PBD) and soft bodies modelled by the material point method (MPM) while considering two-way contact with frictional and drag forces. We introduce a contact coupling method between the PBD suture and the MPM soft tissue, enabling visually plausible suture-tissue interactions. The simulator is optimized for GPU execution with parallel scenes using multiple CUDA streams, and we present a Reinforcement Learning (RL) environment for autonomous suturing sub-tasks, including needle insertion, driving, and extraction. Using ML-Agents, RL agents trained in the simulator show stable learning and achieve 80% and 68% success rates in needle insertion and extraction, respectively, under the strictest distance threshold.

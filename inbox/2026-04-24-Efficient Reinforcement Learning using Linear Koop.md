---
title: "Efficient Reinforcement Learning using Linear Koopman Dynamics for Nonlinear Robotic Systems"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.19980
priority: medium
status: unread
interest: medium
next_step: skim
---
# Efficient Reinforcement Learning using Linear Koopman Dynamics for Nonlinear Robotic Systems
> 原文: [https://arxiv.org/abs/2604.19980](https://arxiv.org/abs/2604.19980)

arXiv:2604.19980v1 Announce Type: new
Abstract: This paper presents a model-based reinforcement learning (RL) framework for optimal closed-loop control of nonlinear robotic systems. The proposed approach learns linear lifted dynamics through Koopman operator theory and integrates the resulting model into an actor-critic architecture for policy optimization, where the policy represents a parameterized closed-loop controller. To reduce computational cost and mitigate model rollout errors, policy gradients are estimated using one-step predictions of the learned dynamics rather than multi-step propagation. This leads to an online mini-batch policy gradient framework that enables policy improvement from streamed interaction data. The proposed framework is evaluated on several simulated nonlinear control benchmarks and two real-world hardware platforms, including a Kinova Gen3 robotic arm and a Unitree Go1 quadruped. Experimental results demonstrate improved sample efficiency over model-free RL baselines, superior control performance relative to model-based RL baselines, and control performance comparable to classical model-based methods that rely on exact system dynamics.

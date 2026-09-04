---
title: "GPU-Accelerated Astrodynamics World Models for Spacecraft Rendezvous and Proximity Operations"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.03067
priority: medium
status: unread
interest: medium
next_step: skim
---
# GPU-Accelerated Astrodynamics World Models for Spacecraft Rendezvous and Proximity Operations
> 原文: [https://arxiv.org/abs/2609.03067](https://arxiv.org/abs/2609.03067)

arXiv:2609.03067v1 Announce Type: new
Abstract: World models are an emerging paradigm in representation learning in which an agent jointly learns state-action dynamics and observation models from offline trajectory data, enabling multi-step planning and trajectory prediction with uncertainty estimates. They have shown strong results in robotics and game environments, but, to the best of our knowledge, have not previously been applied to the space domain. This paper introduces a world model-based approach to cooperative and non-cooperative spacecraft rendezvous and proximity operations. First, we introduce an open-source, JAX-based International Space Station (ISS) docking environment supporting parallel GPU simulation of spacecraft orbit and attitude dynamics, generating the thousands of state-action transitions that world model training requires. Second, we introduce Out-of-this-World-Model, a transformer-based world model that encodes relative kinematic states and body-fixed camera imagery into a latent state and predicts its evolution under commanded thrusts and torques using one-step flow matching. It produces a distribution over future observations, capturing stochastic dynamics and per-timestep uncertainty, and outperforms DreamerV3-style posterior-correction baselines with fewer trainable parameters and hyperparameters. Third, we apply the approach to a capsule autonomously docking with the ISS under keep-out-zone constraints, demonstrating improved sample efficiency and task performance over reinforcement learning baselines (53% versus 29% docking success across ports), better out-of-distribution generalization (on held-out ports the world model more than doubles baseline success, 40% versus 17%), and detection of anomalous objects encountered during approach with 98% classification accuracy. We open-source the simulation environment and model architecture to enable further study of this paradigm.

---
title: "Learning and Control in Physically Coupled Dynamical Systems"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.23502
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning and Control in Physically Coupled Dynamical Systems
> 原文: [https://arxiv.org/abs/2611.23502](https://arxiv.org/abs/2611.23502)

arXiv:2611.23502v1 Announce Type: new
Abstract: We introduce TAG (Testbed for Autonomous Games), a compact, low-cost robotic platform for studying learning and control in physically coupled dynamical systems. TAG combines an actively tilted and steered ball-in-maze board with a top-mounted rotary inverted pendulum. The pendulum's reaction torque and vibration disturb the board and marble, while the board's tilt, driven by the maze-solving policy, simultaneously disturbs the pendulum's balance. The main challenge in learning control policies for each subsystem is accounting for the impact of one subsystem's dynamics on the other's learning process. To address this challenge, we present complementary reinforcement learning paradigms, leveraging model-based and model-free approaches to learn the control policies for the maze and pendulum, respectively. Our key finding is that introducing the pendulum causes an immediate, sharp drop in the maze policy's success rate, but the policy adapts online and recovers to its pre-coupling performance within a small number of learning episodes. Experimental results show that both policies, trained independently, successfully control the maze board and the pendulum despite their physical coupling.

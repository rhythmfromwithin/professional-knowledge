---
title: "Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.17016
priority: medium
status: unread
interest: medium
next_step: skim
---
# Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy
> 原文: [https://arxiv.org/abs/2603.17016](https://arxiv.org/abs/2603.17016)

arXiv:2603.17016v1 Announce Type: new
Abstract: Fine-grained, contact-rich teleoperation remains slow, error-prone, and unreliable in real-world manipulation tasks, even for experienced operators. Shared autonomy offers a promising way to improve performance by combining human intent with automated assistance, but learning effective assistance in simulation requires a faithful model of human behavior, which is difficult to obtain in practice. We propose a real-to-sim-to-real shared autonomy framework that augments human teleoperation with learned corrective behaviors, using a simple yet effective k-nearest-neighbor (kNN) human surrogate to model operator actions in simulation. The surrogate is fit from less than five minutes of real-world teleoperation data and enables stable training of a residual copilot policy with model-free reinforcement learning. The resulting copilot is deployed to assist human operators in real-world fine-grained manipulation tasks. Through simulation experiments and a user study with sixteen participants on industry-relevant tasks, including nut threading, gear meshing, and peg insertion, we show that our system improves task success for novice operators and execution efficiency for experienced operators compared to direct teleoperation and shared-autonomy baselines that rely on expert priors or behavioral-cloning pilots. In addition, copilot-assisted teleoperation produces higher-quality demonstrations for downstream imitation learning.

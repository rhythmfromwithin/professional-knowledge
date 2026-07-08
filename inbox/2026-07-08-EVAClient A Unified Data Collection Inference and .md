---
interest: medium
link: https://arxiv.org/abs/2607.02646
next_step: skim
priority: medium
slack_ts: '1783481435.233489'
source: cs.RO - Robotics
status: unread
title: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework
  for Embodied Policies on Real Robots'
---
# EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots
> 原文: [https://arxiv.org/abs/2607.02646](https://arxiv.org/abs/2607.02646)

arXiv:2607.02646v1 Announce Type: new
Abstract: We present EVA-Client, an open-source framework for deployment, data collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control. Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration surface.

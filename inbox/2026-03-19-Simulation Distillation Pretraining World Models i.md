---
interest: medium
link: https://arxiv.org/abs/2603.15759
next_step: skim
priority: medium
slack_ts: '1773974690.692549'
source: cs.RO - Robotics
status: unread
title: 'Simulation Distillation: Pretraining World Models in Simulation for Rapid
  Real-World Adaptation'
---
# Simulation Distillation: Pretraining World Models in Simulation for Rapid Real-World Adaptation
> 原文: [https://arxiv.org/abs/2603.15759](https://arxiv.org/abs/2603.15759)

arXiv:2603.15759v1 Announce Type: new
Abstract: Simulation-to-real transfer remains a central challenge in robotics, as mismatches between simulated and real-world dynamics often lead to failures. While reinforcement learning offers a principled mechanism for adaptation, existing sim-to-real finetuning methods struggle with exploration and long-horizon credit assignment in the low-data regimes typical of real-world robotics. We introduce Simulation Distillation (SimDist), a sim-to-real framework that distills structural priors from a simulator into a latent world model and enables rapid real-world adaptation via online planning and supervised dynamics finetuning. By transferring reward and value models directly from simulation, SimDist provides dense planning signals from raw perception without requiring value learning during deployment. As a result, real-world adaptation reduces to short-horizon system identification, avoiding long-horizon credit assignment and enabling fast, stable improvement. Across precise manipulation and quadruped locomotion tasks, SimDist substantially outperforms prior methods in data efficiency, stability, and final performance. Project website and code: https://sim-dist.github.io/

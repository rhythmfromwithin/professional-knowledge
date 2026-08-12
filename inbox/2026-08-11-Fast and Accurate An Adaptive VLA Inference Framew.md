---
interest: medium
link: https://arxiv.org/abs/2608.06434
next_step: skim
priority: medium
slack_ts: '1786501784.463559'
source: cs.RO - Robotics
status: unread
title: 'Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware
  Model Selection'
---
# Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection
> 原文: [https://arxiv.org/abs/2608.06434](https://arxiv.org/abs/2608.06434)

arXiv:2608.06434v1 Announce Type: new
Abstract: Embodied intelligence demands both long-horizon reasoning and real-time closed-loop responsiveness. Recent dual-system Vision-Language-Action (VLA) architectures combine fast reactive control with slow deliberative reasoning to balance inference speed and task success rate. However, existing dual-process VLAs tightly couple the fast module to intermediate representations of the slow module, necessitating end-to-end joint training and limiting modularity, extensibility and flexible system switching. In this paper, we propose Environment-aware Model Selection (EMS), an adaptive VLA inference framework that switches between two fully decoupled systems of different scales through environment-aware model selection. The large-scale deliberative system provides globally consistent trajectory planning to ensure task success, while a lightweight reactive system enables high-frequency closed-loop control. A reinforcement-learning-based switching policy dynamically selects which system to invoke based on real-time feedback, enabling sparse use of the slow system and thereby balancing pretrained knowledge utilisation with runtime efficiency. Our design offers three key advantages over prior hierarchical VLA frameworks: (1) a fully decoupled and modular dual-system architecture that supports plug-and-play model replacement; (2) an adaptive, environment-aware switching strategy; (3) high-frequency inference for responsive closed-loop control. We extensively evaluate EMS in both simulation and real-world environments. On the LIBERO benchmark, EMS achieves success rates comparable to the large-scale baseline while increasing the effective action frequency to 93.4 Hz. The framework further demonstrates strong extensibility in real-world dual-arm manipulation tasks, where it accelerates task completion while maintaining robust performance.

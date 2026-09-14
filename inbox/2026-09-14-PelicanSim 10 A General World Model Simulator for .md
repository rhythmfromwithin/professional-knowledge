---
interest: medium
link: https://arxiv.org/abs/2609.12036
next_step: skim
priority: medium
slack_ts: '1789360378.715429'
source: cs.RO - Robotics
status: unread
title: 'Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence'
---
# Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence
> 原文: [https://arxiv.org/abs/2609.12036](https://arxiv.org/abs/2609.12036)

arXiv:2609.12036v1 Announce Type: new
Abstract: In this technical report, we propose Pelican-Sim 1.0, a general world model simulator for embodied intelligence that predicts future observations from visual context and robot actions to support downstream learning and decision making. The model incorporates four key design features: (1) Unified action representation: a 28-dimensional action value space covering most mainstream embodiments, keeping one model valid across heterogeneous devices. (2) Action-visual injection: URDF- and camera-rendered action videos bridge actions and pixels, giving markedly better controllability across embodiments, scenes, and tasks (PSNR +0.904 over alternative fusion baselines). (3) Sparse mixture-of-experts (MoE): sparse MoE layers add capacity for heterogeneous dynamics and absorb the action modality while reducing inter-modality conflict (FVD -6.530 vs. the dense backbone). (4) Efficient rollout generation: causal adaptation and few-step distillation yield a four-step autoregressive simulator, achieving a 5.67-fold speedup over the 35-step model. Benefiting from these designs, we train on approximately one million real-world and simulated trajectories and obtain large gains in action controllability and video quality: PSNR improves over the strongest evaluated baselines by 4.636 on AgiBotWorld Beta, 2.080 on RoboMIND, and 10.343 on RoboTwin, with the adapted EWMBench DYN score up 0.426 on RoboTwin. Relying on this, four downstream applications on RoboTwin succeed: 500 generated trajectories added to 50 demonstrations per task raise policy success from 70% to 93%; policy evaluation reaches a Pearson correlation of 0.994 across five checkpoints; and relative success gains reach 47.7% for action selection and 20.3% for policy improvement. Qualitative generalization across trajectory, scene, object, embodiment, and viewpoint shifts highlights its potential as a general-purpose world model simulator.

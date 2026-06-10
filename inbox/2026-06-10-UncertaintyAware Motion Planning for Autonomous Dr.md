---
title: "Uncertainty-Aware Motion Planning for Autonomous Driving in Mixed Traffic Environment"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.09958
priority: medium
status: unread
interest: medium
next_step: skim
---
# Uncertainty-Aware Motion Planning for Autonomous Driving in Mixed Traffic Environment
> 原文: [https://arxiv.org/abs/2606.09958](https://arxiv.org/abs/2606.09958)

arXiv:2606.09958v1 Announce Type: new
Abstract: In mixed-traffic environments where autonomous and human-driven vehicles may co-exist, motion planning for autonomous vehicles requires anticipating the future behaviors of surrounding human drivers. Existing reinforcement learning-based methods generally directly incorporate the predicted human intents into the observation to enable a proactive planning. However, human intent is inherently uncertain due to the behavioral diversity, perception noise, and partial observability. Treating predicted intends as deterministic states can result in unsafe decisions for autonomous vehicles. To address this problem, we propose Uncertainty-Aware Motion Planning (UAMP), which incorporates uncertainty in human intent prediction for AV decision-making. Specifically, UAMP first introduces a proximity-aware uncertainty estimator to quantify the interaction-conditioned intent uncertainty and constructs an uncertainty-guided joint intent distribution over surrounding human-driven vehicles. Within this uncertainty set, UAMP further introduces Uncertainty-Calibrated Value Learning (UCVL) to correct value function learning biases arising from directly incorporating uncertain human intent predictions into the observation. Extensive experiments in various mixed-traffic scenarios show that UAMP significantly improves safety and driving comfort, while maintaining traffic efficiency compared with existing approaches. The code is released at https://anonymous.4open.science/r/UAMP-5638.

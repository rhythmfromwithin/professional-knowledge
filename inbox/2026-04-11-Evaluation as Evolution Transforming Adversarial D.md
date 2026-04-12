---
interest: medium
link: https://arxiv.org/abs/2604.07378
next_step: skim
priority: medium
slack_ts: '1775964762.735989'
source: cs.RO - Robotics
status: unread
title: 'Evaluation as Evolution: Transforming Adversarial Diffusion into Closed-Loop
  Curricula for Autonomous Vehicles'
---
# Evaluation as Evolution: Transforming Adversarial Diffusion into Closed-Loop Curricula for Autonomous Vehicles
> 原文: [https://arxiv.org/abs/2604.07378](https://arxiv.org/abs/2604.07378)

arXiv:2604.07378v1 Announce Type: new
Abstract: Autonomous vehicles in interactive traffic environments are often limited by the scarcity of safety-critical tail events in static datasets, which biases learned policies toward average-case behaviors and reduces robustness. Existing evaluation methods attempt to address this through adversarial stress testing, but are predominantly open-loop and post-hoc, making it difficult to incorporate discovered failures back into the training process. We introduce Evaluation as Evolution ($E^2$), a closed-loop framework that transforms adversarial generation from a static validation step into an adaptive evolutionary curriculum. Specifically, $E^2$ formulates adversarial scenario synthesis as transport-regularized sparse control over a learned reverse-time SDE prior. To make this high-dimensional generation tractable, we utilize topology-driven support selection to identify critical interacting agents, and introduce Topological Anchoring to stabilize the process. This approach enables the targeted discovery of failure cases while strictly constraining deviations from realistic data distributions. Empirically, $E^2$ improves collision failure discovery by 9.01% on the nuScenes dataset and up to 21.43% on the nuPlan dataset over the strongest baselines, while maintaining low invalidity and high realism. It further yields substantial robustness gains when the resulting boundary cases are recycled for closed-loop policy fine-tuning.

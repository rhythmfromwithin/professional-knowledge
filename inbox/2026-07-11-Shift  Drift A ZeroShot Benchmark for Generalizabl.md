---
interest: medium
link: https://arxiv.org/abs/2607.07844
next_step: skim
priority: medium
slack_ts: '1783913957.972689'
source: cs.RO - Robotics
status: unread
title: 'Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous
  Driving Motion Planning'
---
# Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning
> 原文: [https://arxiv.org/abs/2607.07844](https://arxiv.org/abs/2607.07844)

arXiv:2607.07844v1 Announce Type: new
Abstract: While closed-loop motion planners trained on large-scale, object-level datasets, e.g., nuPlan, demonstrate strong in-distribution (ID) performance, their generalization to novel urban topologies and recovery mechanisms following execution perturbations remain under-explored. To address this, we present Shift & Drift, a novel dual-track benchmark designed to rigorously stress-test motion planners across two critical axes of distribution shift: (1) The Semantic Shift Track leverages a novel conversion pipeline that transforms the aerial, DeepScenario Open 3D dataset into the nuPlan simulation framework. This enables zero-shot evaluation of planners trained on North American and Singaporean data against 1,182 scenarios spanning four German cities and the US city of San Francisco featuring dense pedestrian-cyclist interactions. (2) The State-Distribution Drift Track injects stochastic perturbations into the ego vehicle's dynamics to quantify robustness against compounding execution errors. Based on this, we systematically evaluate the failure modes of diverse planning paradigms under semantic and state-distribution shifts. While imitation learning methods achieve high scores in ID benchmarks, they exhibit significant failures under semantic shift, particularly in pedestrian-dense environments, and suffer from persistent drift when subjected to temporally correlated actuation noise. In contrast, the evaluated reinforcement-learning-based planner demonstrates more graceful degradation, maintaining higher safety and progress metrics across both tracks. Our findings reveal an empirical trade-off between imitation fidelity and closed-loop resilience, providing the community with a rigorous benchmark to evaluate progress toward reliable deployment.

---
interest: medium
link: https://arxiv.org/abs/2609.25442
next_step: skim
priority: medium
slack_ts: '1790137566.059429'
source: cs.DC - Distributed Computing
status: unread
title: 'WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning'
---
# WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning
> 原文: [https://arxiv.org/abs/2609.25442](https://arxiv.org/abs/2609.25442)

arXiv:2609.25442v1 Announce Type: new
Abstract: Weight transfer - the propagation of updated parameters from trainers to rollout generators - is becoming an important performance bottleneck in reinforcement learning (RL) systems for LLMs. The central challenge is supporting the diverse trainer and rollout layouts and synchronization requirements of modern RL workloads without sacrificing efficiency. Existing solutions are efficient under some configurations but perform poorly or lack support under others. We present WeightBridge, a flexible, efficient weight-transfer library designed to deliver high performance across diverse RL configurations. WeightBridge first automatically extracts the correspondence between trainer and rollout weight layouts, then plans and executes redundancy-free and load-balanced weight transfer. It exposes a small, general API while coordinating workers across diverse synchronization modes. Across configurations spanning different models, parallelization layouts, and synchronization modes, WeightBridge reduces average GPU stall time by up to 42$\times$ over the state-of-the-art open-source RL framework and achieves high performance in all settings. A coding agent was able to integrate WeightBridge into two different RL frameworks without manual guidance, demonstrating the generality and ease of use of its APIs.

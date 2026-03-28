---
interest: medium
link: https://arxiv.org/abs/2603.20230
next_step: skim
priority: medium
slack_ts: '1774666173.169479'
source: cs.RO - Robotics
status: unread
title: 'Beyond Scalar Rewards: Distributional Reinforcement Learning with Preordered
  Objectives for Safe and Reliable Autonomous Driving'
---
# Beyond Scalar Rewards: Distributional Reinforcement Learning with Preordered Objectives for Safe and Reliable Autonomous Driving
> 原文: [https://arxiv.org/abs/2603.20230](https://arxiv.org/abs/2603.20230)

arXiv:2603.20230v1 Announce Type: new
Abstract: Autonomous driving involves multiple, often conflicting objectives such as safety, efficiency, and comfort. In reinforcement learning (RL), these objectives are typically combined through weighted summation, which collapses their relative priorities and often yields policies that violate safety-critical constraints. To overcome this limitation, we introduce the Preordered Multi-Objective MDP (Pr-MOMDP), which augments standard MOMDPs with a preorder over reward components. This structure enables reasoning about actions with respect to a hierarchy of objectives rather than a scalar signal. To make this structure actionable, we extend distributional RL with a novel pairwise comparison metric, Quantile Dominance (QD), that evaluates action return distributions without reducing them into a single statistic. Building on QD, we propose an algorithm for extracting optimal subsets, the subset of actions that remain non-dominated under each objective, which allows precedence information to shape both decision-making and training targets. Our framework is instantiated with Implicit Quantile Networks (IQN), establishing a concrete implementation while preserving compatibility with a broad class of distributional RL methods. Experiments in Carla show improved success rates, fewer collisions and off-road events, and deliver statistically more robust policies than IQN and ensemble-IQN baselines. By ensuring policies respect rewards preorder, our work advances safer, more reliable autonomous driving systems.

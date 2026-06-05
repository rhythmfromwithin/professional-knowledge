---
interest: medium
link: https://arxiv.org/abs/2606.05248
next_step: skim
priority: medium
slack_ts: '1780633558.638069'
source: cs.RO - Robotics
status: unread
title: Inverse Manipulation through Symbolic Planning and Residual Operator Learning
---
# Inverse Manipulation through Symbolic Planning and Residual Operator Learning
> 原文: [https://arxiv.org/abs/2606.05248](https://arxiv.org/abs/2606.05248)

arXiv:2606.05248v1 Announce Type: new
Abstract: Inverting a robotic task requires more than reversing symbolic state transitions or rewinding motor trajectories. In robot manipulation tasks, symbolic inverse plans often fail to fully restore the effects of forward executions under continuous interaction dynamics. We present a hybrid framework for inverse manipulation that derives inverse-skill objectives from STRIPS-like operators automatically extracted from demonstrations through soft geometric predicates. For each extracted operator, we construct an inverse restoration objective that preserves preconditions, restores delete effects, and negates add effects. A task planner first attempts to satisfy this objective using available action primitives. Unresolved symbolic predicates then induce a residual operator learning problem solved through Reinforcement Learning (RL). We evaluate the framework on the ManiSkill3 PushCube task. For a forward pushing skill, the symbolic inverse performs a coarse pick-and-place restoration, while a residual Soft Actor-Critic policy refines the cube pose to satisfy the remaining inverse predicates. Our results show that predicate-derived residual control can turn an approximate symbolic inverse into a physically grounded inverse skill.

---
interest: medium
link: https://arxiv.org/abs/2611.08577
next_step: skim
priority: medium
slack_ts: '1794293799.919629'
source: cs.RO - Robotics
status: unread
title: 'Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop
  Manipulation'
---
# Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation
> 原文: [https://arxiv.org/abs/2611.08577](https://arxiv.org/abs/2611.08577)

arXiv:2611.08577v1 Announce Type: new
Abstract: We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced policy segments with human corrections to provide positive and negative supervision for CFG-DAgger without value learning or advantage labeling. A unified end-effector interface supports heterogeneous embodiments, while asynchronous action-chunk merging maintains smooth execution under variable inference latency. An event-driven agent maintains persistent task events and reassesses plans when progress or feasibility changes, enabling cross-task retrieval and conditional task resumption. MR0 achieves 93.6% success on RoboTwin 2.0 and ranks fifth in the RoboDojo VLA track. Under matched HG-DAgger post-training, MR0 achieves higher average success rate and progress score than $\pi\_{0.5}$ across three real-robot tasks. On Ethernet insertion, CFG-DAgger trained with Rollback data reaches 70% success and a progress score of 0.90. Qualitative agent deployments demonstrate cross-task event retrieval and recovery from temporarily unsatisfied task conditions.

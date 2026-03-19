---
title: "Alternating Reinforcement Learning with Contextual Rubric Rewards"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.15646
priority: high
status: unread
interest: medium
next_step: skim
---
# Alternating Reinforcement Learning with Contextual Rubric Rewards
> 原文: [https://arxiv.org/abs/2603.15646](https://arxiv.org/abs/2603.15646)

arXiv:2603.15646v1 Announce Type: new
Abstract: Reinforcement Learning with Rubric Rewards (RLRR) is a framework that extends conventional reinforcement learning from human feedback (RLHF) and verifiable rewards (RLVR) by replacing scalar preference signals with structured, multi-dimensional, contextual rubric-based evaluations. However, existing approaches in RLRR are limited to linearly compressing vector rewards into a scalar reward with a fixed weightings, which is sensitive to artificial score design and fails to capture correlations among reward dimensions. To overcome the limitations of reward aggregation, this work proposes Alternating Reinforcement Learning with Rubric Rewards (ARL-RR), a framework that eliminates the need for a fixed scalarization by optimizing one semantic rubric meta-class at a time. Theoretically, we show that reward aggregation induces a variance contraction effect, which helps explain the performance gains. We further introduce a lightweight, search-based adaptation procedure that selects the next meta-class dynamically based on task performance, enabling the policy to emphasize critical objectives and thereby improve the model performance. Empirically, our experiments on the HealthBench dataset with experts annotations demonstrate that ARL-RR uniformly outperforms scalarized methods in both model performance and training efficiency across different model scales (1.7B, 4B, 8B, and 14B).

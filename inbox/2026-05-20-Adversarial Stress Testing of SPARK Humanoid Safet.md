---
interest: medium
link: https://arxiv.org/abs/2605.19009
next_step: skim
priority: medium
slack_ts: '1779337379.898919'
source: cs.RO - Robotics
status: unread
title: Adversarial Stress Testing of SPARK Humanoid Safety Filters
---
# Adversarial Stress Testing of SPARK Humanoid Safety Filters
> 原文: [https://arxiv.org/abs/2605.19009](https://arxiv.org/abs/2605.19009)

arXiv:2605.19009v1 Announce Type: new
Abstract: Humanoid robots are difficult to deploy safely because they have high-dimensional bodies, many collision constraints, and must operate near people and obstacles. Safety filters help by modifying a nominal control action when it may violate collision-avoidance constraints. Still, nominal benchmark scores do not fully show how these filters behave in harder environments. In this work, we study the robustness of SPARK humanoid safety filters through replication and stress testing. We replicate the SPARK benchmark case G1SportMode\_D1\_WG\_SO\_v1 in MuJoCo and evaluate RSSA, RSSS, SSA, CBF, PFM, and SMA under controlled random seeds. We also built a post-processing pipeline that converts raw SPARK logs into goal-tracking, minimum-distance, and collision-step metrics. Our results show that some methods track the goal more closely, while others reduce collision steps more effectively. The stress tests further indicate that safety behavior can change under obstacle crowding, noisy distance estimates, and delayed obstacle information. These findings suggest that humanoid autonomy should be evaluated beyond nominal performance, using metrics that expose failure modes before deployment.

---
interest: medium
link: https://arxiv.org/abs/2606.10025
next_step: skim
priority: medium
slack_ts: '1781065405.279469'
source: cs.RO - Robotics
status: unread
title: 'GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation'
---
# GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation
> 原文: [https://arxiv.org/abs/2606.10025](https://arxiv.org/abs/2606.10025)

arXiv:2606.10025v1 Announce Type: new
Abstract: We present GHOST, a framework for learning visuomotor manipulation policies that generalize beyond the training distribution. GHOST factorizes control into (i) a high-level policy that predicts the next sub-goal as a distribution over 3D end-effector poses from multi-view RGB-D observations, and (ii) a low-level goal-conditioned controller that executes embodiment-specific actions. To condition image-based policies on 3D goals, we introduce a simple spatial interface that projects predicted goals into the image plane and represents them as end-effector heatmaps. Across a suite of manipulation tasks, this hierarchical factorization consistently improves performance and robustness compared to a flat Diffusion Policy.
Further, we show that this hierarchical interface also makes it easy to incorporate human demonstrations without relying on (noisy) action retargeting. As sub-goals are largely embodiment-agnostic, we train the high-level policy on human video to specify how learned skills should be applied and composed, while keeping the low-level policy trained purely on robot data. This hierarchy enables adaptation to novel objects and task variations using a small number of human demonstrations.

---
interest: medium
link: https://arxiv.org/abs/2603.16978
next_step: skim
priority: medium
slack_ts: '1774320347.945219'
source: cs.RO - Robotics
status: unread
title: 'Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models'
---
# Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models
> 原文: [https://arxiv.org/abs/2603.16978](https://arxiv.org/abs/2603.16978)

arXiv:2603.16978v1 Announce Type: new
Abstract: Well-designed dense reward functions in robot manipulation not only indicate whether a task is completed but also encode progress along the way. Generally, designing dense rewards is challenging and usually requires access to privileged state information available only in simulation, not in real-world experiments. This makes reward prediction models that infer task state information from camera images attractive. A common approach is to predict rewards from expert demonstrations based on visual similarity or sequential frame ordering. However, this biases the resulting reward function towards a specific solution and leaves it undefined in states not covered by the demonstrations. In this work, we introduce Rewarding DINO, a method for language-conditioned reward modeling that learns actual reward functions rather than specific trajectories. The model's compact size allows it to serve as a direct replacement for analytical reward functions with comparatively low computational overhead. We train our model on data sampled from 24 Meta-World+ tasks using a rank-based loss and evaluate pairwise accuracy, rank correlation, and calibration. Rewarding DINO achieves competitive performance in tasks from the training set and generalizes to new settings in simulation and the real world, indicating that it learns task semantics. We also test the model with off-the-shelf reinforcement learning algorithms to solve tasks from our Meta-World+ training set.

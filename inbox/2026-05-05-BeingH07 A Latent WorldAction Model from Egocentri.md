---
interest: medium
link: https://arxiv.org/abs/2605.00078
next_step: skim
priority: medium
slack_ts: '1777952325.731129'
source: cs.RO - Robotics
status: unread
title: 'Being-H0.7: A Latent World-Action Model from Egocentric Videos'
---
# Being-H0.7: A Latent World-Action Model from Egocentric Videos
> 原文: [https://arxiv.org/abs/2605.00078](https://arxiv.org/abs/2605.00078)

arXiv:2605.00078v1 Announce Type: new
Abstract: Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping multimodal observations and language instructions directly to actions, but sparse action supervision often encourages shortcut mappings rather than representations of dynamics, contact, and task progress. Recent world-action models introduce future prediction through video rollouts, yet pixel-space prediction is a costly and indirect substrate for control, as it may model visual details irrelevant to action generation and introduces substantial training or inference overhead. We present Being-H0.7, a latent world-action model that brings future-aware reasoning into VLA-style policies without generating future frames. Being-H0.7 inserts learnable latent queries between perception and action as a compact reasoning interface, and trains them with a future-informed dual-branch design: a deployable prior branch infers latent states from the current context, while a training-only posterior branch replaces the queries with embeddings from future observations. Jointly aligning the two branches at the latent reasoning space leads the prior branch to reason future-aware, action-useful structure from current observations alone. At inference, Being-H0.7 discards the posterior branch and performs no visual rollout. Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies.

---
title: "CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.15771
priority: medium
status: unread
interest: medium
next_step: skim
---
# CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving
> 原文: [https://arxiv.org/abs/2603.15771](https://arxiv.org/abs/2603.15771)

arXiv:2603.15771v1 Announce Type: new
Abstract: Autonomous driving requires safe planning, but most learning-based planners lack explicit self-correction ability: once an unsafe action is proposed, there is no mechanism to correct it. Thus, we propose CorrectionPlanner, an autoregressive planner with self-correction that models planning as motion-token generation within a propose, evaluate, and correct loop. At each planning step, the policy proposes an action, namely a motion token, and a learned collision critic predicts whether it will induce a collision within a short horizon. If the critic predicts a collision, we retain the sequence of historical unsafe motion tokens as a self-correction trace, generate the next motion token conditioned on it, and repeat this process until a safe motion token is proposed or the safety criterion is met. This self-correction trace, consisting of all unsafe motion tokens, represents the planner's correction process in motion-token space, analogous to a reasoning trace in language models. We train the planner with imitation learning followed by model-based reinforcement learning using rollouts from a pretrained world model that realistically models agents' reactive behaviors. Closed-loop evaluations show that CorrectionPlanner reduces collision rate by over 20% on Waymax and achieves state-of-the-art planning scores on nuPlan.

---
interest: medium
link: https://arxiv.org/abs/2606.07550
next_step: skim
priority: high
slack_ts: '1780978312.039879'
source: cs.LG - Machine Learning
status: unread
title: 'Offline Reinforcement Learning for Plasma Control in Nuclear Fusion: Codebase
  and Benchmark'
---
# Offline Reinforcement Learning for Plasma Control in Nuclear Fusion: Codebase and Benchmark
> 原文: [https://arxiv.org/abs/2606.07550](https://arxiv.org/abs/2606.07550)

arXiv:2606.07550v1 Announce Type: new
Abstract: Offline reinforcement learning (RL) offers a promising route for developing plasma controllers from historical tokamak data, since online trial-and-error on real devices is costly and risky. However, progress in this direction remains difficult to measure due to the lack of a standardized offline RL benchmark for realistic multi-actuator, long-horizon plasma control problems in nuclear fusion. We introduce RL4F, an Offline Reinforcement Learning Benchmark for Plasma Control in Nuclear Fusion, providing closed-loop evaluation environments and baseline comparisons across four full-profile tracking tasks: rotation, density, temperature, and pressure. The dynamics function underlying the evaluation environment is built from historical discharge data from DIII-D, a real-world Tokamak. We evaluate a broad set of imitation learning and offline RL baselines under a unified protocol. We find that offline model-based RL methods obtain the best average performance on most objectives, although no single method dominates all tasks, highlighting the importance of dynamics modeling in complex, long-horizon plasma control tasks. To foster further research, we open-source the codebase, datasets, and evaluation framework, providing a benchmark not only for the fusion community but also for algorithm development in offline RL.

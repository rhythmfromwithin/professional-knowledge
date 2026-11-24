---
title: "Rollout Scheduling for Chaotic Neural ODEs: Coverage Gains, Computational Cost, and Predictive Accuracy"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.28192
priority: medium
status: unread
interest: medium
next_step: skim
---
# Rollout Scheduling for Chaotic Neural ODEs: Coverage Gains, Computational Cost, and Predictive Accuracy
> 原文: [https://arxiv.org/abs/2611.28192](https://arxiv.org/abs/2611.28192)

arXiv:2611.28192v1 Announce Type: new
Abstract: Training Neural Ordinary Differential Equations (Neural ODEs) on chaotic systems is difficult because small changes in model parameters can lead to rapidly growing differences in predictions. A rollout is a trajectory predicted by the model. Choosing its length from a single global Lyapunov time overlooks differences in local instability. We study rollout scheduling for training on one contiguous rollout per sampled state, asking whether adapting its length to local instability improves prediction. We find the schedule that uses the most trajectory data under an instability budget, a limit on how much instability any one rollout may accumulate. Under stated assumptions, we bound the resulting coverage gain and the coverage lost when the instability estimates are in error. Numerical checks illustrate the theory. Training experiments on Lorenz-63, Lorenz-96, and Kuramoto--Sivashinsky compare adaptive and constant schedules at the same instability budgets and maximum rollout lengths. The budgets are computed from the true system's finite-time Lyapunov exponents. Across the tested settings, adaptive schedules increase trajectory coverage at additional computational cost, without showing a consistent improvement in prediction accuracy. On Lorenz-63, limiting adaptive rollouts to the horizon used to estimate instability improves prediction at the larger budgets. On Kuramoto--Sivashinsky, most configurations provide useful short-time predictions, while all tested long rollouts eventually fail. These findings show why coverage, prediction accuracy, and long-time behavior need separate evaluation, and why instability estimates should be checked over the windows used in training.

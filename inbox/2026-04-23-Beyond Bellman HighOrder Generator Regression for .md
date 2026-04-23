---
interest: medium
link: https://arxiv.org/abs/2604.18972
next_step: skim
priority: medium
slack_ts: '1776915197.714469'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Beyond Bellman: High-Order Generator Regression for Continuous-Time Policy
  Evaluation'
---
# Beyond Bellman: High-Order Generator Regression for Continuous-Time Policy Evaluation
> 原文: [https://arxiv.org/abs/2604.18972](https://arxiv.org/abs/2604.18972)

arXiv:2604.18972v1 Announce Type: new
Abstract: We study finite-horizon continuous-time policy evaluation from discrete closed-loop trajectories under time-inhomogeneous dynamics. The target value surface solves a backward parabolic equation, but the Bellman baseline obtained from one-step recursion is only first-order in the grid width. We estimate the time-dependent generator from multi-step transitions using moment-matching coefficients that cancel lower-order truncation terms, and combine the resulting surrogate with backward regression. The main theory gives an end-to-end decomposition into generator misspecification, projection error, pooling bias, finite-sample error, and start-up error, together with a decision-frequency regime map explaining when higher-order gains should be visible. Across calibration studies, four-scale benchmarks, feature and start-up ablations, and gain-mismatch stress tests, the second-order estimator consistently improves on the Bellman baseline and remains stable in the regime where the theory predicts visible gains. These results position high-order generator regression as an interpretable continuous-time policy-evaluation method with a clear operating region.

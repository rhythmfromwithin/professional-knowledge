---
interest: medium
link: https://arxiv.org/abs/2607.00877
next_step: skim
priority: medium
slack_ts: '1783050935.077849'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Hierarchical Variational Kalman Filtering
---
# Hierarchical Variational Kalman Filtering
> 原文: [https://arxiv.org/abs/2607.00877](https://arxiv.org/abs/2607.00877)

arXiv:2607.00877v1 Announce Type: new
Abstract: Traditional variational Kalman filtering with unknown noise statistics suffers from inconsistent process covariance estimation and slow convergence speed, limiting its practical utility. To address these issues, we introduce a surrogate variable representing the process-noise-free state, which enables explicit modeling and inference of process noise statistics. In addition, we reformulate the conventional coordinate ascent variation inference (CAVI) as a marginalized maximum a posteriori problem, followed by a single-step hyperparameter fitting. This reformulation obviates the need for multiple inner iterations inherent to CAVI and decouples the design of the covariance tracking filters. Consequently, this architecture permits the deployment of higher-order filters for covariance tracking and enables sliding-window hyperparameter estimation. Notably, when this window encompasses all historical data, the covariance tracking estimator intrinsically operates as a zero-phase filter. Numerical simulations validate the theoretical framework, demonstrating the enhanced convergence speed and superior estimation accuracy compared with existing methods.

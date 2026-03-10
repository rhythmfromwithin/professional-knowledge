---
interest: medium
link: https://arxiv.org/abs/2603.05575
next_step: skim
priority: medium
slack_ts: '1773132508.381339'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Prediction-Powered Conditional Inference
---
# Prediction-Powered Conditional Inference
> 原文: [https://arxiv.org/abs/2603.05575](https://arxiv.org/abs/2603.05575)

arXiv:2603.05575v1 Announce Type: new
Abstract: We study prediction-powered conditional inference in the setting where labeled data are scarce, unlabeled covariates are abundant, and a black-box machine-learning predictor is available. The goal is to perform statistical inference on conditional functionals evaluated at a fixed test point, such as conditional means, without imposing a parametric model for the conditional relationship. Our approach combines localization with prediction-based variance reduction. First, we introduce a reproducing kernel-based localization method that learns a data-adaptive weight function from covariates and reformulates the target conditional moment at the test point as a weighted unconditional moment. Second, we incorporate machine-learning predictions through a correction-based decomposition of this localized moment, yielding a prediction-powered estimator and confidence interval that reduce variance when the predictor is informative while preserving validity regardless of predictor accuracy. We establish nonasymptotic error bounds and minimax-optimal convergence rates for the resulting estimator, prove pointwise asymptotic normality with consistent variance estimation, and provide an explicit variance decomposition that characterizes how machine-learning predictions and unlabeled covariates improve statistical efficiency. Numerical experiments on simulated and real datasets demonstrate valid conditional coverage and substantially sharper confidence intervals than alternative methods.

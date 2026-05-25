---
title: "KAPLAN: Kolmogorov-Arnold Prognostic Learnable Activation Networks for Survival Analysis"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.23082
priority: medium
status: unread
interest: medium
next_step: skim
---
# KAPLAN: Kolmogorov-Arnold Prognostic Learnable Activation Networks for Survival Analysis
> 原文: [https://arxiv.org/abs/2605.23082](https://arxiv.org/abs/2605.23082)

arXiv:2605.23082v1 Announce Type: new
Abstract: Survival analysis aims to model how covariates and time jointly shape the time-to-event distribution under right censoring. Classical methods such as the Cox model and generalised additive models (GAMs) require interactions and time-varying effects to be manually specified, which is increasingly impractical on rich clinical datasets. We introduce KAPLAN-HR, a B-spline Kolmogorov-Arnold Network (KAN) for nonparametric estimation of the conditional hazard as a joint function of covariates and time. A single-layer KAPLAN-HR model recovers a GAM, while deeper architectures capture interactions and time-varying effects through composition. We establish a convergence rate for the nonparametric KAN hazard estimator that depends only on the smoothness of the underlying KAN representation and not on the covariate dimension, thereby mitigating the curse of dimensionality for KAN-representable targets. In evaluations over six clinical benchmark datasets, KAPLAN-HR matches or exceeds the predictive performance of established statistical and deep learning survival methods.

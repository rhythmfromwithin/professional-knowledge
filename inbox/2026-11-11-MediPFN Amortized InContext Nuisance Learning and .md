---
title: "MediPFN: Amortized In-Context Nuisance Learning and Inference for Causal Mediation Analysis"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.13219
priority: medium
status: unread
interest: medium
next_step: skim
---
# MediPFN: Amortized In-Context Nuisance Learning and Inference for Causal Mediation Analysis
> 原文: [https://arxiv.org/abs/2611.13219](https://arxiv.org/abs/2611.13219)

arXiv:2611.13219v1 Announce Type: new
Abstract: Causal mediation analysis decomposes a treatment effect into indirect pathways through mediators and direct pathways through other processes. Tabular foundation models perform classification and regression through in-context learning, providing estimates of conditional means and propensity scores used in causal mediation analysis. Constructing confidence intervals from these estimates requires accounting for uncertainty introduced by fitting and combining several nuisance functions. We introduce MediPFN, an amortized inference framework that adapts a pretrained tabular foundation model to nuisance prediction and combines its predictions through a cross-fitted influence-function estimator. A separate head learns quantiles of the estimator's standardized error from simulated tables with known indirect effects. Supervised fine-tuning, symmetrization, and independent calibration then produce a confidence interval. We establish coverage bounds for the resulting intervals under standard assumptions. Across experiments, MediPFN attains coverage closer to the nominal level than several comparators. It also reduces the computational cost of uncertainty quantification, running 59.1 times faster than bootstrap in matched comparisons.

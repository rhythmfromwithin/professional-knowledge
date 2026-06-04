---
title: "REGAIN: REconciliation GAIN-driven Auxiliary Direction Learning"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2606.04380
priority: medium
status: unread
interest: medium
next_step: skim
---
# REGAIN: REconciliation GAIN-driven Auxiliary Direction Learning
> 原文: [https://arxiv.org/abs/2606.04380](https://arxiv.org/abs/2606.04380)

arXiv:2606.04380v1 Announce Type: new
Abstract: Forecast reconciliation usually starts from a fixed measurement system and asks how forecasts should be projected onto a coherent space. We ask a different question: which additional linear measurements should be forecast and included in the reconciliation system? We propose REGAIN, a reconciliation-gain framework that learns normalized auxiliary directions, forecasts the induced series with a frozen forecasting oracle, and selects directions by their target-weighted loss reduction after augmented generalized least-squares reconciliation. Unlike variance-based components or predictability-based auxiliary selection, REGAIN optimizes the downstream effect of an auxiliary measurement on the final reconciled forecasts. We provide a statistical characterization showing that useful auxiliary directions must provide complementary information about unresolved target uncertainty, rather than merely being easy to forecast. The analysis also clarifies the covariance-risk reduction mechanism, the role of bias changes in realized quadratic risk, and the stability of estimated gain signals. A stagewise learning algorithm with held-out gain screening is developed, together with an optional joint refinement step. Experiments on Beijing PM2.5 and Australian Tourism data show that gain-selected measurements can improve both ordinary multivariate and hierarchical forecasts, especially when they reveal residual uncertainty not captured by the original measurement system.

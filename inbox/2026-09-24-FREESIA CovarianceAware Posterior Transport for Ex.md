---
interest: medium
link: https://arxiv.org/abs/2609.25085
next_step: skim
priority: medium
slack_ts: '1790310819.397769'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'FREESIA: Covariance-Aware Posterior Transport for Expressive and Scalable
  Data Assimilation'
---
# FREESIA: Covariance-Aware Posterior Transport for Expressive and Scalable Data Assimilation
> 原文: [https://arxiv.org/abs/2609.25085](https://arxiv.org/abs/2609.25085)

arXiv:2609.25085v1 Announce Type: new
Abstract: Data assimilation aims to infer the state of complex dynamical systems based on observational data. However, accurate inference of the multimodal posteriors induced by nonlinear or non-injective observation operators remains a key challenge under high-dimensional and sparse observation conditions. Ensemble filters scale to high dimensions but are confined by restrictive distributional assumptions, while training-free generative filters (e.g., EnSF, EnFF) alleviate this limitation but may introduce structural errors and hinder information propagation under sparse observations. To address these issues, we propose a training-free, asymptotically exact posterior transport method. Firstly, a covariance-aware posterior transport scheme is designed, which embeds the forecast cross-covariance into flow-based transport and accurately recovers unobserved states while preserving the non-Gaussian posterior structure. Furthermore, the method combines a tractable observation-adaptive proposal with posterior correction, ensuring accurate approximation of the nonlinear posterior distribution. Finally, we establish the corresponding posterior flow theory, from which the asymptotic exactness of the proposed method relative to finite-ensemble surrogates and the Wasserstein error bound are derived. Experiments on Double-Well, Lorenz-96, and Kolmogorov flow show that the proposed method captures complex posterior structure and remains accurate under sparse, nonlinear, and non-injective observations. In the sparse non-injective setting, it reduces RMSE by 56% relative to the best baseline.

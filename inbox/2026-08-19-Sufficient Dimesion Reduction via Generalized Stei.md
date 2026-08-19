---
title: "Sufficient Dimesion Reduction via Generalized Stein's Lemma"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.15121
priority: medium
status: unread
interest: medium
next_step: skim
---
# Sufficient Dimesion Reduction via Generalized Stein's Lemma
> 原文: [https://arxiv.org/abs/2608.15121](https://arxiv.org/abs/2608.15121)

arXiv:2608.15121v1 Announce Type: new
Abstract: Sufficient dimension reduction (SDR) seeks the minimal subspace of the predictors that captures the full conditional distribution of the response, which is known as the central subspace (CS). When the response is multivariate, the problem becomes considerably more challenging, particularly when the sample size is limited. Existing methods face different limitations:inverse regression approaches rely on strong distributional assumptions and matrix inversion, and their multi-response extensions suffer from severe slice sparsity; forward regression methods depend on computationally intensive iterative smoothing whose cost grows with the response dimension; and deep learning-based approaches demand large amounts of labeled data. To circumvent these shortcomings, we propose an SDR framework based on the generalized Stein's lemma. Our method constructs a cross-moment matrix between the multivariate response and the marginal score function of the predictors, and recovers the CS via its singular value decomposition. The proposed method does not rely on the linearity condition, avoids matrix inversion as well as iterative smoothing, and can leverage unlabeled data when available. We establish convergence guarantees for the proposed estimator under standard regularity conditions. Moreover, we propose a practical rank-selection algorithm to estimate the dimension of the CS. Extensive simulation studies and a real data application demonstrate that the proposed methods consistently outperform existing approaches across a variety of settings, particularly in moderate-dimensional, label-scarce scenarios with high noise levels.

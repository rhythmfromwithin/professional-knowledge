---
interest: medium
link: https://arxiv.org/abs/2604.19091
next_step: skim
priority: medium
slack_ts: '1776915202.414429'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Fast estimation of Gaussian mixture components via centering and singular value
  thresholding
---
# Fast estimation of Gaussian mixture components via centering and singular value thresholding
> 原文: [https://arxiv.org/abs/2604.19091](https://arxiv.org/abs/2604.19091)

arXiv:2604.19091v1 Announce Type: new
Abstract: Estimating the number of components is a fundamental challenge in unsupervised learning, particularly when dealing with high-dimensional data with many components or severely imbalanced component sizes. This paper addresses this challenge for classical Gaussian mixture models. The proposed estimator is simple: center the data, compute the singular values of the centered matrix, and count those above a threshold. No iterative fitting, no likelihood calculation, and no prior knowledge of the number of components are required. We prove that, under a mild separation condition on the component centers, the estimator consistently recovers the true number of components. The result holds in high-dimensional settings where the dimension can be much larger than the sample size. It also holds when the number of components grows to the smaller of the dimension and the sample size, even under severe imbalance among component sizes. Computationally, the method is extremely fast: for example, it processes ten million samples in one hundred dimensions within one minute. Extensive experimental studies confirm its accuracy in challenging settings such as high dimensionality, many components, and severe class imbalance.

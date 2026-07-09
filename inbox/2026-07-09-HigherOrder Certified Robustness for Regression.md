---
title: "Higher-Order Certified Robustness for Regression"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.05536
priority: medium
status: unread
interest: medium
next_step: skim
---
# Higher-Order Certified Robustness for Regression
> 原文: [https://arxiv.org/abs/2607.05536](https://arxiv.org/abs/2607.05536)

arXiv:2607.05536v1 Announce Type: new
Abstract: Randomized smoothing has emerged as a scalable technique for certifying the adversarial robustness of classifiers. However, its application to regression remains under-explored and faces unique challenges. Existing regression certificates rely on probabilistic acceptance regions and fail to exploit the local geometry of the function. In this work, we present a novel framework for certified robust regression that addresses these limitations. We derive a prediction-centered certificate that guarantees the stability of the smoothed model's prediction and ensures practical computability at test time. We investigate several alternatives for constructing these certificates by explicitly incorporating means, variances, and gradients. In particular, we demonstrate on the MNIST rotation task that utilizing gradient information yields significantly tighter robustness certificates compared to the current state-of-the-art, alpha-smoothing.

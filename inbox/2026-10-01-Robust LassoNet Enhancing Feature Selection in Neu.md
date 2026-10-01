---
title: "Robust LassoNet: Enhancing Feature Selection in Neural Networks via Robust Loss Functions"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.38263
priority: medium
status: unread
interest: medium
next_step: skim
---
# Robust LassoNet: Enhancing Feature Selection in Neural Networks via Robust Loss Functions
> 原文: [https://arxiv.org/abs/2609.38263](https://arxiv.org/abs/2609.38263)

arXiv:2609.38263v1 Announce Type: new
Abstract: Feature selection in neural networks remains a challenging problem, particularly in the presence of noisy or contaminated data. LassoNet is a recent approach that addresses this issue by combining neural networks with hierarchical sparsity constraints, enabling simultaneous prediction and variable selection. However, its standard formulation relies on the mean squared error (MSE) loss, which is known to be highly sensitive to outliers. In this paper, we present Robust LassoNet, an extension of LassoNet that incorporates robust loss functions, such as Huber, Cauchy, Tukey's bisquare, and Nonnegative Garrote, to mitigate the effect of extreme observations. The proposed approach preserves the original optimization framework while improving stability under data contamination. Through experiments on synthetic and real datasets, we show that robust LassoNet significantly improves both predictive performance and feature selection accuracy in the presence of outliers or heavy tailed noise, while maintaining comparable performance in clean settings. These results highlight the importance of robustness in neural network based feature selection and suggest practical guidelines for choosing appropriate loss functions.

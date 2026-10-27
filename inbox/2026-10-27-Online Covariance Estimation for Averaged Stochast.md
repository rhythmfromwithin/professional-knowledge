---
title: "Online Covariance Estimation for Averaged Stochastic Gradient Descent on Riemannian Manifolds"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.33419
priority: medium
status: unread
interest: medium
next_step: skim
---
# Online Covariance Estimation for Averaged Stochastic Gradient Descent on Riemannian Manifolds
> 原文: [https://arxiv.org/abs/2610.33419](https://arxiv.org/abs/2610.33419)

arXiv:2610.33419v1 Announce Type: new
Abstract: We study online inference for averaged Riemannian stochastic gradient descent (RSGD) when the unknown parameter lies on a manifold. Although the averaged RSGD iterate is asymptotically normal, practical inference requires estimating the unknown covariance operator in its limiting distribution. Existing online batch-means methods cannot be applied directly because a general Riemannian manifold lacks an addition operation, and the tangent space containing the Riemannian gradient varies across iterations. Through vector transport, we construct overlapping and non-overlapping covariance estimators that adaptively combine information from successive batches while accounting for the changing tangent spaces. The proposed estimators are online, require neither Riemannian Hessian computations nor a prespecified terminal sample size, and attain the same convergence rates as their Euclidean counterparts (Zhu et al., 2023). Together with asymptotic normality, these estimators enable online statistical inference for RSGD on manifolds. We illustrate the proposed framework through a detailed study of streaming principal component analysis on Grassmann manifolds.

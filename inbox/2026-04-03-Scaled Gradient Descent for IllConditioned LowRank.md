---
interest: medium
link: https://arxiv.org/abs/2604.00060
next_step: skim
priority: medium
slack_ts: '1775185092.580679'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Scaled Gradient Descent for Ill-Conditioned Low-Rank Matrix Recovery with Optimal
  Sampling Complexity
---
# Scaled Gradient Descent for Ill-Conditioned Low-Rank Matrix Recovery with Optimal Sampling Complexity
> 原文: [https://arxiv.org/abs/2604.00060](https://arxiv.org/abs/2604.00060)

arXiv:2604.00060v1 Announce Type: new
Abstract: The low-rank matrix recovery problem seeks to reconstruct an unknown $n\_1 \times n\_2$ rank-$r$ matrix from $m$ linear measurements, where $m\ll n\_1n\_2$. This problem has been extensively studied over the past few decades, leading to a variety of algorithms with solid theoretical guarantees. Among these, gradient descent based non-convex methods have become particularly popular due to their computational efficiency. However, these methods typically suffer from two key limitations: a sub-optimal sample complexity of $O((n\_1 + n\_2)r^2)$ and an iteration complexity of $O(\kappa \log(1/\epsilon))$ to achieve $\epsilon$-accuracy, resulting in slow convergence when the target matrix is ill-conditioned. Here, $\kappa$ denotes the condition number of the unknown matrix. Recent studies show that a preconditioned variant of GD, known as scaled gradient descent (ScaledGD), can significantly reduce the iteration complexity to $O(\log(1/\epsilon))$. Nonetheless, its sample complexity remains sub-optimal at $O((n\_1 + n\_2)r^2)$. In contrast, a delicate virtual sequence technique demonstrates that the standard GD in the positive semidefinite (PSD) setting achieves the optimal sample complexity $O((n\_1 + n\_2)r)$, but converges more slowly with an iteration complexity $O(\kappa^2 \log(1/\epsilon))$. In this paper, through a more refined analysis, we show that ScaledGD achieves both the optimal sample complexity $O((n\_1 + n\_2)r)$ and the improved iteration complexity $O(\log(1/\epsilon))$. Notably, our results extend beyond the PSD setting to general low-rank matrix recovery problem. Numerical experiments further validate that ScaledGD accelerates convergence for ill-conditioned matrices with the optimal sampling complexity.

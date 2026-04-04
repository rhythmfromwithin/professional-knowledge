---
title: "Sven: Singular Value Descent as a Computationally Efficient Natural Gradient Method"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.01279
priority: high
status: unread
interest: medium
next_step: skim
---
# Sven: Singular Value Descent as a Computationally Efficient Natural Gradient Method
> 原文: [https://arxiv.org/abs/2604.01279](https://arxiv.org/abs/2604.01279)

arXiv:2604.01279v1 Announce Type: new
Abstract: We introduce Sven (Singular Value dEsceNt), a new optimization algorithm for neural networks that exploits the natural decomposition of loss functions into a sum over individual data points, rather than reducing the full loss to a single scalar before computing a parameter update. Sven treats each data point's residual as a separate condition to be satisfied simultaneously, using the Moore-Penrose pseudoinverse of the loss Jacobian to find the minimum-norm parameter update that best satisfies all conditions at once. In practice, this pseudoinverse is approximated via a truncated singular value decomposition, retaining only the $k$ most significant directions and incurring a computational overhead of only a factor of $k$ relative to stochastic gradient descent. This is in comparison to traditional natural gradient methods, which scale as the square of the number of parameters. We show that Sven can be understood as a natural gradient method generalized to the over-parametrized regime, recovering natural gradient descent in the under-parametrized limit. On regression tasks, Sven significantly outperforms standard first-order methods including Adam, converging faster and to a lower final loss, while remaining competitive with LBFGS at a fraction of the wall-time cost. We discuss the primary challenge to scaling, namely memory overhead, and propose mitigation strategies. Beyond standard machine learning benchmarks, we anticipate that Sven will find natural application in scientific computing settings where custom loss functions decompose into several conditions.

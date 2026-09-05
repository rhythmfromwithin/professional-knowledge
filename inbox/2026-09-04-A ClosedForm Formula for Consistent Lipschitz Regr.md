---
interest: medium
link: https://arxiv.org/abs/2609.03129
next_step: skim
priority: medium
slack_ts: '1788581039.561979'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A Closed-Form Formula for Consistent Lipschitz Regression on Metric Spaces
  with Sparse Neural Network Realizations
---
# A Closed-Form Formula for Consistent Lipschitz Regression on Metric Spaces with Sparse Neural Network Realizations
> 原文: [https://arxiv.org/abs/2609.03129](https://arxiv.org/abs/2609.03129)

arXiv:2609.03129v1 Announce Type: new
Abstract: Several classical machine-learning methods, such as KRRs and SVRs, are both computationally and analytically tractable since their estimators either admit closed-form expressions or are obtained by minimizing convex training objectives; neither feature is generally available for deep neural networks. We address this by introducing a simple closed-form ``two-stage'' compositional formula $\hat{f}$ for reconstructing an unknown Lipschitz function $f:\mathcal{X}\to \mathbb{R}$ on a metric space $(\mathcal X,\rho)$ from $N$ i.i.d. noisy observations.
Our main result is a high-probability uniform ($L^{\infty}$) recovery guarantee that jointly controls approximation and statistical errors while enjoying an optimization error of zero; in particular, we do not assume oracle access to an approximate ERM. Our secondary main results establish the optimality of our formula in three complementary senses. 1) Function space: On Ahlfors-regular metric spaces, the hypothesis class parameterized by our formula attains the optimal fat-shattering dimension. 2) Parameter space: Its dependence on the parameters is maximally numerically stable, in the sense that a smaller approximation error cannot be achieved with a smaller Lipschitz dependence on the model parameters. 3) Forward pass: Its dependence on the input is maximally regular, matching the Lipschitz constant of the target function $f$. When $\mathcal X=[0,1]^d$ is equipped with the $\ell^\infty$ norm, $\hat{f}$ admits algorithmic ReLU-MLP and exact ReLU-multi-head transformer realizations of depth $\mathcal{O}(\log(N))$ with $\mathcal{O}(N)$ nonzero parameters.

---
interest: medium
link: https://arxiv.org/abs/2611.31687
next_step: skim
priority: medium
slack_ts: '1795766096.727189'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Online Statistical Inference for Derivative-Free Constrained Stochastic Optimization
---
# Online Statistical Inference for Derivative-Free Constrained Stochastic Optimization
> 原文: [https://arxiv.org/abs/2611.31687](https://arxiv.org/abs/2611.31687)

arXiv:2611.31687v1 Announce Type: new
Abstract: We study statistical inference for nonlinear equality-constrained stochastic optimization problems in settings where derivative information is unavailable or expensive to obtain. While recent advances in stochastic sequential quadratic programming (SSQP) have enabled efficient online optimization, existing methods either rely on gradient information or suffer from high computational costs. To address these limitations, we develop a sketched derivative-free SSQP (SDF-SSQP) method that simultaneously achieves computational efficiency and valid statistical inference. By leveraging randomized sketching, the proposed method reduces the per-iteration computational cost to $O((d+m)^2)$, where $d$ is the dimension of the decision variable and $m$ is the number of constraints, making it well suited for large-scale problems. To overcome the challenges that both sketching and zeroth-order approximations introduce for statistical inference, we adopt a random-scaling approach that eliminates the need for explicit estimation of the asymptotic covariance matrix. We establish the asymptotic normality of the averaged primal--dual iterates and construct a self-normalized statistic that is asymptotically pivotal. The resulting inference procedure is fully online, requires neither covariance estimation nor matrix inversion, and incurs an additional per-iteration cost of the same order as that of the optimization update. Numerical experiments demonstrate the effectiveness of the proposed method in terms of both optimization performance and statistical inference accuracy.

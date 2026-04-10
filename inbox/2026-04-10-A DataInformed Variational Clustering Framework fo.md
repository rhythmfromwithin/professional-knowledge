---
interest: medium
link: https://arxiv.org/abs/2604.06864
next_step: skim
priority: medium
slack_ts: '1775791744.899219'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A Data-Informed Variational Clustering Framework for Noisy High-Dimensional
  Data
---
# A Data-Informed Variational Clustering Framework for Noisy High-Dimensional Data
> 原文: [https://arxiv.org/abs/2604.06864](https://arxiv.org/abs/2604.06864)

arXiv:2604.06864v1 Announce Type: new
Abstract: Clustering in high-dimensional settings with severe feature noise remains challenging, especially when only a small subset of dimensions is informative and the final number of clusters is not specified in advance. In such regimes, partition recovery, feature relevance learning, and structural adaptation are tightly coupled, and standard likelihood-based methods can become unstable or overly sensitive to noisy dimensions. We propose DIVI, a data-informed variational clustering framework that combines global feature gating with split-based adaptive structure growth. DIVI uses informative prior initialization to stabilize optimization, learns feature relevance in a differentiable manner, and expands model complexity only when local diagnostics indicate underfit. Beyond clustering performance, we also examine runtime scalability and parameter sensitivity in order to clarify the computational and practical behavior of the framework. Empirically, we find that DIVI performs competitively under severe feature noise, remains computationally feasible, and yields interpretable feature-gating behavior, while also exhibiting conservative growth and identifiable failure regimes in challenging settings. Overall, DIVI is best viewed as a practical variational clustering framework for noisy high-dimensional data rather than as a fully Bayesian generative solution.

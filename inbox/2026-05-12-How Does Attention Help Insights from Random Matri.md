---
interest: medium
link: https://arxiv.org/abs/2605.06826
next_step: skim
priority: medium
slack_ts: '1778644942.099899'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: How Does Attention Help? Insights from Random Matrices on Signal Recovery from
  Sequence Models
---
# How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models
> 原文: [https://arxiv.org/abs/2605.06826](https://arxiv.org/abs/2605.06826)

arXiv:2605.06826v1 Announce Type: new
Abstract: We study the spectral properties of sample covariance matrices constructed from pooled sequence representations, where token embeddings are drawn from a fixed two-class Gaussian mixture table and pooled via (fixed) attention weights. Working in the high-dimensional regime $d,V,N\to\infty$ with $d/V\to\delta$ and $d/N\to\gamma$, we derive exact characterizations of the limiting eigenvalue distribution, outlier eigenvalues, and eigenvector alignment with the hidden signal. The bulk spectrum follows a non-Marchenko--Pastur law given by the free multiplicative convolution $\kappa(MP\_\delta\boxtimes MP\_\gamma)$, reflecting the finite vocabulary structure. Signal recovery undergoes two successive BBP-type phase transitions characterized by the scalars: $\delta,\gamma,\alpha=w^{\top} R w$ and $\kappa=\|w\|^2$, where $w$ denotes the attention pooling weights and $R$ the positional correlation matrix. An aftermath of our analysis demonstrates that the optimal attention weights maximizing the signal-to-noise ratio $\alpha/\kappa$ are given by the (normalized) top eigenvector of $R$, and we show (as a particular case of our analysis) that parameter-free causal self-attention with $\tau/d$ score scaling yields deterministic harmonic weights that improve signal recovery over mean pooling whenever early tokens carry more signal. Extensive simulations confirm sharp agreement between theory and finite-dimensional experiments.

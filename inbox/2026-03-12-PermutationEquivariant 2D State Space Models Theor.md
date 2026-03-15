---
interest: medium
link: https://arxiv.org/abs/2603.08753
next_step: skim
priority: medium
slack_ts: '1773544825.379129'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Permutation-Equivariant 2D State Space Models: Theory and Canonical Architecture
  for Multivariate Time Series'
---
# Permutation-Equivariant 2D State Space Models: Theory and Canonical Architecture for Multivariate Time Series
> 原文: [https://arxiv.org/abs/2603.08753](https://arxiv.org/abs/2603.08753)

arXiv:2603.08753v1 Announce Type: new
Abstract: Multivariate time series (MTS) modeling often implicitly imposes an artificial ordering over variables, violating the inherent exchangeability found in many real-world systems where no canonical variable axis exists. We formalize this limitation as a violation of the permutation symmetry principle and require state-space dynamics to be permutation-equivariant along the variable axis. In this work, we theoretically characterize the complete canonical form of linear variable coupling under this symmetry constraint. We prove that any permutation-equivariant linear 2D state-space system naturally decomposes into local self-dynamics and a global pooled interaction, rendering ordered recurrence not only unnecessary but structurally suboptimal. Motivated by this theoretical foundation, we introduce the Variable-Invariant Two-Dimensional State Space Model (VI 2D SSM), which realizes the canonical equivariant form via permutation-invariant aggregation. This formulation eliminates sequential dependency chains along the variable axis, reducing the dependency depth from $\mathcal{O}(C)$ to $\mathcal{O}(1)$ and simplifying stability analysis to two scalar modes. Furthermore, we propose VI 2D Mamba, a unified architecture integrating multi-scale temporal dynamics and spectral representations. Extensive experiments on forecasting, classification, and anomaly detection benchmarks demonstrate that our model achieves state-of-the-art performance with superior structural scalability, validating the theoretical necessity of symmetry-preserving 2D modeling.

---
interest: medium
link: https://arxiv.org/abs/2606.11221
next_step: skim
priority: medium
slack_ts: '1781153117.526669'
source: cs.CV - Computer Vision
status: unread
title: 'LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein
  Alignment'
---
# LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment
> 原文: [https://arxiv.org/abs/2606.11221](https://arxiv.org/abs/2606.11221)

arXiv:2606.11221v1 Announce Type: new
Abstract: We take a Gromov-Wasserstein perspective on Vision-Language-Action (VLA) learning, where the goal is to make the relational geometry of action representations compatible with the semantic geometry of VL embeddings. However, this alignment is non-trivial due to the mathematical heterogeneity between the domains: the semantic space of vision-language is topologically linear and isotropic, whereas the physical manifold of robotic action is non-Euclidean and anisotropic. Their disjoint metric structures render direct regression ill-posed. To resolve this incompatibility, we introduce LAST (Lie-algebraic Action Space Tokenizer), which reconstructs the action space to establish local metric compatibility with the VL modality via a two-stage transformation: (1) Global Topological Linearization: linearizing the action manifold via Lie-algebraic mapping, converting trajectories into a fixed-length, physically additive representation. (2) Local Metric Discretization: hierarchically discretizing the representation into schemas and whitened residuals, yielding approximately isotropic local charts that are statistically aligned with the semantic metric. By resolving the structural mismatch at both global and local levels, LAST enables VLA models with superior convergence and generalizability.

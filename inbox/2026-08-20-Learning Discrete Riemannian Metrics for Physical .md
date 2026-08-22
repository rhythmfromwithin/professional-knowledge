---
interest: medium
link: https://arxiv.org/abs/2608.14556
next_step: skim
priority: high
slack_ts: '1787362730.834659'
source: cs.LG - Machine Learning
status: unread
title: Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame
  Equivarianc
---
# Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame Equivarianc
> 原文: [https://arxiv.org/abs/2608.14556](https://arxiv.org/abs/2608.14556)

arXiv:2608.14556v1 Announce Type: new
Abstract: Physical fields on meshes require a separation between topology and geometry: conservation laws are topological and should be exact, while geometry, material response, and anisotropic coupling must be learned from data. Existing neural surrogates often mix these roles inside unconstrained message passing. We introduce Riemannian Hodge Message Passing (RHMP), which turns this separation into an architectural principle. RHMP fixes the cellular coboundaries ($d\_k$) determined by oriented incidence and learns symmetric positive-definite cochain metrics ($H\_k$) for geometry-dependent propagation. Treating $H\_k$ as the learned metric motivates cochain-frame equivariance: physical propagation should be invariant to orthogonal changes of the hidden cochain feature basis. RHMP implements this principle with metric-weighted Hodge blocks ($d\_k^\top H\_{k+1}d\_k$), yielding exact cochain-complex identities ($d\_{k+1}d\_k=0$), nonnegative Hodge energies, positive-semidefinite operators, and exact Abelian curvature invariance. Across seven physical benchmarks spanning fluids, electromagnetism, gauge fields, and variable-mesh CFD, RHMP achieves the best overall performance, with the largest gains when topology, learned geometry, and field structure interact.

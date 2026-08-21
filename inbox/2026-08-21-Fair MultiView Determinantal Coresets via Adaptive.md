---
title: "Fair Multi-View Determinantal Coresets via Adaptive NEPv"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.18181
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fair Multi-View Determinantal Coresets via Adaptive NEPv
> 原文: [https://arxiv.org/abs/2608.18181](https://arxiv.org/abs/2608.18181)

arXiv:2608.18181v1 Announce Type: new
Abstract: Selecting a small, diverse subset from a large candidate pool often means balancing several incompatible notions of diversity. In trademark curation, for instance, a subset should cover both the language used to describe marks and the visual space of their logos. A single determinantal point process (\DPP) kernel can hide failure in one view, and averaging kernels replaces the multi-view relaxation by an ordinary single-kernel spectral problem. We formulate \emph{fair multi-view determinant selection}: maximize the weakest per-view log determinant of a size-$k$ subset. We smooth this nonsmooth objective and relax it to the Stiefel manifold. The relaxation embeds every discrete subset exactly, but unlike its single-view counterpart it has no closed-form spectral solution in general. Its stationarity condition is a gauge-invariant nonlinear eigenvalue problem with eigenvector-dependent, view-adaptive weights. We derive an adaptive self-consistent-field (\SCF) solver with damping and level shifting, and round the resulting subspace by leverage-score screening followed by fair local refinement. The solver needs only feature-map products for each view. We report conflicting-view synthetic experiments and specify a multimodal USPTO protocol; the real-data multimodal results require aligned logo embeddings and are not claimed in this version.

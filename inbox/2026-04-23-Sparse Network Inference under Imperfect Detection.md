---
title: "Sparse Network Inference under Imperfect Detection and its Application to Ecological Networks"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.18820
priority: medium
status: unread
interest: medium
next_step: skim
---
# Sparse Network Inference under Imperfect Detection and its Application to Ecological Networks
> 原文: [https://arxiv.org/abs/2604.18820](https://arxiv.org/abs/2604.18820)

arXiv:2604.18820v1 Announce Type: new
Abstract: Recovering latent structure from count data has received considerable attention in network inference, particularly when one seeks both cross-group interactions and within-group similarity patterns in bipartite networks, which is widely used in ecology research. Such networks are often sparse and inherently imperfect in their detection. Existing models mainly focus on interaction recovery, while the induced similarity graphs are much less studied. Moreover, sparsity is often not controlled, and scale is unbalanced, leading to oversparse or poorly rescaled estimates with degrading structural recovery. To address these issues, we propose a framework for structured sparse nonnegative low-rank factorization with detection probability estimation. We impose nonconvex $\ell\_{1/2}$ regularization on the latent similarity and connectivity structures to promote sparsity within-group similarity and cross-group connectivity with better relative scale. The resulting optimization problem is nonconvex and nonsmooth. To solve it, we develop an ADMM-based algorithm with adaptive penalization and scale-aware initialization and establish its asymptotic feasibility and KKT stationarity of cluster points under mild regularity conditions. Experiments on synthetic and real-world ecological datasets demonstrate improved recovery of latent factors and similarity/connectivity structure relative to existing baselines.

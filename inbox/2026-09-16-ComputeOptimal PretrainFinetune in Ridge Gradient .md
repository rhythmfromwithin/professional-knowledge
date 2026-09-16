---
title: "Compute-Optimal Pretrain--Fine-tune in Ridge Gradient Descent"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.16262
priority: medium
status: unread
interest: medium
next_step: skim
---
# Compute-Optimal Pretrain--Fine-tune in Ridge Gradient Descent
> 原文: [https://arxiv.org/abs/2609.16262](https://arxiv.org/abs/2609.16262)

arXiv:2609.16262v1 Announce Type: new
Abstract: Pretraining followed by fine-tuning introduces a compute-allocation problem: under a fixed training budget, compute spent improving the upstream objective reduces the compute available for downstream adaptation. Despite its practical importance, this trade-off is not yet well understood theoretically, even in simple models. In this paper, we cast this allocation as a compute-split problem under a two-stage pretrain--fine-tune procedure with fixed total optimisation budget, using regularised least squares trained by gradient descent as a tractable setting. We characterise the optimal split under data-dependent evaluation geometries induced by the fine-tuning problem. Our results show that the allocation depends on how pretraining directions affect fine-tuning predictions and how fine-tuning shifts are seen through downstream data geometry. In particular, the relevant quantities are determined by prediction-relevant spectral components of the pretraining and fine-tuning empirical covariances. Technically, the analysis relies on a basis-invariant, eigenspace-level spectral decomposition, together with perturbative control of the non-commuting pretraining and fine-tuning dynamics.

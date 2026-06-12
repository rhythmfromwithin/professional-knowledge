---
interest: medium
link: https://arxiv.org/abs/2606.12471
next_step: skim
priority: medium
slack_ts: '1781239684.600649'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite
  Temporal Consistency'
---
# Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite Temporal Consistency
> 原文: [https://arxiv.org/abs/2606.12471](https://arxiv.org/abs/2606.12471)

arXiv:2606.12471v1 Announce Type: new
Abstract: Klindt, LeCun, and Balestriero (arXiv:2605.26379) proved that Joint-Embedding Predictive Architectures (JEPAs) achieve linear identifiability, the linear recovery of the world's true latent variables, if and only if the world's latent dynamics follow a Gaussian, stationary process. This Gaussian boundary implies a fundamental limit on temporal consistency: for any non-Gaussian physical system, the representation error of a statistical World Model grows monotonically with time. We prove that this limit is an artifact of the statistical alignment mechanism, not a property of World Models in general. We introduce the Physics-Grounded Symbolic Architecture (PGSA) and prove three results: (1) a PGSA achieves exact linear identifiability for all physical regimes, regardless of the latent distribution; (2) the per-step error of a PGSA is bounded by numerical precision alone; and (3) as a direct consequence, a PGSA maintains temporal consistency for an unbounded number of transitions, a property we term near-infinite temporal consistency. We further prove that statistical World Models cannot achieve this property for any non-Gaussian system, regardless of model capacity or the volume of training data. The algebraic cores of four of the theorems are formalized in Lean 4 with Mathlib4 v4.31.0 (zero sorry placeholders); the Klindt et al. converse is taken as an external premise. The contrast establishes that symbolic grounding in the causal generator of the world's dynamics is the sufficient condition and, in non-Gaussian regimes, the only condition for near-infinite temporal consistency.

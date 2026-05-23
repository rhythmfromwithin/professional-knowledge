---
interest: medium
link: https://arxiv.org/abs/2605.20271
next_step: skim
priority: medium
slack_ts: '1779508587.027529'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Multi-Head Attention as Ensemble Nadaraya-Watson Estimation: Variance Reduction,
  Decorrelation, and Optimal Head Diversity'
---
# Multi-Head Attention as Ensemble Nadaraya-Watson Estimation: Variance Reduction, Decorrelation, and Optimal Head Diversity
> 原文: [https://arxiv.org/abs/2605.20271](https://arxiv.org/abs/2605.20271)

arXiv:2605.20271v1 Announce Type: new
Abstract: We develop a rigorous statistical theory of multi-head attention (MHA) as an ensemble of Nadaraya-Watson (NW) kernel regression estimators. Building on the algebraic identity between single-head softmax attention and the NW estimator, we prove that MHA is a structured ensemble of H NW estimators, each operating in a distinct learned projection subspace of the key space. We derive an explicit Bias-Variance-Covariance decomposition of the MHA mean squared error, showing that variance reduction depends not merely on the number of heads H but fundamentally on the decorrelation of head outputs. Decorrelation is governed by the principal angles between learned projection subspaces: orthogonal projections yield maximum variance reduction; aligned projections yield none. We introduce the Head Diversity Index (HDI), a computable spectral measure of inter-head decorrelation, and prove that MHA mean squared error is monotonically decreasing in HDI. This provides the first rigorous theoretical explanation for the empirically observed specialization of attention heads. Under a fixed total-dimension budget D = H \* d\_k, we solve the optimal head-dimension allocation problem, deriving the MSE-minimizing pair (H\*, d\_k\*) from data distribution and regression smoothness. The solution yields a new architectural scaling law: the optimal per-head dimension grows logarithmically with training set size, while the optimal number of heads grows nearly linearly with the total budget D. Our framework unifies three strands of prior work: the NW theory of single-head attention, the general weighting theory for ensemble learning, and the decorrelation-variance-reduction isomorphism between biological and computational ensembles. Multi-head attention is the Transformer's instantiation of a universal principle: identical agents plus diversity-enforcing mechanisms yields emergent optimality.

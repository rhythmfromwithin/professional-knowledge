---
title: "Inference and Uncertainty Quantification for Streaming $r$-PCA"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.18374
priority: medium
status: unread
interest: medium
next_step: skim
---
# Inference and Uncertainty Quantification for Streaming $r$-PCA
> 原文: [https://arxiv.org/abs/2608.18374](https://arxiv.org/abs/2608.18374)

arXiv:2608.18374v1 Announce Type: new
Abstract: We address two open questions in streaming PCA via Oja's algorithm: sharp operator-norm convergence for general rank under sub-Gaussian data, and distributional inference for the resulting subspace estimator. Existing convergence analyses, even in the rank-one case, either assume bounded data or leave non-vanishing remainder terms that prevent adaptation to a polynomially vanishing tail spectrum, while existing distributional results are confined to the rank-one case. Our convergence theory removes these remainder terms and yields a sharp rate. In the dense-tail spiked covariance regime, this rate matches the minimax rate up to logarithmic factors. More generally, we prove a matching lower bound, up to logarithmic factors, across both dense-tail and sparse-tail regimes under a mild nondegeneracy condition. The analysis yields a linearization of Oja's iterates, which in turn enables a high-dimensional Gaussian approximation for the general-rank subspace estimation error with an explicit limiting covariance. We also establish a row-wise Gaussian approximation over convex sets for the aligned difference, recovering prior rank-one results as special cases. For practical inference, we develop an online multiplier bootstrap algorithm and prove its consistency. Beyond streaming PCA, our techniques contribute to Gaussian approximation and bootstrap inference for nonconvex stochastic approximation.

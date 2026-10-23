---
title: "Spectral Uncertainty Decomposition for Sparse Bayesian Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.30207
priority: high
status: unread
interest: medium
next_step: skim
---
# Spectral Uncertainty Decomposition for Sparse Bayesian Learning
> 原文: [https://arxiv.org/abs/2610.30207](https://arxiv.org/abs/2610.30207)

arXiv:2610.30207v1 Announce Type: new
Abstract: Estimating distributed neural sources from M/EEG measurements is an ill-posed inverse problem where principled uncertainty quantification remains challenging. The usual conditional Gaussian posterior covariance does not explicitly distinguish uncertainty along likelihood-visible source directions from uncertainty that is invisible to the measurements. We propose a spectral framework based on the singular value structure of the prior-preconditioned forward operator, which provides an exact, interpretable decomposition of the posterior covariance into data-informed and indeterminacy epistemic components. This formulation identifies uncertainty contributions that are reducible by better measurements from those that are fundamentally irreducible by sensing geometry. We further derive an equivalent subtractive decomposition that expresses the prior covariance as the sum of posterior and data-driven reduction terms, enabling precise accounting of uncertainty reduction through Bayesian learning. Together, these complementary representations offer both theoretical insight and practical tools for interpretable uncertainty quantification in M/EEG source imaging for linear-Gaussian Bayesian inverse solvers where the posterior covariance is available in closed form.

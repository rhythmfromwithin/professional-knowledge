---
interest: medium
link: https://arxiv.org/abs/2608.25052
next_step: skim
priority: medium
slack_ts: '1787914965.544399'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Improved Analysis for Hessian-free High-resolution Monte Carlo Sampling
---
# Improved Analysis for Hessian-free High-resolution Monte Carlo Sampling
> 原文: [https://arxiv.org/abs/2608.25052](https://arxiv.org/abs/2608.25052)

arXiv:2608.25052v1 Announce Type: new
Abstract: Hessian-free high-resolution (HFHR) dynamics augments underdamped Langevin dynamics (ULD) with reversible position diffusion for sampling problems that arise in machine learning. We establish an explicit quantitative contraction rate for HFHR dynamics under a position Poincar\'e inequality, weighted Hessian and Laplacian bounds, and a compact Sobolev embedding, where the potential function is not necessarily convex. An adapted time-augmented Poincar\'e inequality yields an explicit rate that improves upon the contraction rate of the underdamped Langevin dynamics. We also give a weak-solution construction and a self-contained spectral proof of the divergence lemma underlying the argument. For HFHR Monte Carlo (HFHRMC) algorithm, which is based on a discretization scheme of HFHR dynamics, we use a path-space Girsanov argument to obtain a non-asymptotic convergence bound and an explicit iteration complexity in total variation distance. The bounds hold for every $\alpha\geq0$ and $\gamma>0$ and remain regular at the ULD endpoint. Optimizing the iteration complexity bound yields a positive, accuracy-dependent position-diffusion parameter at finite accuracy, while its leading high-accuracy order coincides with that of the optimized ULD endpoint. Our iteration complexity bound improves upon the existing work on HFHR algorithms. Numerical experiments including Bayesian learning problems on real data are provided to illustrate the effect of positive $\alpha$ and its benefit.

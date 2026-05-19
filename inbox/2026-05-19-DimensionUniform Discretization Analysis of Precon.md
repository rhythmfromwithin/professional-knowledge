---
title: "Dimension-Uniform Discretization Analysis of Preconditioned Annealed Langevin Dynamics for Multimodal Gaussian Mixtures"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.16473
priority: medium
status: unread
interest: medium
next_step: skim
---
# Dimension-Uniform Discretization Analysis of Preconditioned Annealed Langevin Dynamics for Multimodal Gaussian Mixtures
> 原文: [https://arxiv.org/abs/2605.16473](https://arxiv.org/abs/2605.16473)

arXiv:2605.16473v1 Announce Type: new
Abstract: Obtaining stable diffusion-based samplers in high- and infinite-dimensional settings is challenging because errors can accumulate across high-frequency coordinates and make the dynamics unstable under refinement of the finite-dimensional approximation of the underlying function-space problem. Discretization is a typical source of such errors, and preconditioning with a suitable spectral decay is one way to control their accumulation. In this paper, we study this problem for preconditioned annealed Langevin dynamics (ALD) applied to Gaussian mixtures. We first show that Euler-Maruyama (EM) discretization, by treating the stiff linear part of the annealed score with a forward Euler step, imposes a stability constraint coupling the preconditioner with the annealed covariance scale. Together with the conditions ensuring dimension-uniform control of the annealed dynamics, this constraint forces the initial smoothed law to remain uniformly close to the target across dimensions. We then consider an exponential-integrator scheme that integrates the stiff linear part of the annealed score exactly. Under explicit spectral summability conditions coupling the smoothing covariance, the component covariance spectra, and the preconditioner, we prove a dimension-uniform Kullback-Leibler (KL) bound for this scheme. This bound can be made arbitrarily small, uniformly in dimension, by allowing enough time for annealing and then refining the time mesh accordingly. Importantly, these conditions allow regimes in which the KL divergence between the target and the initial smoothed law diverges with dimension, showing that the restrictions imposed by EM are scheme-dependent rather than intrinsic to ALD.

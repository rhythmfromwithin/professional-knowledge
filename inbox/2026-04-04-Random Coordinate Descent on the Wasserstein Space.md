---
title: "Random Coordinate Descent on the Wasserstein Space of Probability Measures"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.01606
priority: medium
status: unread
interest: medium
next_step: skim
---
# Random Coordinate Descent on the Wasserstein Space of Probability Measures
> 原文: [https://arxiv.org/abs/2604.01606](https://arxiv.org/abs/2604.01606)

arXiv:2604.01606v1 Announce Type: new
Abstract: Optimization over the space of probability measures endowed with the Wasserstein-2 geometry is central to modern machine learning and mean-field modeling. However, traditional methods relying on full Wasserstein gradients often suffer from high computational overhead in high-dimensional or ill-conditioned settings. We propose a randomized coordinate descent framework specifically designed for the Wasserstein manifold, introducing both Random Wasserstein Coordinate Descent (RWCD) and Random Wasserstein Coordinate Proximal{-Gradient} (RWCP) for composite objectives. By exploiting coordinate-wise structures, our methods adapt to anisotropic objective landscapes where full-gradient approaches typically struggle. We provide a rigorous convergence analysis across various landscape geometries, establishing guarantees under non-convex, Polyak-{\L}ojasiewicz, and geodesically convex conditions. Our theoretical results mirror the classic convergence properties found in Euclidean space, revealing a compelling symmetry between coordinate descent on vectors and on probability measures. The developed techniques are inherently adaptive to the Wasserstein geometry and offer a robust analytical template that can be extended to other optimization solvers within the space of measures. Numerical experiments on ill-conditioned energies demonstrate that our framework offers significant speedups over conventional full-gradient methods.

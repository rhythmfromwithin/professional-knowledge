---
interest: medium
link: https://arxiv.org/abs/2605.04255
next_step: skim
priority: medium
slack_ts: '1778211648.439439'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Entropic Riemannian Neural Optimal Transport
---
# Entropic Riemannian Neural Optimal Transport
> 原文: [https://arxiv.org/abs/2605.04255](https://arxiv.org/abs/2605.04255)

arXiv:2605.04255v1 Announce Type: new
Abstract: Many machine learning problems involve data supported on curved spaces such as spheres, rotation groups, hyperbolic spaces, and general Riemannian manifolds, where Euclidean geometry can distort distances, averages, and the resulting optimal transport (OT) problem. Existing manifold OT methods have pursued amortized out-of-sample maps, while entropic regularization has made discrete OT more scalable, but these advantages have remained largely disjoint. We propose Entropic Riemannian Neural Optimal Transport (Entropic RNOT), a unified framework that combines intrinsic entropic OT with amortized out-of-sample evaluation on Riemannian manifolds. Our method learns a single target-side Schr\"odinger potential through a neural pullback parameterization, recovers the induced Gibbs coupling, and uses the resulting conditional laws to construct intrinsic transport surrogates. These include barycentric projections on Cartan-Hadamard manifolds and heat-smoothed conditional surrogates on stochastically complete manifolds, the latter turning possibly atomic target laws into absolutely continuous ones. For fixed regularization $\varepsilon>0$, we prove that the proposed hypothesis class recovers the entropic optimal coupling in strong probabilistic metrics. As consequences, barycentric surrogates converge in $L^2$, while heat-smoothed surrogates are stable at fixed heat time and asymptotically unbiased as the heat time vanishes. The guarantees hold for compactly supported data on possibly noncompact manifolds. Empirically, our method matches or improves over Euclidean, tangent-space, and log-Euclidean baselines on benchmarks over $\mathbb{S}^2$, $\mathrm{SO}(3)$, $\mathrm{SPD}(3)$, $\mathrm{SE}(3)$, and $\mathbb{H}^2$, scales favorably relative to discrete manifold Sinkhorn, and in a protein-ligand docking application, refines poses on $\mathrm{SE}(3)$ without retraining or per-instance optimization.

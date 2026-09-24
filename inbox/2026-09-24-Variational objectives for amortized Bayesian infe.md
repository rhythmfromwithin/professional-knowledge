---
title: "Variational objectives for amortized Bayesian inference in inverse problems: The role of posterior conditioning"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.25145
priority: medium
status: unread
interest: medium
next_step: skim
---
# Variational objectives for amortized Bayesian inference in inverse problems: The role of posterior conditioning
> 原文: [https://arxiv.org/abs/2609.25145](https://arxiv.org/abs/2609.25145)

arXiv:2609.25145v1 Announce Type: new
Abstract: Variational autoencoders (VAEs) offer an efficient approach to amortized Bayesian inference for inverse problems, but posterior accuracy can depend strongly on the choice of variational regularization, particularly when the inverse problem contains weakly identified parameter directions. This study investigates three objectives: a reverse Kullback--Leibler formulation (VAE-KL), an asymmetric Jensen--Shannon formulation (VAE-JS), and a Jensen--Shannon--Wasserstein formulation (VAE-JSWA), which replaces the reverse Kullback--Leibler regularizer with the squared 2-Wasserstein distance while retaining forward-Kullback--Leibler posterior supervision. A full-covariance Gaussian encoder and a pre-trained physics-based surrogate are used for amortized posterior inference. A local linear--Gaussian analysis in the generalized Fisher basis is developed to characterize the variance-dependent gradients of the three objectives. The formulations are first evaluated using linear--Gaussian benchmarks with known posterior solutions and subsequently tested on nonlinear physics-based inverse problems, including an inverse problem governed by a linear ODE and two PDE-constrained problems. VAE-KL performs slightly better than the other formulations in the well-conditioned benchmark, where all three approaches yield comparable posterior approximations, whereas VAE-JSWA provides substantially lower posterior errors in the strongly ill-conditioned benchmark. The nonlinear physics-based problems exhibit a similar conditioning-dependent trend, with JS-based formulations providing greater benefit as posterior ill-conditioning increases. These results indicate that posterior conditioning is an important factor in selecting variational objectives and motivate geometry-adaptive variational inference for Bayesian inverse problems.

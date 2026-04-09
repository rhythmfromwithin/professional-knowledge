---
title: "StrADiff: A Structured Source-Wise Adaptive Diffusion Framework for Linear and Nonlinear Blind Source Separation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.04973
priority: medium
status: unread
interest: medium
next_step: skim
---
# StrADiff: A Structured Source-Wise Adaptive Diffusion Framework for Linear and Nonlinear Blind Source Separation
> 原文: [https://arxiv.org/abs/2604.04973](https://arxiv.org/abs/2604.04973)

arXiv:2604.04973v1 Announce Type: new
Abstract: This paper presents a Structured Source-Wise Adaptive Diffusion Framework for linear and nonlinear blind source separation. The framework interprets each latent dimension as a source component and assigns to it an individual adaptive diffusion mechanism, thereby establishing source-wise latent modeling rather than relying on a single shared latent prior. The resulting formulation learns source recovery and the mixing/reconstruction process jointly within a unified end-to-end objective, allowing model parameters and latent sources to adapt simultaneously during training. This yields a common framework for both linear and nonlinear blind source separation. In the present instantiation, each source is further equipped with its own adaptive Gaussian process (GP) prior to impose source-wise temporal structure on the latent trajectories, while the overall framework is not restricted to Gaussian process priors and can in principle accommodate other structured source priors. The proposed model thus provides a general structured diffusion-based route to unsupervised source recovery, with potential relevance beyond blind source separation to interpretable latent modeling, source-wise disentanglement, and potentially identifiable nonlinear latent-variable learning under appropriate structural conditions.

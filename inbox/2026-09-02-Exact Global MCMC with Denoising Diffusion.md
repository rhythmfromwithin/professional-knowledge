---
interest: medium
link: https://arxiv.org/abs/2609.00279
next_step: skim
priority: medium
slack_ts: '1788408228.041479'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Exact Global MCMC with Denoising Diffusion
---
# Exact Global MCMC with Denoising Diffusion
> 原文: [https://arxiv.org/abs/2609.00279](https://arxiv.org/abs/2609.00279)

arXiv:2609.00279v1 Announce Type: new
Abstract: This work shows that diffusion models learned with standard denoising loss can provide effective global MCMC proposals for complex high-dimensional target densities. The method is motivated by the observation that sequentially applying a forward and reverse diffusion process defines a Markov chain with a target stationary distribution for an ideal denoiser trained on samples of the target distribution. This observation can be made exact for any denoiser by applying a Metropolis-Hastings step whose acceptance ratio includes the density of the forward and reverse paths of a discrete time SDE approximation. We therefore propose to train denoising diffusion models on locally convergent MALA samples to learn global MCMC proposals. We call the composition of the global denoiser-based path sampler and a local MALA sampler Denoising Diffusion Monte Carlo (DDMC). Experiments show that DDMC can provide global proposals with high acceptance across a variety of complex target densities. Our results offer preliminary evidence that the established scaling behavior of standard diffusion training transfers directly to exact sampling from high-dimensional unnormalized densities.

---
interest: medium
link: https://arxiv.org/abs/2605.16486
next_step: skim
priority: medium
slack_ts: '1779337378.539859'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'StAD: Stein Amortized Divergence for Fast Likelihoods with Diffusion and Flow'
---
# StAD: Stein Amortized Divergence for Fast Likelihoods with Diffusion and Flow
> 原文: [https://arxiv.org/abs/2605.16486](https://arxiv.org/abs/2605.16486)

arXiv:2605.16486v1 Announce Type: new
Abstract: Diffusion and flow-based models are ubiquitously used for generative modelling and density estimation. They admit a deterministic probability flow ordinary differential equation (PF-ODE), analogous to continuous normalizing flows (CNFs), which describes the transport of the probability mass. Obtaining the likelihood from these models is of interest to many workflows, especially Bayesian analysis, and requires solving the trace of the Jacobian to compute the divergence of the learned PF-ODE, which is either $\mathcal{O}(D^2)$ to compute exactly or $\mathcal{O}(D)$ with a noisy estimate. We introduce StAD, a new distillation method to predict and learn the divergence of the PF-ODE using the Langevin-Stein operator without ever computing the Jacobian. We show that our method is competitive with the Hutchinson and Hutch++ on CIFAR-10, ImageNet and other density estimation tasks, consistently improving the variance and speed of the likelihood predictions compared to the Hutchinson. We additionally show our method will generalize to a varied class of generative models, and show that under some regularity conditions these learned vector fields can be made to satisfy the Stein class.

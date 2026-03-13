---
interest: medium
link: https://arxiv.org/abs/2603.00772
next_step: skim
priority: medium
slack_ts: '1773369784.267419'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Initialization-Aware Score-Based Diffusion Sampling
---
# Initialization-Aware Score-Based Diffusion Sampling
> 原文: [https://arxiv.org/abs/2603.00772](https://arxiv.org/abs/2603.00772)

arXiv:2603.00772v1 Announce Type: new
Abstract: Score-based generative models (SGMs) aim at generating samples from a target distribution by approximating the reverse-time dynamics of a stochastic differential equation. Despite their strong empirical performance, classical samplers initialized from a Gaussian distribution require a long time horizon noising typically inducing a large number of discretization steps and high computational cost. In this work, we present a Kullback-Leibler convergence analysis of Variance Exploding diffusion samplers that highlights the critical role of the backward process initialization. Based on this result, we propose a theoretically grounded sampling strategy that learns the reverse-time initialization, directly minimizing the initialization error. The resulting procedure is independent of the specific score training procedure, network architecture, and discretization scheme. Experiments on toy distributions and benchmark datasets demonstrate competitive or improved generative quality while using significantly fewer sampling steps.

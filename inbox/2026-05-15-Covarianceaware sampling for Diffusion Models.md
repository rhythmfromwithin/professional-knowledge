---
interest: medium
link: https://arxiv.org/abs/2605.13910
next_step: skim
priority: medium
slack_ts: '1778903340.459429'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Covariance-aware sampling for Diffusion Models
---
# Covariance-aware sampling for Diffusion Models
> 原文: [https://arxiv.org/abs/2605.13910](https://arxiv.org/abs/2605.13910)

arXiv:2605.13910v1 Announce Type: new
Abstract: We present a covariance-aware sampler that improves the quality of pixel-space Diffusion Model (DM) sampling in the few-step regime. We hypothesize that in the few-step regime samplers fail because they rely solely on the predicted mean of the reverse distribution, while our solution explicitly models the reverse-process covariance. Our method combines Tweedie's formula to estimate the covariance with an efficient, structured Fourier-space decomposition of the covariance matrix. Implemented as an extension of DDIM, our method requires only a minimal overhead: one extra Jacobian-Vector Product (JVP) per step. We demonstrate that for pixel-based DMs, our method consistently produces superior samples compared to state-of-the-art second order samplers (Heun, DPM-Solver++) and the recent aDDIM sampler, at an identical number of function evaluations (NFE).

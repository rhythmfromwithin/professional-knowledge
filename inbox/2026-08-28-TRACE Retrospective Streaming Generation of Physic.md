---
title: "TRACE: Retrospective Streaming Generation of Physical Fields under Sparse Structured Sensing"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.26219
priority: medium
status: unread
interest: medium
next_step: skim
---
# TRACE: Retrospective Streaming Generation of Physical Fields under Sparse Structured Sensing
> 原文: [https://arxiv.org/abs/2608.26219](https://arxiv.org/abs/2608.26219)

arXiv:2608.26219v1 Announce Type: new
Abstract: Reconstructing continuous physical fields from sparse measurements is central to scientific monitoring, inverse modeling, and digital-twin construction. Generative reconstruction has recently emerged as a promising paradigm for this task by learning data-driven physical priors that complete plausible full fields from limited observations. However, existing methods largely assume fixed, batch conditioning, whereas real sensing systems often produce structured streams: probes scan local regions, instruments observe moving fields of view, and communication constraints may leave entire frames missing. We propose TRACE, a retrospective streaming generative reconstruction framework for physical fields under structured sensing. TRACE performs approximate Bayesian inference in a learned continuous-coordinate latent space, converting sparse off-grid measurements into generative latent evidence, fusing it with a state-space temporal prior through Kalman-style filtering, and refining under-observed past frames via retrospective smoothing. Experiments on active matter, ocean sound-speed fields, and supernova simulations show that TRACE matches or surpasses frame-wise generative reconstructors, offline spatiotemporal methods, and streaming data-assimilation baselines in reconstruction quality under temporally sparse and spatially localized sensing protocols.

---
interest: medium
link: https://arxiv.org/abs/2605.28961
next_step: skim
priority: medium
slack_ts: '1780028401.274169'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Dynamics of Stochastic Momentum with Sparse Updates in High Dimensions
---
# Dynamics of Stochastic Momentum with Sparse Updates in High Dimensions
> 原文: [https://arxiv.org/abs/2605.28961](https://arxiv.org/abs/2605.28961)

arXiv:2605.28961v1 Announce Type: new
Abstract: Existing theory of momentum assumes that gradients arrive at every parameter at a roughly constant rate, an assumption violated in practice by heavy-tailed data distributions and modern architectures. We theoretically analyze the dynamics of two tractable models of momentum under sparse updates: a least squares model with sparse inputs and a logistic regression model with a rare class. Both admit exact closed-form second-moment dynamics whose high-dimensional limits we characterize across three scaling exponents for sparsity, batch size, and momentum decay. The phase structure on both problems is governed by the ratio of two intrinsic timescales: a momentum retention timescale (how many active updates the buffer survives) and a learning timescale (how many active updates it takes to reduce the squared error). When learning is much slower than retention, the limit matches SGD; when learning is faster, the system is unstable; where the timescales coincide, we recover classical heavy-ball dynamics. The oscillatory dynamics occur at different momentum values for different token sparsity, creating a spectral conflict for global momentum across token frequencies.

---
interest: medium
link: https://arxiv.org/abs/2609.10589
next_step: skim
priority: high
slack_ts: '1789100112.208249'
source: cs.LG - Machine Learning
status: unread
title: 'Halo: Improving forecast accuracy through heteroscedastic estimation'
---
# Halo: Improving forecast accuracy through heteroscedastic estimation
> 原文: [https://arxiv.org/abs/2609.10589](https://arxiv.org/abs/2609.10589)

arXiv:2609.10589v1 Announce Type: new
Abstract: Heteroscedastic forecasting, where a network estimates a scale parameter alongside a location parameter, is normally motivated by uncertainty quantification. This paper shows it also improves the point estimate, in contrast to reported negative results for heteroscedastic estimation outside time series. Halo is a modification that reuses an existing deep forecaster's architecture, giving it a second output for the scale of its implied distribution and training it under the matching negative log likelihood. Adapting three state-of-the-art models --- a transformer, a graph network paired with a variational autoencoder, and a single-layer convolutional network --- under both Gaussian and Laplacian losses demonstrates the phenomenon. On the five electricity price markets of a standard forecasting benchmark, Halo improves MSE and MAE in 28 of 30 model-market-metric comparisons, cutting average MSE by 2.6% to 16.5% and average MAE by 1.7% to 11.0%. Two findings emerge: (1) whether the scale estimate comes from a second projection head or from a full parallel network matters far less than whether the network estimates scale, and (2) the improvement holds under the hyperparameters already tuned for the point-estimate baseline, so retuning is optional.

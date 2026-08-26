---
interest: medium
link: https://arxiv.org/abs/2608.20998
next_step: skim
priority: low
slack_ts: '1787708788.956539'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Free-Probability Kernels for Zero-Rollout Hyperparameter Selection in Reservoir
  Computing
---
# Free-Probability Kernels for Zero-Rollout Hyperparameter Selection in Reservoir Computing
> 原文: [https://arxiv.org/abs/2608.20998](https://arxiv.org/abs/2608.20998)

arXiv:2608.20998v1 Announce Type: cross
Abstract: Reservoir computing (RC) couples a fixed recurrent dynamical system with a trained lightweight readout, but this efficiency is partly lost during hyperparameter selection: the recurrent gain, input scale, and leakage rate determine the reservoir's stability and temporal processing regime and are usually tuned through many rollouts. We introduce a deterministic, pilot-informed selector for leaky linear reservoirs followed by coordinate-wise nonlinear features. Free probability yields cross-lag propagation coefficients that summarize how the reservoir mixes past inputs. In the large-width limit, these coefficients define a deterministic temporal kernel that approximates the finite-reservoir feature geometry. Kernel ridge regression on a short labelled pilot sequence therefore ranks candidate operating regimes without instantiating or rolling out a reservoir, and the selected configuration transfers across widths. Across ten synthetic temporal benchmarks, zero-rollout selection obtains a mean deployment score of $0.772$, compared with $0.774$ for exhaustive simulation-based search, while avoiding $156\,600$ selection rollouts. With a small rollout budget, the proposed ranking provides the strongest mean performance at every tested budget and reaches the exhaustive reference using $4.8\%$ of its rollout cost. On four public electricity-transformer-temperature (ETT) forecasting datasets, five retained candidates recover the exhaustive operating point on three datasets. On multivariate cellular-traffic forecasting, 15 rollouts per cell reach the 462-rollout exhaustive reference and outperform random search and Bayesian optimization at low budgets. These results position free-probability kernels as deterministic surrogates for selecting reservoir operating regimes when validation rollouts are scarce.

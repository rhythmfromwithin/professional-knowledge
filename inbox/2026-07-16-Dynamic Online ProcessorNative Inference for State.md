---
interest: medium
link: https://arxiv.org/abs/2607.12095
next_step: skim
priority: medium
slack_ts: '1784258634.330279'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Dynamic Online Processor-Native Inference for State Estimation
---
# Dynamic Online Processor-Native Inference for State Estimation
> 原文: [https://arxiv.org/abs/2607.12095](https://arxiv.org/abs/2607.12095)

arXiv:2607.12095v1 Announce Type: new
Abstract: Sensor-rich data-driven applications increasingly use Bayesian approaches to infer latent states of dynamic systems from noisy sensor measurements and physical models. Yet the computation of the likelihood remains an essential bottleneck for accurate posteriors and performant inference. This paper presents a Bayesian filtering technique that uses processor-native uncertainty tracking for both uncertainty propagation and inference. The technique implements deterministic hierarchical importance restructuring through a native operation, giving deterministic latency and bounded memory use for arbitrary models written as program code. Benchmarks across three nonlinear state-space systems compare the approach against particle filters and Monte-Carlo-based likelihood estimators. The technique enables deterministic approximate filtering with as high as 805$\times$ average speedup against direct Monte Carlo work at matched result quality for model evaluation, and Pareto-dominant accuracy-latency trade-offs for posterior inference while remaining competitive in RMSE with baseline particle filters.

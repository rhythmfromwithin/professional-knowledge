---
interest: medium
link: https://arxiv.org/abs/2604.08569
next_step: skim
priority: high
slack_ts: '1776223649.854009'
source: cs.LG - Machine Learning
status: unread
title: Memory-Guided Trust-Region Bayesian Optimization (MG-TuRBO) for High Dimensions
---
# Memory-Guided Trust-Region Bayesian Optimization (MG-TuRBO) for High Dimensions
> 原文: [https://arxiv.org/abs/2604.08569](https://arxiv.org/abs/2604.08569)

arXiv:2604.08569v1 Announce Type: new
Abstract: Traffic simulation and digital-twin calibration is a challenging optimization problem with a limited simulation budget. Each trial requires an expensive simulation run, and the relationship between calibration inputs and model error is often nonconvex, and noisy. The problem becomes more difficult as the number of calibration parameters increases. We compare a commonly used automatic calibration method, a genetic algorithm (GA), with Bayesian optimization methods (BOMs): classical Bayesian optimization (BO), Trust-Region BO (TuRBO), Multi-TuRBO, and a proposed Memory-Guided TuRBO (MG-TuRBO) method. We compare performance on 2 real-world traffic simulation calibration problems with 14 and 84 decision variables, representing lower- and higher-dimensional (14D and 84D) settings. For BOMs, we study two acquisition strategies, Thompson sampling and a novel adaptive strategy. We evaluate performance using final calibration quality, convergence behavior, and consistency across runs. The results show that BOMs reach good calibration targets much faster than GA in the lower-D problem. MG-TuRBO performs comparably in our 14D setting, it demonstrates noticeable advantages in the 84D problem, particularly when paired with our adaptive strategy. Our results suggest that MG-TuRBO is especially useful for high-D traffic simulation calibration and potentially for high-D problems in general.

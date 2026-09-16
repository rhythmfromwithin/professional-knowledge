---
title: "Mini-batch Sampling Strategies for Long-Tailed Image Classification: An Empirical Study on CIFAR-100-LT"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.16365
priority: medium
status: unread
interest: medium
next_step: skim
---
# Mini-batch Sampling Strategies for Long-Tailed Image Classification: An Empirical Study on CIFAR-100-LT
> 原文: [https://arxiv.org/abs/2609.16365](https://arxiv.org/abs/2609.16365)

arXiv:2609.16365v1 Announce Type: new
Abstract: Real-world datasets often exhibit long-tailed class distributions, where a few head classes contain a large number of training samples while a large number of tail classes have only a few. The composition of each mini-batch, determined by the sampling strategy, governs which classes contribute to the stochastic gradient estimate, and therefore affects convergence behaviour and generalisation across the whole class spectrum. We provide a systematic theoretical and empirical comparison of four mini-batch sampling strategies for long-tailed image classification: uniform instance sampling, class-balanced sampling, square-root sampling, and progressively balanced sampling. We place all four in a unified bias-variance framework describing their effect on gradient estimation, which exposes the tension between unbiased optimisation of the empirical loss and fair representation of rare classes. We then evaluate them under controlled conditions using ResNet-32 on CIFAR-100-LT at three imbalance ratios (rho = 10, 50, 100), with every strategy sharing the same long-tailed subsets and initialisation within a seed. Progressive sampling improves tail-class accuracy by 25% relative to the uniform baseline at rho = 100 (13.5% versus 10.8%), consistently across all three seeds, while its overall accuracy is not distinguishable from that of uniform sampling given the seed-to-seed variation (40.0% versus 39.7%); the tail-class gain, not the overall gain, is the robust effect. At rho = 100, class-balanced sampling degrades accuracy on every class group, including the tail classes it is designed to help, which we attribute to overfitting caused by extreme oversampling of scarce data; at rho = 50 this failure is confined to head and medium classes. These results indicate that when rebalancing is applied during training matters as much as how much rebalancing is applied.

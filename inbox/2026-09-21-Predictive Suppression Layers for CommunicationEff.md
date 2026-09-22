---
interest: medium
link: https://arxiv.org/abs/2609.21583
next_step: skim
priority: low
slack_ts: '1790051344.774429'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Predictive Suppression Layers for Communication-Efficient Spiking Neural Networks
---
# Predictive Suppression Layers for Communication-Efficient Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2609.21583](https://arxiv.org/abs/2609.21583)

arXiv:2609.21583v1 Announce Type: new
Abstract: Feedforward Spiking Neural Networks (SNNs) typically propagate every generated spike indiscriminately, disregarding whether the information is redundant from an information-theoretic perspective. This lack of selectivity induces high redundancy in inter-layer communication, creating an expensive overhead, e.g., in scenarios involving many-core neuromorphic hardware or communication-dominated Internet-of-Things (IoT) where features are transmitted wirelessly. To address this challenge, we trade localized processing for leaner network channels by introducing a minimal predictive coding framework for SNNs. We propose two layer variants sharing a predictor block: error units, which transmit signed spiking residuals, and predictive suppression, which uses residual magnitude to dynamically gate and forward only unpredictable, "surprising" activity. Evaluated on the N-MNIST and Spiking Heidelberg Digits (SHD) datasets using diagnostic metrics that decouple local processing from cross-layer communication, our new predictive coding layers achieve significant communication savings. Numerical results reveal a three-fold reduction in communicated activity, while increasing the task accuracy for both datasets. The latter finding is notable, and suggests that predictive coding layers not only minimize communication overhead, but also produce output feature vectors with a higher representation power.

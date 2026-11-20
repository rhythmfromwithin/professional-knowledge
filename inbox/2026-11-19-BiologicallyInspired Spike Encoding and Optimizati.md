---
interest: medium
link: https://arxiv.org/abs/2611.23242
next_step: skim
priority: high
slack_ts: '1795157493.448129'
source: cs.LG - Machine Learning
status: unread
title: Biologically-Inspired Spike Encoding and Optimization for Spiking Neural Networks
---
# Biologically-Inspired Spike Encoding and Optimization for Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2611.23242](https://arxiv.org/abs/2611.23242)

arXiv:2611.23242v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) offer theoretical energy-efficiency advantages over conventional deep networks, but realizing these advantages on vision tasks requires sparse spike representations that naive rate-coding methods fail to provide. We combine biologically motivated spike-encoding schemes with two training improvements: Rouser adaptive-threshold surrogate gradients and Kronecker-Factored Approximate Curvature (K-FAC) second-order optimization. The spike encoding schemes experimented with are rate coding, latency coding, DVS-style delta modulation, and Difference-of-Gaussians (DoG) filtering. Experiments on MNIST and Fashion-MNIST demonstrate that biologically inspired encoders yield the largest accuracy gains in capacity-constrained regimes and serve as an effective parameter-efficiency lever. DoG and delta modulation encoders produce significantly sparser spike trains than rate coding. K-FAC yields modest but consistent accuracy improvements over Adam-trained baselines, and Rouser's learnable per-neuron thresholds improve Fashion-MNIST accuracy from 87.37% to 88.13% by enabling homeostatic firing-rate regulation. Biologically grounded pre-processing methods can help close the accuracy gap between SNNs and non-spiking baselines without increasing model size.

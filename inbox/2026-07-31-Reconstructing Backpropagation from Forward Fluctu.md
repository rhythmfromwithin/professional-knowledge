---
interest: medium
link: https://arxiv.org/abs/2607.26483
next_step: skim
priority: low
slack_ts: '1785641749.155829'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Reconstructing Backpropagation from Forward Fluctuations in Noise-modulated
  Neural Networks
---
# Reconstructing Backpropagation from Forward Fluctuations in Noise-modulated Neural Networks
> 原文: [https://arxiv.org/abs/2607.26483](https://arxiv.org/abs/2607.26483)

arXiv:2607.26483v1 Announce Type: new
Abstract: A Noise-modulated Neural Network (NNN) learns and infers only in the presence of noise, treating noise as a computational resource rather than a disturbance. The noise lets it learn efficiently by backpropagation while transmitting spike-like signals, but backpropagation needs a reverse path through transposed weights, the weight transport problem, which undermines biological and neuromorphic plausibility. Forward-only alternatives typically substitute a different objective or fixed random feedback, sacrificing stability and accuracy. We show that backpropagation itself can be reconstructed in the NNN from forward-pass statistics alone: a weight mirror estimates each weight matrix from the covariance between a previous-layer unit's output and the next-layer unit's input, and combining it with local differential estimation inside the units propagates the output error recursively along the computational graph, with no transposed-weight readout and no backward data path. The resulting gradient is empirically near-unbiased, and with local per-weight Adam updates it matches the final accuracy of backpropagation on simple regression tasks. With uniformly distributed noise, the local operations reduce to polynomials and comparators, making the whole system, learning rule included, well suited to digital circuits. Thus, in the NNN, noise is a resource not only for inference but also for reconstructing backpropagation.

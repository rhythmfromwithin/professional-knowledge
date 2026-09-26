---
interest: medium
link: https://arxiv.org/abs/2609.30102
next_step: skim
priority: low
slack_ts: '1790397476.187899'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons
---
# Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons
> 原文: [https://arxiv.org/abs/2609.30102](https://arxiv.org/abs/2609.30102)

arXiv:2609.30102v1 Announce Type: new
Abstract: Most ANN-to-SNN conversion methods rely on a specific correspondence between the source activation and the spiking neuron dynamics. We propose a finite-state continuous-time Markov chain (CTMC) neuron framework whose stationary spike flux can approximate every continuous nonnegative monotone activation function on a compact interval. For a generalized CTMC family with affine input-dependent transitions, we prove uniform approximation to arbitrary accuracy over this function class and derive an explicit approximation error bound. In practice, two- and three-state CTMCs fit ReLU, sigmoid, softplus, and clipped ReLU on the evaluated input ranges, and we evaluate corresponding MLP conversions for each activation with layerwise rate scaling. Moderate clipping improves the conversion cost-accuracy tradeoff on the MNIST MLP and reduces SynOps by 27% on VGG-11/MNIST at matched ANN-SNN accuracy gap criteria, whereas the trend reverses on VGG-11/CIFAR-10. Mean-field and layerwise diagnostics indicate that finite-window sampling and terminal-layer mismatch are the main residual errors. Overall, our results establish finite-state CTMC neurons as a theoretically grounded framework for activation-flexible ANN-to-SNN conversion beyond fixed activation-neuron correspondences.

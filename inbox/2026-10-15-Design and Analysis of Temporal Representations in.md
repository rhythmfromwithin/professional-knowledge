---
title: "Design and Analysis of Temporal Representations in Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2610.19730
priority: low
status: unread
interest: medium
next_step: skim
---
# Design and Analysis of Temporal Representations in Neural Networks
> 原文: [https://arxiv.org/abs/2610.19730](https://arxiv.org/abs/2610.19730)

arXiv:2610.19730v1 Announce Type: new
Abstract: The ability to represent temporal information is often hypothesized to underlie the efficiency and learning capabilities of biological neural networks. This motivates the development of spiking neural networks. However, it remains unclear how temporal information is actually represented in neural networks and how different forms of temporal representation affect performance and computational efficiency. We introduce the notion of the degree of temporal representation of a neural network, defined by whether its constituent functions (activation, learning, encoding, and decoding) explicitly manipulate time as a computational variable. This perspective yields a continuum ranging from non-temporal representations, where time does not explicitly appear as a computational variable in the network functions, to fully temporal representations, where computations explicitly operate on temporal variables. Using a fixed deep architecture, we compare different encoding, activation mechanisms and decoding with increasing temporal expressiveness: non-temporal weighted-sum activations used in usual artificial neural networks, non-temporal binary spiking activations used in spiking neural networks, and spike-time-based activations used in delay neural networks. Experiments on event-based datasets show that increasing the degree of temporal representation improves both performance and computational efficiency, allowing state-of-the-art performances on the Google Speech Commands dataset. We further analyze how temporal representations induce distinct forward and backward computational trajectories, leading to gradients that depend explicitly on the history of event times.

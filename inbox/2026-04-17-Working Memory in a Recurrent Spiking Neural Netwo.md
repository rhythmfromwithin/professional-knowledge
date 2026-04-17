---
title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2604.14096
priority: low
status: unread
interest: medium
next_step: skim
---
# Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
> 原文: [https://arxiv.org/abs/2604.14096](https://arxiv.org/abs/2604.14096)

arXiv:2604.14096v1 Announce Type: new
Abstract: Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of length $D$ that uniquely predict spikes at the next time step. On a synthetic benchmark of $M=16$ patterns ($N=512$ neurons, $T=1000$ steps), training achieves a mean F1 score of $1.0$, with recall emerging first near the clamped initialisation window and propagating forward in time. This result demonstrates that heterogeneous delays provide an efficient substrate for working memory in SNNs, enabling energy-efficient neuromorphic edge deployment.

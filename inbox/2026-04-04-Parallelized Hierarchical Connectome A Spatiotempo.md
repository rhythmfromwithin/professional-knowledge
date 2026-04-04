---
interest: medium
link: https://arxiv.org/abs/2604.01295
next_step: skim
priority: low
slack_ts: '1775270933.479249'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework
  for Spiking State-Space Models'
---
# Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models
> 原文: [https://arxiv.org/abs/2604.01295](https://arxiv.org/abs/2604.01295)

arXiv:2604.01295v1 Announce Type: new
Abstract: This work presents the Parallelized Hierarchical Connectome (PHC), a general framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks. Conventional SSMs achieve high-speed sequence processing through parallel scans, yet are limited to temporal recurrence without lateral or feedback interactions within a single timestep. PHC maps the diagonal SSM core to a shared Neuron Layer and inter-neuronal communication to a shared Synapse Layer, where neurons are partitioned into hierarchical regions governed by the connectome topology. A Multi-Transmission Loop enables intra-slice spatial recurrence, allowing signals to propagate across the hierarchical connectome within each temporal window while preserving O(logT) parallelism. This framework enables integration of neuro-physical priors typically intractable for standard SSMs, including adaptive leaky integrate-and-fire dynamics, Dale's Law, short-term plasticity, and reward-modulated spike-timing-dependent plasticity. The framework is instantiated as PHCSSM, the first model to unify recurrent spiking neural network dynamics with diagonal SSM parallelism while enforcing all five biological constraints and learnable lateral connections within a fully parallelizable training pipeline. Empirical results on physiological benchmarks from the UEA multivariate time-series archive demonstrate that PHCSSM achieves performance competitive with state-of-the-art SSMs while reducing parameter complexity from Theta(D^2 L) for L-layer stacked architectures to Theta(D^2). These findings suggest that biologically grounded inductive biases offer a principled route to parameter-efficient sequence modeling, opening diagonal SSMs to spatiotemporal recurrence and enabling fully parallelizable recurrent spiking neural network training.

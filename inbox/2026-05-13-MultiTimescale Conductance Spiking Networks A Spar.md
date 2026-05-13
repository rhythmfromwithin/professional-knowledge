---
interest: medium
link: https://arxiv.org/abs/2605.11835
next_step: skim
priority: low
slack_ts: '1778644965.911089'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable
  Framework with Rich Firing Dynamics for Enhanced Temporal Processing'
---
# Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
> 原文: [https://arxiv.org/abs/2605.11835](https://arxiv.org/abs/2605.11835)

arXiv:2605.11835v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) promise low-power event-driven computation for temporally rich tasks, but commonly used neuron models often trade off gradient-based trainability, dynamical richness, and high activity sparsity. These limitations are acute in regression, where approximation error, noise and spike discretization can severely degrade continuous-valued outputs. Indeed, many state-of-the-art (SOTA) SNNs rely on simple phenomenological dynamics trained with surrogate gradients and offer limited control over spiking diversity and sparsity. To overcome such limitations, we introduce multi-timescale conductance spiking networks, a gradient-trainable framework in which neural dynamics emerge from shaping the current-voltage (I-V) curve by tuning fast, slow and ultra-slow conductances. This parametrization allows systematic control over excitability, can be implemented efficiently in analog circuits, and yields rich firing regimes including tonic, phasic and bursting responses within a single model. We derive a discrete-time formulation of these differentiable dynamics, enabling direct backpropagation through time without surrogate-gradient approximations. To probe both trainability and accuracy, we evaluate feedforward networks of these neurons at the predictability limit of Mackey-Glass time-series regression and compare them to baseline LIF and SOTA AdLIF networks. Our model outperforms LIF and AdLIF networks, while exhibiting substantially sparser activity from both communication and computational perspectives. These results highlight multi-timescale conductance spiking neurons as a promising building block for energy-aware temporal processing and neuromorphic implementation.

---
title: "Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.13283
priority: low
status: unread
interest: medium
next_step: skim
---
# Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2603.13283](https://arxiv.org/abs/2603.13283)

arXiv:2603.13283v1 Announce Type: new
Abstract: Continuous-time, event-native spiking neural networks (SNNs) operate strictly on spike events, treating spike timing and ordering as the representation rather than an artifact of time discretization. This viewpoint aligns with biological computation and with the native resolution of event sensors and neuromorphic processors, while enabling compute and memory that scale with the number of events. However, two challenges hinder practical, end-to-end trainable event-based SNN systems: 1) exact charge--fire--reset dynamics impose inherently sequential processing of input spikes, and 2) precise spike times must be solved without time bins. We address both. First, we use parallel associative scans to consume multiple input spikes at once, yielding up to 44x speedups over sequential simulation while retaining exact hard-reset dynamics. Second, we implement differentiable spike-time solvers that compute spike times to machine precision without discrete-time approximations or restrictive analytic assumptions. We demonstrate the viability of training SNNs using our solutions on four event-based datasets on GPUs.

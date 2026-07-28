---
title: "NUMA balancing hampering performance of spiking network simulations"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2607.22275
priority: low
status: unread
interest: medium
next_step: skim
---
# NUMA balancing hampering performance of spiking network simulations
> 原文: [https://arxiv.org/abs/2607.22275](https://arxiv.org/abs/2607.22275)

arXiv:2607.22275v1 Announce Type: cross
Abstract: Computing centers today mostly operate conventional CPU- and GPU-based systems, where the direct way of decreasing energy consumption is a reduction in the applications' runtime. Neuromorphic computing promises an alternative architecture with improved energy efficiency for artificial intelligence. In this endeavor, code for the simulation of large-scale spiking networks on conventional supercomputers is the reference. We show that turning off automatic NUMA balancing may reduce energy consumption by 30%. This dwarfs other attempts of increasing the energy efficiency of a computing center with respect to cost effectiveness. The memory access pattern of spiking network simulation code dynamically interacts with automatic NUMA balancing. This does not affect the correctness of simulation results and thus goes unnoticed in day-to-day neuroscience research. In performance analysis, however, time measurements fluctuate obstructing attempts to optimize simulation technology. A new time- and compute-node resolved performance display exposes the fine-grained temporal variability of distributed spiking network simulations. The analysis uncovers that automatic NUMA balancing is of disadvantage and affects the jemalloc library for thread-aware memory allocation in a transient manner. The method also allows developers to detect perturbations of the HPC system and target specific improvements to simulation technology. As a consequence, we have equipped our supercomputers with an option to turn on or off automatic NUMA balancing on a per-job basis on the user level. This gives researchers the opportunity to find the best setting for the application at hand. There are indications in the literature that the effect has been observed before, yet it does not seem common knowledge in scientific computing. It remains to be investigated how widespread the phenomenon is among scientific codes.

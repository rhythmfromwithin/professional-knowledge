---
interest: medium
link: https://arxiv.org/abs/2609.09160
next_step: skim
priority: medium
slack_ts: '1789013739.182639'
source: cs.DC - Distributed Computing
status: unread
title: 'LBFAST: A Lightweight Moment-Represented Lattice Boltzmann Solver for Multi-GPU
  Architectures'
---
# LBFAST: A Lightweight Moment-Represented Lattice Boltzmann Solver for Multi-GPU Architectures
> 原文: [https://arxiv.org/abs/2609.09160](https://arxiv.org/abs/2609.09160)

arXiv:2609.09160v1 Announce Type: new
Abstract: We present LBFAST, a GPU-oriented lattice Boltzmann solver based on a lightweight moment-represented formulation, in which post-collision populations are reconstructed on the fly from a reduced set of moments rather than stored explicitly. This approach significantly lowers the memory footprint, enabling large three-dimensional simulations within the constraints of modern accelerator architectures, where VRAM capacity and bandwidth are critical resources. The method is assessed through standard single- and two-component benchmarks demonstrating good accuracy and stability. Extensive scaling experiments on multi-GPU systems show near-ideal weak scaling up to 512 GPUs and sustained performance across different velocity sets. The combination of reduced memory usage, competitive throughput, and stable energy efficiency makes the proposed formulation a practical route for large-scale lattice Boltzmann simulations on current and emerging HPC platforms.

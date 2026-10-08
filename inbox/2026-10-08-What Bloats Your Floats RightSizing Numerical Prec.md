---
title: "What Bloats Your Floats? Right-Sizing Numerical Precision for Scientific Computing"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.09089
priority: medium
status: unread
interest: medium
next_step: skim
---
# What Bloats Your Floats? Right-Sizing Numerical Precision for Scientific Computing
> 原文: [https://arxiv.org/abs/2610.09089](https://arxiv.org/abs/2610.09089)

arXiv:2610.09089v1 Announce Type: new
Abstract: While FP64 (binary64) remains the standard representation of real numbers in scientific computing, hardware trends increasingly favor low-precision formats optimized for AI workloads. This shift prioritizes throughput and energy efficiency over full-precision capabilities. We challenge the necessity of high-precision arithmetic in PDE-governed simulations, where spatial and temporal discretization errors introduce a physical noise floor that masks the lower-order bits of the FP64 format, rendering them irrelevant. We propose a criterion based on the Signal-to-Noise Ratio (SNR) with respect to spatial and temporal refinements to evaluate the impact of safe precision reduction on scientific computations. Finally, we present an automated dataflow-centric workflow for targeted lowering within mixed-precision subgraphs in complex scientific applications. Large-scale evaluations of weather and climate applications show that strategic precision reduction on GPUs achieves up to 1.8x speedup without compromising physical fidelity.

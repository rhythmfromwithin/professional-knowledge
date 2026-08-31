---
interest: medium
link: https://arxiv.org/abs/2608.27612
next_step: skim
priority: low
slack_ts: '1788152853.892549'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Tensor-Accelerated Eager Multi-Resolution Grids for Evolving Large-Scale Substrates
---
# Tensor-Accelerated Eager Multi-Resolution Grids for Evolving Large-Scale Substrates
> 原文: [https://arxiv.org/abs/2608.27612](https://arxiv.org/abs/2608.27612)

arXiv:2608.27612v1 Announce Type: new
Abstract: In neuroevolution, indirect encoding generates neural network connectivity from a compact genome rather than specifying each connection. ES-HyperNEAT automatically discovers where to place hidden nodes by examining CPPN output patterns: it recursively subdivides space using a quadtree, expanding regions where CPPN outputs show high variance. This adaptive approach discovers network topology without manual substrate specification, extending the fixed-grid HyperNEAT framework built on NEAT.
However, the quadtree resists tensorization. Each depth level depends on the parent's variance, forcing sequential evaluation. Different CPPNs produce different subdivision patterns, preventing batching. And variable leaf counts are incompatible with JAX's static shape requirement for JIT compilation. Our prior work confirmed these limits at depths exceeding 5, and a JAX reimplementation of the quadtree yielded only marginal speedup despite batched optimizations, motivating the eager reformulation presented here.
We present EMR-HyperNEAT, which evaluates all positions at all resolutions up front, then filters using the same variance criterion: ES-HyperNEAT's subdivide\_if(var > $\theta$) becomes eval\_all(); filter(var > $\theta$). This performs more CPPN queries than necessary, but all queries become independent and parallelizable across both cores and population members, reducing complexity from \BigO($4^D$) to \BigO($4^D/P$) across $P$ parallel cores. Recurrent substrate configurations become feasible through a connection type taxonomy. The experiments section validates 12-34$\times$ on-device GPU speedup on XOR at depths 5-7, and empirically higher solve rates across benchmarks.

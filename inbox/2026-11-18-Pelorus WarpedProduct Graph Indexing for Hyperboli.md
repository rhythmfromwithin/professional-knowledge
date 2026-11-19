---
interest: medium
link: https://arxiv.org/abs/2611.22159
next_step: skim
priority: low
slack_ts: '1795071560.698849'
source: cs.DB - Databases
status: unread
title: 'Pelorus: Warped-Product Graph Indexing for Hyperbolic Vector Search'
---
# Pelorus: Warped-Product Graph Indexing for Hyperbolic Vector Search
> 原文: [https://arxiv.org/abs/2611.22159](https://arxiv.org/abs/2611.22159)

arXiv:2611.22159v1 Announce Type: new
Abstract: Hyperbolic embeddings capture hierarchical relations, but million-scale approximate nearest neighbor search must reconcile geodesic fidelity with memory efficiency. Flat inner-product indices distort order across radial shells, while native hyperbolic graphs repeatedly access full-precision vectors or quantize coordinates with singular conformal scales. We present Pelorus, a warped-product proximity-graph index for hyperbolic vector search. Pelorus separates unquantized FP32 radial and conformal scalars from scale-invariant 2-bit spherical directional codes and defers full-vector FP64 evaluation to a compact reranking tail. A conformal distortion analysis motivates orthogonal-projection debiasing, purity-gated tangent-cone residuals, and Conformal Jacobian gating. QuadriPrune allocates edges across geodesic fibers, same-shell rings, and radial elevators, with spanning-tree chord swaps restoring entry reachability. A single-page record layout and carry-save AVX2 kernel accelerate traversal. Across eight real and synthetic benchmarks on AMD EPYC 9654, Pelorus builds Cohere-1M indices 5.44x faster than full-precision polar graphs on 32 threads, reducing hot navigation memory to 517.0 MB. At 99% Recall@10, it improves Cohere-1M throughput by 4.30x on one thread and 6.31x on 24 threads, and delivers 53,483 QPS on MERU-1M. On clustered narrow shells, tangent-cone residuals raise recall from 34.22% to 99.385%, while isotropic narrow-shell stress tests expose remaining recall limits.

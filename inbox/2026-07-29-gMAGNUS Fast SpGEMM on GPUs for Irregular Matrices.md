---
interest: medium
link: https://arxiv.org/abs/2607.22866
next_step: skim
priority: medium
slack_ts: '1785468999.317509'
source: cs.DC - Distributed Computing
status: unread
title: '$g$MAGNUS: Fast SpGEMM on GPUs for Irregular Matrices via Hierarchical Multisplit'
---
# $g$MAGNUS: Fast SpGEMM on GPUs for Irregular Matrices via Hierarchical Multisplit
> 原文: [https://arxiv.org/abs/2607.22866](https://arxiv.org/abs/2607.22866)

arXiv:2607.22866v2 Announce Type: new
Abstract: We present $g$MAGNUS, a novel algorithm for sparse matrix-matrix multiplication (SpGEMM) of irregular matrices on GPUs. Such matrices often contain many heavy rows, those with large intermediate products that force local memory accumulators to spill to global memory. $g$MAGNUS addresses this by computing an intra-row reordering of intermediate products, subdividing heavy rows into independent chunks that can be accumulated completely in local memory. This reordering uses novel outer product and hierarchical multisplit operations. The algorithm is input- and system-aware, automatically determining the number of chunks and multisplit levels based on the input matrix dimensions and local memory size. Experimental results on two extensive datasets show that $g$MAGNUS achieves a geometric-mean speedup of 1.81 to 7.62$\times$ over five leading algorithms (including MKL and cuSPARSE) on Intel Ponte Vecchio and NVIDIA H200. Additionally, the core kernels of $g$MAGNUS are evaluated, achieving near-peak performance compared to their theoretical upper bound.

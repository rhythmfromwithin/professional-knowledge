---
interest: medium
link: https://arxiv.org/abs/2604.13433
next_step: skim
priority: medium
slack_ts: '1776482307.215479'
source: cs.DC - Distributed Computing
status: unread
title: 'PackSELL: A Sparse Matrix Format for Precision-Agnostic High-Performance SpMV'
---
# PackSELL: A Sparse Matrix Format for Precision-Agnostic High-Performance SpMV
> 原文: [https://arxiv.org/abs/2604.13433](https://arxiv.org/abs/2604.13433)

arXiv:2604.13433v1 Announce Type: new
Abstract: We propose a new sparse matrix format, PackSELL, designed to support diverse data representations and enable efficient sparse matrix-vector multiplication (SpMV) on GPUs. Building on sliced ELLPACK (SELL), PackSELL incorporates delta encoding of column indices and a novel packing scheme that stores each index-delta-value pair in a single word, thereby reducing memory footprint and data movement. This design further enables fine-grained control over the bit allocation between deltas and values, allowing flexible data representations, including non-IEEE formats. Experimental results show that, when configured for half precision (FP16), the PackSELL-based SpMV kernel outperforms the cuSPARSE SELL-based kernel by up to $1.63\times$. Moreover, with configurations using customized formats, PackSELL achieves FP32-level accuracy while exceeding the performance of FP16 cuSPARSE. These benefits extend to sparse linear solvers; for example, a mixed-precision preconditioned conjugate gradient (PCG) solver using PackSELL achieves up to a $2.09\times$ speedup over the standard full-precision PCG.

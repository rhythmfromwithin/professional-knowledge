---
interest: medium
link: https://arxiv.org/abs/2603.08734
next_step: skim
priority: medium
slack_ts: '1773888800.641729'
source: cs.DC - Distributed Computing
status: unread
title: 'RSH-SpMM: A Row-Structured Hybrid Kernel for Sparse Matrix-Matrix Multiplication
  on GPUs'
---
# RSH-SpMM: A Row-Structured Hybrid Kernel for Sparse Matrix-Matrix Multiplication on GPUs
> 原文: [https://arxiv.org/abs/2603.08734](https://arxiv.org/abs/2603.08734)

arXiv:2603.08734v1 Announce Type: new
Abstract: Sparse Matrix-Matrix Multiplication (SpMM) is a fundamental computation in graph analytics, scientific simulation, and sparse deep learning workloads. However, the extreme irregularity of real-world sparse matrices prevents existing GPU-based methods from maintaining high Tensor Core utilization and stable throughput. We present \textbf{RSH-SpMM}, a fine-grained row-structured hybrid SpMM framework designed to better align irregular sparsity with modern GPU execution pipelines. RSH-SpMM introduces adaptive row partitioning and employs the RS-Tile representation to expose Tensor-Core-efficient dense fragments, while processing irregular rows on a minimal-overhead CUDA execution path. It further employs a load-balanced hybrid kernel with locality-aware reordering to enhance structural coherence and sustain high execution efficiency under highly irregular sparsity. Comprehensive evaluations across diverse sparse workloads demonstrate that RSH-SpMM consistently outperforms state-of-the-art SpMM designs, yielding 1.27x - 6.13x acceleration and maintaining robust performance across matrices with highly irregular sparsity structures.

---
title: "Unifying In-Memory Data Analytics through Sparse Compilation"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.30497
priority: medium
status: unread
interest: medium
next_step: skim
---
# Unifying In-Memory Data Analytics through Sparse Compilation
> 原文: [https://arxiv.org/abs/2609.30497](https://arxiv.org/abs/2609.30497)

arXiv:2609.30497v1 Announce Type: new
Abstract: As modern data analytics workloads become increasingly heterogeneous and hardware-intensive, achieving efficient multi-core performance across diverse applications remains an open challenge. We present Reffine, a compiler-based in-memory analytics engine that delivers high performance across a broad range of data analytics workloads. Reffine introduces a novel intermediate representation (IR), grounded in relational algebra and sparse iteration theory, that provides a unified abstraction for data and computation. This representation enables workload-agnostic, end-to-end optimizations such as operator fusion and automatic parallelization across diverse analytics applications. We further develop a sparse compiler backend that translates Reffine IR into hardware-efficient imperative code, achieving high multi-core performance without domain-specific implementations. On the TPC-H benchmark, Reffine outperforms the in-memory analytical database DuckDB by up to $24.9\times$ and the state-of-the-art compilation-based database Umbra by up to $3.2\times$. Reffine also achieves average speedups of $18.3\times$ and $47.9\times$ over Polars and NetworkX on streaming and graph analytics workloads, respectively. Source code: https://github.com/ampersand-projects/reffine

---
title: "SINDI: An Efficient Index for Sparse Vector Approximate Maximum Inner Product Search"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2509.08395
priority: low
status: unread
interest: medium
next_step: skim
---
# SINDI: An Efficient Index for Sparse Vector Approximate Maximum Inner Product Search
> 原文: [https://arxiv.org/abs/2509.08395](https://arxiv.org/abs/2509.08395)

arXiv:2509.08395v4 Announce Type: replace
Abstract: Sparse vector Maximum Inner Product Search (MIPS) is crucial in multi-path retrieval for Retrieval-Augmented Generation (RAG). Recent inverted index-based and graph-based algorithms have achieved high search accuracy with practical efficiency. However, their performance in production environments is often limited by redundant distance computations and frequent random memory accesses. Furthermore, the compressed storage format of sparse vectors hinders the use of SIMD acceleration. In this paper, we propose the sparse inverted non-redundant distance index (SINDI), which incorporates three key optimizations: (i) Efficient Inner Product Computation: SINDI leverages SIMD acceleration and eliminates redundant identifier lookups, enabling batched inner product computation; (ii) Memory-Friendly Design: SINDI replaces random memory accesses to original vectors with sequential accesses to inverted lists, substantially reducing memory-bound latency. (iii) Vector Pruning: SINDI retains only the high-magnitude non-zero entries of vectors, improving query throughput while maintaining accuracy. We evaluate SINDI on multiple real-world datasets. Experimental results show that SINDI achieves state-of-the-art performance across datasets of varying scales, languages, and models. On the MsMarco dataset, when Recall@50 exceeds 99%, SINDI delivers single-thread query-per-second (QPS) improvements ranging from 4.2$\times$ to 26.4$\times$ compared with SEISMIC and PyANNs. Notably, SINDI has been integrated into Ant Group's open-source vector search library, VSAG.

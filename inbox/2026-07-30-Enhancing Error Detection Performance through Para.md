---
title: "Enhancing Error Detection Performance through Parallel CRC Computation on Multi-Core Architectures"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.24849
priority: medium
status: unread
interest: medium
next_step: skim
---
# Enhancing Error Detection Performance through Parallel CRC Computation on Multi-Core Architectures
> 原文: [https://arxiv.org/abs/2607.24849](https://arxiv.org/abs/2607.24849)

arXiv:2607.24849v1 Announce Type: new
Abstract: Cyclic Redundancy Check (CRC) remains one of the most widely used error-detection mechanisms in communication, storage, and embedded systems. However, conventional software CRC implementations suffer from inherent sequential dependencies that limit efficient utilization of modern multi-core processors. This paper presents a generalized software-based parallel CRC framework for multi-core architectures using POSIX threads. The proposed framework supports multiple CRC variants, including CRC-8, CRC-16, CRC-32, CRC-64, and CRC-128, within a unified implementation model. To preserve correctness during parallel execution, the framework employs a GF(2)-based CRC combination mechanism rather than naive XOR aggregation. The combine stage is formulated using polynomial arithmetic and matrix-based shifting operations over GF(2), ensuring equivalence between parallel and serial CRC computation. The proposed method was evaluated using multiple workload sizes and thread configurations. Experimental analysis includes execution time, throughput, latency, scalability behavior, and energy estimation under varying thread counts. Results indicate that parallel execution significantly improves performance for large datasets, achieving approximately 3-4x speedup on the evaluated platform while preserving exact CRC correctness. Comparative discussion with representative CRC optimization approaches, including lookup-table methods, slicing-by-8, SIMD/vectorized CRC, and hardware-assisted CRC techniques, is also provided to position the proposed framework within the broader CRC optimization landscape. Overall, the proposed approach provides a portable and generalized software framework for correctness-preserving parallel CRC acceleration on general-purpose multi-core systems.

---
interest: medium
link: https://arxiv.org/abs/2608.20725
next_step: skim
priority: medium
slack_ts: '1787708782.677919'
source: cs.DC - Distributed Computing
status: unread
title: Enabling Memory-efficient Im2win Convolution with Multi-precision Support on
  GPU CUDA and Tensor Cores
---
# Enabling Memory-efficient Im2win Convolution with Multi-precision Support on GPU CUDA and Tensor Cores
> 原文: [https://arxiv.org/abs/2608.20725](https://arxiv.org/abs/2608.20725)

arXiv:2608.20725v1 Announce Type: new
Abstract: Convolution is a principal computational bottleneck in deep neural networks, and its efficiency depends on tight integration between algorithms and GPU hardware. Existing GPU convolution methods suffer from large memory overhead, poor cache utilization, limited effectiveness across kernel sizes, or numerical instability. This work extends the im2win paradigm -- a universal, memory-efficient convolution method with contiguous memory access for all kernel sizes -- to run efficiently in full precision on CUDA cores and half precision on tensor cores. By introducing new kernel designs and optimizations such as zig-zag memory access and asynchronous data movement, im2win efficiently exploits hardware-accelerated half-precision matrix multiply-accumulate operations. Across twelve CNN benchmarks, im2win achieves up to 2.8x higher TFLOPS than its CUDA core implementation, 1.4x higher than cuDNN, and 6.4x higher than GEMM-based convolution with cuBLAS, while using as little as 53% and 35% of their memory, respectively. These results establish im2win as a unified, high-performance convolution framework for modern GPU architectures.

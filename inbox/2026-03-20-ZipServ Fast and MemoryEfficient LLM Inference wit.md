---
title: "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.17435
priority: medium
status: unread
interest: medium
next_step: skim
---
# ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression
> 原文: [https://arxiv.org/abs/2603.17435](https://arxiv.org/abs/2603.17435)

arXiv:2603.17435v1 Announce Type: new
Abstract: Lossless model compression holds tremendous promise for alleviating the memory and bandwidth bottlenecks in bit-exact Large Language Model (LLM) serving. However, existing approaches often result in substantial inference slowdowns due to fundamental design mismatches with GPU architectures: at the kernel level, variable-length bitstreams produced by traditional entropy codecs break SIMT parallelism; at the system level, decoupled pipelines lead to redundant memory traffic. We present ZipServ, a lossless compression framework co-designed for efficient LLM inference. ZipServ introduces Tensor-Core-Aware Triple Bitmap Encoding (TCA-TBE), a novel fixed-length format that enables constant-time, parallel decoding, together with a fused decompression-GEMM (ZipGEMM) kernel that decompresses weights on-the-fly directly into Tensor Core registers. This "load-compressed, compute-decompressed" design eliminates intermediate buffers and maximizes compute intensity. Experiments show that ZipServ reduces the model size by up to 30%, achieves up to 2.21x kernel-level speedup over NVIDIA's cuBLAS, and expedites end-to-end inference by an average of 1.22x over vLLM. ZipServ is the first lossless compression system that provides both storage savings and substantial acceleration for LLM inference on GPUs.

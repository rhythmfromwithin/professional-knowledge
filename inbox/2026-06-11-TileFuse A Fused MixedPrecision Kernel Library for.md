---
title: "TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.11357
priority: medium
status: unread
interest: medium
next_step: skim
---
# TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs
> 原文: [https://arxiv.org/abs/2606.11357](https://arxiv.org/abs/2606.11357)

arXiv:2606.11357v1 Announce Type: new
Abstract: With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets. However, practical LLM deployment on current client NPUs remains difficult: widely used quantization formats such as AWQ do not map cleanly onto many existing NPU software stacks, which are often proprietary and expose limited low-level control. In this work, we present \textit{TileFuse}, a close-to-metal mixed-precision kernel library for AMD XDNA2 NPUs that targets transformer linear layers in quantized LLM inference. TileFuse brings practical low-bit formats such as AWQ-style W4A16 and W8A16 directly onto XDNA2, rather than forcing the model to be reshaped around an NPU-specific quantization scheme.
TileFuse co-designs weight layout, metadata placement, mixed-precision microkernels, and array-level dataflow. Specifically, it fuses unpacking, dequantization, and GEMM/GEMV execution into a single kernel flow, introduces an interleaved pre-tiling layout that supports GEMM dimensions up to 32K, and redesigns GEMV dataflow to utilize the full 4x8 AIE array. Across kernel-level evaluations, TileFuse improves performance by up to 121.6% for GEMM and 281% for GEMV over full-precision baselines, while delivering more than 2x performance and energy-efficiency gains over strong iGPU baselines on GEMM. In end-to-end LLM experiments on Ryzen AI laptops, TileFuse achieves up to 2.0x lower prefilling latency with more than 64.6% lower energy consumption. Together, these results show that XDNA2 is a practical target for AWQ-style edge LLM inference and that native NPU support for off-the-shelf quantization can make NPUs substantially more usable in real client deployments.

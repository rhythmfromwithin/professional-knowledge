---
interest: medium
link: https://arxiv.org/abs/2607.02521
next_step: skim
priority: medium
slack_ts: '1783569520.280149'
source: cs.DC - Distributed Computing
status: unread
title: Tile-Level Activation Overlap for Efficient LLM Inference
---
# Tile-Level Activation Overlap for Efficient LLM Inference
> 原文: [https://arxiv.org/abs/2607.02521](https://arxiv.org/abs/2607.02521)

arXiv:2607.02521v1 Announce Type: new
Abstract: SwiGLU is the dominant MLP activation in modern large language models, yet its intermediate tensor materialization costs 9-37% of MLP execution time. We present two complementary CUTLASS-based SM90 kernels that fuse SwiGLU into GeMM at the tile level. Kernel-1 overlaps Swish computation on the Gate accumulator with Up-tile loading using the Pingpong warp-specialized schedule; Kernel-2 interleaves SwiGLU with tile stores via a custom Epilogue Visitor Tree. Evaluated on Qwen-2.5 models (0.5B-72B) on NVIDIA H100, our kernels achieve up to 2.47x speedup over PyTorch, shifting workloads from memory-bound to compute-bound and reaching 79.5% peak BF16 utilization. We demonstrate that torch.compile cannot replicate this fusion (3-7x slower than our kernels), validating the need for hand-crafted tile-level design. Our fused kernels are also numerically superior, achieving zero mismatches compared to 4.5-11% for cuBLAS.

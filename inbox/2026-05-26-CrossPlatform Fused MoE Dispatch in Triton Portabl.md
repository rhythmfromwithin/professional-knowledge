---
interest: medium
link: https://arxiv.org/abs/2605.23911
next_step: skim
priority: medium
slack_ts: '1779941824.709989'
source: cs.DC - Distributed Computing
status: unread
title: 'Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without
  CUDA'
---
# Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without CUDA
> 原文: [https://arxiv.org/abs/2605.23911](https://arxiv.org/abs/2605.23911)

arXiv:2605.23911v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) architectures power the majority of frontier large language models, but their inference is bottlenecked by irregular memory access patterns and expert routing overhead. Existing optimized MoE kernels (Megablocks, Tutel, FasterMoE) are implemented in CUDA and locked to NVIDIA hardware. We present TritonMoE, a fused MoE dispatch kernel written entirely in OpenAI Triton that performs the complete forward pass -- router scoring, token permutation, expert GEMMs, and weighted output combination -- using only portable Triton primitives. Our key optimization is a fused gate+up GEMM kernel that computes both SwiGLU projections from shared L2-cached input tiles with in-register SiLU activation, eliminating 35% of global memory traffic. On an NVIDIA A100, TritonMoE achieves 89-131% of the throughput of the CUDA-optimized Megablocks at inference batch sizes (<= 512 tokens) across Mixtral-8x7B, DeepSeek-V3, and Qwen2-MoE configurations. All 162 correctness tests pass on both NVIDIA A100 and AMD MI300X with zero code changes, validating cross-platform portability. We additionally characterize sensitivity to routing imbalance under Zipfian-skewed expert assignments and identify the regime -- 64+ experts under extreme skew -- where our fixed-tile scheduling underperforms Megablocks' block-sparse layout, motivating dynamic block-to-expert assignment as future work. Code is available at https://github.com/bassrehab/triton-kernels.

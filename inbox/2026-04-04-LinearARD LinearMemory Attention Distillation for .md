---
interest: medium
link: https://arxiv.org/abs/2604.00004
next_step: skim
priority: high
slack_ts: '1775359532.270189'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'LinearARD: Linear-Memory Attention Distillation for RoPE Restoration'
---
# LinearARD: Linear-Memory Attention Distillation for RoPE Restoration
> 原文: [https://arxiv.org/abs/2604.00004](https://arxiv.org/abs/2604.00004)

arXiv:2604.00004v1 Announce Type: new
Abstract: The extension of context windows in Large Language Models is typically facilitated by scaling positional encodings followed by lightweight Continual Pre-Training (CPT). While effective for processing long sequences, this paradigm often disrupts original model capabilities, leading to performance degradation on standard short-text benchmarks. We propose LinearARD, a self-distillation method that restores Rotary Position Embeddings (RoPE)-scaled students through attention-structure consistency with a frozen native-RoPE teacher. Rather than matching opaque hidden states, LinearARD aligns the row-wise distributions of dense $Q/Q$, $K/K$, and $V/V$ self-relation matrices to directly supervise attention dynamics. To overcome the quadratic memory bottleneck of $n \times n$ relation maps, we introduce a linear-memory kernel. This kernel leverages per-token log-sum-exp statistics and fuses logit recomputation into the backward pass to compute exact Kullback-Leibler divergence and gradients. On LLaMA2-7B extended from 4K to 32K, LinearARD recovers 98.3\% of the short-text performance of state-of-the-art baselines while surpassing them on long-context benchmarks. Notably, our method achieves these results using only \textbf{4.25M} training tokens compared to the \textbf{256M} tokens required by LongReD and CPT. Our code is available at https://github.com/gracefulning/LinearARD.

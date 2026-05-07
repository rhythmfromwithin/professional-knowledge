---
title: "StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.02904
priority: high
status: unread
interest: medium
next_step: skim
---
# StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing
> 原文: [https://arxiv.org/abs/2605.02904](https://arxiv.org/abs/2605.02904)

arXiv:2605.02904v1 Announce Type: new
Abstract: We present StateSMix, a fully self-contained lossless compressor that couples an online-trained Mamba-style State Space Model (SSM) with sparse n-gram context mixing and arithmetic coding. The model is initialised from scratch and trained token-by-token on the file being compressed, requiring no pre-trained weights, no GPU, and no external dependencies. The SSM (DM=32, NL=2, approximately 120K active parameters per file) provides a continuously-updated probability estimate over BPE tokens, while nine sparse n-gram hash tables (bigram through 32-gram, 16M slots each) add exact local and long-range pattern memorisation via a softmax-invariant logit-bias mechanism that updates only non-zero-count tokens. An entropy-adaptive scaling mechanism modulates the n-gram contribution based on the SSM's predictive confidence, preventing over-correction when the neural model is already well-calibrated. On the standard enwik8 benchmark, StateSMix achieves 2.123 bpb on 1 MB, 2.149 bpb on 3 MB, and 2.162 bpb on 10 MB, beating xz -9e (LZMA2) by 8.7%, 5.4%, and 0.7% respectively. Ablation experiments establish the SSM as the dominant compression engine: it alone accounts for a 46.6% size reduction over a frequency-count baseline and beats xz without any n-gram component, while n-gram tables provide a complementary 4.1% gain through exact context memorisation. OpenMP parallelisation of the training loop yields 1.9x speedup on 4 cores. The system is implemented in pure C with AVX2 SIMD and processes approximately 2,000 tokens per second on commodity x86-64 hardware.

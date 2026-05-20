---
interest: medium
link: https://arxiv.org/abs/2605.16617
next_step: skim
priority: medium
slack_ts: '1779250490.451779'
source: cs.DC - Distributed Computing
status: unread
title: Exceeding the Numerical and Performance Characteristics of IEEE-754 SGEMM with
  BFloat16 Tensor Cores on GPUs for Scientific Computing
---
# Exceeding the Numerical and Performance Characteristics of IEEE-754 SGEMM with BFloat16 Tensor Cores on GPUs for Scientific Computing
> 原文: [https://arxiv.org/abs/2605.16617](https://arxiv.org/abs/2605.16617)

arXiv:2605.16617v1 Announce Type: new
Abstract: Largely due to their increased native capacity for numerical intensity and power efficiency, reduced-precision floating-point computing resources, primarily used in artificial intelligence (AI) applications, have expanded at a greater rate than their higher-precision relatives. This has led to various efforts focused upon leveraging plentiful reduced-precision hardware to mimic higher-precision mathematical calculations. This paper studies a specific use case, namely the use of bfloat16 (BF16) Tensor Cores found on modern GPUs in service of single precision (FP32) matrix multiply operations. Given that BF16 and FP32 share the same dynamic range, the option to accumulate BF16 operations into FP32 accumulators (at full-speed), and additional BF16 arithmetic characteristics specific to the Blackwell GPU architecture, such as integrated scaling hardware, such emulation is highly motivated. This paper examines the performance, efficiency, power, and numerical characteristics of FP32 matrix multiplication via BF16-based emulation and demonstrates how it exceeds numerical and performance characteristics of native FP32 for scientific applications. We also discuss a full library-ready implementation that correctly deals with denormals.

---
title: "Signed Symmetric Quantization for Few-Bit Integers"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.08779
priority: high
status: unread
interest: medium
next_step: skim
---
# Signed Symmetric Quantization for Few-Bit Integers
> 原文: [https://arxiv.org/abs/2607.08779](https://arxiv.org/abs/2607.08779)

arXiv:2607.08779v1 Announce Type: new
Abstract: The signed integer alphabet contains one more negative representable value than positive. Yet, by convention, the standard symmetric integer quantizer fixes its scale to be strictly positive, which assigns this extra representable value to the negative tail and can force clipping of positive outliers. In this work, we show that, at few-bit precision, such clipping is a non-trivial source of quantization error. Asymmetric quantization addresses this problem with a zero point, shifting the grid toward the observed data range; however, this flexibility is well-known to carry a runtime penalty. For example, in llama.cpp on an AMD EPYC(TM) "Turin" CPU, a 4-bit symmetric format uses up to 9% less memory with up to 2.45$\times$ higher throughput than its asymmetric counterpart. We highlight signed symmetric quantization as a third option that retains the runtime profile of symmetric quantization without the penalty of the asymmetric format: our signed absmax grid places the extra representable value on the dominant-outlier tail through a principled and lightweight sign selection rule while keeping the zero point at zero. Our theoretical analysis offers two main results. First, we establish the signed absmax grid as conditionally bound-optimal on $\ell\_2$ quantization error, and show that the condition holds for 88-99% of weight groups across pre-trained large language models (LLMs) at low bit widths. Second, we show that negating the scale of a standard symmetric quantizer is analytically equivalent to a unit zero point shift on the same signed integer alphabet. We empirically validate our proposal on models from the Qwen3, Qwen3.5, and Llama3 families, and observe improvement in perplexity and downstream few-shot accuracy over the standard unsigned symmetric quantizer at no extra inference cost

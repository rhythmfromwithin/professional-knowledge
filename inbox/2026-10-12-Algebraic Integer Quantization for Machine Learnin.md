---
title: "Algebraic Integer Quantization for Machine Learning Applications"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.12494
priority: high
status: unread
interest: medium
next_step: skim
---
# Algebraic Integer Quantization for Machine Learning Applications
> 原文: [https://arxiv.org/abs/2610.12494](https://arxiv.org/abs/2610.12494)

arXiv:2610.12494v1 Announce Type: new
Abstract: In this article, we propose algebraic integer number formats (AINF) as a framework for highly configurable and accurate compressed computation. A key property of AINF is its straightforward reduction to purely integer arithmetic, enabling error-free multiply-accumulate operations. We develop a matrix multiplication engine that exploits this property, obtaining performance within a predictable factor of the most efficient numerical counterparts on modern hardware accelerators. Another key advantage of AIQ is the freedom to select algebraic integers tailored to the numerical characteristics of a given use case, offering optimization opportunities that are fundamentally unavailable in floating-point or fixed-point formats. Motivated by these properties, we introduce algebraic integer quantization (AIQ), a lossy compression format for large language model (LLM) inference, and provide results demonstrating that AIQ achieves competitive accuracy compared to the industry-standard MX format across a diverse set of models and benchmarks at equivalent bit-per-parameter budgets. The experiments presented in this article employ algebraic integers of degree two (quadratic integers); generalizations to higher-order and, in particular, multidimensional algebraic integers promise even greater computational advantages and remain a promising direction for future work.

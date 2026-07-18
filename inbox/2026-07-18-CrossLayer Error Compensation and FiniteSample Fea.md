---
interest: medium
link: https://arxiv.org/abs/2607.14630
next_step: skim
priority: low
slack_ts: '1784344412.386259'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Cross-Layer Error Compensation and Finite-Sample Feature-Statistics Matching
  for Extreme Low-Bit Quantization of Large Language Models
---
# Cross-Layer Error Compensation and Finite-Sample Feature-Statistics Matching for Extreme Low-Bit Quantization of Large Language Models
> 原文: [https://arxiv.org/abs/2607.14630](https://arxiv.org/abs/2607.14630)

arXiv:2607.14630v1 Announce Type: new
Abstract: Layer-wise post-training quantization of large language models minimizes each layer's reconstruction error in isolation, allowing quantization errors to accumulate across depth and causing severe degradation in extreme low-bit regimes. We formulate quantization as a joint optimization over the discrete codes and scales of all layers, driven by two mechanisms: (i) cross-layer error compensation, which maintains the network-level accumulated error through the recursion e\_{l+1} = A\_l e\_l + q\_l, with a propagation operator A\_l derived from the layer's input differential and a local quantization residual q\_l evaluated at teacher features; and (ii) finite-sample feature-statistics matching, which aligns means, projected covariances, and centered empirical kernels between the full-precision and quantized networks under relative normalization. We prove that instantiating the propagation operator as a finite difference of the quantized network makes the recursion exact for arbitrary nonlinear layers, enabling an efficient forward-difference implementation. Binary weights are optimized via a mirror-descent parameterization u = tanh(beta\*z) with annealed inverse temperature and group-wise log-scales. On Qwen2.5-1.5B with 1.125-bit group-binary weights, error compensation alone reaches a perplexity ratio of 9.56 +/- 0.15 over the FP16 teacher, outperforming logit distillation (14.09 +/- 0.53; 32 percent relative, more than 8 sigma over 3 seeds) and layer-local reconstruction by two orders of magnitude. The same objective transfers unchanged to 4-bit quantization (1.060 vs. 1.088 for layer-local). Out-of-domain evaluations (C4, CNN/DailyMail) show the advantage of error compensation grows off-domain, while statistics matching keeps feature-statistics discrepancy low off-domain (0.42-0.88 vs. 1.41-2.99 without it), revealing a complementary division of labor between the two mechanisms.

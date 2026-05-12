---
interest: medium
link: https://arxiv.org/abs/2605.06675
next_step: skim
priority: high
slack_ts: '1778558029.388749'
source: cs.LG - Machine Learning
status: unread
title: 'RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion
  Theory'
---
# RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory
> 原文: [https://arxiv.org/abs/2605.06675](https://arxiv.org/abs/2605.06675)

arXiv:2605.06675v1 Announce Type: new
Abstract: Large language models cache all previously computed key-value (KV) pairs during generation, and this KV cache grows linearly with sequence length, making it a primary memory bottleneck for serving. Quantizing the KV cache to fewer bits reduces this cost, yet all current quantizers assign the same bit-width to every attention head, ignoring the large variation in head importance. A natural idea is to allocate more bits to important heads and fewer to the rest. We show, however, that such mixed-precision allocation has a hidden pitfall: each quantizer follows a different distortion curve D(b)=alpha\*beta^{-b}, and the decay rate beta varies from 3.6 to 5.3 across quantizer designs. Applying one quantizer's distortion model to another inverts the allocation order and makes performance worse than uniform quantization. We call this failure mode distortion model mismatch and propose RateQuant to resolve it. RateQuant fits a per-quantizer distortion model from a small calibration set, then solves the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction) and improves QuaRot by 6.6 PPL. The entire calibration takes 1.6 s on a single GPU and adds zero overhead at inference time.

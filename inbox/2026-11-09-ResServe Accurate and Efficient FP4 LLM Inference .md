---
interest: medium
link: https://arxiv.org/abs/2611.08713
next_step: skim
priority: medium
slack_ts: '1794203482.532739'
source: cs.DC - Distributed Computing
status: unread
title: 'ResServe: Accurate and Efficient FP4 LLM Inference with Residue Compensation'
---
# ResServe: Accurate and Efficient FP4 LLM Inference with Residue Compensation
> 原文: [https://arxiv.org/abs/2611.08713](https://arxiv.org/abs/2611.08713)

arXiv:2611.08713v1 Announce Type: new
Abstract: Block-scaled 4-bit floating-point (FP4) quantization reduces large language model inference costs but can degrade task quality. Higher-precision computation can mitigate this loss at the expense of some of the efficiency gains from FP4 inference. Narrow matrix computations common in decoding often leave spare hardware capacity for low-cost precision recovery. ResServe combines an FP4 activation base with an FP4-quantized residue representing information lost during quantization. It uses this spare capacity to compute the residue's contribution and combines results on-chip, avoiding extra result transfers. We apply this principle to linear layers and decode attention, while selective compensation limits added work when processing input prompts. On NVIDIA B200, compensated linear kernels using the NVFP4 format improve numerical precision while retaining latency close to uncompensated execution for the evaluated operations with few rows. In the evaluated NVFP4 inference configurations, ResServe adds at most 3.4% request-latency overhead over W4A4 and reduces request latency by 22.4-53.3% relative to W4A8. Across five models, code-generation accuracy improves over same-format uncompensated inference, with mean relative gains of 15.04% for NVFP4 and 53.57% for MXFP4.

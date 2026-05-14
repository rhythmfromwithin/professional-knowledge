---
interest: medium
link: https://arxiv.org/abs/2605.10959
next_step: skim
priority: high
slack_ts: '1778731263.572679'
source: cs.LG - Machine Learning
status: unread
title: 'QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization'
---
# QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization
> 原文: [https://arxiv.org/abs/2605.10959](https://arxiv.org/abs/2605.10959)

arXiv:2605.10959v1 Announce Type: new
Abstract: There is currently no unified metric for evaluating the efficiency of quantized neural networks. We propose QuIDE, built around the Intelligence Index I = (C x P)/log\_2(T+1), which collapses the compression-accuracy-latency trade-off into a single score. Experiments across six settings -- SimpleCNN (MNIST, CIFAR), ResNet-18 (ImageNet-1K), and Llama-3-8B -- show a task-dependent Pareto Knee. 4-bit quantization is optimal for MNIST and large LLMs, while 8-bit is the sweet spot for complex CNN tasks (ResNet-18 on ImageNet), where 4-bit PTQ collapses accuracy catastrophically. The accuracy-gated variant I' correctly flags these non-viable configurations that the raw I would reward. QuIDE provides a reproducible evaluation protocol and a ready-to-use fitness function for mixed-precision search.

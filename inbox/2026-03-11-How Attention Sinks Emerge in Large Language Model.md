---
title: "How Attention Sinks Emerge in Large Language Models: An Interpretability Perspective"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.06591
priority: high
status: unread
interest: medium
next_step: skim
---
# How Attention Sinks Emerge in Large Language Models: An Interpretability Perspective
> 原文: [https://arxiv.org/abs/2603.06591](https://arxiv.org/abs/2603.06591)

arXiv:2603.06591v1 Announce Type: new
Abstract: Large Language Models (LLMs) often allocate disproportionate attention to specific tokens, a phenomenon commonly referred to as the attention sink. While such sinks are generally considered detrimental, prior studies have identified a notable exception: the model's consistent emphasis on the first token of the input sequence. This structural bias can influence a wide range of downstream applications and warrants careful consideration. Despite its prevalence, the precise mechanisms underlying the emergence and persistence of attention sinks remain poorly understood. In this work, we trace the formation of attention sinks around the first token of the input. We identify a simple mechanism, referred to as the P0 Sink Circuit, that enables the model to recognize token at position zero and induce an attention sink within two transformer blocks, without relying on any semantic information. This mechanism serves as the basis for the attention sink on position zero. Furthermore, by analyzing training traces from a 30B A3B MoE model trained from scratch, we find that this mechanism emerges early in training and becomes increasingly concentrated in the first two layers, suggesting a possible signal for tracking pre training convergence states.

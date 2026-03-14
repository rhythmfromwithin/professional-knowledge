---
title: "Summarize Before You Speak with ARACH: A Training-Free Inference-Time Plug-In for Enhancing LLMs via Global Attention Reallocation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.11067
priority: high
status: unread
interest: medium
next_step: skim
---
# Summarize Before You Speak with ARACH: A Training-Free Inference-Time Plug-In for Enhancing LLMs via Global Attention Reallocation
> 原文: [https://arxiv.org/abs/2603.11067](https://arxiv.org/abs/2603.11067)

arXiv:2603.11067v1 Announce Type: new
Abstract: Large language models (LLMs) achieve remarkable performance, yet further gains often require costly training. This has motivated growing interest in post-training techniques-especially training-free approaches that improve models at inference time without updating weights. Most training-free methods treat the model as a black box and improve outputs via input/output-level interventions, such as prompt design and test-time scaling through repeated sampling, reranking/verification, or search. In contrast, they rarely offer a plug-and-play mechanism to intervene in a model's internal computation. We propose ARACH(Attention Reallocation via an Adaptive Context Hub), a training-free inference-time plug-in that augments LLMs with an adaptive context hub to aggregate context and reallocate attention. Extensive experiments across multiple language modeling tasks show consistent improvements with modest inference overhead and no parameter updates. Attention analyses further suggest that ARACH mitigates the attention sink phenomenon. These results indicate that engineering a model's internal computation offers a distinct inference-time strategy, fundamentally different from both prompt-based test-time methods and training-based post-training approaches.

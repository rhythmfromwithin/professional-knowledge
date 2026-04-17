---
interest: medium
link: https://arxiv.org/abs/2604.13054
next_step: skim
priority: high
slack_ts: '1776396659.056439'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Caption First, VQA Second: Knowledge Density, Not Task Format, Drives Multimodal
  Scaling'
---
# Caption First, VQA Second: Knowledge Density, Not Task Format, Drives Multimodal Scaling
> 原文: [https://arxiv.org/abs/2604.13054](https://arxiv.org/abs/2604.13054)

arXiv:2604.13054v1 Announce Type: new
Abstract: Multimodal large language models (MLLMs) have achieved rapid progress, yet their scaling behavior remains less clearly characterized and often less predictable than that of text-only LLMs. Increasing model size and task diversity often yields diminishing returns. In this work, we argue that the primary bottleneck in multimodal scaling is not task format, but knowledge density in training data. We first show that task-specific supervision such as Visual Question Answering (VQA) contributes little incremental semantic information beyond image captions: VQA signals can be reconstructed from captions with negligible performance loss. We then demonstrate that increasing knowledge density -- through structured caption enrichment and cross-modal knowledge injection -- leads to consistent performance improvements across multimodal and downstream benchmarks. Across controlled experiments, performance correlates more strongly with semantic coverage than with task diversity. These findings suggest that current MLLMs fail to scale primarily because training data lacks sufficient knowledge coverage. We advocate for knowledge-centric multimodal training as a principled foundation for scalable multimodal models.

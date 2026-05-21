---
interest: medium
link: https://arxiv.org/abs/2605.16359
next_step: skim
priority: medium
slack_ts: '1779337376.013209'
source: cs.CV - Computer Vision
status: unread
title: How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token
  Pruning with F^3A
---
# How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token Pruning with F^3A
> 原文: [https://arxiv.org/abs/2605.16359](https://arxiv.org/abs/2605.16359)

arXiv:2605.16359v1 Announce Type: new
Abstract: Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token budget? Existing training-free pruning methods typically answer this with one-shot proxies such as decoder attention, visual similarity, or conditional diversity. We argue that visual token pruning is better viewed as task-conditioned evidence search, especially under aggressive compression and across model scales. We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens. F^3A builds lightweight question-conditioned cues, matches them to visual-grid tokens through frozen sparse sensing heads, and allocates a fixed vision token budget via coarse evidence localization, local refinement, coverage-preserving competition, and recovery of under-covered regions. It requires no model training, no extra LLM forward pass and preserves the original multimodal prompting and decoding pipeline.

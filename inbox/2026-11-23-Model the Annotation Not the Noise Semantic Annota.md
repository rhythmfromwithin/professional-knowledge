---
interest: medium
link: https://arxiv.org/abs/2611.26702
next_step: skim
priority: medium
slack_ts: '1795512708.690389'
source: cs.CV - Computer Vision
status: unread
title: 'Model the Annotation, Not the Noise: Semantic Annotation-Channel Prompt Learning
  against Noisy Labels'
---
# Model the Annotation, Not the Noise: Semantic Annotation-Channel Prompt Learning against Noisy Labels
> 原文: [https://arxiv.org/abs/2611.26702](https://arxiv.org/abs/2611.26702)

arXiv:2611.26702v1 Announce Type: new
Abstract: Parameter-efficient prompt learning has become a cornerstone for adapting pre-trained vision-language models (VLMs), yet it remains highly vulnerable to label noise in few-shot Web and retrieval scenarios. Existing noise robust methods typically rely on hard sample selection or deterministic label correction, which discard valuable semantic ambiguity and overlook how observed annotations are actually generated. To bridge this gap, we reformulate noisy prompt learning through the perspective of data generation, proposing SACP, a Semantic-aware Annotation Channel-based Prompt learning framework. Instead of suppressing noise heuristically, SACP decouples latent clean-label prediction from instance-dependent annotation generation. By integrating frozen VLM semantic priors with lightweight visual residuals, SACP constructs a structured annotation channel optimized via generalized expectation-maximization with soft posteriors. Furthermore, a posterior-aware memory is introduced to preserve label uncertainty during test-time inference. Extensive experiments across different synthetic benchmarks and the real-world noisy Food101N dataset demonstrate that SACP achieves state-of-the-art performance against its counterparts in different label noise patterns, especially under severe asymmetric noise.

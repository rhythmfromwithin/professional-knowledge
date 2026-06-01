---
interest: medium
link: https://arxiv.org/abs/2605.27374
next_step: skim
priority: high
slack_ts: '1780290086.374679'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized
  Preference Alignment'
---
# ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment
> 原文: [https://arxiv.org/abs/2605.27374](https://arxiv.org/abs/2605.27374)

arXiv:2605.27374v1 Announce Type: new
Abstract: Recent advances in multimodal large language models (MLLMs) and diffusion models (DMs) have opened new possibilities for AI-generated content. Yet, personalized cover image generation remains underexplored, despite its critical role in boosting user engagement on digital platforms. We propose ICG, a novel framework that integrates MLLM-based prompting with personalized preference alignment to generate high-quality, contextually relevant covers. ICG extracts semantic features from item titles and reference images via meta tokens, refines them with user embeddings, and injects the resulting personalized context into the diffusion model. To address the lack of labeled supervision, we adopt a multi-reward learning strategy that combines public aesthetic and relevance rewards with a personalized preference model trained from user behavior. Unlike prior pipelines relying on handcrafted prompts and disjointed modules, ICG employs an adapter to bridge MLLMs and diffusion models for end-to-end training. Experiments demonstrate that ICG significantly improves image quality, semantic fidelity, and personalization, leading to stronger user appeal and offline recommendation accuracy in downstream tasks. As a plug-and-play adapter bridging MLLMs and diffusion models, ICG is compatible with common checkpoints and requires no ground-truth labels during optimization.

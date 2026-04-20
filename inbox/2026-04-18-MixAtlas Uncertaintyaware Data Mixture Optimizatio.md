---
interest: medium
link: https://arxiv.org/abs/2604.14198
next_step: skim
priority: high
slack_ts: '1776656355.408029'
source: cs.LG - Machine Learning
status: unread
title: 'MixAtlas: Uncertainty-aware Data Mixture Optimization for Multimodal LLM Midtraining'
---
# MixAtlas: Uncertainty-aware Data Mixture Optimization for Multimodal LLM Midtraining
> 原文: [https://arxiv.org/abs/2604.14198](https://arxiv.org/abs/2604.14198)

arXiv:2604.14198v1 Announce Type: new
Abstract: Domain reweighting can improve sample efficiency and downstream generalization, but data-mixture optimization for multimodal midtraining remains largely unexplored. Current multimodal training recipes tune mixtures along a single dimension, typically data format or task type. We introduce MixAtlas, a method that produces benchmark-targeted data recipes that can be inspected, adapted, and transferred to new corpora. MixAtlas decomposes the training corpus along two axes: image concepts (10 visual-domain clusters discovered via CLIP embeddings) and task supervision (5 objective types including captioning, OCR, grounding, detection, and VQA). Using small proxy models (Qwen2-0.5B) paired with a Gaussian-process surrogate and GP-UCB acquisition, MixAtlas searches the resulting mixture space with the same proxy budget as regression-based baselines but finds better-performing mixtures. We evaluate on 10 benchmarks spanning visual understanding, document reasoning, and multimodal reasoning. On Qwen2-7B, optimized mixtures improve average performance by 8.5%-17.6% over the strongest baseline; on Qwen2.5-7B, gains are 1.0%-3.3%. Both settings reach baseline-equivalent training loss in up to 2 times fewer steps. Recipes discovered on 0.5B proxies transfer to 7B-scale training across Qwen model families.

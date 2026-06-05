---
title: "Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2606.05966
priority: low
status: unread
interest: medium
next_step: skim
---
# Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs
> 原文: [https://arxiv.org/abs/2606.05966](https://arxiv.org/abs/2606.05966)

arXiv:2606.05966v1 Announce Type: new
Abstract: Understanding and reasoning about the physical world is the foundation of intelligent behavior, yet state-of-the-art vision-language models (VLMs) still fail at causal physical reasoning, often producing plausible but incorrect answers. To address this gap, we introduce CausalPhys, a benchmark of over 3,000 carefully curated video- and image-based questions spanning four domains: Perception, Anticipation, Intervention, and Goal Orientation. Each question is paired with an expert-annotated causal graph capturing object-attribute-event dependencies, enabling interpretable and fine-grained evaluation of causal understanding. Building on this, we formulate a causal-graph-grounded metric that quantitatively measures how well a model's chain-of-thought reasoning aligns with the correct causal relations, moving beyond answer-only accuracy and enabling systematic diagnosis of VLMs' causal reasoning failures. Using this metric, we conduct a comprehensive analysis of leading VLMs, revealing systematic gaps in capturing causal dependencies and underscoring the need for causality-aware learning. To address these limitations, we further propose Causal Rationale-informed Fine-Tuning (CRFT), which explicitly aligns VLM reasoning with causal structures. Extensive experiments demonstrate that CRFT substantially enhances both reasoning accuracy and interpretability across multiple model backbones. By unifying dataset curation, causal evaluation, and causality-informed learning, CausalPhys establishes a strong foundation for advancing modern VLMs toward causally grounded physical reasoning.

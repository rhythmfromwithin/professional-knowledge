---
interest: medium
link: https://arxiv.org/abs/2603.20275
next_step: skim
priority: medium
slack_ts: '1774581551.857199'
source: cs.CV - Computer Vision
status: unread
title: Understanding Pruning Regimes in Vision-Language Models Through Domain-Aware
  Layer Selection
---
# Understanding Pruning Regimes in Vision-Language Models Through Domain-Aware Layer Selection
> 原文: [https://arxiv.org/abs/2603.20275](https://arxiv.org/abs/2603.20275)

arXiv:2603.20275v1 Announce Type: new
Abstract: Transformer-based vision-language models (VLMs) contain substantial depth redundancy, yet the effect of removing specific decoder layers remains poorly understood, especially for domains that require tight coupling between perception and multi-step reasoning. We study structured decoder layer pruning through the lens of domain-aware activation similarity, measuring how strongly each layer transforms representations for math versus non-math inputs. This yields simple math-aware, non-math-aware, and mixed ranking criteria that identify layers whose input-output activations change least within a target domain. Across two state-of-the-art VLMs and a broad suite of math and general multimodal benchmarks, we uncover a consistent three-regime structure: at low pruning budgets, performance is highly sensitive to which layers are removed; at moderate budgets, methods converge as structural damage accumulates; and at high budgets, structural continuity dominates, favoring spacing-aware strategies. Our domain-aware rankings achieve the strongest stability in the ranking-sensitive regime, while matching or exceeding structure-aware baselines at larger budgets. These results provide a clearer picture of how depth contributes to domain-specific behavior in VLMs and offer a practical, interpretable approach to reducing model depth without sacrificing essential mathematical or general vision-language capabilities.

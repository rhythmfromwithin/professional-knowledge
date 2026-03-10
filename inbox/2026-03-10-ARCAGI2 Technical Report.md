---
interest: medium
link: https://arxiv.org/abs/2603.06590
next_step: skim
priority: high
slack_ts: '1773132497.387129'
source: cs.CL - Computation and Language (NLP)
status: unread
title: ARC-AGI-2 Technical Report
---
# ARC-AGI-2 Technical Report
> 原文: [https://arxiv.org/abs/2603.06590](https://arxiv.org/abs/2603.06590)

arXiv:2603.06590v1 Announce Type: new
Abstract: The Abstraction and Reasoning Corpus (ARC) is designed to assess generalization beyond pattern matching, requiring models to infer symbolic rules from very few examples. In this work, we present a transformer-based system that advances ARC performance by combining neural inference with structure-aware priors and online task adaptation. Our approach is built on four key ideas. First, we reformulate ARC reasoning as a sequence modeling problem using a compact task encoding with only 125 tokens, enabling efficient long-context processing with a modified LongT5 architecture. Second, we introduce a principled augmentation framework based on group symmetries, grid traversals, and automata perturbations, enforcing invariance to representation changes. Third, we apply test-time training (TTT) with lightweight LoRA adaptation, allowing the model to specialize to each unseen task by learning its transformation logic from demonstrations. Fourth, we design a symmetry-aware decoding and scoring pipeline that aggregates likelihoods across augmented task views, effectively performing ``multi-perspective reasoning'' over candidate solutions. We demonstrate that these components work synergistically: augmentations expand hypothesis space, TTT sharpens local reasoning, and symmetry-based scoring improves solution consistency. Our final system achieves a significant improvement over transformer baselines and surpasses prior neural ARC solvers, closing the gap toward human-level generalization.

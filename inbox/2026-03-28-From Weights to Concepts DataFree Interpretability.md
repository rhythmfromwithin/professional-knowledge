---
interest: medium
link: https://arxiv.org/abs/2603.24653
next_step: skim
priority: medium
slack_ts: '1774754607.543319'
source: cs.CV - Computer Vision
status: unread
title: 'From Weights to Concepts: Data-Free Interpretability of CLIP via Singular
  Vector Decomposition'
---
# From Weights to Concepts: Data-Free Interpretability of CLIP via Singular Vector Decomposition
> 原文: [https://arxiv.org/abs/2603.24653](https://arxiv.org/abs/2603.24653)

arXiv:2603.24653v1 Announce Type: new
Abstract: As vision-language models are deployed at scale, understanding their internal mechanisms becomes increasingly critical. Existing interpretability methods predominantly rely on activations, making them dataset-dependent, vulnerable to data bias, and often restricted to coarse head-level explanations. We introduce SITH (Semantic Inspection of Transformer Heads), a fully data-free, training-free framework that directly analyzes CLIP's vision transformer in weight space. For each attention head, we decompose its value-output matrix into singular vectors and interpret each one via COMP (Coherent Orthogonal Matching Pursuit), a new algorithm that explains them as sparse, semantically coherent combinations of human-interpretable concepts. We show that SITH yields coherent, faithful intra-head explanations, validated through reconstruction fidelity and interpretability experiments. This allows us to use SITH for precise, interpretable weight-space model edits that amplify or suppress specific concepts, improving downstream performance without retraining. Furthermore, we use SITH to study model adaptation, showing how fine-tuning primarily reweights a stable semantic basis rather than learning entirely new features.

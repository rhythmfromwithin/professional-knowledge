---
interest: medium
link: https://arxiv.org/abs/2607.01394
next_step: skim
priority: high
slack_ts: '1783136978.542679'
source: cs.AI - Artificial Intelligence
status: unread
title: The Wiola Architecture for Efficient Small Language Models
---
# The Wiola Architecture for Efficient Small Language Models
> 原文: [https://arxiv.org/abs/2607.01394](https://arxiv.org/abs/2607.01394)

arXiv:2607.01394v1 Announce Type: new
Abstract: We present Wiola, a fully original Small Language Model (SLM) architecture built from first principles, sharing no structural lineage with any existing model family including GPT, LLaMA, Mistral, or Falcon. Wiola introduces five independently novel components: (i) Spiral Rotary Positional Encoding (SRPE), which embeds token positions on a three-dimensional helical manifold combining absolute, relative, and hierarchical positional signals; (ii) Gated Cross-Layer Attention (GCLA), providing each decoder layer with soft cross-attention access to compressed summaries of two preceding layers for inter-layer coherence; (iii) Adaptive Token Merging (ATM), which dynamically merges se mantically redundant adjacent tokens in middle network layers to reduce attention complexity without information loss; (iv) Dual Stream Feed-Forward (DSFF), replacing the conventional MLP with two parallel streams fused by a learned per-dimension gate; and (v) WiolaRMSNorm, a modified normalisation introducing a per-dimension learned offset vector that prevents representation collapse. We provide complete mathematical derivations, architectural block diagrams, complexity analyses, and systematic comparisons against GPT-2, LLaMA-2, and Mistral. Wiola is released in four sizes (120M, 360M, 700M, and 1.5B parameters) and is fully compatible with the HuggingFace Transformers ecosystem, with all 22 architectural unit tests passing.

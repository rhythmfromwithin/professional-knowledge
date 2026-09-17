---
title: "DANTINOX: A Unified Framework for Multi-Paradigm Language Modeling"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2609.17535
priority: high
status: unread
interest: medium
next_step: skim
---
# DANTINOX: A Unified Framework for Multi-Paradigm Language Modeling
> 原文: [https://arxiv.org/abs/2609.17535](https://arxiv.org/abs/2609.17535)

arXiv:2609.17535v1 Announce Type: new
Abstract: Language generation research increasingly spans three paradigms: autoregressive decoding, discrete masked diffusion, and continuous flow-matching. Comparing them is difficult because each lives in a separate codebase, so measured differences often reflect implementation details rather than the paradigms themselves. We present DantinoX, an open-source JAX/Flax library in which a single modular Transformer backbone serves all three paradigms. Switching the generation paradigm, attention mechanism, or hardware topology requires only a configuration change, while the backbone architecture, tokenizer, initialization strategy, and training infrastructure remain consistent. This enables controlled cross-paradigm comparisons within one API for training, streaming inference, and benchmarking.

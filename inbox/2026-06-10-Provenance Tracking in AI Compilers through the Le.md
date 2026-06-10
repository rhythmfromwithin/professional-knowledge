---
interest: medium
link: https://arxiv.org/abs/2606.10937
next_step: skim
priority: low
slack_ts: '1781065411.026709'
source: cs.DB - Databases
status: unread
title: Provenance Tracking in AI Compilers through the Lens of Coalgebra
---
# Provenance Tracking in AI Compilers through the Lens of Coalgebra
> 原文: [https://arxiv.org/abs/2606.10937](https://arxiv.org/abs/2606.10937)

arXiv:2606.10937v1 Announce Type: new
Abstract: AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation. Reliable provenance is essential for attaching platform-specific postprocessing, debugging compiler behavior, and validating transformations, yet existing solutions are either invasive or ad hoc under non-injective graph rewrites.
We present a lightweight, generative approach to provenance tracking based on observational semantics. Instead of propagating identifiers through compiler passes, we observe graph transformations and reason about provenance in terms of observable computational actions. We formalize this approach using a coalgebraic model and bisimulation, which preserves provenance even when intermediate nodes are eliminated. Furthermore, we implement this approach in a prototype AI compiler COVAN, demonstrating stable provenance across compilation pipelines with minimal engineering overhead.

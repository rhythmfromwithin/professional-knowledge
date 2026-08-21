---
title: "Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.18084
priority: high
status: unread
interest: medium
next_step: skim
---
# Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving
> 原文: [https://arxiv.org/abs/2608.18084](https://arxiv.org/abs/2608.18084)

arXiv:2608.18084v1 Announce Type: new
Abstract: Theorem proving in real-world Lean 4 projects is challenging because proofs often depend on project-specific context. While iterative refinement can use compiler errors to repair failed proofs, reusing failed attempts requires careful search control: some proofs provide better starting points than others, and later revisions may degrade a partially correct proof. We propose a compiler-guided proof search framework that balances exploration and exploitation. It explores diverse starting points through dual-model generation and stagnation-triggered resampling, while exploiting promising proof states through current-best refinement guided by compiler-grounded pairwise comparison. Experiments on seven real-world Lean 4 projects from miniCTX-v2 show that our method achieves a better effectiveness--efficiency tradeoff than pass@k baselines. Within the pass@32 budget, our method improves average pass rate by 12.8 percentage points while reducing LLM calls by 21.9%.

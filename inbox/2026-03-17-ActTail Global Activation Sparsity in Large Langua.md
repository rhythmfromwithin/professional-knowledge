---
title: "ActTail: Global Activation Sparsity in Large Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.12272
priority: high
status: unread
interest: medium
next_step: skim
---
# ActTail: Global Activation Sparsity in Large Language Models
> 原文: [https://arxiv.org/abs/2603.12272](https://arxiv.org/abs/2603.12272)

arXiv:2603.12272v1 Announce Type: new
Abstract: Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement. However, existing activation sparsity methods typically apply uniform sparsity across projections, ignoring the heterogeneous statistical properties of Transformer weights and thereby amplifying performance degradation. In this paper, we propose ActTail, a TopK magnitude-based activation sparsity method with global activation sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Specifically, we capture this heterogeneity via the heavy-tail exponent computed from each projection's empirical spectral density (ESD), which is used as a quantitative indicator to assign projection-specific sparsity budgets. Importantly, we provide a theoretical analysis that establishes an explicit relationship between the activation sparsity ratio and the heavy-tail exponent under the HT-SR regime, offering principled guidance for sparsity allocation beyond heuristic design. Experiments on LLaMA and Mistral models show that our method improves both perplexity and downstream task performance at high sparsity compared to uniform allocation. At 80% sparsity, perplexity is reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, and 9.4% on Mistral-7B.

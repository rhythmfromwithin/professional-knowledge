---
title: "RIMS: Preference Optimization via Smoothed Multi-pair Aggregation for Small-Scale LLM Retrieval-Augmented Generation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.16431
priority: high
status: unread
interest: medium
next_step: skim
---
# RIMS: Preference Optimization via Smoothed Multi-pair Aggregation for Small-Scale LLM Retrieval-Augmented Generation
> 原文: [https://arxiv.org/abs/2607.16431](https://arxiv.org/abs/2607.16431)

arXiv:2607.16431v1 Announce Type: new
Abstract: Small-scale language models (SLMs) are attractive for retrieval-augmented generation (RAG) in resource-constrained settings, but their limited capacity makes them highly sensitive to noisy or spurious retrieved evidence. Existing preference-based methods such as RoseRAG select only the hardest single preference pair via hard argmin/argmax, discarding the remaining signal; others treat multiple pairs as independent binary comparisons, resulting in low data utilization. We propose RIMS, a three-stage preference optimization framework comprising (1) synthetic chain-of-thought preference data generation via rejection sampling using the target SLM itself without relying on proprietary models, (2) a differentiable soft aggregation mechanism that replaces hard selection with a smooth operator, preserving gradient signal from all preference pairs while retaining the discriminative structure of margin-aware selection, and (3) preference optimization with the smoothed objective applied to multiple alignment algorithms. We theoretically show that the smoothed approximation admits a controllable error bound and that smooth aggregation yields provably tighter gradient alignment to the oracle objective than hard selection. Experiments on four multi-hop question answering benchmarks show that our approach outperforms state-of-the-art baselines across multiple SLM backbones, achieving consistent gains in Exact Match and F1 under noisy retrieval conditions. Our implementation is available at https://github.com/tptrix29/RIMS.

---
title: "Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.19765
priority: high
status: unread
interest: medium
next_step: skim
---
# Do Hallucination Neurons Generalize? Evidence from Cross-Domain Transfer in LLMs
> 原文: [https://arxiv.org/abs/2604.19765](https://arxiv.org/abs/2604.19765)

arXiv:2604.19765v1 Announce Type: new
Abstract: Recent work identifies a sparse set of "hallucination neurons" (H-neurons), less than 0.1% of feed-forward network neurons, that reliably predict when large language models will hallucinate. These neurons are identified on general-knowledge question answering and shown to generalize to new evaluation instances. We ask a natural follow-up question: do H-neurons generalize across knowledge domains? Using a systematic cross-domain transfer protocol across 6 domains (general QA, legal, financial, science, moral reasoning, and code vulnerability) and 5 open-weight models (3B to 8B parameters), we find they do not. Classifiers trained on one domain's H-neurons achieve AUROC 0.783 within-domain but only 0.563 when transferred to a different domain (delta = 0.220, p < 0.001), a degradation consistent across all models tested. Our results suggest that hallucination is not a single mechanism with a universal neural signature, but rather involves domain-specific neuron populations that differ depending on the knowledge type being queried. This finding has direct implications for the deployment of neuron-level hallucination detectors, which must be calibrated per domain rather than trained once and applied universally.

---
interest: medium
link: https://arxiv.org/abs/2603.26045
next_step: skim
priority: low
slack_ts: '1775014234.214379'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: H-Node Attack and Defense in Large Language Models
---
# H-Node Attack and Defense in Large Language Models
> 原文: [https://arxiv.org/abs/2603.26045](https://arxiv.org/abs/2603.26045)

arXiv:2603.26045v1 Announce Type: cross
Abstract: We present H-Node Adversarial Noise Cancellation (H-Node ANC), a mechanistic framework that identifies, exploits, and defends hallucination representations in transformer-based large language models (LLMs) at the level of individual hidden-state dimensions. A logistic regression probe trained on last-token hidden states localizes hallucination signal to a small set of high-variance dimensions -- termed Hallucination Nodes (H-Nodes) -- with probe AUC reaching 0.90 across four architectures. A white-box adversarial attack amplifies these dimensions at inference time via a real-time forward hook, achieving a selectivity of 3.02x with less than 10% visibility to the defender. Adaptive ANC defense suppresses H-Node excess in-pass using confidence-weighted cancellation, reducing grounded activation drift by 33-42% over static cancellation. A dynamic iterative extension that re-ranks cancellation targets across successive passes recovers up to 0.69 robustness from a single-pass baseline of 8%. All contributions are validated on OPT-125M, Phi-3-mini-4k-instruct, LLaMA-3-8B-Instruct, and Mistral-7B-Instruct-v0.3 (125M-8B parameters). Perplexity impact is surgical (<5%) and MMLU degradation is at most 3%, confirming that the defense does not impair general reasoning capability.

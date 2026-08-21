---
title: "Model Card for OpenAI Privacy Filter"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.18274
priority: low
status: unread
interest: medium
next_step: skim
---
# Model Card for OpenAI Privacy Filter
> 原文: [https://arxiv.org/abs/2608.18274](https://arxiv.org/abs/2608.18274)

arXiv:2608.18274v1 Announce Type: new
Abstract: OpenAI Privacy Filter is a compact, bidirectional token-classification model for detecting and redacting personally identifiable information (PII) and secrets in unstructured text. The model is derived from an autoregressively pretrained checkpoint and converted into a bidirectional, banded-attention classifier that labels an input sequence in a single forward pass. A constrained Viterbi decoder produces coherent spans across eight privacy categories and exposes configurable operating points for precision-recall tradeoffs. Privacy Filter has 1.5 billion total parameters, 50 million active parameters per token, and a 128,000-token context window. It is designed for efficient local deployment and domain-specific fine-tuning. Privacy Filter is intended as a configurable data-minimization component within layered privacy workflows, not as an anonymization or compliance guarantee.

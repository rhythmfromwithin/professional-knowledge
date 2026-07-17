---
interest: medium
link: https://arxiv.org/abs/2607.11889
next_step: skim
priority: high
slack_ts: '1784258641.744159'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Scaling Point-in-Time Language Models
---
# Scaling Point-in-Time Language Models
> 原文: [https://arxiv.org/abs/2607.11889](https://arxiv.org/abs/2607.11889)

arXiv:2607.11889v1 Announce Type: new
Abstract: Large language models trained on unrestricted internet corpora inevitably embed information from the future, introducing lookahead bias that compromises the validity of backtests and causal inference in finance and the social sciences. Point-in-time language models--trained exclusively on text available up to each calendar date--eliminate this leakage by construction, but existing efforts typically produce models that lag substantially behind their unconstrained counterparts. We show that this performance gap can be substantially narrowed through scale. Training decoder-only transformers with up to 4 billion parameters on 1 trillion chronologically filtered tokens from FineWeb, we construct a sequence of monthly model checkpoints spanning 2013-2024. Across a range of common-sense reasoning and language understanding benchmarks, our models approach the performance of leading open-weight models of comparable size (e.g., Gemma-3-4B and LLaMA-7B) trained on temporally unrestricted data, although a performance gap remains on several tasks. Instruction fine-tuning via LoRA further improves downstream usability. We release the complete pipeline--including dataset construction, training infrastructure, and evaluation code--to enable reproducible point-in-time language modeling and to support research applications that require strict temporal validity.

---
interest: medium
link: https://arxiv.org/abs/2604.26990
next_step: skim
priority: low
slack_ts: '1777780640.427339'
source: cs.SE - Software Engineering
status: unread
title: 'UCSC-NLP at SemEval-2026 Task 13: Multi-View Generalization and Diagnostic
  Analysis of Machine-Generated Code Detection'
---
# UCSC-NLP at SemEval-2026 Task 13: Multi-View Generalization and Diagnostic Analysis of Machine-Generated Code Detection
> 原文: [https://arxiv.org/abs/2604.26990](https://arxiv.org/abs/2604.26990)

arXiv:2604.26990v1 Announce Type: new
Abstract: With the rapid growth of large language models for code generation, distinguishing between human-written and AI-generated code has become increasingly critical for academic integrity, hiring evaluations, and software security. We present our system for SemEval-2026 Task 13: Multilingual Machine-Generated Code Detection, participating in Subtask A (binary detection) and Subtask B (multi-class attribution across 10 LLM families). For Subtask A, we fine-tune UniXcoder-base with a multi-view training framework that promotes generator-invariant representations. The framework combines domain-specific structural prefixes, delexicalization with symmetric KL consistency loss, token dropout, and mixed-content augmentation. Our system achieves 0.993 macro F1 on validation and 0.845 macro F1 on the test set, which spans unseen languages and domains. For Subtask B, we show that severe class imbalance (88.4% human code, 221:1 majority-to-minority ratio) causes catastrophic minority-class failure under standard fine-tuning, with macro F1 collapsing to 0.086 despite 88.4% accuracy. A class-weighted extension trained for 3 epochs recovers macro F1 to 0.345 (+301% relative), confirming that multi-class attribution requires imbalance-aware training strategies.

---
interest: medium
link: https://arxiv.org/abs/2607.06613
next_step: skim
priority: low
slack_ts: '1783740350.538159'
source: cs.SE - Software Engineering
status: unread
title: 'Pre-Training on Software Engineering Texts: Effects on Domain Adaptation and
  General-Language Understanding'
---
# Pre-Training on Software Engineering Texts: Effects on Domain Adaptation and General-Language Understanding
> 原文: [https://arxiv.org/abs/2607.06613](https://arxiv.org/abs/2607.06613)

arXiv:2607.06613v1 Announce Type: new
Abstract: Generalist and code-focused Language Models (LMs) are increasingly applied to software engineering (SE), yet whether they are optimized for understanding SE textual artifacts (e.g., issues, commit messages, developer discussions) remains unclear, as most evidence comes from code-focused benchmarks. We study how to adapt encoder and decoder LMs to SE text, comparing continual pre-training (CPT) against pre-training from scratch (PTS) on a new SE corpus, and evaluating both domain adaptation (SELU) and general-language understanding (SuperGLUE). To keep the comparisons fair, we control pre-training under constant-token and compute-matched budgets. We find that across families and sizes, reusing an existing LM dominates training a domain-native one from scratch: CPT yields small and mostly inconclusive domain gains while leaving general-language understanding essentially unchanged, whereas PTS pays a large and usually decisive penalty on both axes and becomes competitive only for small LMs under a token-rich budget. We distill these results into practical guidance for adapting LMs to SE text and release our corpus and pre-trained LMs in our replication kit.

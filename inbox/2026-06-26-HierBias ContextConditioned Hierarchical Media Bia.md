---
interest: medium
link: https://arxiv.org/abs/2606.26100
next_step: skim
priority: high
slack_ts: '1782447548.491619'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'HierBias: Context-Conditioned Hierarchical Media Bias Detection with Multi-Task
  Type Classification'
---
# HierBias: Context-Conditioned Hierarchical Media Bias Detection with Multi-Task Type Classification
> 原文: [https://arxiv.org/abs/2606.26100](https://arxiv.org/abs/2606.26100)

arXiv:2606.26100v1 Announce Type: new
Abstract: Media bias detection is a critical task for ensuring fair and balanced information dissemination, yet existing sentence-level approaches classify each sentence independently, ignoring inter-sentence contextual signals that human annotators naturally exploit. We present \textbf{HierBias}, a hierarchical context-conditioned media bias detector that formally models document context in bias prediction. We introduce the \emph{context-conditioned bias probability} and prove theoretically that leveraging document context strictly reduces the Bayes error of sentence-level classification when inter-sentence mutual information is non-zero. A multi-task generalization bound further establishes that jointly training binary bias detection and fine-grained bias type classification improves sample efficiency on small annotated corpora. Architecturally, HierBias pairs a sentence-level RoBERTa encoder with a cross-sentence Transformer aggregator and dual output heads for binary detection and four-class type classification. Evaluated on BABE and BASIL, HierBias achieves 0.853 F1 and 0.723 MCC, surpassing the state-of-the-art bias-detector by $+2.6\%$ F1 and $+4.3\%$ MCC (McNemar's test, $p < 0.05$). Ablation experiments confirm that each theoretical component contributes independently and consistently.

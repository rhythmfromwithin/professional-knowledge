---
interest: medium
link: https://arxiv.org/abs/2610.27019
next_step: skim
priority: low
slack_ts: '1792556424.572189'
source: cs.DB - Databases
status: unread
title: 'MultiCard: Multiple Attribute Cardinality Estimation via Deep Learning'
---
# MultiCard: Multiple Attribute Cardinality Estimation via Deep Learning
> 原文: [https://arxiv.org/abs/2610.27019](https://arxiv.org/abs/2610.27019)

arXiv:2610.27019v1 Announce Type: new
Abstract: Cardinality estimation is essential for query optimization, but most existing learned estimators focus on a single predicate type, such as string LIKE clauses or numerical range filters. In practice, analytical workloads often combine both types, while the accuracy of string estimators tends to decrease with longer patterns. We introduce MultiCard, a comprehensive learned cardinality estimator that unifies LIKE predicates and numerical filters within a single end-to-end architecture. By combining a Transformer for long-range sparse patterns with an LSTM for short, frequent patterns, MultiCard achieves robust pattern modeling. In parallel, a numerical encoder integrates catalog histograms and structural predicate features, enabling the model to dynamically assess histogram estimation accuracy across different operators and data skew conditions. A final Transformer layer captures interactions among heterogeneous predicates before a multilayer perceptron predicts query cardinalities. We also introduce UPCI, a workload generator that produces length-balanced LIKE patterns, multi-column numerical predicates, and exact cardinality labels for training and evaluation. Experiments on five real-world datasets show that, for string-only workloads, MultiCard achieves the best or near-best Q-error across all datasets compared with state-of-the-art methods. For mixed multi-attribute queries, MultiCard reduces PostgreSQL's mean Q-error by up to 16 times while maintaining an inference latency below 5 ms.

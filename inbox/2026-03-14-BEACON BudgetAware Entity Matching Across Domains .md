---
interest: medium
link: https://arxiv.org/abs/2603.11391
next_step: skim
priority: low
slack_ts: '1773974640.732049'
source: cs.DB - Databases
status: unread
title: 'BEACON: Budget-Aware Entity Matching Across Domains (Extended Technical Report)'
---
# BEACON: Budget-Aware Entity Matching Across Domains (Extended Technical Report)
> 原文: [https://arxiv.org/abs/2603.11391](https://arxiv.org/abs/2603.11391)

arXiv:2603.11391v1 Announce Type: new
Abstract: Entity Matching (EM)--the task of determining whether two data records refer to the same real-world entity--is a core task in data integration. Recent advances in deep learning have set a new standard for EM, particularly through fine-tuning Pretrained Language Models (PLMs) and, more recently, Large Language Models (LLMs). However, fine-tuning typically requires large amounts of labeled data, which are expensive and time-consuming to obtain. In the context of e-commerce matching, labeling scarcity varies widely across domains, raising the question of how to intelligently train accurate domain-specific EM models with limited labeled data. In this work we assume users have only limited amount of labels for a specific target domain but have access to labeled data from other domains. We introduce BEACON, a distribution-aware, budget-aware framework for low-resource EM across domains. BEACON leverages the insight that embedding representations of pairwise candidate matches can guide the effective selection of out-of-domain samples under limited in-domain supervision. We conduct extensive experiments across multiple domain-partitioned datasets derived from established EM benchmarks, demonstrating that BEACON consistently outperforms state-of-the-art methods under different training budgets.

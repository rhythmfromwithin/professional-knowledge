---
interest: medium
link: https://arxiv.org/abs/2609.38053
next_step: skim
priority: low
slack_ts: '1790745154.042539'
source: cs.DB - Databases
status: unread
title: 'VADER: Filtered Vector Search with Declarative Recall'
---
# VADER: Filtered Vector Search with Declarative Recall
> 原文: [https://arxiv.org/abs/2609.38053](https://arxiv.org/abs/2609.38053)

arXiv:2609.38053v1 Announce Type: new
Abstract: Approximate filtered vector search (FVS), a core operation in many data management tasks that combine structured data with vector embeddings, exhibits increased complexity due to the characteristics of filtering predicates. Each predicate is defined by selectivity (i.e., the fraction of vectors that satisfy the predicate) and correlation (i.e., the relationship between the filter and the vector space), which can significantly affect search difficulty even for the same query vector. This poses a key challenge for users aiming to integrate vector search with structured data, as efficient execution often requires extensive manual tuning of algorithm parameters. In this paper, we present VADER, the first approach that eliminates hyperparameter tuning by introducing declarative recall for approximate filtered vector search. With declarative recall, users specify a desired recall target, and VADER executes FVS queries to meet this target without requiring manual configuration. VADER achieves this by employing a filter-aware recall predictor that generalizes across varying selectivities and correlations without explicit tuning, and by performing early termination once the predicted recall reaches the user-defined target. Through extensive experimental evaluation, we show that VADER achieves near-optimal early termination, while providing significant speedups of up to 53% faster and improved result quality of 28% compared to the best-performing baseline.

---
interest: medium
link: https://arxiv.org/abs/2603.07235
next_step: skim
priority: low
slack_ts: '1773132507.371809'
source: cs.DB - Databases
status: unread
title: Novel Table Search [Technical Report]
---
# Novel Table Search [Technical Report]
> 原文: [https://arxiv.org/abs/2603.07235](https://arxiv.org/abs/2603.07235)

arXiv:2603.07235v1 Announce Type: new
Abstract: Avoiding redundancy in query results has been extensively studied in relational databases and information retrieval, yet its implications for data lakes remain largely unexplored. We bridge this gap by investigating how to discover unionable tables that contribute new information for a given query table in large-scale data lakes. We formally define Novel Table Search (NTS) as the problem of finding tables that are novel with respect to a given query table and identify two desirable properties that any scoring function for NTS should satisfy. We introduce a concrete scoring mechanism designed to maximize syntactic novelty, prove that it satisfies the proposed properties, and show that the associated optimization problem is NP-hard. To address this challenge, we develop an efficient approximation technique based on penalization, i.e., Attribute-Based Novel Table Search (ANTs). We propose three additional NTS variants to achieve syntactic novelty and introduce two evaluation metrics for syntactic novelty. Through extensive experiments, we demonstrate that ANTs outperforms other methods in capturing syntactic novelty across evaluation metrics and various benchmarks, while also achieving the lowest execution time.

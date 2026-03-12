---
title: "Evaluating the Practical Effectiveness of LLM-Driven Index Tuning with Microsoft Database Tuning Advisor"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.09181
priority: low
status: unread
interest: medium
next_step: skim
---
# Evaluating the Practical Effectiveness of LLM-Driven Index Tuning with Microsoft Database Tuning Advisor
> 原文: [https://arxiv.org/abs/2603.09181](https://arxiv.org/abs/2603.09181)

arXiv:2603.09181v1 Announce Type: new
Abstract: Index tuning is critical for the performance of modern database systems. Industrial index tuners, such as the Database Tuning Advisor (DTA) developed for Microsoft SQL Server, rely on the "what-if" API provided by the query optimizer to estimate the cost of a query given an index configuration, which can lead to suboptimal recommendations when the estimations are inaccurate. Large language model (LLM) offers a new approach to index tuning, with knowledge learned from web-scale training datasets. However, the effectiveness of LLM-driven index tuning, especially beyond what is already achieved by commercial index tuners, remains unclear.
In this paper, we study the practical effectiveness of LLM-driven index tuning using both industrial benchmarks and real-world enterprise customer workloads, and compare it with DTA. Our results show that although DTA is generally more reliable, with a few invocations, LLM can identify configurations that significantly outperform those found by DTA in execution time in a considerable number of cases, highlighting its potential as a complementary technique. We also observe that LLM's reasoning captures human-intuitive insights that may be distilled to potentially improve DTA. However, adopting LLM-driven index tuning in production remains challenging due to its substantial performance variance, limited and often negative impact when directly integrated into DTA, and the high cost of performance validation. This work provides motivation, lessons, and practical insights that will inspire future work on LLM-driven index tuning both in academia and industry.

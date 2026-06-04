---
interest: medium
link: https://arxiv.org/abs/2606.04610
next_step: skim
priority: low
slack_ts: '1780548678.748229'
source: cs.DB - Databases
status: unread
title: Selectivity Estimation for Semantic Filters on Image Data
---
# Selectivity Estimation for Semantic Filters on Image Data
> 原文: [https://arxiv.org/abs/2606.04610](https://arxiv.org/abs/2606.04610)

arXiv:2606.04610v1 Announce Type: new
Abstract: Semantic data systems integrate Large Language Models (LLMs) and Vision-Language Models (VLMs) directly into database query execution, enabling expressive queries on multi-modal data. However, optimizing these queries requires accurate selectivity estimates to determine the most efficient operator execution order. Contemporary systems rely on online sample-based profiling, a process that incurs severe latency overheads and struggles with low-selectivity queries. In this paper, we introduce Semantic Histograms, a novel selectivity estimator for semantic filters on image data that leverages shared embedding spaces to bypass traditional profiling. We realize that all semantic filters are implicit range queries, as they match a range of different images. Some filter predicates are more general, yielding a wide range, while others are more specific, yielding a smaller range. To address the challenge of implicit ranges, we propose two approaches to estimate the queries' specificity, with an ensemble of the two performing best. The evaluation shows that Semantic Histograms can reduce the end-to-end runtime overhead of query optimization and execution by up to 86%.

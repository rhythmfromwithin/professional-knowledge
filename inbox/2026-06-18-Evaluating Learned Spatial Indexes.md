---
interest: medium
link: https://arxiv.org/abs/2606.19034
next_step: skim
priority: low
slack_ts: '1781759641.353879'
source: cs.DB - Databases
status: unread
title: Evaluating Learned Spatial Indexes
---
# Evaluating Learned Spatial Indexes
> 原文: [https://arxiv.org/abs/2606.19034](https://arxiv.org/abs/2606.19034)

arXiv:2606.19034v1 Announce Type: new
Abstract: Learned indexes improve query performance by adapting search structures to data and workload distributions. Although many learned indexes have been proposed, their trade-offs remain insufficiently understood for spatial range queries, where performance depends not only on model accuracy but also on data and query skew, layout granularity, selectivity, and storage behavior.
In this work, we perform an experimental study of learned indexes for spatial range queries. We examine a representative set of indexes and address seven fundamental questions: (1) How does block size influence query latency, and what configurations yield optimal performance under varying selectivities? (2) How do skewed data and query distributions impact index performance? (3) How do indexes balance refinement and scan costs, and which designs favor one over the other? (4) How do disk-based storage conditions alter optimal block size and latency trade-offs compared to in-memory settings? (5) What are the construction costs of different indexes, and under what query volumes are these costs amortized? (6) For a given data and query workload, which index is expected to perform best? (7) Do index-selection insights learned from synthetic data generalize to real-world data distributions? To enable the analysis, we use a framework with a common storage backend, standardized query execution pipelines, and controlled variations in data and query skew.
Our experiments reveal critical insights into refinement vs. scan trade-offs, the impact of block size, and the interplay between selectivity and layout effectiveness. We synthesize these findings into a workload-based decision tree for index selection and validate it on real OpenStreetMap point sets with synthetic queries, confirming that its recommendations exhibit minimal decision regret and typically yield near-optimal query performance.

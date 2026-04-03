---
interest: medium
link: https://arxiv.org/abs/2603.28769
next_step: skim
priority: medium
slack_ts: '1775185074.617679'
source: cs.DC - Distributed Computing
status: unread
title: 'Spark-LLM-Eval: A Distributed Framework for Statistically Rigorous Large Language
  Model Evaluation'
---
# Spark-LLM-Eval: A Distributed Framework for Statistically Rigorous Large Language Model Evaluation
> 原文: [https://arxiv.org/abs/2603.28769](https://arxiv.org/abs/2603.28769)

arXiv:2603.28769v1 Announce Type: new
Abstract: Evaluating large language models at scale remains a practical bottleneck for many organizations. While existing evaluation frameworks work well for thousands of examples, they struggle when datasets grow to hundreds of thousands or millions of samples. This scale is common when assessing model behavior across diverse domains or conducting comprehensive regression testing. We present Spark-LLM-Eval, a distributed evaluation framework built natively on Apache Spark. The system treats evaluation as a data-parallel problem, partitioningexamplesacrossexecutorsandaggregatingresultswithproperstatistical accounting. Beyond raw throughput, we emphasize statistical rigor: every reported metric includes bootstrap confidence intervals, and model comparisons come with appropriate significance tests (paired t-tests, McNemar's test, or Wilcoxon signed-rank, depending on the metric type). The framework also addresses the cost problem inherent in LLM evaluation through content-addressable response caching backed by Delta Lake, which allows iterating on metric definitions without re-running inference. We describe the system architecture, the statistical methodology, and report benchmark results showing linear scaling with cluster size. The framework and all evaluation code are available as open source.

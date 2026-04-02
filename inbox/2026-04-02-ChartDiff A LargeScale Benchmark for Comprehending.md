---
title: "ChartDiff: A Large-Scale Benchmark for Comprehending Pairs of Charts"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.28902
priority: high
status: unread
interest: medium
next_step: skim
---
# ChartDiff: A Large-Scale Benchmark for Comprehending Pairs of Charts
> 原文: [https://arxiv.org/abs/2603.28902](https://arxiv.org/abs/2603.28902)

arXiv:2603.28902v1 Announce Type: new
Abstract: Charts are central to analytical reasoning, yet existing benchmarks for chart understanding focus almost exclusively on single-chart interpretation rather than comparative reasoning across multiple charts. To address this gap, we introduce ChartDiff, the first large-scale benchmark for cross-chart comparative summarization. ChartDiff consists of 8,541 chart pairs spanning diverse data sources, chart types, and visual styles, each annotated with LLM-generated and human-verified summaries describing differences in trends, fluctuations, and anomalies. Using ChartDiff, we evaluate general-purpose, chart-specialized, and pipeline-based models. Our results show that frontier general-purpose models achieve the highest GPT-based quality, while specialized and pipeline-based methods obtain higher ROUGE scores but lower human-aligned evaluation, revealing a clear mismatch between lexical overlap and actual summary quality. We further find that multi-series charts remain challenging across model families, whereas strong end-to-end models are relatively robust to differences in plotting libraries. Overall, our findings demonstrate that comparative chart reasoning remains a significant challenge for current vision-language models and position ChartDiff as a new benchmark for advancing research on multi-chart understanding.

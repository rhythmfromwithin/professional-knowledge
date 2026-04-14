---
interest: medium
link: https://arxiv.org/abs/2604.08935
next_step: skim
priority: medium
slack_ts: '1776137317.457889'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A novel hybrid approach for positive-valued DAG learning
---
# A novel hybrid approach for positive-valued DAG learning
> 原文: [https://arxiv.org/abs/2604.08935](https://arxiv.org/abs/2604.08935)

arXiv:2604.08935v1 Announce Type: new
Abstract: Causal discovery from observational data remains a fundamental challenge in machine learning and statistics, particularly when variables represent inherently positive quantities such as gene expression levels, asset prices, company revenues, or population counts, which often follow multiplicative rather than additive dynamics. We propose the Hybrid Moment-Ratio Scoring (H-MRS) algorithm, a novel method for learning directed acyclic graphs (DAGs) from positive-valued data by combining moment-based scoring with log-scale regression. The key idea is that for positive-valued variables, the moment ratio $\frac{\mathbb{E}[X\_j^2]}{\mathbb{E}[(\mathbb{E}[X\_j \mid S])^2]}$ provides an effective criterion for causal ordering, where $S$ denotes candidate parent sets. H-MRS integrates log-scale Ridge regression for moment-ratio estimation with a greedy ordering procedure based on raw-scale moment ratios, followed by Elastic Net-based parent selection to recover the final DAG structure. Experiments on synthetic log-linear data demonstrate competitive precision and recall. The proposed method is computationally efficient and naturally respects positivity constraints, making it suitable for applications in genomics and economics. These results suggest that combining log-scale modeling with raw-scale moment ratios provides a practical framework for causal discovery in positive-valued domains.

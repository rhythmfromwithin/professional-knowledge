---
interest: medium
link: https://arxiv.org/abs/2607.06607
next_step: skim
priority: high
slack_ts: '1783655939.190529'
source: cs.LG - Machine Learning
status: unread
title: 'NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts'
---
# NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts
> 原文: [https://arxiv.org/abs/2607.06607](https://arxiv.org/abs/2607.06607)

arXiv:2607.06607v1 Announce Type: new
Abstract: Accurate long-term forecasting in complex systems is frequently compromised by dataset-level distribution shifts, where diverse underlying behavioral modes and evolving system states drive the dynamic multivariate time-series. While existing methods predominantly focus on local temporal shifts, they fail to explicitly model the global structural challenge where datasets are composites of distinct operational regimes. In this paper, we propose NEST, a specialized framework designed to model and recompose these evolving structures through a two-phase dense MoE architecture. NEST first facilitates structural specialization by partitioning the dataset into distinct operational regimes through unsupervised clustering in a principled moment-entropy space. We introduce a regime-oriented router mechanism that generates initial expert weights based on temporal content, subsequently refined through geometric modulation to regime centroids. Crucially, rather than acting as monolithic predictors, individual experts function as specialized kernels that capture regime-specific dynamics by evolving unique variate-attention patterns. Extensive evaluations on diverse benchmarks, including heterogeneous network traffic and physical phenomena, demonstrate that NEST consistently achieves state-of-the-art performance. Our code and datasets are available at https://github.com/Aaralshin/NEST

---
title: "DySCo: Dynamic Semantic Compression for Effective Long-term Time Series Forecasting"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.01261
priority: high
status: unread
interest: medium
next_step: skim
---
# DySCo: Dynamic Semantic Compression for Effective Long-term Time Series Forecasting
> 原文: [https://arxiv.org/abs/2604.01261](https://arxiv.org/abs/2604.01261)

arXiv:2604.01261v1 Announce Type: new
Abstract: Time series forecasting (TSF) is critical across domains such as finance, meteorology, and energy. While extending the lookback window theoretically provides richer historical context, in practice, it often introduces irrelevant noise and computational redundancy, preventing models from effectively capturing complex long-term dependencies. To address these challenges, we propose a Dynamic Semantic Compression (DySCo) framework. Unlike traditional methods that rely on fixed heuristics, DySCo introduces an Entropy-Guided Dynamic Sampling (EGDS) mechanism to autonomously identify and retain high-entropy segments while compressing redundant trends. Furthermore, we incorporate a Hierarchical Frequency-Enhanced Decomposition (HFED) strategy to separate high-frequency anomalies from low-frequency patterns, ensuring that critical details are preserved during sparse sampling. Finally, a Cross-Scale Interaction Mixer(CSIM) is designed to dynamically fuse global contexts with local representations, replacing simple linear aggregation. Experimental results demonstrate that DySCo serves as a universal plug-and-play module, significantly enhancing the ability of mainstream models to capture long-term correlations with reduced computational cost.

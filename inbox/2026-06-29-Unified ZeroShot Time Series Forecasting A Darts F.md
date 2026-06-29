---
interest: medium
link: https://arxiv.org/abs/2606.27438
next_step: skim
priority: high
slack_ts: '1782708435.417649'
source: cs.LG - Machine Learning
status: unread
title: 'Unified Zero-Shot Time Series Forecasting: A Darts Foundation'
---
# Unified Zero-Shot Time Series Forecasting: A Darts Foundation
> 原文: [https://arxiv.org/abs/2606.27438](https://arxiv.org/abs/2606.27438)

arXiv:2606.27438v1 Announce Type: new
Abstract: Since its initial release in 2020, Darts has become a widely used open-source Python library for time series analysis. A series of foundation models have recently claimed accuracy improvements in zero-shot forecasting, promising a paradigm shift from training custom models to harnessing pre-trained general-purpose forecasters. Foundation models, however, are often released as isolated packages with fragmented interfaces and limited interoperability with common tooling, making joint evaluation and integration within complete pipelines difficult. In Darts, we developed a unified $\texttt{FoundationModel}$ class collection (Chronos-2, TimesFM 2.5, TiRex, PatchTST-FM) that provides standardized, full-cycle forecasting interfaces with minimal external dependencies for integrating foundation models into the ecosystem. Existing Darts pipelines can now use foundation models with only a name change; new pipelines can use them for zero-shot or fine-tuned forecasting, uncertainty estimation, and backtesting, combined with data processing and evaluation tooling, all within a unified framework.

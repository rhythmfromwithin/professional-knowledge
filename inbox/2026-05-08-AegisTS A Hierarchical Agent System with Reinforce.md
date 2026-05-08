---
title: "AegisTS: A Hierarchical Agent System with Reinforcement Learning for Multivariate Time Series Data Cleaning"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.04902
priority: low
status: unread
interest: medium
next_step: skim
---
# AegisTS: A Hierarchical Agent System with Reinforcement Learning for Multivariate Time Series Data Cleaning
> 原文: [https://arxiv.org/abs/2605.04902](https://arxiv.org/abs/2605.04902)

arXiv:2605.04902v2 Announce Type: new
Abstract: Multivariate time series (MTS) are frequently affected by co-occurring quality issues, such as missing values, outliers, and constraint violations, which significantly undermine downstream analytics. Existing cleaning approaches fix only a limited set of such issues, making them ill-suited for scenarios where multiple quality problems arise simultaneously. Furthermore, these methods commonly depend on the availability of ground truth data or domain-specific rules, both of which are rarely accessible in real-world applications.
In this paper, we introduce \sys, an agent system with reinforcement learning designed to clean multiple data quality issues in MTS. We cast the cleaning process as a joint optimization problem that simultaneously handles quality issue order and cleaning model selection, allowing efficient navigation of the large space of possible cleaning pipelines. Our framework relies on a hierarchical agent architecture, where a high-level agent determines the order in which data quality issues should be processed, while a low-level agent identifies the most suitable cleaning method for each issue. To guide the agent toward an optimal cleaning pipeline, we propose a dual-stage reward mechanism that couples upstream (cleaning) and downstream performance, enabling effective optimization without relying on ground truth. Our experimental results show that \sys consistently outperforms existing methods, achieving up to 96\% improvement in data cleaning quality and 27\% improvement in downstream performance.

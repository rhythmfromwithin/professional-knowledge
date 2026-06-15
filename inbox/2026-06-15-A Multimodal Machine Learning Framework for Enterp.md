---
interest: medium
link: https://arxiv.org/abs/2606.13699
next_step: skim
priority: low
slack_ts: '1781500239.305369'
source: cs.DB - Databases
status: unread
title: A Multimodal Machine Learning Framework for Enterprise Database Workload-Aware
  Root Cause Analysis
---
# A Multimodal Machine Learning Framework for Enterprise Database Workload-Aware Root Cause Analysis
> 原文: [https://arxiv.org/abs/2606.13699](https://arxiv.org/abs/2606.13699)

arXiv:2606.13699v1 Announce Type: new
Abstract: Root cause analysis for enterprise database incidents is often a manual and time consuming process that requires operators to inspect logs, performance metrics, and workload behavior. Existing approaches commonly focus on a single source of evidence, which limits their ability to capture the broader operational context behind incidents such as CPU saturation, I/O bottlenecks, lock contention, deadlocks, and slow query execution.
This paper presents a multimodal machine learning framework for workload-aware root cause analysis in enterprise database environments. The proposed approach combines workload characteristics, system telemetry, and operational signals from compute, storage, and accelerator oriented datasets. Engineered workload aware features are used to classify workload behavior and support downstream diagnosis of likely incident causes.
The framework evaluates Random Forest, LightGBM, and feedforward neural network models for workload classification and root cause analysis support. Experimental results show that workload aware feature engineering improves workload separability, with LightGBM providing the strongest balance of predictive performance and interpretability. The results suggest that combining multimodal telemetry with workload context can provide a practical foundation for automated and explainable root cause analysis systems.

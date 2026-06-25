---
interest: medium
link: https://arxiv.org/abs/2606.25388
next_step: skim
priority: low
slack_ts: '1782360771.060039'
source: cs.DB - Databases
status: unread
title: 'TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning'
---
# TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning
> 原文: [https://arxiv.org/abs/2606.25388](https://arxiv.org/abs/2606.25388)

arXiv:2606.25388v1 Announce Type: new
Abstract: Reliable analytics and machine-learning pipelines depend on clean tabular data, yet production tables often contain missing values, typographical errors, inconsistent formats, violated dependencies, unit mismatches, and ambiguous categorical values. Existing cleaning systems make different trade-offs. Constraint-based systems need experts to specify rules. Learning-based systems need labels or retraining. Recent LLM-based cleaners reduce setup effort, but many call an LLM on rows, cells, or repeated workflow steps, so their cost grows with table size and with every recurring batch.
We present TabClean, a model-training-free system that compiles LLM reasoning into reusable guarded cleaning programs. Given a dirty table and a small annotated development set, TabClean profiles table evidence, diagnoses repair mechanisms, synthesizes executable Python transformations, validates candidates with cell-level feedback, and commits the best program for reuse on schema-compatible batches. The key abstraction is an evidence-backed guarded repair clause. A deterministic transformation may fire only when its dirty pattern, target-negative condition, evidence support, and scope constraints are satisfied. Across six benchmarks, TabClean achieves high precision, improves F1 over representative rule-based, learning-based, and LLM-based baselines on five datasets, and substantially reduces recurring runtime and API cost by replacing repeated LLM inference with deterministic program execution.

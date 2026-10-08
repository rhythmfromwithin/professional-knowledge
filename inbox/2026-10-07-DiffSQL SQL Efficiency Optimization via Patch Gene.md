---
interest: medium
link: https://arxiv.org/abs/2610.06857
next_step: skim
priority: low
slack_ts: '1791438074.442219'
source: cs.DB - Databases
status: unread
title: 'Diff-SQL: SQL Efficiency Optimization via Patch Generation and Constraint
  Alignment'
---
# Diff-SQL: SQL Efficiency Optimization via Patch Generation and Constraint Alignment
> 原文: [https://arxiv.org/abs/2610.06857](https://arxiv.org/abs/2610.06857)

arXiv:2610.06857v1 Announce Type: new
Abstract: SQL efficiency optimization aims to transform slow queries into semantically equivalent but faster alternatives. However, directly optimizing SQL with large language models in an end-to-end fashion often induces Objective Misalignment which creates a fundamental tension between optimization and correctness, making direct full SQL rewriting unreliable for execution-facing database applications. To address this problem, we propose Diff-SQL, a two-stage framework that decouples efficiency-oriented optimization from constraint-aware alignment. The first stage identifies optimization opportunities and proposes targeted edits in the form of a unified diff patch, while the second stage is trained with on-policy reinforcement learning to revise outputs under executability and semantic-equivalence constraints. To train and evaluate Diff-SQL, we construct an automated pipeline that mines optimization knowledge from StackOverflow and builds Slow-Fast SQL pairs through cascaded filtering. We further introduce Effi-SQL, a benchmark containing 1,100 human-verified Slow-Fast pairs across five SQL dialects. Experiments show that Objective Misalignment is widespread across existing LLM-based SQL optimization methods, where direct full SQL optimization causes an average 22.7% execution accuracy degradation across frontier models such as Claude-Opus-4.6, with the worst model dropping by 43.0%. Diff-SQL alleviates this trade-off. As an inference-only strategy, it improves R-VES by 10.0% on average while reducing execution accuracy degradation by 6.11% on average across three strong base models. With execution-grounded training, Diff-SQL further enables a 7B model to improve R-VES from 33.42% to 46.83%, demonstrating that the proposed two-stage optimization-and-alignment paradigm can deliver both stronger efficiency and better correctness in local, small model deployment settings.

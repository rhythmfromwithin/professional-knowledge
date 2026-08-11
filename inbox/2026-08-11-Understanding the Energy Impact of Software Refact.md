---
title: "Understanding the Energy Impact of Software Refactoring: A Workload-Aware Study of Controlled Examples and Real-World Commits"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.06620
priority: low
status: unread
interest: medium
next_step: skim
---
# Understanding the Energy Impact of Software Refactoring: A Workload-Aware Study of Controlled Examples and Real-World Commits
> 原文: [https://arxiv.org/abs/2608.06620](https://arxiv.org/abs/2608.06620)

arXiv:2608.06620v1 Announce Type: new
Abstract: Refactoring improves software maintainability while preserving functional behavior, yet behavior preservation does not imply energy neutrality. Existing studies primarily examine isolated refactorings under fixed or simple workloads, leaving the effects of workload variation, real-world refactoring practices, explanatory factors, and energy regression identification insufficiently understood. We present the first large-scale empirical study of the energy impact of refactoring across two complementary Java benchmarks: a Micro-benchmark, comprising 68 refactoring types evaluated under diverse workloads, and a Practical-benchmark, containing 481 real-world refactoring commits from 430 GitHub projects. Using repeated paired energy measurements, we analyze workload sensitivity, refactoring patterns, explanatory factors, and the effectiveness of metric- and LLM-based regression identification. In the Micro-benchmark, 199 of 384 refactoring-workload pairs (51.8%) exhibit statistically significant energy differences, and 45.3% of refactoring instances change energy-impact classification across workloads. In the Practical-benchmark, only 36 commits (7.5%) show significant energy changes, although two-thirds differ by at least 10%. Refactoring type alone is insufficient to predict energy outcomes, while certain recurring refactoring combinations are associated with energy reductions. Changes in execution time consistently explain energy variation in the controlled benchmark but correlate weakly with energy changes in real-world commits. Our findings highlight the need for workload-diverse evaluation of the energy impact of refactoring; neither existing metric-based approaches nor LLM-based predictors can reliably identify refactoring-induced energy regressions, motivating the development of more accurate techniques for predicting the energy impact of refactoring.

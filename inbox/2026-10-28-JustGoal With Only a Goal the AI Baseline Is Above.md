---
title: "JustGoal: With Only a Goal, the AI Baseline Is Above the Expert Kernels"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.36434
priority: medium
status: unread
interest: medium
next_step: skim
---
# JustGoal: With Only a Goal, the AI Baseline Is Above the Expert Kernels
> 原文: [https://arxiv.org/abs/2610.36434](https://arxiv.org/abs/2610.36434)

arXiv:2610.36434v1 Announce Type: new
Abstract: A small number of GPU kernels often determines the efficiency of large language model training and inference. High-performance kernel development typically relies on expert knowledge through manual implementation, collaboration with general-purpose models, or specialized agents equipped with domain knowledge, evaluation methods, and search workflows. We investigate how much value this knowledge provides as foundation models become stronger. We introduce JustGoal, a goal-only baseline in which a general-purpose agent receives only the optimization objective and constraints, without kernel-specific infrastructure, knowledge bases, or predefined workflows, and builds its own evaluation loop. On NVIDIA B200 GPUs, JustGoal outperforms open-source libraries on 8 of 10 operators, achieving per-operator geometric mean speedups of 1.14x to 2.34x. It also surpasses the fastest publicly released specialized-agent kernel on 5 of 9 operators with available comparisons. In a controlled same-model comparison using Fable 5.1 on single shapes, the KDA-0.5 harness reaches 0.95x of JustGoal's performance, while single-mechanism ablations show no consistent benefit from domain knowledge or predefined workflows. These results indicate that specialized machinery should be justified by clear gains over a same-model, same-scope goal-only baseline and reevaluated whenever the foundation model changes.

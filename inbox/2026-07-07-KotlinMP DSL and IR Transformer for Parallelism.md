---
interest: medium
link: https://arxiv.org/abs/2607.02519
next_step: skim
priority: medium
slack_ts: '1783397057.210609'
source: cs.DC - Distributed Computing
status: unread
title: 'Kotlin-MP: DSL and IR Transformer for Parallelism'
---
# Kotlin-MP: DSL and IR Transformer for Parallelism
> 原文: [https://arxiv.org/abs/2607.02519](https://arxiv.org/abs/2607.02519)

arXiv:2607.02519v1 Announce Type: new
Abstract: While Kotlin provides exceptional abstractions for asynchronous concurrency (like Coroutines for I/O), it lacks low-overhead, directive-based constructs for true hardware parallelism. When developers attempt to parallelize compute-bound mathematical loops using standard task-parallel libraries, they encounter significant runtime overhead such as lambda allocations and state-machine generation due to the abstraction layers, and face difficulties in ensuring readability, reliability and maintainability in implementing them.
To address this, this project proposes Kotlin-MP, a native Kotlin Domain-Specific Language (DSL) paired with a custom Intermediate Representation (IR) transformer as a Kotlin compiler plugin. The DSL provides an intuitive, OpenMP-like syntax for developers to denote parallel regions, schedules, and critical sections. Instead of acting as a standard runtime wrapper, the IR transformer intercepts this DSL at compile-time and structurally rewrites the code. It lowers the parallelized sections directly into optimized \textit{java.util.concurrent.ForkJoinPool} tasks, automatically managing loop chunking, performing thread scheduling, and injecting hardware synchronization and mutual exclusion.

---
title: "Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.20370
priority: medium
status: unread
interest: medium
next_step: skim
---
# Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf
> 原文: [https://arxiv.org/abs/2608.20370](https://arxiv.org/abs/2608.20370)

arXiv:2608.20370v1 Announce Type: new
Abstract: We present XPerf, a benchmarking framework that load-tests LLM serving systems with diverse agentic AI workloads. It provides detailed profiling of the serving system and hardware, enabling users to identify performance bottlenecks introduced by agentic workloads. Benchmarking LLM serving systems under agentic workloads is challenging - agentic applications rely on nondeterministic LLM outputs to guide their control flow; therefore, workload patterns vary unpredictably from run to run. XPerf minimizes this workload variation with a fine-grained trace replay approach: it enables users to easily collect traces from real agentic applications, synthesize new workloads with various patterns if needed, and reproducibly replay them on different LLM serving systems. XPerf includes eight agentic applications across diverse use cases (e.g., coding, deep research, and Q&A) by default. Our empirical study using these workloads shows that XPerf accurately replays agentic workloads, provides detailed performance breakdowns, scales to larger serving systems, and assists in serving system debugging. We will open-source XPerf on GitHub.

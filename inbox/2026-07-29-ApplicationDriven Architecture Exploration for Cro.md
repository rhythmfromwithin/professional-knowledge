---
title: "Application-Driven Architecture Exploration for Cross-Layer Heterogeneous Systems"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.23042
priority: medium
status: unread
interest: medium
next_step: skim
---
# Application-Driven Architecture Exploration for Cross-Layer Heterogeneous Systems
> 原文: [https://arxiv.org/abs/2607.23042](https://arxiv.org/abs/2607.23042)

arXiv:2607.23042v1 Announce Type: new
Abstract: AI and HPC infrastructure increasingly serves workload portfolios that combine dense tensor computation, sparse kernels, large memory footprints, and communication-intensive collectives. Supporting these portfolios requires coordinated choices across accelerators, memory tiers, scale-up fabrics, and cluster networks. The resulting Cross-layer Heterogeneous System (XHS) design space is difficult to explore: hardware choices change legal task mappings, while rack power, switch radix, cabling, and cost constraints invalidate many candidates. We present CHASE, an application-driven framework that searches physically feasible XHS architectures through the workloads they must execute. CHASE represents candidates as hierarchical typed graphs and rejects designs that violate deployment constraints. It avoids intractable joint hardware-mapping search with a decoupled two-level loop: an inner mapper translates hardware-independent workload DAGs into topology-aware event traces, a calibrated event-driven simulator evaluates each mapping, and an outer telemetry-guided optimizer evolves the hardware graph. We evaluate CHASE on sparse-computing and LLM workloads. Its mapper remains within 6.06% of exhaustive optima while reducing mapping time by 60.5% on average relative to PEFT. Compute-model errors average 4.4-7.5%, and communication validation reproduces key trends across physical platforms. The outer search reaches near-global optima within 64 iterations. End-to-end case studies show that sparse workloads favor criticality-aware heterogeneous pods, whereas LLM inference favors scale-up islands; the resulting designs deliver 6.20$\times$ and 2.12$\times$ geomean speedups, respectively, while reducing cost and power relative to the baselines.

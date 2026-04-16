---
interest: medium
link: https://arxiv.org/abs/2604.09556
next_step: skim
priority: medium
slack_ts: '1776310484.744259'
source: cs.DC - Distributed Computing
status: unread
title: 'Para-B&B: Load-Balanced Deterministic Parallelization of Solving MIP'
---
# Para-B&B: Load-Balanced Deterministic Parallelization of Solving MIP
> 原文: [https://arxiv.org/abs/2604.09556](https://arxiv.org/abs/2604.09556)

arXiv:2604.09556v1 Announce Type: new
Abstract: Mixed-integer programming (MIP) extends linear programming by incorporating both continuous and integer decision variables, making it widely used in production planning, logistics scheduling, and resource allocation. However, MIP remains NP-hard and cannot generally be solved to optimality in polynomial time. Branch-and-bound, a fundamental exact method, faces significant parallelization challenges due to computational heterogeneity and strict determinism requirements in commercial applications. This paper presents the first fully open-source implementation of deterministic parallel branch-and-bound for HiGHS, a high-performance MIP solver. Our approach introduces a novel data-parallel architecture ensuring strict determinism by replicating complete solver state across worker threads and eliminating non-deterministic synchronization primitives. A key innovation is our AI-driven load balancing mechanism employing multi-stage workload prediction models that estimate node computational complexity based on structural characteristics and historical performance data, coupled with dynamic parameter adjustment strategies. The framework executes orchestrated parallel phases including concurrent dive operations, systematic data consolidation, and intelligent node selection. Comprehensive experimental evaluation on 80 MIPLIB 2017 benchmark instances demonstrates effectiveness, achieving a geometric mean speedup of 2.17 using eight threads while maintaining complete deterministic guarantees. Performance gains become increasingly pronounced for higher node counts, with speedup factors reaching 5.12 for computationally intensive instances and thread idle rates averaging 34.7%.

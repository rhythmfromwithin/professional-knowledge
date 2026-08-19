---
interest: medium
link: https://arxiv.org/abs/2608.13824
next_step: skim
priority: medium
slack_ts: '1787103713.262539'
source: cs.DC - Distributed Computing
status: unread
title: 'Balancing Workload Performance and Slurm Stress: Four Nextflow Deployment
  Strategies'
---
# Balancing Workload Performance and Slurm Stress: Four Nextflow Deployment Strategies
> 原文: [https://arxiv.org/abs/2608.13824](https://arxiv.org/abs/2608.13824)

arXiv:2608.13824v1 Announce Type: new
Abstract: Wide Nextflow fan-outs on shared Slurm clusters can submit tens of thousands of short tasks. Deployment choices - individual jobs, arrays, or nested schedulers within allocations - affect both workflow turnaround and RPC volume, a shared cost that can degrade scheduler responsiveness. Existing studies compare whole workflow systems, while per-task queueing metrics do not span architectures that dispatch inside an existing allocation. We present a reproducible measurement protocol and bench harness with two key elements. First, a clean-start clock begins before any backend service or allocation request, placing different architectures on a common time axis. Second, per-user Slurm sdiag counters measure attributable RPC demand, with controller processing time reported as a sensitivity context separate from cluster-wide state. We evaluate four multi-node strategies: Slurm native, Slurm job arrays, HyperQueue, and Flux, on the shared ASU Phoenix production cluster; the single-user Dev campaign includes native, arrays, and Flux. The fixed workload contains 4,823 LASTZ tasks, with one clean-start trial per configuration in this preliminary campaign. Results show a walltime-RPC trade-off. On Phoenix, arrays and HyperQueue reached the milestone in 0.32 h, while Flux took 0.65 h but reduced attributable RPCs to 1,396 per 1,000 terminal tasks; all three were non-dominated. On Dev, arrays and Flux formed the observed frontier: 0.80 h for arrays versus 0.84 h for Flux, with Flux reducing RPCs to 1,769 per 1,000 terminal tasks. The method enables HPC sites to compare deployment strategies using metrics that capture both user experience and scheduler impact, and to choose the fastest strategy within a site-specific RPC budget.

---
interest: medium
link: https://arxiv.org/abs/2610.04236
next_step: skim
priority: medium
slack_ts: '1791266366.777339'
source: cs.DC - Distributed Computing
status: unread
title: 'OACM: Optimistic Asynchronous Communication Model for Large-Scale SNN Simulation'
---
# OACM: Optimistic Asynchronous Communication Model for Large-Scale SNN Simulation
> 原文: [https://arxiv.org/abs/2610.04236](https://arxiv.org/abs/2610.04236)

arXiv:2610.04236v1 Announce Type: new
Abstract: Spiking Neural Network (SNN) simulation serves as a crucial tool for understanding brain dynamics and advancing neuromorphic computing, but faces significant scalability challenges in large-scale distributed implementations. The primary bottlenecks arise from frequent synchronization overhead in time-driven simulators and extensive secondary rollbacks in optimistic PDES approaches, compounded by inefficient communication patterns that underutilize network bandwidth. In this paper, we propose OACM, an Optimistic Asynchronous Communication Model that addresses these challenges through three key innovations. First, we design Optimistic Hybrid SNN Simulation that combines the implementation simplicity of time-driven approaches with reduced synchronization frequency through strategic rollback mechanisms within synchronization windows. Second, we implement asynchronous one-sided communication using the UNR library, eliminating handshake latency and achieving complete computation-communication overlap. Third, we develop adaptive message aggregation and routing strategies within a 2D-HyperX virtual topology to optimize bandwidth utilization for small message traffic. Experimental evaluation on a high-performance computing cluster demonstrates that OACM achieves up to 1.4x speedup over the original CORTEX simulator and over 22.6x speedup compared to NEST when simulating a multi-area marmoset brain model at scales of up to 174 compute nodes.

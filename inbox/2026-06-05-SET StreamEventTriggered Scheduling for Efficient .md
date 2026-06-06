---
interest: medium
link: https://arxiv.org/abs/2606.05495
next_step: skim
priority: medium
slack_ts: '1780718920.490979'
source: cs.DC - Distributed Computing
status: unread
title: 'SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines'
---
# SET: Stream-Event-Triggered Scheduling for Efficient CUDA Graph Pipelines
> 原文: [https://arxiv.org/abs/2606.05495](https://arxiv.org/abs/2606.05495)

arXiv:2606.05495v1 Announce Type: new
Abstract: Achieving peak GPU performance remains a significant challenge as the system throughput is constrained by host-device synchronization delays and kernel scheduling overheads, even with aggressive kernel optimizations and batch processing. Furthermore, existing approaches often underutilize hardware resources such as compute cores and copy engines due to scheduling overheads. To address these problems, we propose a CUDA runtime framework for task-parallel pipelines to minimize the synchronization overheads and the gap between kernel executions. The proposed solution combines two innovations: (1) a multi-stream task-parallel pipeline programming model that leverages event-chaining and work-stealing mechanisms to fully utilize available hardware resources; (2) a graph-based execution flow with per-stream buffers to ensure memory safety for multiple in-flight jobs running concurrently. Extensive evaluations on representative real-world workloads show 1.15--1.44X speedup and reduce scheduling overheads by 18--54% compared to state-of-the-art CUDA graph baselines.

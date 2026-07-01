---
interest: medium
link: https://arxiv.org/abs/2606.30848
next_step: skim
priority: medium
slack_ts: '1782880938.430579'
source: cs.DC - Distributed Computing
status: unread
title: 'StreamGuard: Low-Overhead Resilience for Real-time HPC Data Streams'
---
# StreamGuard: Low-Overhead Resilience for Real-time HPC Data Streams
> 原文: [https://arxiv.org/abs/2606.30848](https://arxiv.org/abs/2606.30848)

arXiv:2606.30848v1 Announce Type: new
Abstract: Real-time scientific workflows operate on continuous data streams and must produce timely, high-quality results despite executing on complex, failure-prone infrastructure. Hardware faults, network disruptions, and performance anomalies caused by resource contention or system heterogeneity can severely degrade performance and violate real-time constraints. We focus on strengthening the resilience of the producer-consumer streaming pattern, a fundamental building block of scientific streaming workflows. We present two complementary techniques: (i) a dynamic, asynchronous, non-blocking checkpointing mechanism that preserves progress without interrupting computation, and (ii) a progress-aware load redistribution strategy that detects slow workers and proactively rebalances tasks. Together, these mechanisms maintain forward progress and balanced execution even in highly error-prone environments. Experimental results show that our approach reduces the impact of failures and performance anomalies by up to 6x, while introducing less than 1% overhead in failure-free execution.

---
interest: medium
link: https://arxiv.org/abs/2608.05633
next_step: skim
priority: medium
slack_ts: '1786154735.303579'
source: cs.DC - Distributed Computing
status: unread
title: Serverless platform driven CPU loadbalancing
---
# Serverless platform driven CPU loadbalancing
> 原文: [https://arxiv.org/abs/2608.05633](https://arxiv.org/abs/2608.05633)

arXiv:2608.05633v1 Announce Type: new
Abstract: Serverless platforms maintain a global view of function invocations and resource utilization, yet existing systems largely restrict CPU scheduling decisions to the operating system scheduler. This paper presents a serverless platform-driven CPU load balancing framework that enables the control plane to directly influence CPU scheduling through a custom Linux scheduler built on SchedExt(SCX). The proposed scheduler introduces configurable scheduling domains and a shared interface that allows the control plane to assign functions to domains based on their historical inter-arrival times. Within each domain, a single-queue load-balancing strategy combined with a virtual-time prioritization policy improves task placement while reducing interference from busy-polling tasks. Results show that an eight-domain configuration achieves the best trade-off, reducing system energy consumption by approximately 15% while increasing invocation cost by only 5%. Under heavily loaded workloads, the proposed scheduler also reduces request latency by up to 50% compared to the default Linux Completely Fair Scheduler (CFS). These results demonstrate that exposing CPU scheduling decisions to the serverless control plane can improve both energy efficiency and workload performance while preserving scheduling flexibility.

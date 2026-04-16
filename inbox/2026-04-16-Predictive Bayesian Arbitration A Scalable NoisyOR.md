---
interest: medium
link: https://arxiv.org/abs/2604.11989
next_step: skim
priority: medium
slack_ts: '1776310499.032129'
source: cs.DC - Distributed Computing
status: unread
title: 'Predictive Bayesian Arbitration: A Scalable Noisy-OR Model with Service Criticality
  Awareness'
---
# Predictive Bayesian Arbitration: A Scalable Noisy-OR Model with Service Criticality Awareness
> 原文: [https://arxiv.org/abs/2604.11989](https://arxiv.org/abs/2604.11989)

arXiv:2604.11989v1 Announce Type: new
Abstract: Geographically High-Available (Geo-HA) cluster systems are essential for service continuity in distributed cloud-native environments. However, traditional arbitration mechanisms, which are often predicated on deterministic node-level heartbeats, are resource-intensive and inherently reactive. This necessitates a dedicated arbiter per deployment and leads to reactive switchovers that incur unavoidable downtime, occurring only after a failure has already compromised the system. This paper presents a novel predictive arbitration framework that utilizes a shared, microservice-based architecture to consolidate arbitration logic across multiple Geo-HA domains, significantly reducing the aggregate infrastructure footprint. Central to our approach is an adaptive online learning mechanism grounded in a Bayesian Noisy-OR model that autonomously discovers and learns temporal cascade dependencies from emergent failure patterns. To overcome the "cold start" challenge, the system utilizes expert-informed priors that are dynamically refined at runtime without manual configuration. Experimental results demonstrate that this framework achieves a 60\% reduction in Mean Time to Failure Detection (MTTFD) and improves total switchover efficiency by up to 77.8\% compared to traditional reactive standards. By enabling a significant predictive lead time, the system allows switchovers to initiate proactively before hard failures occur, while maintaining a linear $O(n)$ computational complexity. This approach provides a scalable, context-aware alternative that bridges the performance-durability gap in modern microservice architectures.

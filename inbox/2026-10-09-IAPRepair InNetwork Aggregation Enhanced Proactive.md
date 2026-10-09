---
title: "IAPRepair: In-Network Aggregation Enhanced Proactive Repair for Erasure-Coded Storage System"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.11114
priority: medium
status: unread
interest: medium
next_step: skim
---
# IAPRepair: In-Network Aggregation Enhanced Proactive Repair for Erasure-Coded Storage System
> 原文: [https://arxiv.org/abs/2610.11114](https://arxiv.org/abs/2610.11114)

arXiv:2610.11114v1 Announce Type: new
Abstract: Erasure-coded storage provides fault tolerance with substantially lower storage overhead than full replication, but repairing lost or at-risk blocks requires intensive cross-node data transfer. Existing reactive repair schemes start only after a failure, while proactive schemes can move data before failure but commonly treat migration, reconstruction, and network aggregation as loosely coupled operations. As a result, receiver?side bottlenecks, heterogeneous available bandwidth, and limited programmable-switch state continue to constrain repair paral?lelism. This paper presents IAPRepair, an in-network aggre?gation enhanced proactive repair framework for erasure-coded storage. IAPRepair jointly constructs each repair batch, assigns reconstruction providers and replacement nodes according to normalized transmission loads, schedules migration around the remaining receive capacity, and selectively enables in-network aggregation for reconstruction blocks that would otherwise over?load healthy nodes. The selective design reduces receiver-side traffic while retaining migration parallelism and respecting a configurable switch-resource budget. We implement IAPRepair with a Tofino programmable switch and 16 storage nodes, and evaluate it using both a prototype testbed and large-scale simu?lations. Across coding parameters, block sizes, node populations, and multiple STF-node scenarios, IAPRepair reduces repair time by at least 47.83% compared with the evaluated state-of-the-art methods. The results demonstrate that coordinating proactive repair decisions with in-network processing is an effective way to improve repair efficiency under bandwidth heterogeneity.

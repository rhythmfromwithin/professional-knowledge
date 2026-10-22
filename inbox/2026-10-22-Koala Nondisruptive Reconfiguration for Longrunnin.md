---
interest: medium
link: https://arxiv.org/abs/2610.28939
next_step: skim
priority: medium
slack_ts: '1792642791.799159'
source: cs.DC - Distributed Computing
status: unread
title: 'Koala: Non-disruptive Reconfiguration for Long-running Stateful Dataflows'
---
# Koala: Non-disruptive Reconfiguration for Long-running Stateful Dataflows
> 原文: [https://arxiv.org/abs/2610.28939](https://arxiv.org/abs/2610.28939)

arXiv:2610.28939v1 Announce Type: new
Abstract: Stateful dataflow systems must decide where state lives relative to the tasks that process it. For long-running applications that require frequent reconfiguration due to changes in resource allocation, partitioning, or task placement, this design choice presents a core trade-off between adaptability and performance. Co-locating state with computation ensures low latency at steady state but makes reconfiguration disruptive, as any change forces state migration. On the other hand, keeping state in an external store makes reconfiguration seamless, but incurs overhead on every access.
We present Koala, a reconfiguration protocol for distributed dataflow systems that retains the operational performance of embedded-state architectures while matching the disruption-free adaptability of external-state designs. Unlike prior protocols which relocate all state regardless of whether it will soon be accessed, Koala migrates state in a fine-grained, lazy manner. To achieve that, it employs a lightweight ownership transfer mechanism that safely decouples event routing from state location. We implement Koala in a new streaming dataflow system and evaluate it on real-world and synthetic benchmarks. When compared with the state-of-the-art protocol DRRS, Koala consumes backlog up to 23x faster and transfers 8.7x less state on average during reconfiguration.

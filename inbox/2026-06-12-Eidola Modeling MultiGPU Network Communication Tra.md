---
interest: medium
link: https://arxiv.org/abs/2606.12638
next_step: skim
priority: medium
slack_ts: '1781239681.232849'
source: cs.DC - Distributed Computing
status: unread
title: 'Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI
  Workloads'
---
# Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads
> 原文: [https://arxiv.org/abs/2606.12638](https://arxiv.org/abs/2606.12638)

arXiv:2606.12638v1 Announce Type: new
Abstract: As distributed AI workloads grow in scale, multi-GPU systems have become essential for training large models. Although techniques like kernel fusion and overlapping communication with computation help reduce delays, they also introduce irregular and transient traffic patterns that are difficult to model using existing tools. These techniques rely heavily on fine-grained synchronization and peer-to-peer communication, which place significant pressure on interconnect bandwidth and latency.
In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic. The extension is scalable as our GPU model serves as a succinct eidolon, emulating the minimal characteristics needed for traffic modeling. Eidola uses annotated timing profiles from real applications to emulate peer-to-peer GPU writes with cycle-level precision. This allows researchers to simulate and analyze synchronization behavior across large multi-GPU configurations. The simulator supports configurable per-GPU traffic patterns and enables isolated performance analysis under different communication scenarios.
We demonstrate Eidola's effectiveness by reproducing variability in fused kernel execution and by implementing a SyncMon-inspired synchronization mechanism, confirming reductions in polling-related memory traffic. Our results show that Eidola provides a flexible and scalable platform for studying inter-GPU communication and supports architectural exploration in modern distributed GPU systems.

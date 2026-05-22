---
interest: medium
link: https://arxiv.org/abs/2605.18755
next_step: skim
priority: medium
slack_ts: '1779423489.017479'
source: cs.DC - Distributed Computing
status: unread
title: Operational Memory Architecture for Kubernetes:Preserving Causal Context Across
  the Evidence Horizon
---
# Operational Memory Architecture for Kubernetes:Preserving Causal Context Across the Evidence Horizon
> 原文: [https://arxiv.org/abs/2605.18755](https://arxiv.org/abs/2605.18755)

arXiv:2605.18755v1 Announce Type: new
Abstract: Kubernetes clusters generate rich operational events during pod lifecycle transitions, yet the platform's native event retention model discards the most diagnostically valuable context. The LastTerminationState field, which records a container's last failure, is overwritten shortly after a pod restart. We define this as the evidence horizon. During high-frequency crash loops, this horizon may be crossed multiple times before inspection, permanently losing critical evidence.
This paper introduces the Operational Memory Architecture (OMA) to preserve causal failure evidence before event rotation. OMA encodes evidence retention and causal reconstruction as explicit architectural requirements. It captures operational events into causal chains using three patterns: P001 (OOMKill chain), P002 (ConfigMap variable misconfiguration), and P003 (ConfigMap volume mount propagation).
We implement OMA as an open-source system with a Go-based Kubernetes watcher, SQLite operational memory store, and a simple query interface. Experiments on Minikube and AKS include a 30-run latency analysis and stress tests with up to 20 crash-looping pods. Causal edges are built with mean latency below 1 ms. The collector processes ~2.8 events/sec while using under 10 MB memory, showing minimal overhead and effective evidence preservation.

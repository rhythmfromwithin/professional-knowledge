---
interest: medium
link: https://arxiv.org/abs/2605.29346
next_step: skim
priority: medium
slack_ts: '1780290089.098319'
source: cs.DC - Distributed Computing
status: unread
title: Understanding and Reducing Metadata-Driven Host Overheads in Sampling-Based
  GNN Training
---
# Understanding and Reducing Metadata-Driven Host Overheads in Sampling-Based GNN Training
> 原文: [https://arxiv.org/abs/2605.29346](https://arxiv.org/abs/2605.29346)

arXiv:2605.29346v1 Announce Type: new
Abstract: Modern deep learning workloads increasingly exhibit dynamic, metadata-driven execution, where runtime-generated information determines memory provisioning and kernel launch decisions. In sampling-based graph neural network (GNN) training, this behavior places the CPU on the critical path, introducing persistent host-device orchestration overhead and frequent GPU-CPU synchronization, which dominate end-to-end runtime when GPU computation is small. Existing approaches, including CUDA Graphs and GPU dynamic parallelism, fail to address this problem because the metadata-driven control loop remains host-mediated, and execution structure varies across iterations. We present ZEROGNN, a system that removes the host from the metadata-driven control loop and enables fully GPU-resident execution under dynamic behavior. ZEROGNN keeps runtime metadata on-device, mediates dynamic execution within a fixed launch structure, and provisions a conservative yet tight execution envelope to restore CUDA Graph replayability. Experiments on sampling-based GNN workloads show that ZEROGNN achieves up to 5.28 x end-to-end speedup, near 100% GPU execution fraction, and memory efficiency comparable to ideal metadata-informed allocation, while enabling strong multi-GPU scaling by eliminating host-side bottlenecks.

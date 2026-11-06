---
interest: medium
link: https://arxiv.org/abs/2611.07084
next_step: skim
priority: medium
slack_ts: '1793945335.057889'
source: cs.DC - Distributed Computing
status: unread
title: 'DMuon: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix
  Ownership and Communication'
---
# DMuon: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix Ownership and Communication
> 原文: [https://arxiv.org/abs/2611.07084](https://arxiv.org/abs/2611.07084)

arXiv:2611.07084v1 Announce Type: new
Abstract: Matrix optimizers such as Muon update whole weight matrices, which conflicts with the element- or row-wise sharding of data-parallel runtimes. Once parameters are sharded as well, matrix optimizers incur extra communication or repeated computation. We present DMuon, a matrix-granular optimizer runtime for PyTorch FSDP (ZeRO-2/3) and HSDP. DMuon assigns each matrix a unique owner, which performs the Newton--Schulz (NS) iteration and optimizer update on the full matrix, and balances the load across owners by computational cost. On HSDP, ownership is global across replicas, so the cluster keeps a single copy of gradients and optimizer state, and updated parameters are published across nodes as soon as they are ready, overlapping subsequent computation. This layout makes every collective sparse and variable in length, so DMuon schedules these collectives as their data becomes ready and routes them along the cluster's two-level network. On up to 256 H100 GPUs, across three dense LLMs and two VLA models, DMuon matches or exceeds the training throughput of PyTorch FSDP2 with AdamW, reaching 1.05$\times$ that of FSDP2 with AdamW at the median on 256 GPUs. The optimized parameter gathering and gradient reduction absorb the extra communication and computation a matrix optimizer requires. Against a gather-then-replicate Muon baseline, DMuon's throughput is 2.1 times as high at the median.

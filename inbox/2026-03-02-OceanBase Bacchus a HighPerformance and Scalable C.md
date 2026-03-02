---
title: "OceanBase Bacchus: a High-Performance and Scalable Cloud-Native Shared Storage Architecture for Multi-Cloud"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2602.23571
priority: low
status: unread
---
# OceanBase Bacchus: a High-Performance and Scalable Cloud-Native Shared Storage Architecture for Multi-Cloud
> 原文: [https://arxiv.org/abs/2602.23571](https://arxiv.org/abs/2602.23571)

arXiv:2602.23571v1 Announce Type: new
Abstract: Although an increasing number of databases now embrace shared-storage architectures, current storage-disaggregated systems have yet to strike an optimal balance between cost and performance. In high-concurrency read/write scenarios, B+-tree-based shared storage struggles to efficiently absorb frequent in-place updates. Existing LSM-tree-backed disaggregated storage designs are hindered by the intricate implementation of cross-node shared-log mechanisms, where no satisfactory solution yet exists.
This paper presents OceanBase Bacchus, an LSM-tree architecture tailored for object storage provided by cloud vendors. The system sustains high-performance reads and writes while rendering compute nodes stateless through shared service-oriented PALF (Paxos-backed Append-only Log File system) logging and asynchronous background services. We employ a Shared Block Cache Service to flexibly utilize cache resources. Our design places log synchronization into a shared service, providing a novel solution for log sharing in storage-compute-separated databases. The architecture decouples functionality across modules, enabling elastic scaling where compute, cache, and storage resources can be resized rapidly and independently. Through experimental evaluation using multiple benchmark tests, including SysBench and TPC-H, we confirm that OceanBase Bacchus achieves performance comparable to or superior to that of HBase in OLTP scenarios and significantly outperforms StarRocks in OLAP workloads. Leveraging Bacchus's support for multi-cloud deployment and consistent performance, we not only retain high availability and competitive performance but also achieve substantial reductions in storage costs by 59% in OLTP scenarios and 89% in OLAP scenarios.

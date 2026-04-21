---
interest: medium
link: https://arxiv.org/abs/2604.15731
next_step: skim
priority: medium
slack_ts: '1776742301.251209'
source: cs.DC - Distributed Computing
status: unread
title: 'BlockRaFT: A Distributed Framework for Fault-Tolerant and Scalable Blockchain
  Nodes'
---
# BlockRaFT: A Distributed Framework for Fault-Tolerant and Scalable Blockchain Nodes
> 原文: [https://arxiv.org/abs/2604.15731](https://arxiv.org/abs/2604.15731)

arXiv:2604.15731v1 Announce Type: new
Abstract: Blockchain technology enhances transparency by maintaining a distributed ledger among mutually untrusting parties. Despite its advantages, scalability and availability remain critical bottlenecks that hinder widespread adoption. The increasing complexity of blockchain nodes further necessitates robust fault tolerance and high throughput to ensure seamless operations.
We present BlockRaFT, a crash-tolerant distributed framework designed to improve both the scalability and reliability of blockchain node operations. BlockRaFT framework utilizes RAFT consensus protocol to elect a leader within a cluster of systems. The elected leader coordinates and distributes workloads across follower nodes, thereby optimizing resource utilization and work load balancing. We analyzed the tasks performed by blockchain nodes and partition them according to their stateful and stateless characteristics. Stateless operations are centralized at the leader, while stateful operations are replicated and coordinated across the cluster to ensure consistency and fault tolerance. We evaluate whether this distributed intra-node architecture provides measurable benefits over traditional single-node execution models in terms of scalability, availability, and performance.
Additionally, we introduce a concurrent Merkle tree optimization that decouples smart contract execution from tree updates, significantly reducing one of the significant performance overheads in blockchain systems. Our design philosophy is rooted in utilizing the well-established principles of distributed computing and customizing them for the blockchain domain rather than reinventing them.

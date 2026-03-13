---
title: "CD-Raft: Reducing the Latency of Distributed Consensus in Cross-Domain Sites"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.10555
priority: medium
status: unread
interest: medium
next_step: skim
---
# CD-Raft: Reducing the Latency of Distributed Consensus in Cross-Domain Sites
> 原文: [https://arxiv.org/abs/2603.10555](https://arxiv.org/abs/2603.10555)

arXiv:2603.10555v1 Announce Type: new
Abstract: Today's massive AI computation loads push heavy data synchronization across sites, i.e., nodes in data centers. Any reduction in such consensus latency can significantly improve the overall performance of desired systems. This consensus challenge explosively peaks at cross-domain sites. In this paper, we proposed CD-Raft to address the cross-domain latency challenge, an optimized Raft protocol for strong consistency in cross-domain sites. CD-Raft can significantly reduce consensus latency by optimizing cross-domain round-trip time (RTT) for reads and writes, as well as carefully positioning the leader node. We verified the correctness of CD-Raft in a formal specification using the TLA+ specification, guaranteeing the strong consistency across sites. We have prototyped CD-Raft and evaluated it using the YCSB benchmark. Empirical results show that compared to the classic Raft, CD-Raft reduces the average latency by 32.90% and (99th percentile) tail latency by 49.24% for renown traces across multiple sites.

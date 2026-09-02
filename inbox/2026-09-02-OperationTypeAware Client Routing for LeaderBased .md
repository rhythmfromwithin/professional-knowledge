---
title: "Operation-Type-Aware Client Routing for Leader-Based Consensus Datastores"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.00392
priority: medium
status: unread
interest: medium
next_step: skim
---
# Operation-Type-Aware Client Routing for Leader-Based Consensus Datastores
> 原文: [https://arxiv.org/abs/2609.00392](https://arxiv.org/abs/2609.00392)

arXiv:2609.00392v1 Announce Type: new
Abstract: Leader-based consensus datastores (etcd, ZooKeeper) face two competing routing goals: spread load evenly across members, and route operations to the member whose protocol role matches the operation. Writes must commit through the leader, so sending them elsewhere adds a forwarding hop. Linearizable reads need only a lightweight leader confirmation before any member can serve them locally. The upstream etcd client uses gRPC's round\_robin balancer, distributing reads and writes uniformly across cluster members. An operation-aware client resolves this by pinning writes to the leader and distributing reads across the healthy read pool. In steady state on a 3-node etcd cluster (80/20 read/write mix, 5 trials), this lowers write P50 by 29% and raises throughput by 9%. When a follower degrades silently, the operation-aware client detects the latency shift and removes it from the read pool, cutting read P99 by 64%, write P99 by 74%, and raising throughput by 89%. The same routing rule applied to ZooKeeper (ZAB protocol, different implementation) points in the same direction, showing that the result follows from leader-based consensus structure rather than one system's implementation. The key obstacle to discovering this policy adaptively is that the leader confirmation round-trip occurs between cluster members, so the client sees only a blended latency signal rather than the decisive coordination cost directly.

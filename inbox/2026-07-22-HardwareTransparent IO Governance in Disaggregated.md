---
interest: medium
link: https://arxiv.org/abs/2607.16578
next_step: skim
priority: medium
slack_ts: '1784777493.756709'
source: cs.DC - Distributed Computing
status: unread
title: Hardware-Transparent I/O Governance in Disaggregated Heterogeneous Storage
---
# Hardware-Transparent I/O Governance in Disaggregated Heterogeneous Storage
> 原文: [https://arxiv.org/abs/2607.16578](https://arxiv.org/abs/2607.16578)

arXiv:2607.16578v1 Announce Type: new
Abstract: Shared-nothing disaggregated storage clusters that serve both latency-sensitive databases and opaque block-volume workloads face two governance problems unsolved by existing schedulers: maintaining consistent performance across heterogeneous hardware generations, and enforcing global I/O limits when access patterns skew to a subset of storage nodes. We present the I/O Resource Manager (IORM), a multi-stage distributed scheduler deployed in production within Oracle Exadata Exascale. IORM combines three mechanisms: a hardware-aware cost modeler that normalizes I/O accounting using datasheet-derived fixed costs to make limits invariant across hardware generations; a quantum-based rate limiter with bounded carry-forward credits that accommodates database micro-bursts while enforcing long-term SLOs; and a distributed adaptive feedback controller that redistributes unused entitlements across the cluster to resolve topological access skew. Beyond design, we share operational lessons from production deployment. On an 8-node test cluster running up to 100 concurrent tenant volumes, IORM converges within 5\% of provisioned limits under extreme sequential skew, scales without inter-tenant interference, and recovers full throughput within 15 seconds of a storage-node failure.

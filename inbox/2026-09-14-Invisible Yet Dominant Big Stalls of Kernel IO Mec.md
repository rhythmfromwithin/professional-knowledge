---
interest: medium
link: https://arxiv.org/abs/2609.12597
next_step: skim
priority: low
slack_ts: '1789360374.624159'
source: cs.DB - Databases
status: unread
title: 'Invisible Yet Dominant: Big Stalls of Kernel I/O Mechanisms in Cloud OLTP
  Databases'
---
# Invisible Yet Dominant: Big Stalls of Kernel I/O Mechanisms in Cloud OLTP Databases
> 原文: [https://arxiv.org/abs/2609.12597](https://arxiv.org/abs/2609.12597)

arXiv:2609.12597v1 Announce Type: new
Abstract: Most databases, including PostgreSQL, RocksDB, and recent AI KV-cache middleware, rely on buffered I/O, delegating write-back to the Linux kernel. On the distributed block storage standard in the cloud, this delegation inherits a hidden bottleneck: each device is drained by a single kernel flusher thread over a high-latency, shallow-queue path. When the drain falls behind, dirty throttling pauses write() system calls, and even reads that must evict dirty pages stall. These stalls are invisible to iostat and every standard counter. This poster observes the stall from inside the kernel, using the multi-volume data placement proposed in SteelDB as the experimental lever. eBPF probes on writeback and block tracepoints separate write-back by issuing context and count every throttle pause. Across three configurations with identical provisioned IOPS and bandwidth but 1, 2, and 4 devices, we show that adding drains, not bandwidth, cuts throttle pauses by 70%, reduces maximum transaction latency by 59%, and raises throughput by 23%.

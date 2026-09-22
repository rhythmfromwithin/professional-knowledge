---
interest: medium
link: https://arxiv.org/abs/2609.22781
next_step: skim
priority: low
slack_ts: '1790051361.035689'
source: cs.DB - Databases
status: unread
title: 'io_uring in Oracle Database: A Hybrid Storage I/O Architecture at Production
  Scale'
---
# io_uring in Oracle Database: A Hybrid Storage I/O Architecture at Production Scale
> 原文: [https://arxiv.org/abs/2609.22781](https://arxiv.org/abs/2609.22781)

arXiv:2609.22781v1 Announce Type: new
Abstract: We describe the integration of io\_uring into Oracle Database's storage layer and the architectural decisions required to deploy it in a production multi-process RDBMS. Our design uses per-process ring contexts that eliminate inter-process synchronization, a shared buffer registration mechanism now part of the mainline Linux kernel, and a transparent fallback to libaio on error. Evaluation on an internal development build of Oracle Database 26ai shows that io\_uring's benefits concentrate on asynchronous batched I/O paths: on a mixed OLTP workload (TPC-C), io\_uring delivers identical throughput while reducing server CPU utilization by 1.2 percentage points through more efficient background writes; on analytical queries (TPC-H), CPU per query drops by 8.5% (geometric mean). Isolating the write path alone shows 29% lower CPU per write and 34% higher throughput. Synchronous read paths -- the dominant I/O in OLTP -- show no improvement and even increased CPU usage for very large I/O sizes. These results motivate a hybrid I/O architecture that retains pread/pwrite for synchronous operations, adopts io\_uring for asynchronous batched I/O, and falls back transparently to libaio -- a selective strategy that may also be relevant to other database systems facing the same integration question.

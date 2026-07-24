---
title: "RCC: Speculative Write Versioning with Redo Logs"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.19697
priority: low
status: unread
interest: medium
next_step: skim
---
# RCC: Speculative Write Versioning with Redo Logs
> 原文: [https://arxiv.org/abs/2607.19697](https://arxiv.org/abs/2607.19697)

arXiv:2607.19697v1 Announce Type: new
Abstract: Modern OLTP engines rely on multi-versioning to eliminate read-write conflicts, yet their concurrency is severely limited for write-write conflicts. The conventional wisdom of updating records in place and immediately causes only one transaction to update a record at a time, and other update-conflicting transactions to wait for the former to commit or abort. Thus, conflicting transactions are serialized. We propose RCC, which leverages redo logs to resolve conflicting writes. A transaction updates a record out of place by creating a speculative write version using the redo log. With multiple speculative versions, RCC allows concurrent transactions to be pipelined after the update-conflicting point. Each update made by a transaction is installed to its record upon commit. This lazy update policy enables lightweight rollback: a transaction aborts by discarding its speculative versions. To realize the performance potential of its speculative versioning, RCC proposes two novel techniques: commit-time deadlock detection and columnar RCC (RCC-C). The former detects cycles only once lazily at commit time and the latter eliminates record-level false WW conflicts by leveraging column-granule redo logs. RCC guarantees serializability using lock-based access-time conflict ordering and dependency graph tracking. We implement RCC on MySQL and PostgreSQL, integrating the concurrency control mechanism with their buffer managers, lock managers, and recovery modules. RCC improves TPC-C's transaction throughput and latency over Vanilla versions by an order of magnitude when running 64 concurrent threads on a machine with 128 cores. RCC-C further boosts throughput and latency by avoiding false conflict-induced deadlocks and unnecessary aborts. For a high-contention YCSB benchmark, commit-time deadlock detection enables RCC to scale to 128 clients while competing schemes do not scale beyond 32 threads.

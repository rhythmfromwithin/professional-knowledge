---
interest: medium
link: https://arxiv.org/abs/2608.12367
next_step: skim
priority: low
slack_ts: '1786757985.420059'
source: cs.DB - Databases
status: unread
title: 'Lifecycle-Aware Archival for Asymmetric Financial Datasets: A Production Study'
---
# Lifecycle-Aware Archival for Asymmetric Financial Datasets: A Production Study
> 原文: [https://arxiv.org/abs/2608.12367](https://arxiv.org/abs/2608.12367)

arXiv:2608.12367v1 Announce Type: new
Abstract: Large-scale financial transaction databases face a fundamental tension between operational freshness requirements and storage efficiency. We present the design, implementation, and production evaluation of a lifecycle-aware archival system for a financial transaction service at Razorpay managing billions of records on PostgreSQL Aurora (version 14), occupying tens of terabytes of storage and sustaining peak write throughput in the thousands of TPS. We make two contributions. First, we analytically characterize the Celebrity Partition Problem: lifecycle-state partitioning concentrates all operationally active rows in a single default partition, incurring O(N x M) planning overhead, O(N) execution I/O regression, and write amplification on every state transition. Second, we present an ID-monotonicity-based deduplication technique that exploits temporal encoding in monotonically increasing ID schemes (Snowflake IDs, ULIDs, and equivalent) to route only potentially-archived re-inserts to a warm database lookup, requiring no Bloom filters, idempotency tables, or external dependencies. We report production results from a fully deployed system: 95% hot storage size reduction, 53% reduction in monthly database infrastructure cost, ~60% reduction in service-level p99 processing latency, 51 percentage-point reduction in writer CPU utilization, and sustained operation at peak write TPS - without schema changes to the primary transaction table.

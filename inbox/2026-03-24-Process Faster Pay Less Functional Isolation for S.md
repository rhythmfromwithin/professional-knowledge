---
title: "Process Faster, Pay Less: Functional Isolation for Stream Processing"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.19445
priority: low
status: unread
interest: medium
next_step: skim
---
# Process Faster, Pay Less: Functional Isolation for Stream Processing
> 原文: [https://arxiv.org/abs/2603.19445](https://arxiv.org/abs/2603.19445)

arXiv:2603.19445v1 Announce Type: new
Abstract: Concurrent workloads often extract insights from high-throughput, real-time data streams. Existing stream processing engines isolate each query's resources, ensuring robust performance but incurring high infrastructure costs. In contrast, sharing work reduces the amount of necessary resources but introduces inter-query interference, leading to performance degradation for some queries. We introduce FunShare, a stream-processing system that improves resource efficiency without compromising performance by dynamically grouping queries based on their performance characteristics. FunShare strategically relaxes query interdependencies and minimizes redundant computation while preserving individual query performance. It achieves this by using an adaptive optimization framework that monitors execution metrics, accurately estimates computation overlaps, and reconfigures execution plans on the fly in response to changes in the underlying data streams. Our evaluation demonstrates that FunShare minimizes resource consumption compared to isolated execution while maintaining or improving throughput for all queries.

---
title: "Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2606.04196
priority: low
status: unread
interest: medium
next_step: skim
---
# Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines
> 原文: [https://arxiv.org/abs/2606.04196](https://arxiv.org/abs/2606.04196)

arXiv:2606.04196v1 Announce Type: new
Abstract: We describe a design pattern and concrete implementation for embedding distributed approximate nearest neighbor indexes inside the Apache Iceberg table format, using the Puffin sidecar file as the storage container and the snapshot summary as the binding mechanism. Modern analytical query engines increasingly adopt a compute disaggregated architecture: executors are stateless, scale elastically, and read all data from object storage. Adding vector similarity search to such an engine traditionally requires a dedicated index storage layer with its own lifecycle, consistency model, and operational surface breaking the disaggregation in variant. We show that the Puffin format, originally introduced portable level statistics and deletion vectors, is sufficient to carry full Vamana graphs at billion vector scale, and that linking these blobs through the existing statistics file snapshot summary property reduces ANN index management to standard Iceberg snapshot operations. We present a binary layout for sharded graph indexes inside Puffin, a coordinator executor protocol for distributed index build, probe, and incremental refresh, the integration into the existing optimistic-concurrency commit path of an Iceberg REST catalog, and a tiered probe strategy that places small centroid indexes on the coordinator and large DiskANN graphs on executor SSDs. The pattern inherits atomicity, time travel, multi engine read ability, and orphan file garbage collection from the table format at zero implementation cost. We discuss the recall/latency trade-offs introduced by the independent-shard design and quantify projected query and build performance for tables up to 109 vectors. Our implementation extends FlockDB, a distributed MPP engine built on DuckDB.

---
interest: medium
link: https://arxiv.org/abs/2607.00406
next_step: skim
priority: low
slack_ts: '1783050943.427369'
source: cs.DB - Databases
status: unread
title: 'TVA: A Version-aware Temporal Graph Storage System for Real-time Analytics'
---
# TVA: A Version-aware Temporal Graph Storage System for Real-time Analytics
> 原文: [https://arxiv.org/abs/2607.00406](https://arxiv.org/abs/2607.00406)

arXiv:2607.00406v1 Announce Type: new
Abstract: Analyzing temporal graphs can reveal valuable insights that are typically hidden in static graphs. Unfortunately, existing graph storage systems either lack native temporal support or suffer from high latency when querying temporal graphs. This paper presents TVA, a new temporal graph storage system designed for efficient temporal query processing. First, TVA introduces a specialized multi-version storage architecture that separates version metadata from actual data, i.e., the property values associated with different versions of vertices and edges. This architecture enables efficient version retrieval for a vertex or edge by quickly locating valid version metadata and directly dereferencing it to access the corresponding property values. Second, we design tailored data structures, namely the temporal table and enhanced hopscotch-based hashing, to compactly organize the version metadata of adjacent vertices and edges, thus reducing random I/O for metadata lookups during the neighborhood scan initiated from a vertex. Finally, to further accelerate neighborhood scans over multiple vertices, we propose a version-kipping strategy that reuses temporal information obtained from prior scans, thereby avoiding redundant metadata lookups across scans. Empirical evaluations demonstrate that TVA achieves up to 9.9x lower temporal query latency and 2.2x lower storage overhead compared to state-of-the-art temporal graph storage systems.

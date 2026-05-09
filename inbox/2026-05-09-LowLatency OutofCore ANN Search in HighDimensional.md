---
title: "Low-Latency Out-of-Core ANN Search in High-Dimensional Space"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.05787
priority: low
status: unread
interest: medium
next_step: skim
---
# Low-Latency Out-of-Core ANN Search in High-Dimensional Space
> 原文: [https://arxiv.org/abs/2605.05787](https://arxiv.org/abs/2605.05787)

arXiv:2605.05787v1 Announce Type: new
Abstract: In-memory graph-based approximate nearest neighbor (ANN) search has superior search performance but incurs significant memory footprint. Disk-based methods reduce memory usage but suffer from high disk access latency. A common challenge is how to achieve low-latency search while significantly reducing memory footprint. In this paper, we propose SkipDisk, a disk-memory hybrid ANN search that significantly reduces memory footprint while achieving search latency comparable to or lower than in-memory method HNSW. By analyzing existing disk-based methods, we observed that disk access remains the primary bottleneck, and existing lower bound based filtering methods are two loose to effectively reduce disk access. Therefore, we design SkipDisk to achieve tight lower bound with low memory footprint to reduce the search latency. First, we design a dedicated pivot for each point to improve the lower bound of the triangle inequality for effective filtering. We further design an estimation-based approach based on this lower bound. Second, to reduce the memory footprint, we employ a three-level data pruning strategy to preserve informative data in memory. Third, to further reduce search latency, we design an asynchronous I/O strategy based on the decoupling of in-memory search and disk access by storing neighbor nodes in memory. Experiments show that our method achieves a latency of 85 of HNSW's latency with approximately 10 memory footprint, and a latency to 63 of HNSW's with a slightly higher memory footprint of around 20.

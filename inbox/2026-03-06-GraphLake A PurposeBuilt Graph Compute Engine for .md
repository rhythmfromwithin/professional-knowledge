---
title: "GraphLake: A Purpose-Built Graph Compute Engine for Lakehouse"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.03705
priority: low
status: unread
---
# GraphLake: A Purpose-Built Graph Compute Engine for Lakehouse
> 原文: [https://arxiv.org/abs/2603.03705](https://arxiv.org/abs/2603.03705)

arXiv:2603.03705v1 Announce Type: new
Abstract: In this paper, we introduce GraphLake, a purpose-built graph compute engine for Lakehouse. GraphLake is built on top of the commercial graph database TigerGraph. It maps Lakehouse tables to vertex and edge types in a labeled property graph and supports graph analytics over Lakehouse tables using GSQL. To minimize startup time, it loads only the graph topology. Furthermore, it introduces a series of techniques to ensure query efficiency over Lakehouse tables, including a graph-aware caching mechanism and two Lakehouse-optimized parallel primitives. Extensive experiments demonstrate that GraphLake significantly outperforms PuppyGraph, the current state-of-the-art graph compute engine for Lakehouse, by achieving both lower startup and query time.

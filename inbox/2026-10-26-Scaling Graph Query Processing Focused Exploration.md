---
title: "Scaling Graph Query Processing: Focused Exploration on Partitions Using Load Balancing"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.32015
priority: low
status: unread
interest: medium
next_step: skim
---
# Scaling Graph Query Processing: Focused Exploration on Partitions Using Load Balancing
> 原文: [https://arxiv.org/abs/2610.32015](https://arxiv.org/abs/2610.32015)

arXiv:2610.32015v1 Announce Type: new
Abstract: The focus of this paper is on query processing and not search (approximate or exact). The goal is to find all or k answers and the expressiveness of a query (as opposed to a search expression which is typically simpler) is considered important. Although SQL query processing has matured over the last several decades, query processing over graph data has not received the same attention. Only recently, systems, such as Neo4J, and others have started using graphs for data representation on a large scale. Their approaches and algorithms remain proprietary.
In this paper, we address the problem of answering graph queries and their efficient processing on arbitrary-sized graphs. We propose the partitioning of graphs and the use of the distributed paradigm to achieve efficiency and scalability. Our approach takes a subgraph as query input including wild cards and comparison operations. Our partitioned approach leverages focused exploration and distributed processing to achieve the desired parallelism and improve the response time. We also present heuristics to reduce the number of partitions loaded for query processing. We present our partitioning algorithm, distributed processing architecture used, and load balancing for computing query answers. We establish the correctness of the approach in the presence of partitions, compare heuristics for load balancing, and extensive experimental results over large synthetic and real-world graph data sets.

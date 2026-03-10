---
title: "Overcoming Latency-bound Limitations of Distributed Graph Algorithms using the HPX Runtime System"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.04583
priority: medium
status: unread
interest: medium
next_step: skim
---
# Overcoming Latency-bound Limitations of Distributed Graph Algorithms using the HPX Runtime System
> 原文: [https://arxiv.org/abs/2603.04583](https://arxiv.org/abs/2603.04583)

arXiv:2603.04583v1 Announce Type: new
Abstract: Graph processing at scale presents many challenges, including the irregular structure of graphs, the latency-bound nature of graph algorithms, and the overhead associated with distributed execution. While existing frameworks such as Spark GraphX and the Parallel Boost Graph Library (PBGL) have introduced abstractions for distributed graph processing, they continue to struggle with inherent issues like load imbalance and synchronization overhead. In this work, we present a distributed library prototype and a distributed implementation of three key graph algorithms - Breadth-First Search (BFS), PageRank, and Triangle Counting, using C++ mechanisms from the NWgraph library and leveraging HPX's distributed containers and asynchronous constructs. These algorithms span the categories of Traversal, centrality, and Pattern matching, and are selected to represent diverse computational characteristics. We evaluate our HPX-based implementations against GraphX, and PBGL, showing that a high-performance runtime such as HPX enables the construction of algorithms that significantly outperform conventional frameworks by exploiting asynchronous execution, latency hiding, and fine-grained parallelism in shared memory. All algorithms in our prototype follow a unified execution model in which local and remote computations are expressed using the same programming abstractions, with asynchrony managed transparently by the runtime. This design explicitly leverages shared-memory parallelism within each locality while overlapping communication and computation across localities, providing a practical foundation for extending this approach to a broader class of distributed graph algorithms.

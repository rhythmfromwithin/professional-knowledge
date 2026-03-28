---
title: "PDET-LSH: Scalable In-Memory Indexing for High-Dimensional Approximate Nearest Neighbor Search with Quality Guarantees"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.24920
priority: low
status: unread
interest: medium
next_step: skim
---
# PDET-LSH: Scalable In-Memory Indexing for High-Dimensional Approximate Nearest Neighbor Search with Quality Guarantees
> 原文: [https://arxiv.org/abs/2603.24920](https://arxiv.org/abs/2603.24920)

arXiv:2603.24920v1 Announce Type: new
Abstract: Locality-sensitive hashing (LSH) is a well-known solution for approximate nearest neighbor (ANN) search with theoretical guarantees. Traditional LSH-based methods mainly focus on improving the efficiency and accuracy of query phase by designing different query strategies, but pay little attention to improving the efficiency of the indexing phase. They typically fine-tune existing data-oriented partitioning trees to index data points and support their query strategies. However, their strategy to directly partition the multidimensional space is time-consuming, and performance degrades as the space dimensionality increases. In this paper, we design an encoding-based tree called Dynamic Encoding Tree (DE-Tree) to improve the indexing efficiency and support efficient range queries. Based on DE-Tree, we propose a novel LSH scheme called DET-LSH. DET-LSH adopts a novel query strategy, which performs range queries in multiple independent index DE-Trees to reduce the probability of missing exact NN points. Extensive experiments demonstrate that while achieving best query accuracy, DET-LSH achieves up to 6x speedup in indexing time and 2x speedup in query time over the state-of-the-art LSH-based methods. In addition, to further improve the performance of DET-LSH, we propose PDET-LSH, an in-memory method adopting the parallelization opportunities provided by multicore CPUs. PDET-LSH exhibits considerable advantages in indexing and query efficiency, especially on large-scale datasets. Extensive experiments show that, while achieving the same query accuracy as DET-LSH, PDET-LSH offers up to 40x speedup in indexing time and 62x speedup in query answering time over the state-of-the-art LSH-based methods. Our theoretical analysis demonstrates that DET-LSH and PDET-LSH offer probabilistic guarantees on query answering accuracy. This paper was published in TKDE.

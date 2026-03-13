---
interest: medium
link: https://arxiv.org/abs/2603.10177
next_step: skim
priority: low
slack_ts: '1773369884.508939'
source: cs.DB - Databases
status: unread
title: 'K-Join: Combining Vertex Covers for Parallel Joins'
---
# K-Join: Combining Vertex Covers for Parallel Joins
> 原文: [https://arxiv.org/abs/2603.10177](https://arxiv.org/abs/2603.10177)

arXiv:2603.10177v1 Announce Type: new
Abstract: Significant research effort has been devoted to improving the performance of join processing in the massively parallel computation model, where the goal is to evaluate a query with the minimum possible data transfer between machines. However, it is still an open question to determine the best possible parallel algorithm for any join query. In this paper, we present an algorithm that takes a step forward in this endeavour. Our new algorithm is simple and builds on two existing ideas: data partitioning and the HyperCube primitive. The novelty in our approach comes from a careful choice of the HyperCube shares, which is done as a linear combination of multiple vertex covers. The resulting load with input size $n$ and $p$ processors is characterized as $n/p^{1/\kappa}$, where $\kappa$ is a new hypergraph theoretic measure we call the reduced quasi vertex-cover. The new measure matches or improves on all state-of-the-art algorithms and exhibits strong similarities to the edge quasi-packing that describes the worst-case optimal load in one-round algorithms.

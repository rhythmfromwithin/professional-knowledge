---
title: "DynLP: Parallel Dynamic Batch Update for Label Propagation in Semi-Supervised Learning"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.06596
priority: medium
status: unread
interest: medium
next_step: skim
---
# DynLP: Parallel Dynamic Batch Update for Label Propagation in Semi-Supervised Learning
> 原文: [https://arxiv.org/abs/2604.06596](https://arxiv.org/abs/2604.06596)

arXiv:2604.06596v1 Announce Type: new
Abstract: Semi-supervised learning aims to infer class labels using only a small fraction of labeled data. In graph-based semi-supervised learning, this is typically achieved through label propagation to predict labels of unlabeled nodes. However, in real-world applications, data often arrive incrementally in batches. Each time a new batch appears, reapplying the traditional label propagation algorithm to recompute all labels is redundant, computationally intensive, and inefficient. To address the absence of an efficient label propagation update method, we propose DynLP, a novel GPU-centric Dynamic Batched Parallel Label Propagation algorithm that performs only the necessary updates, propagating changes to the relevant subgraph without requiring full recalculation. By exploiting GPU architectural optimizations, our algorithm achieves on average 13x and upto 102x speedup on large-scale datasets compared to state-of-the-art approaches.

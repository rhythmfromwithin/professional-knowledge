---
interest: medium
link: https://arxiv.org/abs/2606.18520
next_step: skim
priority: medium
slack_ts: '1781759640.373679'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Compact Geometric Representations of Hierarchies
---
# Compact Geometric Representations of Hierarchies
> 原文: [https://arxiv.org/abs/2606.18520](https://arxiv.org/abs/2606.18520)

arXiv:2606.18520v1 Announce Type: new
Abstract: Computing geometric representations of data is a cornerstone of modern machine learning, typically achieved by training dual encoders which map queries and documents into a shared embedding space. Recent work of You et al. [NeurIPS '25] has extended this approach to hierarchical retrieval, where relevance is determined by the ancestor-descendant relationships in a Directed Acyclic Graph (DAG). While previous work has shown that valid embeddings exist when the number of descendants is small, these bounds degrade significantly for deep hierarchies, requiring dimensions as large as the total number of nodes.
In this paper, we investigate compact reachability embeddings for more general graph classes and provide theoretical guarantees for representing hierarchies using embeddings whose dimension depends on structural graph parameters. We prove that for any directed tree, there exists a reachability embedding in constant dimension 3, independent of the tree's size or depth. We generalize this result to graphs characterized by treewidth $t$, constructing embeddings of dimension $O(t \log n)$, where $n$ is the number of nodes. Complementing these upper bounds, we provide matching or near-matching lower bounds, showing that dimension $\Omega(n)$ is necessary for general DAGs and $\Omega(t/\log(n/t))$ is required for graphs of treewidth $t$. We also obtain upper and lower bounds parameterized by the number of cross-edges in the DAG. We additionally show that our embeddings can be constructed on real world datasets, and that they give much smaller dimensions in high recall regimes compared to prior embeddings with theoretical guarantees.

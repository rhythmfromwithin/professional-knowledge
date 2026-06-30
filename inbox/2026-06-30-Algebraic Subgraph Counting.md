---
interest: medium
link: https://arxiv.org/abs/2606.29128
next_step: skim
priority: low
slack_ts: '1782792820.005209'
source: cs.DB - Databases
status: unread
title: Algebraic Subgraph Counting
---
# Algebraic Subgraph Counting
> 原文: [https://arxiv.org/abs/2606.29128](https://arxiv.org/abs/2606.29128)

arXiv:2606.29128v1 Announce Type: new
Abstract: Subgraph isomorphism counting is a fundamental problem in graph analytics, which aims to find the number of subgraph isomorphisms of a query graph in a data graph. The candidate tree-based framework provides a promising foundation for subgraph counting tasks, offering a unified counting paradigm that can be extended beyond tree patterns. However, supporting subgraph isomorphism within this framework remains challenging, as it requires handling both the non-tree edge constraint and the injective mapping constraint. Although existing solutions employ sampling or learning techniques to address these constraints in this framework, they still either suffer from inherent sampling failures or rely heavily on supervision. In this paper, we propose ASC, an algebraic subgraph counting approach built on the candidate tree-based counting framework. In our method, the non-tree edge constraint is directly incorporated into the candidate tree-based counting process through a matrix-based computation method, enabling subgraph homomorphism counting with high accuracy in polynomial time. Based on the resulting subgraph homomorphism count, we further apply a local sampling method to address the injective mapping constraint, thereby obtaining the final subgraph isomorphism count. Extensive experiments show that ASC can achieve substantially better and more stable performance over the baselines across various datasets, while scaling to billion-edge graphs. Most impressively, as a non-learning method, ASC can even achieve more than an order of magnitude higher average accuracy than the state-of-the-art learning-based method FlowSC with similar efficiency. This paper is the full version of the work accepted at SIGMOD 2027. The code is available at https://github.com/EricaGuoQiuyu/AlgebraicSubgraphCounting.

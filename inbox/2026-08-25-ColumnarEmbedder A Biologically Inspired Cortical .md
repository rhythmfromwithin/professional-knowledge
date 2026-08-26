---
interest: medium
link: https://arxiv.org/abs/2608.20408
next_step: skim
priority: low
slack_ts: '1787708780.890399'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Columnar-Embedder: A Biologically Inspired Cortical Architecture for Binary
  Sparse Distributed Graph Representations'
---
# Columnar-Embedder: A Biologically Inspired Cortical Architecture for Binary Sparse Distributed Graph Representations
> 原文: [https://arxiv.org/abs/2608.20408](https://arxiv.org/abs/2608.20408)

arXiv:2608.20408v1 Announce Type: new
Abstract: Finding a representative description of graph entities that captures their structural roles and homophily is a challenging goal for graph embedding techniques due to the non-Euclidean nature of graphs. Traditionally, Graph embeddings achieve top performance via random-walk methods and graph neural networks. However, these methods are transductive and utilize an expensive global optimization via softmax or a dense representation trained in an end-to-end pipeline with gradient descent. Nonetheless, other variants of GNNs can map to unseen nodes; they still rely on iterative message passing and backpropagation, incurring high computational and memory costs. Conversely, the mammalian cortex solves structurally similar problems by learning to map its input stream of patterns into a compact representation for downstream regions. We present the biologically inspired Columnar-Embedder architecture for learning binary Sparse Distributed Representations (SDRs) of graph nodes. The learning is driven by a local Bienenstock-Cooper-Munro (BCM) Hebbian rule modulated by positive pointwise mutual information (PPMI) computed from online streams of random walks. Continuous learning from streaming random-walk pairs without labels, backpropagation, or supervision enables the architecture to exhibit natural resistance to catastrophic forgetting. Across five graph benchmarks, the performance of SDRs is competitive with that of real-valued dense embeddings on node classification and link prediction, while the architecture exhibits portability, resilience to noise, and robustness to data corruption.

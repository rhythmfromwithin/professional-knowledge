---
interest: medium
link: https://arxiv.org/abs/2604.19116
next_step: skim
priority: low
slack_ts: '1777001710.693859'
source: cs.DB - Databases
status: unread
title: 'LIVE: Learnable Monotonic Vertex Embedding for Efficient Exact Subgraph Matching
  (Technical Report)'
---
# LIVE: Learnable Monotonic Vertex Embedding for Efficient Exact Subgraph Matching (Technical Report)
> 原文: [https://arxiv.org/abs/2604.19116](https://arxiv.org/abs/2604.19116)

arXiv:2604.19116v1 Announce Type: new
Abstract: Exact subgraph matching is a fundamental graph operator that supports many graph analytics tasks, yet it remains computationally challenging due to its NP-completeness. Recent learning-based approaches accelerate query processing via dominance-preserving vertex embeddings, but they suffer from expensive offline training, limited pruning effectiveness, and heavy reliance on complex index structures, all of which hinder the scalability to large graphs. In this paper, we propose \textit{\underline{L}earnable Monoton\underline{I}c \underline{V}ertex \underline{E}mbedding} (\textsc{LIVE}), a learning-based framework for efficient exact subgraph matching that scales to large graphs. \textsc{LIVE} enforces monotonicity among vertex embeddings by design, making dominance correctness an inherent structural property and enabling embedding learning to directly optimize vertex-level pruning power. To this end, we introduce a query cost model with a differentiable surrogate objective to guide efficient offline training. Moreover, we design a lightweight one-dimensional \textit{iLabel} index that preserves dominance relationships and supports efficient online query processing. Extensive experiments on both synthetic and real-world datasets demonstrate that \textsc{LIVE} significantly outperforms state-of-the-art methods in efficiency and pruning effectiveness.

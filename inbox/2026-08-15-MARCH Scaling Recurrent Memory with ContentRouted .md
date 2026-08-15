---
title: "MARCH: Scaling Recurrent Memory with Content-Routed State Anchors"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2608.12435
priority: high
status: unread
interest: medium
next_step: skim
---
# MARCH: Scaling Recurrent Memory with Content-Routed State Anchors
> 原文: [https://arxiv.org/abs/2608.12435](https://arxiv.org/abs/2608.12435)

arXiv:2608.12435v1 Announce Type: new
Abstract: Transformers owe much of their strong long-context retrieval capability to a token-level memory that grows with context length. This flexibility, however, incurs a quadratic computation complexity during training and a key--value cache that grows linearly during autoregressive inference. Recurrent alternatives offer efficient decoding by compressing the entire history into a fixed-size state, but often underperform on recall-intensive tasks since earlier associations usually get overwritten by subsequent updates, and only the most recent contextual information is retained. In this paper, we introduce Memory-Anchor Routing across Context History (MARCH), a network architecture that effectively scales state-space models beyond a fixed-size dimension, while maintaining computational efficiency over long-sequences. MARCH periodically caches cumulative recurrent-state checkpoints as state anchors and associates each anchor with a compact, content-conditioned anchor key. This lets MARCH maintain a memory bank, which can grow as context length increases, providing a controllable trade-off between historical resolution and memory cost. At each token, MARCH produces an anchor query to attend all causally available state anchors, and the output is calculated as an attention-style aggregation over all historical anchors along the current state. We show that after standard pretraining, MARCH consistently outperforms multiple linear attention variants across commonsense reasoning, LongBench, and in-context retrieval. These results demonstrate that content-routed state caching substantially strengthens recurrent long-range memory while preserving its native computation path.

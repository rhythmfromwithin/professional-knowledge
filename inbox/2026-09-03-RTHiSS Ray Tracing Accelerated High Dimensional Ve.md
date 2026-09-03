---
interest: medium
link: https://arxiv.org/abs/2609.01975
next_step: skim
priority: medium
slack_ts: '1788408246.638009'
source: cs.DC - Distributed Computing
status: unread
title: 'RT-HiSS: Ray Tracing Accelerated High Dimensional Vector Similarity Searches'
---
# RT-HiSS: Ray Tracing Accelerated High Dimensional Vector Similarity Searches
> 原文: [https://arxiv.org/abs/2609.01975](https://arxiv.org/abs/2609.01975)

arXiv:2609.01975v1 Announce Type: new
Abstract: Recent GPU generations include special-purpose ray tracing (RT) cores for graphics applications. While RT cores are primarily used for rendering, recent works show they can be leveraged for general-purpose tasks, including similarity searches. However, existing approaches do not support datasets exceeding three dimensions. In this work, we propose RT-HiSS, the first exact GPU RT-core-based similarity search algorithm for high-dimensional datasets. GPU similarity search often scales poorly for large datasets with substantial search distances. To address this, RT-HiSS uses RT cores for fast index construction and searches, followed by candidate refinement on CUDA cores. We introduce a two-pass approach to estimate an upper bound on result size, enabling efficient batching under GPU memory constraints with near-perfect load balancing. Additionally, we examine shared memory tiling and compressed result masks to improve GPU resource utilization. RT-HiSS yields speedups up to 8.37$\times$ over competitive state-of-the-art GPU algorithms and up to 2,368.26$\times$ relative to the brute-force algorithm across six real-world datasets.

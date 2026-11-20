---
title: "Twindex: Index Cache Offloading with Coarse-to-Fine Selection for Long-Context Sparse-Attention Serving"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.25078
priority: medium
status: unread
interest: medium
next_step: skim
---
# Twindex: Index Cache Offloading with Coarse-to-Fine Selection for Long-Context Sparse-Attention Serving
> 原文: [https://arxiv.org/abs/2611.25078](https://arxiv.org/abs/2611.25078)

arXiv:2611.25078v1 Announce Type: new
Abstract: In long-context decoding, GPU memory (HBM) caps how many requests a GPU decodes at once. Sparse-attention models such as Qwen3.8-Flash-Next, DeepSeek V4.1-Flash and GLM-5.2 add an indexer: at every step it scores all past index entries with its own indexer cache, and attention reads the main KV of only the top-k entries. We find that once serving systems move the main KV to host memory, the indexer cache becomes the HBM bottleneck, at 63% of per-request HBM on Qwen and 75% on V4.1 at 1M tokens. Therefore, we introduce Twindex, which keeps only a compact copy of the indexer cache in HBM and the full indexer cache in host memory. At each step, the copy selects a larger candidate set, and the model's own indexer picks the top-k from the original rows of the candidates in host memory. The copy combines the shared component with the compressed residuals, both learned once offline. Twindex changes no model weights and runs inside CUDA graphs. At 1M tokens on modern GPUs, Twindex fits $1.78\times$, $1.62\times$ and $3.03\times$ as many requests as KV offloading alone on Qwen, V4.1 and GLM-5.2, and reaches $1.44\times$, $1.25\times$ and $2.54\times$ decode throughput when host memory does not limit the batch. Every request keeps its own index, and Qwen and GLM requests share prefix main KV in host memory. In our evaluations, mean benchmark scores are at most 3.1% below the baseline's.

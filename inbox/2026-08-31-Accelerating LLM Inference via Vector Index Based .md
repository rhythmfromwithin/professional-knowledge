---
interest: medium
link: https://arxiv.org/abs/2608.27460
next_step: skim
priority: high
slack_ts: '1788152840.729199'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Accelerating LLM Inference via Vector Index Based Output Embeddings
---
# Accelerating LLM Inference via Vector Index Based Output Embeddings
> 原文: [https://arxiv.org/abs/2608.27460](https://arxiv.org/abs/2608.27460)

arXiv:2608.27460v1 Announce Type: new
Abstract: Large output embedding matrices create a significant memory bandwidth bottleneck during autoregressive decoding, especially for compact LLMs with large multilingual vocabularies. We reformulate the output projection followed by top-k token selection as a maximum inner product search over token embeddings and replace the dense vocabulary projection with an HNSW-based vector index. The resulting output head retrieves only a small candidate set of high-scoring tokens and can be integrated into existing decoding pipelines by scattering retrieved logits into a sparse full-vocabulary tensor. On CPU inference with Gemma 3, Llama 3.2, and Qwen 3 models, our method substantially accelerates the output projection and improves end-to-end batch-size-one decoding throughput by up to 82% for Gemma 3 270M, while preserving generation quality under AlpacaEval evaluation. These results suggest approximate retrieval is a practical alternative to dense output projections in latency-sensitive small-batch decoding.

---
interest: medium
link: https://arxiv.org/abs/2607.01237
next_step: skim
priority: high
slack_ts: '1783136969.793239'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Kara: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression'
---
# Kara: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression
> 原文: [https://arxiv.org/abs/2607.01237](https://arxiv.org/abs/2607.01237)

arXiv:2607.01237v1 Announce Type: new
Abstract: Reasoning language models often generate long chain-of-thought (CoT), which accumulates a massive KV cache during the decoding phase and incurs high decoding latency and limited throughput. To address these issues, KV cache compression has emerged as a promising technique for reducing memory overhead by selectively removing unimportant KV pairs while preserving useful ones for subsequent decoding. Nevertheless, we identify two key limitations in existing KV cache compression methods: 1) their threshold-triggered compression policy may provide limited throughput improvement or even reduce throughput, and may fully eliminate KV pairs from certain blocks of the sequence, potentially worsening information loss. 2) they typically retain either isolated KV pairs or fixed-size chunks with rigid boundaries, failing to preserve important flexible-sized chunks at arbitrary token positions. To overcome these limitations, we propose Kara, a sliding-window KV cache compression method that performs decoding-time compression by operating only on the recently generated context. Kara leverages bidirectional attention to score and select informative KV pairs in the window. To enable flexible preservation of important semantic information, we design a Token2Chunk module to expand a subset of selected KV pairs into chunks. Furthermore, we adapt Kara to PagedAttention and develop KvLLM, an inference framework built upon vLLM, which reduces KV cache memory usage and effectively improves output throughput. Extensive experiments demonstrate consistent performance improvements of proposed Kara and KvLLM.

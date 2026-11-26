---
interest: medium
link: https://arxiv.org/abs/2611.28171
next_step: skim
priority: high
slack_ts: '1795679635.280529'
source: cs.LG - Machine Learning
status: unread
title: 'RefineKV: Query-Adaptive KV Cache Compression via Attention-Error Bounds'
---
# RefineKV: Query-Adaptive KV Cache Compression via Attention-Error Bounds
> 原文: [https://arxiv.org/abs/2611.28171](https://arxiv.org/abs/2611.28171)

arXiv:2611.28171v1 Announce Type: new
Abstract: Repeatedly accessing the full key--value (KV) cache is a major bottleneck in long-context language model decoding. We find that small query-specific subsets can accurately approximate full attention, yet their union covers nearly the entire cache, motivating query-adaptive access for the KV cache. A natural approach is to split the KV cache into clusters, using compact representatives for clusters that incur negligible error while expanding the rest to their original KV entries. We derive a selection criterion from an upper bound on attention-output error, which reveals two complementary factors governing the error: importance measures the impact of a cluster, while distortion measures how faithfully the cluster can be represented. Based on this criterion, we propose RefineKV, a decoding-time query-adaptive KV compression method. Experiments on two models and three benchmarks demonstrate that RefineKV retains near-full-attention quality while achieving up to 7.6x speedup in the attention phase and 1.66x faster decoding, establishing a new quality-latency Pareto frontier.

---
interest: medium
link: https://arxiv.org/abs/2603.18017
next_step: skim
priority: high
slack_ts: '1774407038.327379'
source: cs.LG - Machine Learning
status: unread
title: 'Frayed RoPE and Long Inputs: A Geometric Perspective'
---
# Frayed RoPE and Long Inputs: A Geometric Perspective
> 原文: [https://arxiv.org/abs/2603.18017](https://arxiv.org/abs/2603.18017)

arXiv:2603.18017v1 Announce Type: new
Abstract: Rotary Positional Embedding (RoPE) is a widely adopted technique for encoding position in language models, which, while effective, causes performance breakdown when input length exceeds training length. Prior analyses assert (rightly) that long inputs cause channels to rotate ``out of distribution,'' but it is not clear how extra rotation relates to or causes pathological behavior. Through empirical and theoretical analysis we advance a unified geometric understanding of attention behavior with RoPE. We find that attention induces tight clustering of separated key and query latent point clouds, allowing for creation of sink tokens: placeholders that allow attention heads to avoid token mixing when not required. RoPE applied to longer inputs damages this key/query cluster separation, producing pathological behavior by inhibiting sink token functionality. From this geometric perspective, we propose RoPE-ID (In Distribution), a straightforward modification that allows attention layers to generalize to longer inputs out of the box: apply RoPE with high frequency to a subset of channels. We demonstrate the effectiveness of RoPE-ID for extended inputs using 1B and 3B parameter Transformers on the LongBench and RULER information retrieval benchmarks.

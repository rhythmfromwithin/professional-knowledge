---
interest: medium
link: https://arxiv.org/abs/2605.12697
next_step: skim
priority: medium
slack_ts: '1778817947.858919'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A Unified Framework for Critical Scaling of Inverse Temperature in Self-Attention
---
# A Unified Framework for Critical Scaling of Inverse Temperature in Self-Attention
> 原文: [https://arxiv.org/abs/2605.12697](https://arxiv.org/abs/2605.12697)

arXiv:2605.12697v1 Announce Type: new
Abstract: Length-dependent logit rescaling is widely used to stabilize long-context self-attention, but existing analyses and methods suggest conflicting inverse-temperature laws for the context length $n$, ranging from $(\log n)^{1/2}$ to $\log n$ and $(\log n)^2$. We provide a general theory showing that the desirable scale is determined by the gap-counting function $N\_n$ of each attention row. Counting how many competitors lie within each gap from the maximum, we define an upper-tail accumulation scale and prove that it gives the critical inverse-temperature scale for softmax concentration: below this scale, the top competitors remain unseparated, whereas above it, the attention entropy collapses. This framework unifies prior scaling laws as different $N\_n$ and yields a direct diagnostic for attention-score families, from idealized theoretical models to more practical transformers.

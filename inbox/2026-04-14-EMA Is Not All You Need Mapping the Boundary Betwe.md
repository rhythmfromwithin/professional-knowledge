---
interest: medium
link: https://arxiv.org/abs/2604.08556
next_step: skim
priority: high
slack_ts: '1776137320.655389'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'EMA Is Not All You Need: Mapping the Boundary Between Structure and Content
  in Recurrent Context'
---
# EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context
> 原文: [https://arxiv.org/abs/2604.08556](https://arxiv.org/abs/2604.08556)

arXiv:2604.08556v1 Announce Type: new
Abstract: What exactly do efficient sequence models gain over simple temporal averaging? We use exponential moving average (EMA) traces, the simplest recurrent context (no gating, no content-based retrieval), as a controlled probe to map the boundary between what fixed-coefficient accumulation can and cannot represent. EMA traces encode temporal structure: a Hebbian architecture with multi-timescale traces achieves 96% of a supervised BiGRU on grammatical role assignment with zero labels, surpassing the supervised model on structure-dependent roles. EMA traces destroy token identity: a 130M-parameter language model using only EMA context reaches C4 perplexity 260 (8x GPT-2), and a predictor ablation (replacing the linear predictor with full softmax attention) yields identical loss, localizing the entire gap to the traces. The traces apply lossy, data-independent compression; by the data processing inequality, no downstream predictor can recover the discarded information. Fixed-coefficient accumulation, whether across time or depth, suffers irreversible information dilution that only learned, input-dependent selection can resolve.

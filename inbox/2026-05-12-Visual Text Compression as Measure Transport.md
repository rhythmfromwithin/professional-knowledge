---
interest: medium
link: https://arxiv.org/abs/2605.06708
next_step: skim
priority: medium
slack_ts: '1778558048.249629'
source: cs.CV - Computer Vision
status: unread
title: Visual Text Compression as Measure Transport
---
# Visual Text Compression as Measure Transport
> 原文: [https://arxiv.org/abs/2605.06708](https://arxiv.org/abs/2605.06708)

arXiv:2605.06708v1 Announce Type: new
Abstract: Visual text compression (VTC) promises efficient long-context processing by rendering text into an image and re-encoding it with a vision-language model, often producing $3$--$20\times$ fewer decoder tokens than subword tokenization. Yet token savings do not translate predictably into downstream utility: on some tasks the visual path matches or exceeds the text path, on others it collapses, and the compression ratio itself does not predict which regime will occur. The missing quantity is therefore not another summary of efficiency, but a principled measure of task-relevant information loss induced by visual encoding. We address this problem by formulating VTC in the language of measure transport. Treating text and visual tokens as empirical probability measures, we show that the ViT patch encoder induces a push-forward map whose transport cost decomposes into a precision cost from within-patch aggregation and a coverage cost from cross-patch fragmentation. Both terms are estimable from downstream-label-free probes. This formulation yields two operational consequences: a downstream-label-free routing criterion that selects whether to use the visual path for a given input or benchmark instance, and a transport-informed foveation mechanism that re-encodes high-cost regions at higher resolution. Across $24$ NLP datasets at Qwen3-4B, our label-free rule matches the per-dataset oracle on $17/24$ datasets ($70.8\%$), and improves the average task score by $+3.3\%$ with $-10.3\%$ average tokens relative to a pure-LLM.

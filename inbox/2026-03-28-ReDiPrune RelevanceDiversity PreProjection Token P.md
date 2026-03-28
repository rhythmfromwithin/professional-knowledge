---
interest: medium
link: https://arxiv.org/abs/2603.24680
next_step: skim
priority: medium
slack_ts: '1774666242.489039'
source: cs.CV - Computer Vision
status: unread
title: 'ReDiPrune: Relevance-Diversity Pre-Projection Token Pruning for Efficient
  Multimodal LLMs'
---
# ReDiPrune: Relevance-Diversity Pre-Projection Token Pruning for Efficient Multimodal LLMs
> 原文: [https://arxiv.org/abs/2603.24680](https://arxiv.org/abs/2603.24680)

arXiv:2603.24680v1 Announce Type: new
Abstract: Recent multimodal large language models are computationally expensive because Transformers must process a large number of visual tokens. We present \textbf{ReDiPrune}, a training-free token pruning method applied before the vision-language projector, where visual features remain rich and discriminative. Unlike post-projection pruning methods that operate on compressed representations, ReDiPrune selects informative tokens directly from vision encoder outputs, preserving fine-grained spatial and semantic cues. Each token is scored by a lightweight rule that jointly consider text-conditioned relevance and max-min diversity, ensuring the selected tokens are both query-relevant and non-redundant. ReDiPrune is fully plug-and-play, requiring no retraining or architectural modifications, and can be seamlessly inserted between the encoder and projector. Across four video and five image benchmarks, it consistently improves the accuracy-efficiency trade-off. For example, on EgoSchema with LLaVA-NeXT-Video-7B, retaining only 15\% of visual tokens yields a +2.0\% absolute accuracy gain while reducing computation by more than $6\times$ in TFLOPs. Code is available at https://github.com/UA-CVML/ReDiPrune.

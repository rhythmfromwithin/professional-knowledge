---
title: "Not All Modalities Are Equal: Instruction-Aware Gating for Multimodal Videos"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.26232
priority: medium
status: unread
interest: medium
next_step: skim
---
# Not All Modalities Are Equal: Instruction-Aware Gating for Multimodal Videos
> 原文: [https://arxiv.org/abs/2605.26232](https://arxiv.org/abs/2605.26232)

arXiv:2605.26232v1 Announce Type: new
Abstract: Pre-trained video large language models excel at visual reasoning. However, they struggle when videos arrive with auxiliary streams, such as audio, depth map, or dense temporal evidence. In such a scenario, uniform fusion induces modality interference, allowing irrelevant channels to distract the model. To address this issue, we present a unified multimodal video understanding framework, named UniMVU, that performs instruction-aware fusion across video, audio, depth map, or any other modality inputs via two levels of dynamic gating: inner-modality gates emphasize salient regions within each modality, whereas modality-level gates re-weight whole streams; both are conditioned on the text instruction to adaptively balance modality importance. Our UniMVU combines cross-modal self-attention with instruction-driven inner-modality gating module and a modality-level gating module with control token; for time-aligned streams we further adopt a fast-to-slow fusion scheme that reduces redundancy. Across six benchmarks (AVQA, AVSD, Music-AVQA, ScanQA, SQA3D and MVBench), our UniMVU achieves consistent gains over static-fusion baselines achieving gains as high as 13.5 in terms of CIDEr metric. Further, our analysis shows that the gating mechanism aligns with the human-interpretable modality relevance, and ablations show the contributions of inner-modality and modality-level gating. Our UniMVU provides a simple, unified recipe for instruction-aware multimodal video understanding that scales to diverse modalities without hand-crafted fusion rules.

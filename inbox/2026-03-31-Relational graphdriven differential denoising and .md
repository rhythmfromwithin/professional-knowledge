---
interest: medium
link: https://arxiv.org/abs/2603.25752
next_step: skim
priority: high
slack_ts: '1775098514.392969'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Relational graph-driven differential denoising and diffusion attention fusion
  for multimodal conversation emotion recognition
---
# Relational graph-driven differential denoising and diffusion attention fusion for multimodal conversation emotion recognition
> 原文: [https://arxiv.org/abs/2603.25752](https://arxiv.org/abs/2603.25752)

arXiv:2603.25752v1 Announce Type: new
Abstract: In real-world scenarios, audio and video signals are often subject to environmental noise and limited acquisition conditions, resulting in extracted features containing excessive noise. Furthermore, there is an imbalance in data quality and information carrying capacity between different modalities. These two issues together lead to information distortion and weight bias during the fusion phase, impairing overall recognition performance. Most existing methods neglect the impact of noisy modalities and rely on implicit weighting to model modality importance, thereby failing to explicitly account for the predominant contribution of the textual modality in emotion understanding. To address these issues, we propose a relation-aware denoising and diffusion attention fusion model for MCER. Specifically, we first design a differential Transformer that explicitly computes the differences between two attention maps, thereby enhancing temporally consistent information while suppressing time-irrelevant noise, which leads to effective denoising in both audio and video modalities. Second, we construct modality-specific and cross-modality relation subgraphs to capture speaker-dependent emotional dependencies, enabling fine-grained modeling of intra- and inter-modal relationships. Finally, we introduce a text-guided cross-modal diffusion mechanism that leverages self-attention to model intra-modal dependencies and adaptively diffuses audiovisual information into the textual stream, ensuring more robust and semantically aligned multimodal fusion.

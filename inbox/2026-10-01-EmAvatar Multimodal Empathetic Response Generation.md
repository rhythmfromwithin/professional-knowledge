---
title: "EmAvatar: Multimodal Empathetic Response Generation via Conflict Resolution and Expressive Guidance"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2609.38182
priority: low
status: unread
interest: medium
next_step: skim
---
# EmAvatar: Multimodal Empathetic Response Generation via Conflict Resolution and Expressive Guidance
> 原文: [https://arxiv.org/abs/2609.38182](https://arxiv.org/abs/2609.38182)

arXiv:2609.38182v1 Announce Type: new
Abstract: Avatar-based multimodal empathetic response generation has emerged as a pivotal capability in human-centric systems, aiming to recognize user emotions and synthesize responses with synchronized text, audio, and talking-face video. Despite recent progress, existing methods still suffer from three critical limitations: (1) overlooking conflicting emotions across modalities, (2) lacking explicit multimodal synthesis guidance, and (3) neglecting inherent error propagation of multimodal response generation. To address these limitations, we propose EmAvatar, a novel framework for precise emotion perception and expressive response generation. It first performs deliberative multimodal emotion recognition by exposing inter-modal prediction conflicts and then initiates a multi-round QA process between a Conflict Inspector and an Evidence Collector to gather evidence for conflict resolution, leading to a robust, evidence-aware prediction. Regarding response generation, EmAvatar first synthesizes a composite script that couples the textual response with an expressive instruction. Moreover, to ensure high-quality synthesis, an iterative refinement mechanism evaluates and revises the script until it aligns with predefined criteria, serving as reliable guidance for subsequent audio and video synthesis. Extensive experiments across four tasks demonstrate that EmAvatar outperforms state-of-the-art methods. Our code will be publicly released.

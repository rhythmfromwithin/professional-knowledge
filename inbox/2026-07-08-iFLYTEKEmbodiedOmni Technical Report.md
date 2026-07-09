---
interest: medium
link: https://arxiv.org/abs/2607.02542
next_step: skim
priority: high
slack_ts: '1783569521.490499'
source: cs.AI - Artificial Intelligence
status: unread
title: iFLYTEK-Embodied-Omni Technical Report
---
# iFLYTEK-Embodied-Omni Technical Report
> 原文: [https://arxiv.org/abs/2607.02542](https://arxiv.org/abs/2607.02542)

arXiv:2607.02542v1 Announce Type: new
Abstract: General-purpose embodied agents must understand multimodal instructions, anticipate how their environment will evolve, and produce precise control actions over extended horizons. Existing approaches typically specialize in visual-language reasoning, video-based world modeling, or action generation, while cascaded pipelines that first synthesize future observations and then infer actions can introduce interface bottlenecks and compound prediction errors. We present iFLYTEK-Embodied-Omni, a unified multimodal foundation model that jointly models vision(videos and images), language, and action within a single Omni framework. Its modality-specific visual-language, video-generation, and action-generation components communicate through shared multimodal self-attention. This design establishes brain-cerebellum collaboration: the vision-language modeland video generation model form a high-level brain for instruction understanding, task planning, progress tracking, and future visual-state prediction, whereas the action generation modelserves as a low-level cerebellum that directly converts planned subgoals and shared multimodal context into executable action chunks. To develop these capabilities, we combine action-annotated and action-free embodied videos from human demonstrations and robot interactions with embodied reasoning, embodied perception, and general-purpose image-text data to construct a comprehensive dataset. We further adopt a four-stage strategy that progressively trains the VLM, VGM, and AGM before jointly fine-tuning the complete model.

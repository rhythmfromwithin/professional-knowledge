---
title: "GaugeVLM: Structuring Spatial Supervision with Measured Geometric Interventions"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.38285
priority: medium
status: unread
interest: medium
next_step: skim
---
# GaugeVLM: Structuring Spatial Supervision with Measured Geometric Interventions
> 原文: [https://arxiv.org/abs/2609.38285](https://arxiv.org/abs/2609.38285)

arXiv:2609.38285v1 Announce Type: new
Abstract: Vision-language models (VLMs) can contradict themselves across views of the same spatial relation and fail to respond when that relation changes. Addressing these failures requires supervision that captures error magnitude and geometric dependencies across observations, both of which remain implicit in training on individual answers or ordinal preferences. Therefore, we introduce GaugeVLM, which makes this structure explicit through controlled object and camera interventions in explicit 3D scenes, producing linked observations with measured differences between spatial relations and shared truths across views. To translate this structure into learning signals, its core objective, GaugeDPO, converts measured errors into preference margins, directly supervises correct canonical rankings across views, and links intervention-induced answer-odds contrasts to measured relation changes with view-specific scales. Our analysis bounds canonical prediction error and establishes that the cross-view and intervention constraints can be jointly satisfied. Empirically, GaugeVLM improves all 10 established spatial metrics over supervised fine-tuning across three VLM backbones, with the main 7B model gaining 15.0 and 18.9 percentage points on MSMU distance and QSpatial+, respectively. These gains also extend to autonomous driving and embodied reasoning, demonstrating the robust generalization across domains.

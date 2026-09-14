---
interest: medium
link: https://arxiv.org/abs/2609.12078
next_step: skim
priority: medium
slack_ts: '1789360369.443119'
source: cs.CV - Computer Vision
status: unread
title: Feature Recovery for Object Understanding After Irreversible Fire Damage
---
# Feature Recovery for Object Understanding After Irreversible Fire Damage
> 原文: [https://arxiv.org/abs/2609.12078](https://arxiv.org/abs/2609.12078)

arXiv:2609.12078v1 Announce Type: new
Abstract: Objects in post-fire environments often undergo irreversible physical transformations that change their geometry, material state, and visual appearance. Detecting and identifying these remnants is critical for locating hazards, reconstructing pre-incident contents, and inventorying losses. Unlike standard image corruptions, these degradations affect the physical structure of the object itself. To study this setting, we introduce TRACE, a transformation-aware benchmark for post-fire object understanding. TRACE contains 21.4K real-image-grounded synthetic scenes and paired object-level pristine-to-degraded progressions spanning 499 object identities across 189 categories. We define five tasks targeting localization and pre-degradation understanding: degraded-object detection, pristine-state recovery and retrieval, original material recovery, pristine description generation, and functional reasoning. Existing models degrade sharply with severity. From the least to the most severe level, RF-DETR mAP decreases by 71% relative, while InternVL3.5 retrieval R@1 falls from 93.85 to 28.11. To address this, we propose the Feature Recovery Module (FRM), a plug-and-play module that maps degraded encoder features to pristine-aligned representations while keeping the host frozen. Trained only with paired feature supervision, FRM improves scene-level detection, CLIP/SigLIP2 feature recovery, and all four object-level VLM tasks, with larger gains under more severe degradation. Across VLM hosts and severity levels, relative gains average 12.5% for retrieval, 20.1% for material recovery, 13.2% for description generation, and 12.4% for functional reasoning.

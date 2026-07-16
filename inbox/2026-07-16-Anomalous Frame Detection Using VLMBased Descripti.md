---
title: "Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.11957
priority: medium
status: unread
interest: medium
next_step: skim
---
# Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity
> 原文: [https://arxiv.org/abs/2607.11957](https://arxiv.org/abs/2607.11957)

arXiv:2607.11957v1 Announce Type: new
Abstract: Maintenance of critical infrastructures, such as railways and power plants, is essential for ensuring operational safety and reliability. However, the declining number of skilled maintenance workers highlights the need to transfer expert know-how to less experienced workers. Previous studies have attempted to extract candidates of expert knowledge by comparing videos of manual-based work with those of expert workers, mainly focusing on differences in observable actions. However, expert know-how is often embedded not only in actions but also in contextual decision-making during task execution. This paper proposes a method that detects anomalous frames between two task videos to automatically extract candidate scenes containing expert-specific actions and contextual decision-making scenes. The method generates frame-wise visual descriptions using a vision-language model (VLM). Expert-specific actions are extracted based on frame similarities computed from description comparisons between two videos, while contextual decision-making scenes are extracted using segment similarities derived from intra-video self-similarity of the descriptions. In simulated distribution board maintenance experiments involving 27 task scenarios, the proposed method achieved extraction rates of 65% for action candidates and 61% for decision-scene candidates, improving over conventional methods that achieved 59% and 33%, respectively. These results demonstrate the effectiveness of the proposed approach in discovering candidate scenes containing expert know-how.

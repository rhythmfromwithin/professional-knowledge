---
title: "ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.10993
priority: medium
status: unread
interest: medium
next_step: skim
---
# ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2605.10993](https://arxiv.org/abs/2605.10993)

arXiv:2605.10993v1 Announce Type: new
Abstract: Memory capacity is a critical factor determining the performance of Vision-Language-Action (VLA) models in long-horizon manipulation tasks. Existing memory-augmented architectures primarily rely on linear or flat storage, lacking structural priors for manipulation categories and hierarchical organization. This deficiency hinders efficient experience retrieval and limits generalization to unseen long-horizon task compositions. Inspired by the hierarchical organization of human experience, we propose ECHO (Experience Consolidation and Hierarchical Organization), a novel memory framework operating within a Continuous Hierarchical Space. By employing a hyperbolic autoencoder, ECHO maps VLA hidden states into this space. Leveraging hyperbolic metrics and entailment constraint mechanisms, experience vectors are organized into a semantic memory tree that supports efficient top-down retrieval. In parallel, a background consolidation mechanism continuously refines the memory tree through geometric interpolation and structural splitting, supporting virtual memory synthesis in the continuous space. We integrate ECHO into the $\pi\_0$ foundation model. Evaluations on LIBERO and preliminary real-world experiments demonstrate the effectiveness of our approach, notably achieving a 12.8% absolute improvement in execution success rate over the $\pi\_0$ baseline on LIBERO-Long, while improving compositional generalization on cross-suite unseen long-horizon tasks.

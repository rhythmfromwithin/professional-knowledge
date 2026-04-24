---
title: "TactileEval: A Step Towards Automated Fine-Grained Evaluation and Editing of Tactile Graphics"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.19829
priority: medium
status: unread
interest: medium
next_step: skim
---
# TactileEval: A Step Towards Automated Fine-Grained Evaluation and Editing of Tactile Graphics
> 原文: [https://arxiv.org/abs/2604.19829](https://arxiv.org/abs/2604.19829)

arXiv:2604.19829v1 Announce Type: new
Abstract: Tactile graphics require careful expert validation before reaching blind and visually impaired (BVI) learners, yet existing datasets provide only coarse holistic quality ratings that offer no actionable repair signal. We present TactileEval, a three-stage pipeline that takes a first step toward automating this process. Drawing on expert free-text comments from the TactileNet dataset, we establish a five-category quality taxonomy; encompassing view angle, part completeness, background clutter, texture separation, and line quality aligned with BANA standards. We subsequently gathered 14,095 structured annotations via Amazon Mechanical Turk, spanning 66 object classes organized into six distinct families. A reproducible ViT-L/14 feature probe trained on this data achieves 85.70% overall test accuracy across 30 different tasks, with consistent difficulty ordering suggesting the taxonomy suggesting the taxonomy captures meaningful perceptual structure. Building on these evaluations, we present a ViT-guided automated editing pipeline that routes classifier scores through family-specific prompt templates to produce targeted corrections via gpt-image-1 image editing. Code, data, and models are available at https://TactileEval.github.io/

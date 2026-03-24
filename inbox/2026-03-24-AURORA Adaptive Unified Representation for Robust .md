---
interest: medium
link: https://arxiv.org/abs/2603.19364
next_step: skim
priority: medium
slack_ts: '1774320360.060969'
source: cs.CV - Computer Vision
status: unread
title: 'AURORA: Adaptive Unified Representation for Robust Ultrasound Analysis'
---
# AURORA: Adaptive Unified Representation for Robust Ultrasound Analysis
> 原文: [https://arxiv.org/abs/2603.19364](https://arxiv.org/abs/2603.19364)

arXiv:2603.19364v1 Announce Type: new
Abstract: Ultrasound images vary widely across scanners, operators, and anatomical targets, which often causes models trained in one setting to generalize poorly to new hospitals and clinical conditions. The Foundation Model Challenge for Ultrasound Image Analysis (FMC-UIA) reflects this difficulty by requiring a single model to handle multiple tasks, including segmentation, detection, classification, and landmark regression across diverse organs and datasets. We propose a unified multi-task framework based on a transformer visual encoder from the Qwen3-VL family. Intermediate token features are projected into spatial feature maps and fused using a lightweight multi-scale feature pyramid, enabling both pixel-level predictions and global reasoning within a shared representation. Each task is handled by a small task-specific prediction head, while training uses task-aware sampling and selective loss balancing to manage heterogeneous supervision and reduce task imbalance. Our method is designed to be simple to optimize and adaptable across a wide range of ultrasound analysis tasks. The performance improved from 67% to 85% on the validation set and achieved an average score of 81.84% on the official test set across all tasks. The code is publicly available at: https://github.com/saitejalekkala33/FMCUIA-ISBI.git

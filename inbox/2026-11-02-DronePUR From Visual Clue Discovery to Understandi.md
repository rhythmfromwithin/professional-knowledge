---
title: "Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.40801
priority: medium
status: unread
interest: medium
next_step: skim
---
# Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes
> 原文: [https://arxiv.org/abs/2610.40801](https://arxiv.org/abs/2610.40801)

arXiv:2610.40801v1 Announce Type: new
Abstract: The reasoning capabilities of vision-language models (VLMs) can be limited by incomplete or inaccurate visual observations in the general domain. In unmanned aerial vehicle (UAV) scenes, small targets, subtle attributes, and changing viewpoints further complicate perception and understanding. Therefore, we introduce Drone-PUR, a dataset and benchmark organized around visual clue discovery, interpretation, and integration, corresponding to the three capability dimensions of perception, understanding, and reasoning. Reasoning samples are designed to require models to combine multiple visual clues to derive visually grounded conclusions. Its 11 tasks provide 175k training and 20k test samples spanning single images, image sequences, cross-modal images, and multiple viewpoints. All test samples undergo human review. Evaluating 22 general-purpose VLMs reveals persistent limitations in spatial judgment and cross-modal and cross-view reasoning. Across models, stronger perception is associated with better reasoning, while single-task fine-tuning further reveals selective bidirectional transfer between these capabilities. To examine domain adaptation, we develop UAV-PUR from Qwen3-VL through staged fine-tuning with auxiliary supervision. Its 4B and 8B variants improve overall multiple-choice accuracy by 18.33 and 17.52 percentage points over their pretrained counterparts, respectively. The dataset and project resources are available at https://drone-pur.github.io.

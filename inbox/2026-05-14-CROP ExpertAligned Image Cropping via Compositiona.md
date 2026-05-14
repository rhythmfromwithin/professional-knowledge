---
title: "CROP: Expert-Aligned Image Cropping via Compositional Reasoning and Optimizing Preference"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.12545
priority: medium
status: unread
interest: medium
next_step: skim
---
# CROP: Expert-Aligned Image Cropping via Compositional Reasoning and Optimizing Preference
> 原文: [https://arxiv.org/abs/2605.12545](https://arxiv.org/abs/2605.12545)

arXiv:2605.12545v1 Announce Type: new
Abstract: Aesthetic image cropping aims to enhance the aesthetic quality of an image by improving its composition through spatial cropping. Previous methods often rely on saliency prediction or retrieval augmentation, ignoring the task's core requirement: a deep understanding of composition and aesthetics. Consequently, saliency-based methods struggle to make compositional trade-offs in complex scenes, while retrieval-based methods blindly refer to similar cases, lacking adaptive reasoning for unique scenes. Both approaches fail to align their automated cropping results with those of human experts. To address the above issues, we propose a novel paradigm that reformulates aesthetic cropping as a multimodal reasoning task, aiming to activate the VLM's analytical and comprehension capabilities in aesthetics. We design a Compositional Reasoning and Optimizing Preference method (CROP) that directs the VLM to think like a professional photographer. It deconstructs a complex and subjective aesthetic problem into an "analysis-proposal-decision" process, reasoning step by step through the analysis of scene elements and compositional principles. Meanwhile, our expert preference alignment module makes the model's decision consistent with human expert aesthetics. Extensive experiments across multiple datasets validate our method's superiority and component effectiveness.

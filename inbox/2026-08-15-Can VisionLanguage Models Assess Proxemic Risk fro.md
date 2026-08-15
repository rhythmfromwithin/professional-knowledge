---
title: "Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.12515
priority: medium
status: unread
interest: medium
next_step: skim
---
# Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?
> 原文: [https://arxiv.org/abs/2608.12515](https://arxiv.org/abs/2608.12515)

arXiv:2608.12515v1 Announce Type: new
Abstract: Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning. We evaluate three opensource vision-language models (VLMs) (\textit{InternVL}, \textit{Qwen-VL}, and \textit{SmolVLM}) on the classification of egocentric robot images into four danger levels, comparing three prompting strategies and two rounds of QLoRA fine-tuning against a stratified random baseline. Without fine-tuning, all models perform near the baseline, while fine-tuning yields only modest overall improvements. However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models. An analysis of person localization further shows that correct danger classification does not correspond to better spatial grounding, indicating that a model may produce a useful safety label without attending to the relevant region of the scene. These results show that current VLMs remain limited in fine-grained proxemic reasoning and spatial grounding, although targeted prompting and fine-tuning can improve high-danger detection in selected models.

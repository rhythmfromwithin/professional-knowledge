---
interest: medium
link: https://arxiv.org/abs/2610.20750
next_step: skim
priority: medium
slack_ts: '1792209646.738519'
source: cs.RO - Robotics
status: unread
title: Causal Analysis of Robot Foundation Models Enables Efficiency Gains
---
# Causal Analysis of Robot Foundation Models Enables Efficiency Gains
> 原文: [https://arxiv.org/abs/2610.20750](https://arxiv.org/abs/2610.20750)

arXiv:2610.20750v1 Announce Type: new
Abstract: Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($\pi\_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input image and the instruction shape actions. Across the three models, activation patching shows that causally relevant information influences the action expert (AE) through a narrow band of mid-to-late cross-attention layers, which we term the action-conditioning interface. The content of this information changes with token and layer within the model. Early-to-mid layer representations of the target noun token determine which object is selected, whereas mid-to-late layers carry the spatial information in text tokens that redirects the movement when patched. Where spatial information is stored in prompt tokens various based on the architecture. In MolmoAct2 the model forms task-conditioned representations at the text positions that follow the instruction, whereas $\pi\_{0.5}$ additionally stores this information at image token positions. We show that these findings can be translated directly into improving model efficiency. We find that restricting MolmoBot's action expert conditioning to only 3 out of 36 layers reduces inference FLOPs by up to $33\%$ while maintaining comparable task success with the default model across 3,000 evaluation episodes ($46.7\%$ vs. $46.9\%$), and the same principle carries over to real-robot deployment of $\pi\_{0.5}$.

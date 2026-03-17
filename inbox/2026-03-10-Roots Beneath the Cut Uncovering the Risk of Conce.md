---
interest: medium
link: https://arxiv.org/abs/2603.06640
next_step: skim
priority: medium
slack_ts: '1773715516.516659'
source: cs.CV - Computer Vision
status: unread
title: 'Roots Beneath the Cut: Uncovering the Risk of Concept Revival in Pruning-Based
  Unlearning for Diffusion Models'
---
# Roots Beneath the Cut: Uncovering the Risk of Concept Revival in Pruning-Based Unlearning for Diffusion Models
> 原文: [https://arxiv.org/abs/2603.06640](https://arxiv.org/abs/2603.06640)

arXiv:2603.06640v1 Announce Type: new
Abstract: Pruning-based unlearning has recently emerged as a fast, training-free, and data-independent approach to remove undesired concepts from diffusion models. It promises high efficiency and robustness, offering an attractive alternative to traditional fine-tuning or editing-based unlearning. However, in this paper we uncover a hidden danger behind this promising paradigm. We find that the locations of pruned weights, typically set to zero during unlearning, can act as side-channel signals that leak critical information about the erased concepts. To verify this vulnerability, we design a novel attack framework capable of reviving erased concepts from pruned diffusion models in a fully data-free and training-free manner. Our experiments confirm that pruning-based unlearning is not inherently secure, as erased concepts can be effectively revived without any additional data or retraining. Extensive experiments on diffusion-based unlearning based on concept related weights lead to the conclusion: once the critical concept-related weights in diffusion models are identified, our method can effectively recover the original concept regardless of how the weights are manipulated. Finally, we explore potential defense strategies and advocate safer pruning mechanisms that conceal pruning locations while preserving unlearning effectiveness, providing practical insights for designing more secure pruning-based unlearning frameworks.

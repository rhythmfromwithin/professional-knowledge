---
interest: medium
link: https://arxiv.org/abs/2610.20767
next_step: skim
priority: medium
slack_ts: '1792296495.828549'
source: cs.RO - Robotics
status: unread
title: Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping
  in Robot Foundation Models
---
# Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models
> 原文: [https://arxiv.org/abs/2610.20767](https://arxiv.org/abs/2610.20767)

arXiv:2610.20767v1 Announce Type: new
Abstract: Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover several multi-dimensional task-relevant features underlying the model's computation (e.g., perception, language, proprioceptive state, episode phase, and control variables). We causally validate these features through fine-grained steering: targeted changes in visual perception, semantic representation, and spatial localization produce predictable changes in downstream action prediction. Finally, we use feature-based data attribution to isolate where a specific behavior (failure recovery) arises in the training dataset, identifying fewer than $1.4\%$ of training tokens whose masking is sufficient to remove the targeted behavior. Overall, our results show how matching featurizers to representation geometry can provide more effective tools for understanding and changing robot behavior.

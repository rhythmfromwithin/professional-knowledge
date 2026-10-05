---
title: "Learning Style, Forgetting Semantics: A Case Study of SFT and RFT on Classification Tasks"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.02437
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning Style, Forgetting Semantics: A Case Study of SFT and RFT on Classification Tasks
> 原文: [https://arxiv.org/abs/2610.02437](https://arxiv.org/abs/2610.02437)

arXiv:2610.02437v1 Announce Type: new
Abstract: Why does supervised fine-tuning (SFT) lead to more forgetting than reinforcement fine-tuning (RFT), even when all teacher demonstrations are semantically correct? We study this question on classification tasks where tokens within each semantic class express the same semantic answer in different styles. The tasks share an underlying semantic rule but differ in their prompt distributions and teachers' stylistic preferences. Using a tractable linear-softmax policy, we derive an exact decomposition of the updates into semantic and style components. We show that, at a common policy and prompt, SFT and RFT have parallel semantic updates but differ in their style dynamics. Starting from a policy with no within-class style preference, RFT with exact policy gradients preserves this symmetry, whereas SFT with a nonuniform teacher develops off-axis style drift along a nonzero task mean under population updates. We use this drift to establish a separation under explicit conditions: for population updates from a common perfectly fitted checkpoint, SFT forgetting admits a strictly positive lower bound over a finite training interval, while RFT retains zero semantic error. Simulations over task sequences support these theoretical predictions.

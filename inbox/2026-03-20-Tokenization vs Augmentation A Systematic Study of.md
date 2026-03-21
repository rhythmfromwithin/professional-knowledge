---
interest: medium
link: https://arxiv.org/abs/2603.16883
next_step: skim
priority: medium
slack_ts: '1774060664.348189'
source: cs.CV - Computer Vision
status: unread
title: 'Tokenization vs. Augmentation: A Systematic Study of Writer Variance in IMU-Based
  Online Handwriting Recognition'
---
# Tokenization vs. Augmentation: A Systematic Study of Writer Variance in IMU-Based Online Handwriting Recognition
> 原文: [https://arxiv.org/abs/2603.16883](https://arxiv.org/abs/2603.16883)

arXiv:2603.16883v1 Announce Type: new
Abstract: Inertial measurement unit-based online handwriting recognition enables the recognition of input signals collected across different writing surfaces but remains challenged by uneven character distributions and inter-writer variability. In this work, we systematically investigate two strategies to address these issues: sub-word tokenization and concatenation-based data augmentation. Our experiments on the OnHW-Words500 dataset reveal a clear dichotomy between handling inter-writer and intra-writer variance. On the writer-independent split, structural abstraction via Bigram tokenization significantly improves performance to unseen writing styles, reducing the word error rate (WER) from 15.40% to 12.99%. In contrast, on the writer-dependent split, tokenization degrades performance due to vocabulary distribution shifts between the training and validation sets. Instead, our proposed concatenation-based data augmentation acts as a powerful regularizer, reducing the character error rate by 34.5% and the WER by 25.4%. Further analysis shows that short, low-level tokens benefit model performance and that concatenation-based data augmentation performance gain surpasses those achieved by proportionally extended training. These findings reveal a clear variance-dependent effect: sub-word tokenization primarily mitigates inter-writer stylistic variability, whereas concatenation-based data augmentation effectively compensates for intra-writer distributional sparsity.

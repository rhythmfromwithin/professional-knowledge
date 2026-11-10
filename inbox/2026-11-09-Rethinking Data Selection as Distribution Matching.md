---
interest: medium
link: https://arxiv.org/abs/2611.08495
next_step: skim
priority: high
slack_ts: '1794293803.497059'
source: cs.LG - Machine Learning
status: unread
title: Rethinking Data Selection as Distribution Matching on Semantic Manifolds
---
# Rethinking Data Selection as Distribution Matching on Semantic Manifolds
> 原文: [https://arxiv.org/abs/2611.08495](https://arxiv.org/abs/2611.08495)

arXiv:2611.08495v1 Announce Type: new
Abstract: Instruction tuning of large language models and large vision language models relies on massive training data, which incurs substantial computational and storage costs. Meanwhile, training data often contains redundancy, noise, and low quality samples. Existing data selection methods mostly rely on diversity, importance, or a combination of both, without explicitly constraining the distributional consistency between the selected subset and the full data in the embedding space. We propose QMAC, a quality aware multiband characteristic function matching method that formulates data selection as a joint optimization problem of distribution matching and quality filtering. QMAC matches the empirical characteristic functions of the selected subset and the full data across multiple frequency scales, capturing both global semantic coverage and local perturbations, while using task related quality scores to filter noisy and low quality samples. We systematically evaluate QMAC on 4 data types, 8 target models, and 44 benchmarks. Experimental results show that QMAC outperforms existing data selection baselines on standard image-text instruction data, substantially surpasses random selection on standard text instruction, image-text reasoning, and text reasoning data, and exceeds full data training in multiple model and budget combinations. The code will be made publicly available upon acceptance of the paper.

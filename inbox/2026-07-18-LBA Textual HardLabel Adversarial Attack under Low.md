---
title: "LBA: Textual Hard-Label Adversarial Attack under Low Query Budgets"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.14101
priority: high
status: unread
interest: medium
next_step: skim
---
# LBA: Textual Hard-Label Adversarial Attack under Low Query Budgets
> 原文: [https://arxiv.org/abs/2607.14101](https://arxiv.org/abs/2607.14101)

arXiv:2607.14101v1 Announce Type: new
Abstract: Generating high-quality adversarial texts with low query budgets remains a challenging problem in the hard-label scenario. Most existing approaches rely on greedy algorithms, where one position in the text is selected for substitution, followed by the substitutions of other positions. This local search approach may fail to discover high-quality adversarial examples and often leads to excessive query costs. Ideally, an optimal adversarial sample would consider all possible position combinations in the text, but exhaustive search is computationally impractical. To address this challenge, we propose a sampling-based method called LBA, which constructs an approximate distribution of high-quality adversarial examples by integrating both prior and posterior knowledge, and utilizes this distribution for sampling. As sampling progresses, posterior knowledge updates the approximate distribution, which in turn guides more effective sampling. Extensive experiments on six language models, ranging from small-scale to large-scale architectures across four datasets, demonstrate that LBA significantly outperforms state-of-the-art baselines on all evaluation metrics. Additionally, LLM-based assessment indicates that LBA generates more semantically preserved and comprehensible adversarial texts.

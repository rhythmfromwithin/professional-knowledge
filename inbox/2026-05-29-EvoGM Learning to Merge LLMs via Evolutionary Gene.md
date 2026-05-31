---
interest: medium
link: https://arxiv.org/abs/2605.29295
next_step: skim
priority: low
slack_ts: '1780202384.423899'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization'
---
# EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization
> 原文: [https://arxiv.org/abs/2605.29295](https://arxiv.org/abs/2605.29295)

arXiv:2605.29295v1 Announce Type: new
Abstract: Evolutionary model merging provides a powerful framework for the automated, training-free composition of LLMs through parameter-space search. However, existing methods predominantly rely on stochastic, hand-crafted operators that overlook the underlying performance landscape of the coefficient space. We propose Evolutionary Generative Merging (EvoGM), a framework that transcends manual heuristics by employing learnable generative modeling to optimize merging coefficients. Specifically, EvoGM features a dual-generator architecture with cycle-consistent learning to adaptively sample and refine promising merging candidates. By constructing winner-loser pairs from historical search trajectories, our framework effectively captures high-performance parameter distributions and maximizes data efficiency. This generative process is seamlessly integrated into a multi-round evolutionary pipeline, where elite merged models iteratively serve as new expert foundations. Extensive experiments across diverse benchmarks demonstrate that EvoGM significantly outperforms state-of-the-art baselines, exhibiting robust performance on both seen and unseen tasks. Code and data are available at https://github.com/JiangTao97/evogm.

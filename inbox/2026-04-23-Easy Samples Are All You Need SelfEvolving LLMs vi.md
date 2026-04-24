---
interest: medium
link: https://arxiv.org/abs/2604.18639
next_step: skim
priority: high
slack_ts: '1777001709.154209'
source: cs.LG - Machine Learning
status: unread
title: 'Easy Samples Are All You Need: Self-Evolving LLMs via Data-Efficient Reinforcement
  Learning'
---
# Easy Samples Are All You Need: Self-Evolving LLMs via Data-Efficient Reinforcement Learning
> 原文: [https://arxiv.org/abs/2604.18639](https://arxiv.org/abs/2604.18639)

arXiv:2604.18639v1 Announce Type: new
Abstract: Previous LLMs-based RL studies typically follow either supervised learning with high annotation costs, or unsupervised paradigms using voting or entropy-based rewards. However, their performance remains far from satisfactory due to the substantial annotation cost and issues such as model collapse or reward hacking. To address these issues, we introduce a new perspective inspired by cognitive learning theory and propose a novel approach called EasyRL. The core of EasyRL is to simulate the human cognitive acquisition curve by integrating reliable knowledge transfer from easy labeled data with a progressive divide-and-conquer strategy that tackles increasingly difficult unlabeled data. Specifically, we initialize a warm-up model using supervised RL with few-shot labeled data. This is followed by a divide-and-conquer pseudo-labeling strategy on difficult unlabeled data, combining consistency-based selection for low-uncertainty cases and reflection-based resolution for medium-uncertainty cases. Finally, difficulty-progressive self-training with iterative pseudo-labeling and RL further strengthens the model's reasoning capability. EasyRL provides a unified self-evolving framework that facilitates data-efficient post-training of LLMs. Experimental results on mathematical and scientific benchmarks demonstrate that EasyRL, using only 10% of easy labeled data, consistently outperforms state-of-the-art baselines.

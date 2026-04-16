---
interest: medium
link: https://arxiv.org/abs/2604.09784
next_step: skim
priority: medium
slack_ts: '1776310479.110629'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Discrete Flow Maps
---
# Discrete Flow Maps
> 原文: [https://arxiv.org/abs/2604.09784](https://arxiv.org/abs/2604.09784)

arXiv:2604.09784v2 Announce Type: new
Abstract: The sequential nature of autoregressive next-token prediction imposes a fundamental speed limit on large language models. While continuous flow models offer a path to parallel generation, they traditionally demand expensive iterative integration. Flow Maps bypass this bottleneck by compressing generative trajectories into single-step mappings, theoretically enabling the generation of full text sequences from noise in a single forward pass. However, standard formulations rely on Euclidean regression losses that are geometrically ill-suited for discrete data. In this work, we resolve this conflict with Discrete Flow Maps, a framework that reconciles trajectory compression with the geometry of the probability simplex. We recast standard flow map training for the discrete domain, aligning the training dynamics with the discrete nature of language. Empirically, this strict geometric alignment allows our method to surpass previous state-of-the-art results in discrete flow modeling.

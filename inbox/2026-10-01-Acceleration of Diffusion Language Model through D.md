---
interest: medium
link: https://arxiv.org/abs/2609.38364
next_step: skim
priority: medium
slack_ts: '1790918087.942449'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Acceleration of Diffusion Language Model through Discrete Average Generator
---
# Acceleration of Diffusion Language Model through Discrete Average Generator
> 原文: [https://arxiv.org/abs/2609.38364](https://arxiv.org/abs/2609.38364)

arXiv:2609.38364v1 Announce Type: new
Abstract: Discrete diffusion models and flow matching have emerged as powerful frameworks for generative modeling over discrete state spaces, yet efficient few-step generation remains a fundamental challenge. In this work, we introduce the Discrete Average Generator, a principled extension of MeanFlow to Continuous-Time Markov Chains (CTMCs). Analogously to how MeanFlow defines an average velocity field over a time interval in continuous spaces, we define an average generator as the normalized increment of the transition kernel over a time interval. We show that this average generator satisfies a self-consistency identity, which provides the foundation for our training objective. We further develop training strategies that align with the standard training paradigm of diffusion language models while keeping the resulting objective tractable. When projected onto per-coordinate marginals, the self-consistency identity admits a closed-form expression, enabling efficient training and inference. In Potts model simulations, our objective reduces the total variation distance of the $K$-step sampler by up to 67%. On OpenWebText, our method achieves the lowest generative perplexity among the evaluated methods for 8 to 64 sampling steps while enabling a $16\times$ acceleration, and achieves comparable performance to existing methods on ImageNet.

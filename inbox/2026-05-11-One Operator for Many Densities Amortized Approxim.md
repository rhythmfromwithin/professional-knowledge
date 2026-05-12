---
interest: medium
link: https://arxiv.org/abs/2605.06873
next_step: skim
priority: medium
slack_ts: '1778558027.257549'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'One Operator for Many Densities: Amortized Approximation of Conditioning by
  Neural Operators'
---
# One Operator for Many Densities: Amortized Approximation of Conditioning by Neural Operators
> 原文: [https://arxiv.org/abs/2605.06873](https://arxiv.org/abs/2605.06873)

arXiv:2605.06873v1 Announce Type: new
Abstract: Probabilistic conditioning is concerned with the identification of a distribution of a random variable $X$ given a random variable $Y$. It is a cornerstone of scientific and engineering applications where modeling uncertainty is key. This problem has traditionally been addressed in machine learning by directly learning the conditional distribution of a fixed joint distribution. This paper introduces a novel perspective: we propose to solve the conditioning problem by identifying a single operator that maps any joint density to its conditional, thus amortizing over joint-conditional pairs. We establish that the conditioning operator can be approximated to arbitrary accuracy by neural operators. Our proof relies on new results establishing continuity of the conditioning operator over suitable classes of densities. Finally, we learn the conditioning map for a class of Gaussian mixtures using neural operators, illustrating the promise of our framework. This work provides the theoretical underpinnings for general-purpose, amortized methods for probabilistic conditioning, such as foundation models for Bayesian inference.

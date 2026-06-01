---
title: "Unicorn: Scaling High-Dimensional Time Series Forecasting via Universal Correlation Modeling"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.30376
priority: high
status: unread
interest: medium
next_step: skim
---
# Unicorn: Scaling High-Dimensional Time Series Forecasting via Universal Correlation Modeling
> 原文: [https://arxiv.org/abs/2605.30376](https://arxiv.org/abs/2605.30376)

arXiv:2605.30376v1 Announce Type: new
Abstract: Modern time series architectures face a fundamental trade-off: channel-independent models scale well with increasing data volume but ignore critical inter-channel dependencies, while channel-dependent models are expressive but remain ``dimension-bounded'', struggling to generalize across heterogeneous datasets.To bridge this gap, we introduce Unicorn (Universal Correlation Network), a framework for scalable, multi-dataset pretraining on high-dimensional time series. At the core of Unicorn is a latent prototype codebook that decouples correlation modeling from specific channel identities. By projecting heterogeneous channels into a shared latent space, UniCorN learns identity-agnostic, reusable interaction patterns that transfer across domains with diverse dimensionalities and semantics. Extensive experiments show that Unicorn significantly outperforms state-of-the-art forecasting architectures, particularly in few-shot transfer scenarios, offering a scalable path toward multivariate time series foundation models.

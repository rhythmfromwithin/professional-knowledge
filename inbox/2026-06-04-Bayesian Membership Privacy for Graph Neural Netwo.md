---
title: "Bayesian Membership Privacy for Graph Neural Networks"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.04069
priority: low
status: unread
interest: medium
next_step: skim
---
# Bayesian Membership Privacy for Graph Neural Networks
> 原文: [https://arxiv.org/abs/2606.04069](https://arxiv.org/abs/2606.04069)

arXiv:2606.04069v1 Announce Type: new
Abstract: Existing privacy analyses for Graph Neural Networks (GNNs) largely inherit assumptions from non-graph settings, overlooking structural correlations and stochastic training-graph sampling. In particular, node-dependent priors make type-I and type-II errors alone insufficient to characterize the best membership inference test. To address this, we introduce Bayesian Membership Privacy (BMP), a sampling-aware formulation of node-level membership privacy that incorporates node-dependent priors and treats graph sampling probabilities as part of the adversary's knowledge. BMP casts membership inference as a Bayesian hypothesis test and accordingly quantifies membership privacy in terms of posterior membership probability. We explore theoretical properties of BMP in relation to the existing definitions in the literature. We further propose a practical, sampling-aware auditing mechanism to estimate the parameters of BMP as a measure of node-level privacy leakage in GNNs. We conduct experiments on benchmark graph datasets and show that BMP yields fine-grained privacy insights that are not visible through global attack accuracy alone.

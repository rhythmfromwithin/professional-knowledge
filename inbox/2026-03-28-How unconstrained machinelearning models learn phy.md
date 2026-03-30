---
interest: medium
link: https://arxiv.org/abs/2603.24638
next_step: skim
priority: high
slack_ts: '1774841190.650439'
source: cs.LG - Machine Learning
status: unread
title: How unconstrained machine-learning models learn physical symmetries
---
# How unconstrained machine-learning models learn physical symmetries
> 原文: [https://arxiv.org/abs/2603.24638](https://arxiv.org/abs/2603.24638)

arXiv:2603.24638v1 Announce Type: new
Abstract: The requirement of generating predictions that exactly fulfill the fundamental symmetry of the corresponding physical quantities has profoundly shaped the development of machine-learning models for physical simulations. In many cases, models are built using constrained mathematical forms that ensure that symmetries are enforced exactly. However, unconstrained models that do not obey rotational symmetries are often found to have competitive performance, and to be able to \emph{learn} to a high level of accuracy an approximate equivariant behavior with a simple data augmentation strategy. In this paper, we introduce rigorous metrics to measure the symmetry content of the learned representations in such models, and assess the accuracy by which the outputs fulfill the equivariant condition. We apply these metrics to two unconstrained, transformer-based models operating on decorated point clouds (a graph neural network for atomistic simulations and a PointNet-style architecture for particle physics) to investigate how symmetry information is processed across architectural layers and is learned during training. Based on these insights, we establish a rigorous framework for diagnosing spectral failure modes in ML models. Enabled by this analysis, we demonstrate that one can achieve superior stability and accuracy by strategically injecting the minimum required inductive biases, preserving the high expressivity and scalability of unconstrained architectures while guaranteeing physical fidelity.

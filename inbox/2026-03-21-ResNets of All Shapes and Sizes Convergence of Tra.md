---
interest: medium
link: https://arxiv.org/abs/2603.18168
next_step: skim
priority: medium
slack_ts: '1774148093.695949'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale
  Limit'
---
# ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit
> 原文: [https://arxiv.org/abs/2603.18168](https://arxiv.org/abs/2603.18168)

arXiv:2603.18168v1 Announce Type: new
Abstract: We establish convergence of the training dynamics of residual neural networks (ResNets) to their joint infinite depth L, hidden width M, and embedding dimension D limit. Specifically, we consider ResNets with two-layer perceptron blocks in the maximal local feature update (MLU) regime and prove that, after a bounded number of training steps, the error between the ResNet and its large-scale limit is O(1/L + sqrt(D/(L M)) + 1/sqrt(D)). This error rate is empirically tight when measured in embedding space. For a budget of P = Theta(L M D) parameters, this yields a convergence rate O(P^(-1/6)) for the scalings of (L, M, D) that minimize the bound. Our analysis exploits in an essential way the depth-two structure of residual blocks and applies formally to a broad class of state-of-the-art architectures, including Transformers with bounded key-query dimension. From a technical viewpoint, this work completes the program initiated in the companion paper [Chi25] where it is proved that for a fixed embedding dimension D, the training dynamics converges to a Mean ODE dynamics at rate O(1/L + sqrt(D)/sqrt(L M)). Here, we study the large-D limit of this Mean ODE model and establish convergence at rate O(1/sqrt(D)), yielding the above bound by a triangle inequality. To handle the rich probabilistic structure of the limit dynamics and obtain one of the first rigorous quantitative convergence for a DMFT-type limit, we combine the cavity method with propagation of chaos arguments at a functional level on so-called skeleton maps, which express the weight updates as functions of CLT-type sums from the past.

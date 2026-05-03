---
title: "Binary Spiking Neural Networks as Causal Models"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2604.27007
priority: high
status: unread
interest: medium
next_step: skim
---
# Binary Spiking Neural Networks as Causal Models
> 原文: [https://arxiv.org/abs/2604.27007](https://arxiv.org/abs/2604.27007)

arXiv:2604.27007v1 Announce Type: new
Abstract: We provide a causal analysis of Binary Spiking Neural Networks (BSNNs) to explain their behavior. We formally define a BSNN and represent its spiking activity as a binary causal model. Thanks to this causal representation, we are able to explain the output of the network by leveraging logic-based methods. In particular, we show that we can successfully use a SAT as well as a SMT solver to compute abductive explanations from this binary causal model. To illustrate our approach, we trained the BSNN on the standard MNIST dataset and applied our SAT-based and SMT-based methods to finding abductive explanations of the network's classifications based on pixel-level features. We also compared the found explanations against SHAP, a popular method used in the area of explainable AI. We show that, unlike SHAP, our approach guarantees that a found explanation does not contain completely irrelevant features.

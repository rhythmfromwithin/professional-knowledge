---
interest: medium
link: https://arxiv.org/abs/2605.30362
next_step: skim
priority: low
slack_ts: '1780548650.841909'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'XOResNet: Exclusive-OR Meta-Residuals Facilitate Deep Spiking Neural Networks
  Learning'
---
# XOResNet: Exclusive-OR Meta-Residuals Facilitate Deep Spiking Neural Networks Learning
> 原文: [https://arxiv.org/abs/2605.30362](https://arxiv.org/abs/2605.30362)

arXiv:2605.30362v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) hold promise for demonstrating superior learning and representation capabilities in deep models. Given the tremendous success of ResNet in deep learning, it would naturally follow to train deep SNNs with residual learning. However, existing residual structures for constructing deep SNNs still present challenges of spike redundancy or information loss, as well as redundant learning. In the present study, we first aim to address issues of relative spike redundancy in identity mapping and information loss in non-identity mapping. To this end, we propose an OR-ADD (OA) shortcut connection to merge output spikes/currents from two branches in the residual structure. Furthermore, to mitigate redundant learning in the backbone branch of the residual structure, we introduce the concept of XOR meta-residuals, i.e., selecting pre-learning residuals using the Exclusive-OR (XOR) operation for the backbone branch. Finally, by integrating the OA shortcut and XOR meta-residuals, we devise the XOR residual block and further construct XOResNet with varying depths based on this block. Extensive experiments on four datasets, Fashion-MNIST, CIFAR-10, CIFAR-100, and miniImageNet, show that the proposed XOResNet outperforms existing state-of-the-art deep SNNs optimized via gradient descent. These results validate the effectiveness of our OA shortcut and XOR meta-residual components in overcoming fundamental limitations of residual learning in SNNs, providing new architectural insights for building high-performance neuromorphic systems.

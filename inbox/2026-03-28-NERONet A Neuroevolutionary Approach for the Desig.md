---
title: "NERO-Net: A Neuroevolutionary Approach for the Design of Adversarially Robust CNNs"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.25517
priority: low
status: unread
interest: medium
next_step: skim
---
# NERO-Net: A Neuroevolutionary Approach for the Design of Adversarially Robust CNNs
> 原文: [https://arxiv.org/abs/2603.25517](https://arxiv.org/abs/2603.25517)

arXiv:2603.25517v1 Announce Type: new
Abstract: Neuroevolution automates the complex task of neural network design but often ignores the inherent adversarial fragility of evolved models which is a barrier to adoption in safety-critical scenarios. While robust training methods have received significant attention, the design of architectures exhibiting intrinsic robustness remains largely unexplored. In this paper, we propose NERO-Net, a neuroevolutionary approach to design convolutional neural networks better equipped to resist adversarial attacks. Our search strategy isolates architectural influence on robustness by avoiding adversarial training during the evolutionary loop. As such, our fitness function promotes candidates that, even trained with standard (non-robust) methods, achieve high post-attack accuracy without sacrificing the accuracy on clean samples. We assess NERO-Net on CIFAR-10 with a specific focus on $L\_\infty$-robustness. In particular, the fittest individual emerged from evolutionary search with 33% accuracy against FGSM, used as an efficient estimator for robustness during the search phase, while maintaining 87% clean accuracy. Further standard training of this individual boosted these metrics to 47% adversarial and 93% clean accuracy, suggesting inherent architectural robustness. Adversarial training brings the overall accuracy of the model up to 40% against AutoAttack.

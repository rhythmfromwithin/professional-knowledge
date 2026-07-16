---
title: "Burst Spiking Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.11914
priority: low
status: unread
interest: medium
next_step: skim
---
# Burst Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2607.11914](https://arxiv.org/abs/2607.11914)

arXiv:2607.11914v1 Announce Type: new
Abstract: A central goal of current Spiking Neural Network (SNN) research is to improve their accuracy toward becoming low-power alternatives to Artificial Neural Networks (ANNs). This work further argues that realizing this ambition requires improving not only accuracy but also robustness, defined as the ability to maintain correct predictions under input perturbations. We identify two key issues in existing SNN methods that undermine robustness. First, binary spiking activations can produce large activation-state changes under small perturbations. Second, the lack of effective weight constraints makes network outputs more sensitive to input variations. To this end, we propose Burst Spiking Neural Networks (BuSNNs), built upon Burst-enhanced Spiking Neurons (BSNs) and a Dynamic Weight Constraint (DWC) mechanism. BSNs incorporate burst firing to provide a graded spiking pattern. This spiking mechanism mitigates perturbation-induced transitions in activation states and thereby enhances robustness. DWC penalizes connection weights based on activation states, effectively reducing weight magnitudes and improving robustness while preserving accuracy. We provide theoretical analyses to support these robustness effects. Experimental results further show that, on smaller-scale benchmarks such as CIFAR-10, BuSNNs outperform both SNN and ANN counterparts in accuracy and robustness. On large-scale ImageNet, BuSNN with the MS ResNet-34 backbone further improves top-1 accuracy and corruption robustness over the corresponding SNN baseline by 3.18% and 2.66%, respectively. Despite using spike-based activations, BuSNNs surpass 4-bit activation-quantized ANN baselines and approach 8-bit ANN baselines on ImageNet. They also preserve SNNs' low-power advantage. This work studies the accuracy-robustness problem in SNNs, advancing their practical viability in robust and energy-efficient applications.

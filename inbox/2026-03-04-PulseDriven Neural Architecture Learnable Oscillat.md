---
title: "Pulse-Driven Neural Architecture: Learnable Oscillatory Dynamics for Robust Continuous-Time Sequence Processing"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.00153
priority: low
status: unread
---
# Pulse-Driven Neural Architecture: Learnable Oscillatory Dynamics for Robust Continuous-Time Sequence Processing
> 原文: [https://arxiv.org/abs/2603.00153](https://arxiv.org/abs/2603.00153)

arXiv:2603.00153v1 Announce Type: new
Abstract: We introduce PDNA (Pulse-Driven Neural Architecture), a method for augmenting continuous-time recurrent networks with learnable oscillatory dynamics that maintain internal state evolution independently of external input. Built on Closed-form Continuous-time (CfC) networks, PDNA adds two components: (1) a pulse module that generates structured oscillations $A \cdot \sin(\omega t + \varphi(h))$ with learnable frequencies and state-dependent phase, and (2) a self-attend module that applies recurrent self-attention to the hidden state. Through a controlled ablation study on sequential MNIST (sMNIST) with five random seeds, we evaluate gap robustness -- the ability to maintain performance when portions of the input sequence are removed at test time. Our key finding is that structured oscillatory dynamics significantly improve robustness to input interruptions: the self-attend variant achieves a statistically significant 2.78 percentage point multi-gap advantage over baseline ($p = 0.041$), while the pulse variant shows a 4.62 pp advantage with large effect size (Cohen's $d = 0.87$). A noise control (random perturbation of equal magnitude) provides no benefit, confirming that the advantage is structural rather than merely dynamic. These results provide evidence that continuous-time models can benefit from biologically-inspired internal oscillatory mechanisms for temporal robustness.

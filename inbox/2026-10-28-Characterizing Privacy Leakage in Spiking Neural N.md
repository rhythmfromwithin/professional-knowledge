---
interest: medium
link: https://arxiv.org/abs/2610.36243
next_step: skim
priority: low
slack_ts: '1793337885.896539'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Characterizing Privacy Leakage in Spiking Neural Networks: A Systematic Analysis
  of Temporal Dynamics, Stochasticity, Neuronal Dynamics and Learning Mechanisms'
---
# Characterizing Privacy Leakage in Spiking Neural Networks: A Systematic Analysis of Temporal Dynamics, Stochasticity, Neuronal Dynamics and Learning Mechanisms
> 原文: [https://arxiv.org/abs/2610.36243](https://arxiv.org/abs/2610.36243)

arXiv:2610.36243v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) encode information not only in whether neurons fire but also in when they fire, and this temporal dimension shapes what a trained network reveals about its training data. Biologically inspired firing patterns can reduce membership leakage in SNNs without changing the network architecture, which positions temporal dynamics as a design variable for privacy. A change in firing behavior, however, alters stochasticity, spike timing, neuronal response, and the learning problem at once, so harnessing this effect requires identifying which of these properties produces it. This study traces that origin by separating temporal representation, stochasticity, intrinsic neuron dynamics, and learning within a common experimental framework, evaluated under a black-box membership inference attack across image and tabular benchmarks. Varying the temporal representation shows that burst-like firing patterns reduce leakage relative to regular spiking, but at a cost in accuracy. Injecting randomness into the input, spike timing, and spike trains does not reproduce this reduction in leakage, which shows that the reduction arises from how spikes are arranged in time rather than from noise. The privacy benefit further depends on where these firing patterns originate. When neurons generate these patterns through their own adaptive dynamics, leakage falls while accuracy is preserved, so privacy no longer comes at the expense of performance. The learning algorithm then sets the baseline leakage. Under evolutionary training, the attack already performs near chance level, leaving temporal dynamics little room to improve privacy further. Privacy in SNNs is therefore not an inherent property of spikes but a product of how temporal activity is generated, processed, and learned, which offers a principled basis for designing neuromorphic systems that protect sensitive data.

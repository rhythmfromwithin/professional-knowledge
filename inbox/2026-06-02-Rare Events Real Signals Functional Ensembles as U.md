---
title: "Rare Events, Real Signals: Functional Ensembles as Units of Computation in Deep Spiking Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2606.00073
priority: low
status: unread
interest: medium
next_step: skim
---
# Rare Events, Real Signals: Functional Ensembles as Units of Computation in Deep Spiking Networks
> 原文: [https://arxiv.org/abs/2606.00073](https://arxiv.org/abs/2606.00073)

arXiv:2606.00073v1 Announce Type: new
Abstract: We investigate how internal representations emerge across hierarchical processing systems by introducing a neuroscience-inspired framework for analyzing deep spiking neural networks (SNN) through the lens of functional connectivity. Drawing on concepts from systems neuroscience and information theory, we form the first-order functionally-connected (1FC) group of a neuron based on its statistically significant pairwise correlations with neurons from the previous layer of a trained SNN architecture. We then track its response properties during inference under various conditions. Our analysis shows that several principles of functional connectivity previously observed in biological cortex are preserved in spiking ResNet architectures. These 1FC ensembles display interesting properties: their aggregate cofiring reliably predicts downstream neuronal responses through a robust, ReLU-like input-output relationship, whose gain scales systematically with ensemble size. Reliable encoding of the presented class emerges only during high 1FC cofiring events, which themselves occur infrequently, indicating that informative representations are concentrated in rare but highly coordinated activity patterns. Under uniform random noise or adversarial perturbations, these response profiles are disrupted, particularly in early and intermediate layers. This enables a targeted high-resolution interrogation at specific nodes and pathways. We showed that the functional connectivity structure is shaped by learning and this structure breaks under weight permutation. These establish 1FC ensembles as a functionally meaningful substrate for input encoding and information transfer, with potential implications in designing targeted fine-grained diagnostics on the information flow.

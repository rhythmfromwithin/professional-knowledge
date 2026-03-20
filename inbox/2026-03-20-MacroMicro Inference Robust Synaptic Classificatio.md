---
title: "Macro-Micro Inference: Robust Synaptic Classification via Spike-Triggered Extrapolation"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2603.16884
priority: low
status: unread
interest: medium
next_step: skim
---
# Macro-Micro Inference: Robust Synaptic Classification via Spike-Triggered Extrapolation
> 原文: [https://arxiv.org/abs/2603.16884](https://arxiv.org/abs/2603.16884)

arXiv:2603.16884v1 Announce Type: new
Abstract: This work introduces a framework for reconstructing the interaction graph of neuronal networks modeled as multivariate point processes. The methodology performs bivariate inference, identifying synaptic links exclusively from the spike trains of a pair of neurons, without requiring observations of the remaining network activity. We propose a Macro-Micro Extrapolation algorithm to address data sparsity at the micro-scale, inferring synaptic interactions in the limit $\Delta \to 0^+$. A key contribution is the Spike-Triggered Estimator, which leverages the local reset property of Galves-L\"ocherbach dynamics to decouple local synaptic jumps from higher-order network contributions, significantly reducing estimation variance and eliminating spurious dependencies on baseline firing intensities. By employing an adaptive hybrid logic that switches between sample averaging and our novel Pyramid Extrapolation, we ensure robust classification of excitatory, inhibitory, and null connections even in low signal-to-noise regimes. The framework's scalability and precision are validated by numerical results on dense cliques and structured layered networks, achieving perfect classification accuracy across diverse topological motifs.

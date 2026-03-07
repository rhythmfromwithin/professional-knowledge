---
title: "INTENSE: Detecting and disentangling neuronal selectivity in calcium imaging data"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2603.04622
priority: low
status: unread
---
# INTENSE: Detecting and disentangling neuronal selectivity in calcium imaging data
> 原文: [https://arxiv.org/abs/2603.04622](https://arxiv.org/abs/2603.04622)

arXiv:2603.04622v1 Announce Type: new
Abstract: Neurons encode information about the environment through their activity. As animals explore the environment, neurons rapidly acquire selectivity for distinct features of the external world; characterizing how these selectivity patterns emerge, reorganize, and overlap is key to linking neural activity to behavior and cognition. Calcium imaging in freely behaving animals can record large neuronal populations, but quantifying neuron-behavior selectivity directly from continuous fluorescence is challenging because both signals are temporally autocorrelated and calcium kinetics introduce time lags.
Here we present INTENSE (INformation-Theoretic Evaluation of Neuronal SElectivity), an open-source framework that uses mutual information to detect neuron-behavior associations from raw calcium fluorescence data. INTENSE controls false discoveries using circular-shift permutation testing that preserves temporal structure and optimizes temporal delays to account for indicator kinetics and prospective/retrospective encoding. To separate genuine mixed selectivity from associations driven by behavioral covariance, INTENSE applies conditional mutual information-based disentanglement.
We validated INTENSE on synthetic datasets, demonstrating robust detection across diverse signal-to-noise ratios and reliability conditions, whereas methods lacking temporal controls show poor performance. Applied to CA1 miniscope recordings in mice freely exploring an open field, INTENSE reveals robust selectivity to multiple variables (place, head direction, object interaction, locomotion) and refines mixed-selectivity estimates by distinguishing redundant from genuinely multi-variable encoding. Together, INTENSE enables high-throughput, information-theoretic selectivity mapping with principled control of temporal structure and behavioral covariance, bridging large-scale recordings to circuit-level hypotheses.

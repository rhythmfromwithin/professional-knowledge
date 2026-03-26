---
title: "The Coordinate System Problem in Persistent Structural Memory for Neural Architectures"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.22858
priority: low
status: unread
interest: medium
next_step: skim
---
# The Coordinate System Problem in Persistent Structural Memory for Neural Architectures
> 原文: [https://arxiv.org/abs/2603.22858](https://arxiv.org/abs/2603.22858)

arXiv:2603.22858v1 Announce Type: cross
Abstract: We introduce the Dual-View Pheromone Pathway Network (DPPN), an architecture that routes sparse attention through a persistent pheromone field over latent slot transitions, and use it to discover two independent requirements for persistent structural memory in neural networks. Through five progressively refined experiments using up to 10 seeds per condition across 5 model variants and 4 transfer targets, we identify a core principle: persistent memory requires a stable coordinate system, and any coordinate system learned jointly with the model is inherently unstable. We characterize three obstacles -- pheromone saturation, surface-structure entanglement, and coordinate incompatibility -- and show that neither contrastive updates, multi-source distillation, Hungarian alignment, nor semantic decomposition resolves the instability when embeddings are learned from scratch. Fixed random Fourier features provide extrinsic coordinates that are stable, structure-blind, and informative, but coordinate stability alone is insufficient: routing-bias pheromone does not transfer (10 seeds, p>0.05). DPPN outperforms transformer and random sparse baselines for within-task learning (AULC 0.700 vs 0.680 vs 0.670). Replacing routing bias with learning-rate modulation eliminates negative transfer: warm pheromone as a learning-rate prior achieves +0.003 on same-family tasks (17 seeds, p<0.05) while never reducing performance. A structure completion function over extrinsic coordinates produces +0.006 same-family bonus beyond regularization, showing the catch-22 between stability and informativeness is partially permeable to learned functions. The contribution is two independent requirements for persistent structural memory: (a) coordinate stability and (b) graceful transfer mechanism.

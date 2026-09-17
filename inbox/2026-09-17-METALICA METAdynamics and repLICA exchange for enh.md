---
title: "METALICA: METAdynamics and repLICA exchange for enhanced diffusion sampling"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.17823
priority: medium
status: unread
interest: medium
next_step: skim
---
# METALICA: METAdynamics and repLICA exchange for enhanced diffusion sampling
> 原文: [https://arxiv.org/abs/2609.17823](https://arxiv.org/abs/2609.17823)

arXiv:2609.17823v1 Announce Type: new
Abstract: Many proteins function through transitions between conformational states, yet rare states are rarely sampled by diffusion models trained on an equilibrium ensemble, demanding better sampling methods. We introduce METALICA, which implements Metadynamics on a pretrained diffusion model via Replica Exchange. It accumulates a bias potential along a Collective Variable, repels new samples from previous ones through biased sampling, and reweights samples onto the unbiased distribution. METALICA holds one replica per diffusion level, forming a Markov Chain that evolves through inter-replica communication and is refined in place as the bias grows. METALICA is the dual of sequential control, in which Sequential Monte Carlo parallelizes the sampler over a batch of particles. Parallelism over the levels of the diffusion-time schedule instead allows METALICA to generate samples from long chains, essential for the discovery of rare events, with accuracy set by run length rather than by the memory available. We validate on a bimodal target with known free energies, then apply METALICA to the unfolding of a protein. At a budget for which sequential control yields no unfolded structure, METALICA populates the basin and resolves a second free energy minimum.

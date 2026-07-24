---
title: "Boltzmann-Expected Molecular Design with Decoupled Annealing Flows"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.19519
priority: medium
status: unread
interest: medium
next_step: skim
---
# Boltzmann-Expected Molecular Design with Decoupled Annealing Flows
> 原文: [https://arxiv.org/abs/2607.19519](https://arxiv.org/abs/2607.19519)

arXiv:2607.19519v1 Announce Type: new
Abstract: Most 3D properties relevant to molecular design, including free energies and shape descriptors, are $\textit{expectations}$ over the Boltzmann distribution over 3D configurations of a molecular graph. However, existing property-guided generative models tie each property to a single structure, ignoring the underlying ensemble. We recast 3D molecular design as $\textbf{Boltzmann-expected design}$ and realise it with $\textbf{DECAF}$ (Decoupled Annealing Flows), which factorise the joint distribution over graphs and coordinates into two conditional flow models: a graph-conditioned flow $p(x\mid\mathcal{G})$, acting as a $\textit{Boltzmann emulator}$, and a coordinate-conditioned flow $p(\mathcal{G}\mid x)$, proposing new graphs from 3D information. By alternating the two flows, DECAF optimises molecular graphs with a simulated-annealing acceptance rule whose scoring function is evaluated on ensembles drawn from $p(x\mid\mathcal{G})$, making ensemble statistics, not single-conformer properties, the design target. The resulting loop requires no retraining to change objectives. On GEOM-Drugs, we show that ensemble-aware optimisation produces graphs whose mean radius of gyration and solvent-accessible surface area consistently shift toward targets, while single-conformer optimisation degrades on larger drug-like molecules where Boltzmann distributions are broadest. DECAF extends to multi-objective trade-offs and, uniquely among 3D generative models, to $\textbf{higher-moment design}$: jointly optimising an ensemble property's variance and skewness to produce flexible molecules biased to a prescribed conformational regime: we verify the conformational distributions of these higher-moment designs with all-atom MD simulations.

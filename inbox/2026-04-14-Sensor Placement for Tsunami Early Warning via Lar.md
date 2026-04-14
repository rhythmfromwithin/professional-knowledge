---
title: "Sensor Placement for Tsunami Early Warning via Large-Scale Bayesian Optimal Experimental Design"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.08812
priority: medium
status: unread
interest: medium
next_step: skim
---
# Sensor Placement for Tsunami Early Warning via Large-Scale Bayesian Optimal Experimental Design
> 原文: [https://arxiv.org/abs/2604.08812](https://arxiv.org/abs/2604.08812)

arXiv:2604.08812v1 Announce Type: new
Abstract: Real-time tsunami early warning relies on distributed sensor networks to infer seismic sources and seafloor motion. Optimizing these networks via Bayesian optimal experimental design (OED) is exceptionally challenging for systems governed by hyperbolic partial differential equations, which lack the spectral decay required by standard low-rank approximations. We present a scalable Bayesian OED framework for linear time-invariant systems. By reformulating the inverse problem in the data space, we transform OED into dense matrix subset selection. We propose a multi-GPU, Schur-complement-update-based, greedy algorithm that solves the OED problem using a pipelined approach that fully overlaps I/O with GPU computations. Our framework achieves near-perfect weak and strong scaling across hundreds of GPUs on Perlmutter and Frontier. Applied to the 2025 Gordon Bell Prize-winning digital twin for tsunami forecasting in the Cascadia Subduction Zone, we optimize a 175-sensor network, minimizing the uncertainty of a parameter field with over one billion degrees of freedom.

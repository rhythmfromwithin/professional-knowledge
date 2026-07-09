---
interest: medium
link: https://arxiv.org/abs/2607.05439
next_step: skim
priority: high
slack_ts: '1783569527.488749'
source: cs.LG - Machine Learning
status: unread
title: 'Design-CP: Context Parallelism for Design of Protein Nanoparticles'
---
# Design-CP: Context Parallelism for Design of Protein Nanoparticles
> 原文: [https://arxiv.org/abs/2607.05439](https://arxiv.org/abs/2607.05439)

arXiv:2607.05439v1 Announce Type: new
Abstract: Many all-atom generative protein models can in principle design large multimeric complexes by jointly modelling all chains, but their quadratic token- and atom-pair representations quickly exceed single-GPU memory as the number of chains and residues modelled grows. We introduce Design-CP, two context-parallel (CP) inference strategies for RFdiffusion 3 (1D row-sharding and 2D grid sharding with ring attention) that distribute the quadratic activations across a multi-GPU mesh while preserving pretrained weights. We characterise their scaling when sampling icosahedral assemblies, showing that the maximum feasible asymmetric subunit (ASU) size grows with the expected square-root trend in GPU count and that 2D sharding achieves better wall-clock scaling. Moreover, we show how strong point-group symmetry constraints make CP usable out of the box for end-to-end, all-atom design of icosahedral nanoparticles, yielding favourable in silico structural and interface metrics. Finally, we demonstrate octahedral nanoparticle design on a small cluster of workstation-grade 16GB GPUs, illustrating how Design-CP can be a practical path towards democratising large-assembly protein design.

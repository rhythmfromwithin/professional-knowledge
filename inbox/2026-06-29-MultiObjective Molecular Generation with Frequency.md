---
interest: medium
link: https://arxiv.org/abs/2606.27467
next_step: skim
priority: low
slack_ts: '1782708428.855899'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Multi-Objective Molecular Generation with Frequency-Controlled Evolutionary
  Dynamics
---
# Multi-Objective Molecular Generation with Frequency-Controlled Evolutionary Dynamics
> 原文: [https://arxiv.org/abs/2606.27467](https://arxiv.org/abs/2606.27467)

arXiv:2606.27467v1 Announce Type: new
Abstract: Molecule generation methods that leverage generative models have been successfully applied to drug discovery. However, they often require extensive pre-training, suffer statistical biases in the training data, and might suffer from limited interpretability of generated chemical structures. In this work, we introduce SpectralMol, an algorithm based on evolutionary computation that processes chemical structures as a compact matrix of Fourier coefficients, projected onto a fixed basis to generate position-wise latent vectors for SELFIES decoding. The NSGA-II algorithm enforces diversity and enable separate objective functions rather than collapsed objectives into a scalar reward. The quality of the algorithm was tested against standardized benchmarks. The results show comparable aggregate benchmark performance with a task-dependent profile: SpectralMol is strongest on several multi-parameter optimization tasks. The same benchmark was used to perform an ablation study to demonstrate the advantages of a structured latent matrix. Finally, method was tested on a realistic ClpP-targeted drug-discovery benchmark, comparing it with the reinforcement-learning-based model under a fixed oracle-call budget. SpectralMol generates more docking hits and more diverse scaffolds while maintaining competitive physicochemical properties. The representation adopted in this work can cleanly separates scaffold-level modifications from localized substructure variations, as the former occur with perturbations of low-frequency Fourier modes and the latter with perturbations of high-frequency Fourier modes. The results support the evidence that frequency-controlled evolutionary dynamics provide an interpretable, efficient, and training-free route to multi-objective molecular design.

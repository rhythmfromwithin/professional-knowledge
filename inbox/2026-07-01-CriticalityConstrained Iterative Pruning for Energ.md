---
interest: medium
link: https://arxiv.org/abs/2606.30676
next_step: skim
priority: low
slack_ts: '1782880928.880459'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural
  Networks via Combined Importance Scoring
---
# Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring
> 原文: [https://arxiv.org/abs/2606.30676](https://arxiv.org/abs/2606.30676)

arXiv:2606.30676v1 Announce Type: new
Abstract: Deploying spiking neural networks (SNNs) on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies either neglect neuronal criticality or rely on convex relaxations of the inherently combinatorial pruning problem whose fractional masks, upon binarisation, destroy accuracy at moderate-to-high sparsity. We present Criticality-Constrained Quadratic Pruning (CQP), a native PyTorch pipeline that fuses weight magnitude with surrogate-gradient criticality into an analytically exact importance metric, eliminating the rounding artefacts endemic to solver-based approaches. We formally characterise a continuous-relaxation trap wherein OSQP-solver fractional masks overshoot the intended sparsity by up to 12 percentage points (pp), precipitating a 44 pp accuracy collapse. We identify and remediate a zombie-weight failure mode in which Adam's first-moment tensors resurrect pruned synapses, violating the binary sparsity guarantee. An iterative schedule - prune, fine-tune with gradient masking, recompute criticality, and repeat - eliminates gradient staleness at high sparsity. A KL-divergence temporal analysis identifies a redundant simulation timestep, enabling a free 10% theoretical energy reduction without weight modification. On MNIST (60,000 training examples), CQP yields 95.6% accuracy at 90% sparsity versus 93.4% for magnitude pruning (+2.2 pp). A criticality-threshold sweep reveals an empirical criticality cliff: accuracy falls from 87.0% to 14.4% as the threshold reaches tau = 0.9, constituting a quantitative SNN-level analogue of the Critical Brain Hypothesis. Combined weight sparsification and temporal truncation yield a compound 73% reduction in per-inference energy at 70% sparsity, confirming the practical value of the proposed pipeline for neuromorphic deployment.

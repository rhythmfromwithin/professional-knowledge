---
interest: medium
link: https://arxiv.org/abs/2603.13037
next_step: skim
priority: low
slack_ts: '1773974661.728719'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Federated Few-Shot Learning on Neuromorphic Hardware: An Empirical Study Across
  Physical Edge Nodes'
---
# Federated Few-Shot Learning on Neuromorphic Hardware: An Empirical Study Across Physical Edge Nodes
> 原文: [https://arxiv.org/abs/2603.13037](https://arxiv.org/abs/2603.13037)

arXiv:2603.13037v1 Announce Type: new
Abstract: Federated learning on neuromorphic hardware remains unexplored because on-chip spike-timing-dependent plasticity (STDP) produces binary weight updates rather than the floating-point gradients assumed by standard algorithms. We build a two-node federated system with BrainChip Akida AKD1000 processors and run approximately 1,580 experimental trials across seven analysis phases. Of four weight-exchange strategies tested, neuron-level concatenation (FedUnion) consistently preserves accuracy while element-wise weight averaging (FedAvg) destroys it (p = 0.002). Domain-adaptive fine-tuning of the upstream feature extractor accounts for most of the accuracy gains, confirming feature quality as the dominant factor. Scaling feature dimensionality from 64 to 256 yields 77.0% best-strategy federated accuracy (n=30, p < 0.001). Two independent asymmetries (wider features help federation more than individual learning, while binarization hurts federation more) point to a shared prototype complementarity mechanism: cross-node transfer scales with the distinctiveness of neuron prototypes.

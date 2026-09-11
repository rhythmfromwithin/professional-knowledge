---
interest: medium
link: https://arxiv.org/abs/2609.11518
next_step: skim
priority: low
slack_ts: '1789100108.686939'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based
  Neuroevolution'
---
# Breaking the Central Bias: Spatially Partitioned Experts for Coordinate-Based Neuroevolution
> 原文: [https://arxiv.org/abs/2609.11518](https://arxiv.org/abs/2609.11518)

arXiv:2609.11518v1 Announce Type: new
Abstract: Evolvable-Substrate HyperNEAT (ES-HyperNEAT), a bio-inspired indirect encoding that determines neuron placement and connection weights from spatial coordinates, exhibits a failure mode on MNIST as a diagnostic benchmark. Because input pixels map to a coordinate space centered at the origin, evolved networks converge on a small central cluster of input pixels, a spatial-concentration bias; prior work observed only 21% mean accuracy in this regime. Is this bias an optimization artifact or an architectural ceiling? Inspired by Mixture-of-Experts (MoE) principles, we partition the input into non-overlapping spatial segments, each assigned to a separately evolved specialist network. With 13 such experts, this design reaches 43% mean accuracy, a 106% relative improvement over the baseline. The architectural gain does not depend on data-driven aggregation: equal-weighted averaging, which uses no validation data, already yields a 70% improvement; the gain comes from partitioning, not the weighting. Receptive-field analysis shows the mechanism: partitioning forces evolution to discover features across the entire image, expanding active pixel coverage from 4% to 79%. Absolute accuracy stays below gradient-trained baselines, but the relative gain points to central bias, not the evolutionary search. Two tools are designed to generalize beyond MNIST: a receptive-field diagnostic for silent input-coverage collapse, and a spatial-partitioning remedy that restores coverage.

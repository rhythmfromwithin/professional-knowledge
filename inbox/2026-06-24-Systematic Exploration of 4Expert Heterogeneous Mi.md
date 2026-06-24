---
interest: medium
link: https://arxiv.org/abs/2606.23739
next_step: skim
priority: high
slack_ts: '1782274339.912069'
source: cs.LG - Machine Learning
status: unread
title: Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated
  Pipeline Search
---
# Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated Pipeline Search
> 原文: [https://arxiv.org/abs/2606.23739](https://arxiv.org/abs/2606.23739)

arXiv:2606.23739v1 Announce Type: new
Abstract: We present an automated large-scale search pipeline for heterogeneous 4-Expert Mixture-of-Experts (MoE4) architectures within the LEMUR neural network dataset ecosystem. Building on a hand-crafted heterogeneous MoE reference model, we replace manual design with a deterministic code-assembly generator that systematically combines base architecture families drawn from the LEMUR database into MoE4 ensembles, each governed by a convolutional gating network with temperature scaling, mixup augmentation, and cosine-annealed learning rate scheduling. Over a 28-day campaign on an NVIDIA RTX 4090, the pipeline generated 4,463 candidate models across 197 batches, of which 1,021 were evaluated successfully. A critical finding emerged from the campaign: due to alphabetical enumeration via itertools.combinations, the entire explored search space (4.8% of the theoretical 23,751 possible 4-family combinations) is anchored to a single family, AirNet. We characterise this coverage bias precisely, identify the root cause in the generator, and propose a stratified random sampling fix. Within the AirNet anchored scope, ShuffleNet and MobileNetV3 consistently co-produce the highest-accuracy ensembles (mean accuracy up to 0.632), while FractalNet and MNASNet are identified as low-yield families warranting exclusion in future campaigns. The pipeline, analysis artefacts, and corrected generator are released as part of the open-source NNGPT project at https://github.com/ABrain-One/nn-gpt

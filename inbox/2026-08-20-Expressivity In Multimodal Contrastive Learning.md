---
interest: medium
link: https://arxiv.org/abs/2608.17203
next_step: skim
priority: medium
slack_ts: '1787276738.509649'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Expressivity In Multimodal Contrastive Learning
---
# Expressivity In Multimodal Contrastive Learning
> 原文: [https://arxiv.org/abs/2608.17203](https://arxiv.org/abs/2608.17203)

arXiv:2608.17203v1 Announce Type: new
Abstract: Contrastive learning has become a cornerstone of modern representation learning, powering CLIP-style models that underpin text-to-image generation, vision-language models, and retrieval across a rapidly growing range of modalities. Despite this empirical success, the expressive power of these architectures remains poorly understood. To gain insight, we study expressivity by adopting a population-level, density-estimation viewpoint: each architecture comprises a parameterized set of densities whose parameters may be chosen to approximate the joint distribution of the modalities. This isolates a question of pure representational capacity: which joint distributions can a given contrastive family of parameterizations approximate to arbitrary accuracy? We show that expressivity is sharply architecture-dependent. For two modalities, the simple two-tower CLIP architecture is a universal approximator. A natural generalization of CLIP, widely used in practice when three or more modalities are present, is based on a loss found by summing over all pairwise similarities. This provably cannot represent arbitrary joint distributions, although we prove that it remains expressive enough to match all pairwise conditionals. Motivated by this gap, we propose Hadamard-CLIP, which adds a single learned weight vector on top of the existing encoders and restores universal approximation of the joint for any number of modalities while preserving CLIP's fast, precomputable-embedding retrieval.

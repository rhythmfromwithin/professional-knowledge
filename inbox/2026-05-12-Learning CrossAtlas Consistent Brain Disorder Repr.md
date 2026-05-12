---
title: "Learning Cross-Atlas Consistent Brain Disorder Representations via Disentangled Multi-Atlas Functional Connectivity Learning"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2605.07026
priority: low
status: unread
interest: medium
next_step: skim
---
# Learning Cross-Atlas Consistent Brain Disorder Representations via Disentangled Multi-Atlas Functional Connectivity Learning
> 原文: [https://arxiv.org/abs/2605.07026](https://arxiv.org/abs/2605.07026)

arXiv:2605.07026v1 Announce Type: new
Abstract: Functional connectivity (FC) derived from resting-state fMRI is widely used to characterize large-scale brain network alterations in neurological and psychiatric disorders. However, FC construction critically depends on the choice of brain atlas, and different parcellations may emphasize distinct organizational features, leading to heterogeneous and sometimes inconsistent representations. Existing multi-atlas approaches partially alleviate this issue but often fuse atlas-derived features or predictions at a relatively shallow level, while single-atlas disentanglement methods do not explicitly address cross-atlas heterogeneity. We propose Multi-Atlas Disentangled Connectivity LEarning (MADCLE), a multi-branch representation learning framework that jointly encodes FC matrices derived from different brain atlases. Rather than introducing a single explicitly shared latent variable across parcellations, MADCLE learns atlas-wise disease-related representations and encourages them to be cross-atlas consistent through distributional alignment. Meanwhile, covariate-related and atlas-dependent residual factors are modeled separately using covariate similarity supervision, atlas-specific reconstruction, and decorrelation constraints, thereby reducing the leakage of non-disease and parcellation-dependent information into the disease-related embeddings. Experiments on the ADNI and ADHD-200 datasets suggest that MADCLE achieves competitive or improved performance compared with single-atlas baselines, multi-atlas GNN/Transformer models, and recent multi-atlas consistency frameworks. These results support the potential value of structured disentanglement for FC-based disorder identification under heterogeneous parcellation schemes.

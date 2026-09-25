---
title: "Token Clustering and Semantic Sequence Mamba for Hyperspectral Image Classification"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.28580
priority: medium
status: unread
interest: medium
next_step: skim
---
# Token Clustering and Semantic Sequence Mamba for Hyperspectral Image Classification
> 原文: [https://arxiv.org/abs/2609.28580](https://arxiv.org/abs/2609.28580)

arXiv:2609.28580v1 Announce Type: new
Abstract: Although hyperspectral images (HSIs) provide rich spectral-spatial information, accurate pixel-level classification remains challenging because of spectral-spatial heterogeneity and complex spatial structures. Existing vision state space models (Mamba) typically construct sequences according to predefined spatial neighborhoods, without explicitly accounting for semantic similarity or spatial non-stationarity. To address this limitation, we propose Token Clustering and Semantic Sequence Mamba (STMamba), which organizes sparse tokens into semantically coherent sequences for hyperspectral image classification with the following features. First, at the macro level, a hierarchical encoder decoder progressively selects semantic tokens with the Token Clustering Module (TCM) and restores dense features using a parameter-free Cross-scale Neighborhood Attention (CNA) Upsampler. Second, at the micro level, TCM first identifies representative cluster centers through density-aware clustering and estimates soft memberships based on feature similarity. A quadtree-based dynamic selection strategy then retains sparse and spatially distributed tokens from each semantic cluster, forming coherent semantic-token sequences while reducing redundant pixel-wise representations. Third, parallel Spatial and Spectral Semantic-wise Sequencing Mamba (SWSM) modules capture complementary long-range spatial and spectral dependencies within homogeneous semantic token sequences while suppressing irrelevant interactions across heterogeneous regions. Experimental results on three large-scale benchmark datasets demonstrate that STMamba outperforms the SOTA methods with respect to quantitative and qualitative results.

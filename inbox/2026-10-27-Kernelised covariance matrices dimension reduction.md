---
interest: medium
link: https://arxiv.org/abs/2610.33177
next_step: skim
priority: medium
slack_ts: '1793251497.564229'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Kernelised covariance matrices, dimension reduction and imbalanced spectral
  clustering
---
# Kernelised covariance matrices, dimension reduction and imbalanced spectral clustering
> 原文: [https://arxiv.org/abs/2610.33177](https://arxiv.org/abs/2610.33177)

arXiv:2610.33177v1 Announce Type: new
Abstract: The Gaussian Mixture Model (abbrv. GMM) is a classic generative model for clustered data, for which spectral clustering based on dimension reduction via PCA has been an effective framework. In this work, we investigate kernelised covariance matrices as an alternative mechanism for dimension reduction and spectral clustering, focusing on truncation kernels that select pairs of data points with suitable separation constraints. The structure of these matrices is motivated by considerations from statistical mechanics of repulsive particle systems. Our approach is particularly relevant for the setting of imbalanced clusters, where the sizes of the largest and smallest clusters have a diverging ratio with the problem size, and existing PCA-based methods turn out to be of limited effectiveness.
We demonstrate efficient dimension reduction and clustering performance of these modified covariance matrices, substantiated by quantitative bounds. In particular, they achieve superior dimension reduction guarantees compared to PCA for a wide range of parameters in the regime of imbalanced clusters. For spectral clustering, our approach exhibits improvements over PCA in the imbalanced setting, in particular guaranteeing accurate clustering in a much larger regime of intra-cluster separations. Our theoretical guarantees reflected in a range of simulation experiments that exhibit these improvements for unbalanced clustering problems. Our analytical approach, based on kernel Laplacians, provide a toolbox as well as a relevant conceptual ingredient for clustering problems at large. We believe that our work will motivate the application of such kernelised covariance matrices for related classes of statistical problems, as well as spur new investigations in the theory of random matrices.

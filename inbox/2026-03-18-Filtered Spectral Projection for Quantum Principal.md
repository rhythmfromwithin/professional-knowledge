---
title: "Filtered Spectral Projection for Quantum Principal Component Analysis"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.13441
priority: medium
status: unread
interest: medium
next_step: skim
---
# Filtered Spectral Projection for Quantum Principal Component Analysis
> 原文: [https://arxiv.org/abs/2603.13441](https://arxiv.org/abs/2603.13441)

arXiv:2603.13441v1 Announce Type: new
Abstract: Quantum principal component analysis (qPCA) is commonly formulated as the extraction of eigenvalues and eigenvectors of a covariance-encoded density operator. Yet in many qPCA settings, the practical objective is simpler: projecting data onto the dominant spectral subspace. In this work, we introduce a projection-first framework, the Filtered Spectral Projection Algorithm (FSPA), which bypasses explicit eigenvalue estimation while preserving the essential spectral structure. FSPA amplifies any nonzero warm-start overlap with the leading principal subspace and remains robust in small-gap and near-degenerate regimes without inducing artificial symmetry breaking in the absence of bias. To connect this approach to classical datasets, we show that for amplitude-encoded centered data, the ensemble density matrix $\rho=\sum\_i p\_i|\psi\_i\rangle\langle\psi\_i|$ coincides with the covariance matrix. For uncentered data, $\rho$ corresponds to PCA without centering, and we derive eigenvalue interlacing bounds quantifying the deviation from standard PCA. We further show that ensembles of quantum states admit an equivalent centered covariance interpretation. Numerical demonstrations on benchmark datasets, including Breast Cancer Wisconsin and handwritten Digits, show that downstream performance remains stable whenever projection quality is preserved. These results suggest that, in a broad class of qPCA settings, spectral projection is the essential primitive, and explicit eigenvalue estimation is often unnecessary.

---
interest: medium
link: https://arxiv.org/abs/2605.01492
next_step: skim
priority: medium
slack_ts: '1778125806.883149'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Stabilizing Private LASSO under Heterogeneous Covariates via Anisotropic Objective
  Perturbation
---
# Stabilizing Private LASSO under Heterogeneous Covariates via Anisotropic Objective Perturbation
> 原文: [https://arxiv.org/abs/2605.01492](https://arxiv.org/abs/2605.01492)

arXiv:2605.01492v1 Announce Type: new
Abstract: We study high-dimensional LASSO under differential privacy via objective perturbation with heterogeneous covariate scales. In practical scenarios, covariates often exhibit diverse scales; however, standard preprocessing is problematic under privacy constraints, as it consumes additional privacy budget. This heterogeneity induces effective anisotropy in the objective perturbation via the inverse Gram matrix of covariates, which can degrade the stability and accuracy of algorithms. To address this, we propose a Gram-based anisotropic objective perturbation, a ``pre-distortion" strategy that counteracts the distortion from the covariate structure to restore isotropy in the estimation process. Using an Approximate Message Passing (AMP) framework and state evolution analysis, we demonstrate that our proposed perturbation significantly stabilizes convergence and improves both statistical efficiency and privacy performance compared to standard uniform noise injection. Our results provide theoretical insights into designing stable and efficient private estimators without relying on data-dependent preprocessing.

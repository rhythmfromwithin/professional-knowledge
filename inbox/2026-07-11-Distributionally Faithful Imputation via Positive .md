---
title: "Distributionally Faithful Imputation via Positive Semi-Definite Kernel Density Estimation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.07767
priority: medium
status: unread
interest: medium
next_step: skim
---
# Distributionally Faithful Imputation via Positive Semi-Definite Kernel Density Estimation
> 原文: [https://arxiv.org/abs/2607.07767](https://arxiv.org/abs/2607.07767)

arXiv:2607.07767v1 Announce Type: new
Abstract: Missing values undermine statistical inference and machine learning pipelines, yet most imputation methods rely on heuristics or restrictive parametric assumptions that ignore the joint data distribution. We recast imputation under missing completely at random (MCAR) as density estimation from masked observations: estimate a distribution whose observed marginals exactly match those in the data. Leveraging positive semi definite (PSD) kernel densities we obtain a convex empirical risk problem with closed form marginals, solvable by a Newton interior point method. The resulting PSD Impute model yields both single and multiple imputations from the same fitted density, enjoys statistical consistency with fast adaptive excess risk beating the curse of dimensionality for very regular probabilities. Preliminary experiments on one synthetic and eleven real world datasets already indicate competitive distributional accuracy compared with popular imputation baselines, suggesting strong practical promise.

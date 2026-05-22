---
title: "Local Covariate Selection for Average Causal Effect Estimation without Pretreatment and Causal Sufficiency Assumptions"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.21548
priority: medium
status: unread
interest: medium
next_step: skim
---
# Local Covariate Selection for Average Causal Effect Estimation without Pretreatment and Causal Sufficiency Assumptions
> 原文: [https://arxiv.org/abs/2605.21548](https://arxiv.org/abs/2605.21548)

arXiv:2605.21548v1 Announce Type: new
Abstract: We study the problem of selecting covariates for unbiased estimation of the total causal effect.Existing approaches typically rely on global causal structure learning over all variables, or on strong assumptions such as causal sufficiency - where observed variables share no latent confounders - or the pretreatment assumption, which limits covariates to those unaffected by the treatment or outcome. These requirements are often unrealistic in practice, and global learning becomes computationally prohibitive in high-dimensional settings.To address these challenges, we propose a novel local learning method for covariate selection in nonparametric causal effect estimation that avoids both the pretreatment and causal sufficiency assumptions. We first characterize a local boundary that contains at least one valid adjustment set whenever one exists for identifying the causal effect, and then develop local identification procedures to efficiently search within this boundary.We prove that the proposed method is sound and complete. Experiments on multiple synthetic datasets and two real-world datasets show that our approach achieves accurate causal effect estimation while substantially improving computational efficiency.

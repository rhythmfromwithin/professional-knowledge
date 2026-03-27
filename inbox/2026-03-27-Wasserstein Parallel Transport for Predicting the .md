---
title: "Wasserstein Parallel Transport for Predicting the Dynamics of Statistical Systems"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.23736
priority: medium
status: unread
interest: medium
next_step: skim
---
# Wasserstein Parallel Transport for Predicting the Dynamics of Statistical Systems
> 原文: [https://arxiv.org/abs/2603.23736](https://arxiv.org/abs/2603.23736)

arXiv:2603.23736v1 Announce Type: new
Abstract: Many scientific systems, such as cellular populations or economic cohorts, are naturally described by probability distributions that evolve over time. Predicting how such a system would have evolved under different forces or initial conditions is fundamental to causal inference, domain adaptation, and counterfactual prediction. However, the space of distributions often lacks the vector space structure on which classical methods rely. To address this, we introduce a general notion of parallel dynamics at a distributional level. We base this principle on parallel transport of tangent dynamics along optimal transport geodesics and call it ``Wasserstein Parallel Trends''. By replacing the vector subtraction of classic methods with geodesic parallel transport, we can provide counterfactual comparisons of distributional dynamics in applications such as causal inference, domain adaptation, and batch-effect correction in experimental settings. The main mathematical contribution is a novel notion of fanning scheme on the Wasserstein manifold that allows us to efficiently approximate parallel transport along geodesics while also providing the first theoretical guarantees for parallel transport in the Wasserstein space. We also show that Wasserstein Parallel Trends recovers the classic parallel trends assumption for averages as a special case and derive closed-form parallel transport for Gaussian measures. We deploy the method on synthetic data and two single-cell RNA sequencing datasets to impute gene-expression dynamics across biological systems.

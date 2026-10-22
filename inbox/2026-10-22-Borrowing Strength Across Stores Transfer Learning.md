---
title: "Borrowing Strength Across Stores: Transfer Learning for Choice-Based Revenue Management"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.28708
priority: medium
status: unread
interest: medium
next_step: skim
---
# Borrowing Strength Across Stores: Transfer Learning for Choice-Based Revenue Management
> 原文: [https://arxiv.org/abs/2610.28708](https://arxiv.org/abs/2610.28708)

arXiv:2610.28708v1 Announce Type: new
Abstract: Large retail chains must tailor assortment and pricing decisions to local customer preferences, yet even retailers with extensive sales records often have limited data for estimating demand at the store or local market level, particularly in product categories with short selling windows. Local estimation (fitting a demand model for each store on its own) can therefore be unreliable, while pooling data across stores improves estimation precision at the cost of ignoring local demand heterogeneity. We study how retailers can balance these competing effects through transfer learning under a multinomial logit (MNL) demand model. We propose a shrinkage estimator that combines store-specific demand estimates with information pooled from other stores. Unlike the linear or quadratic settings underlying much of the existing theoretical literature on information transfer in operations, the nonlinear MNL likelihood does not admit a straightforward bias-variance decomposition. By exploiting its self-concordant-like properties, we establish finite-sample performance guarantees that characterize when information transfer improves demand estimation and how the appropriate degree of shrinkage depends on local sample size, feature dimensionality, and cross-store heterogeneity. We further derive regret bounds for downstream assortment and pricing decisions. Numerical experiments demonstrate the operational benefits of shrinkage across different data environments. An empirical study using data from several hundred stores of a European apparel retailer shows that shrinkage improves out-of-sample product prioritization and revenue capture relative to both local estimation and full pooling. Our findings demonstrate how retailers can leverage information across their store networks to improve revenue management decisions while preserving local demand differences.

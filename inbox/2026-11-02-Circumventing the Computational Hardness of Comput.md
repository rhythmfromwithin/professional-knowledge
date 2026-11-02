---
title: "Circumventing the Computational Hardness of Computational Arbitrage"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.40831
priority: high
status: unread
interest: medium
next_step: skim
---
# Circumventing the Computational Hardness of Computational Arbitrage
> 原文: [https://arxiv.org/abs/2610.40831](https://arxiv.org/abs/2610.40831)

arXiv:2610.40831v1 Announce Type: new
Abstract: AI model marketplaces host providers with heterogeneous costs and capabilities. These differences create an opportunity for computational arbitrage (Olmedo et al., 2026), in which an intermediary purchases inference from a portfolio of models and resells it to users at a profit. Beyond creating profit opportunities for the arbitrageur, computational arbitrage offers financial value to both consumers and providers and could therefore significantly influence AI model markets. While prior work empirically demonstrates the feasibility of computational arbitrage for small model pools, scaling it to large marketplaces requires arbitrage strategies that are both computationally tractable and inexpensive to identify and deploy. In this work, we formalize computational arbitrage as an allocation problem and prove that it is generally NP-hard. However, we show that the optimal allocation can be computed efficiently under a natural diminishing-returns condition on how model performance scales with inference spending. We further develop a sample-efficient method for estimating model performance from limited data, reducing the upfront cost of identifying arbitrage strategies. Our analysis also yields several economic insights: at the optimum, every funded model delivers the same marginal utility per dollar; arbitrage directs revenue away from providers offering little utility relative to their prices; and it rewards complementary specialization.

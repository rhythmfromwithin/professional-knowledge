---
title: "Bayesian X-Learner: Calibrated Posterior Inference for Heterogeneous Treatment Effects under Heavy-Tailed Outcomes"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.27394
priority: medium
status: unread
interest: medium
next_step: skim
---
# Bayesian X-Learner: Calibrated Posterior Inference for Heterogeneous Treatment Effects under Heavy-Tailed Outcomes
> 原文: [https://arxiv.org/abs/2604.27394](https://arxiv.org/abs/2604.27394)

arXiv:2604.27394v1 Announce Type: new
Abstract: Conditional Average Treatment Effect (CATE) estimation in practice demands three properties simultaneously: heterogeneous effects $\tau(x)$, calibrated uncertainty over them, and robustness to the heavy tails that contaminate real outcome data. Meta-learners (K\"unzel et al., 2019) give (i); causal forests and BART give (i)-(ii) with Gaussian-tail assumptions; no widely used tool gives all three. We present Bayesian X-Learner, an X-Learner built on cross-fitted doubly robust pseudo-outcomes (Kennedy, 2020) with a full MCMC posterior over $\tau(x)$ via a Welsch redescending pseudo-likelihood. On Hill's IHDP benchmark the default configuration attains mean $\sqrt{\varepsilon\_{\mathrm{PEHE}}} = 0.56$ on 5 replications (lowest mean; differences from S-/T-/X-learners, full-config Causal BART, and a causal forest baseline are not significant at $\alpha=0.05$, and rank ordering is unstable at 10 replications -- IHDP comparisons are competitive rather than dominant). On contaminated "whale" DGPs with up to 20-25% tail density, a one-flag extension (contamination\_severity) that selects a Huber-$\delta$ nuisance loss per Huber's minimax-$\delta$ relation recovers RMSE $\approx 0.13$ with tight credible intervals (single-cross-fit 30-seed coverage 83% [Wilson 66%, 93%] at 20% density; modular-Bayes pooling with Bayesian-bootstrap nuisance draws restores nominal 95% coverage).

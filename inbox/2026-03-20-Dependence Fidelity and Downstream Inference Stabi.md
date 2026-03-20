---
interest: medium
link: https://arxiv.org/abs/2603.17041
next_step: skim
priority: medium
slack_ts: '1773974695.716909'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Dependence Fidelity and Downstream Inference Stability in Generative Models
---
# Dependence Fidelity and Downstream Inference Stability in Generative Models
> 原文: [https://arxiv.org/abs/2603.17041](https://arxiv.org/abs/2603.17041)

arXiv:2603.17041v1 Announce Type: new
Abstract: Recent advances in generative AI have led to increasingly realistic synthetic data, yet evaluation criteria remain focused on marginal distribution matching. While these diagnostics assess local realism, they provide limited insight into whether a generative model preserves the multivariate dependence structures governing downstream inference. We introduce covariance-level dependence fidelity as a practical criterion for evaluating whether a generative distribution preserves joint structure beyond univariate marginals. We establish three core results. First, distributions can match all univariate marginals exactly while exhibiting substantially different dependence structures, demonstrating marginal fidelity alone is insufficient. Second, dependence divergence induces quantitative instability in downstream inference, including sign reversals in regression coefficients despite identical marginal behavior. Third, explicit control of covariance-level dependence divergence ensures stable behavior for dependence-sensitive tasks such as principal component analysis. Synthetic constructions illustrate how dependence preservation failures lead to incorrect conclusions despite identical marginal distributions. These results highlight dependence fidelity as a useful diagnostic for evaluating generative models in dependence-sensitive downstream tasks, with implications for diffusion models and variational autoencoders. These guarantees apply specifically to procedures governed by covariance structure; tasks requiring higher-order dependence such as tail-event estimation require richer criteria.

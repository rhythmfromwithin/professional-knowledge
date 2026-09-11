---
interest: medium
link: https://arxiv.org/abs/2609.09245
next_step: skim
priority: medium
slack_ts: '1789100104.781449'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: What Fixed-Rollout pass@k Evaluations Can Identify
---
# What Fixed-Rollout pass@k Evaluations Can Identify
> 原文: [https://arxiv.org/abs/2609.09245](https://arxiv.org/abs/2609.09245)

arXiv:2609.09245v1 Announce Type: new
Abstract: Repeated-sampling evaluations increasingly extrapolate pass@k far beyond the number n of samples collected per problem. We show that, in the pooled/random-task conditional-Binomial model, fixed-n success counts identify only the n free moments of the latent per-task success distribution. Consequently, direct pass@k is identified for k <= n, but generic extrapolated pass@k, tail exponents, and tail constants are not identified for k > n, even with arbitrarily many exchangeable tasks at the same rollout budget. This is stronger than the observation that the usual estimator is undefined beyond n: it characterizes the information missing from the fixed-depth count-law experiment. We give exact count-law-preserving constructions with incompatible extrapolations, state the exceptional unique-extension case, and compute sharp population identified intervals through Hausdorff principal representations. On the public 10,000-rollout-per-problem release of Brown et al., counterfactual n = 16 evaluations leave failure at k = 1000 ambiguous by factors from 1.5 to over 2,600 across four MATH/GSM8K/CodeContests configurations. The calibration shows that intermediate-scale failure share alone does not determine width. Our result does not reject parametric inference-time scaling laws; it supplies the nonparametric baseline against which their assumptions can be evaluated. We give an exact, conservative one-coordinate finite-task confidence certificate and a reporting standard separating direct estimates, identified sets, and model-conditioned forecasts.

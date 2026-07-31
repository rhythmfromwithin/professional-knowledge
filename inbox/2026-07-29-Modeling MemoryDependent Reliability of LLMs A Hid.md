---
interest: medium
link: https://arxiv.org/abs/2607.22951
next_step: skim
priority: medium
slack_ts: '1785468995.590769'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Modeling Memory-Dependent Reliability of LLMs: A Hidden Markov Model'
---
# Modeling Memory-Dependent Reliability of LLMs: A Hidden Markov Model
> 原文: [https://arxiv.org/abs/2607.22951](https://arxiv.org/abs/2607.22951)

arXiv:2607.22951v1 Announce Type: new
Abstract: Reliability assessment of large language models (LLMs) seeks to estimate the probability that a model produces correct responses under a specified operational profile. Conventional benchmark-based evaluation, often summarized by aggregate accuracy, provides a point estimate of performance but does not characterize the uncertainty associated with reliability claims. Currently, statistical inference methods for LLM reliability assessment are emerging. However, a key assumption underlying these models is that test outcomes can be treated as independent repeated trials. This assumption may be inappropriate in sequential settings, where later responses depend on earlier interactions through retained context, error propagation, or an evolving interaction state. We extend a hierarchical Bayesian framework for LLM reliability assessment by relaxing the assumption of independent task outcomes and introducing a Hidden Markov Model to capture sequential dependence in benchmark-constructed interaction sessions. In this formulation, outcomes are generated from a latent interaction state evolving according to a first-order Markov process, capturing changes in interaction context. Through experiments using Anthropic Claude and OpenAI on four datasets, we demonstrate the potential impact of sequential dependence on reliability assessment. The results suggest that ignoring sequential dependence may lead to overconfident reliability estimates.

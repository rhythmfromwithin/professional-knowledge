---
interest: medium
link: https://arxiv.org/abs/2610.02302
next_step: skim
priority: low
slack_ts: '1791266343.641249'
source: cs.CR - Cryptography and Security
status: unread
title: 'Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional
  Attacks'
---
# Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional Attacks
> 原文: [https://arxiv.org/abs/2610.02302](https://arxiv.org/abs/2610.02302)

arXiv:2610.02302v1 Announce Type: new
Abstract: Recent work has shown that large language models (LLMs) can be vulnerable to jailbreak attacks in which harmful intent is obscured through composition with benign tasks. A harmful request refused in isolation may elicit a different response when embedded within a larger, seemingly benign query. We study these compositional intent-hiding jailbreaks from an information-theoretic perspective. Our formulation associates each task with an estimated probability of being judged harmful: the average over the full task collection defines the prior probability of harmful intent, while the average over a selected bundle containing the target defines the posterior. Selecting auxiliary tasks so that these averages agree, which we call prior-posterior matching, leaves the estimated intent unchanged even though the harmful target remains in the bundle.
We study two settings that differ in whether query construction is part of the optimization. In the query-independent setting, tasks are selected without regard to how they will be expressed in the final query. We show that exact prior-posterior matching under a bundle-size constraint is computationally hard, derive an optimal water-filling solution for fractional weights, and characterize the smallest bundle satisfying a prescribed safety threshold. In the query-dependent setting, task selection and query construction are considered jointly, and intent concealment and target preservation are evaluated on the resulting query. We evaluate jailbreak effectiveness and preservation of the target behavior across bundle sizes, query generators, and several open-source models. These results show that compositional queries can elicit target behaviors beyond the direct-request baseline under the evaluated search budgets, while revealing a trade-off: as bundle size increases, response-level target preservation tends to decrease for several models.

---
interest: medium
link: https://arxiv.org/abs/2607.02583
next_step: skim
priority: low
slack_ts: '1783397053.344669'
source: cs.SE - Software Engineering
status: unread
title: 'Better Together, in the Right Order: Classical-then-LLM Optimization for SE'
---
# Better Together, in the Right Order: Classical-then-LLM Optimization for SE
> 原文: [https://arxiv.org/abs/2607.02583](https://arxiv.org/abs/2607.02583)

arXiv:2607.02583v1 Announce Type: new
Abstract: A growing body of work combines large language models (LLMs) with classical optimizers for software engineering (SE) configuration tasks. Often, the classical optimizer is in charge: it owns the search loop and calls the LLM only to assist in subroutines (e.g. to warm-start the first generation, propose a mutation, or stand in as a surrogate). We report that there is much value in the reverse approach: seeding an LLM with the results from a cheap classical learner.
We call this method SNAP2. Applied to over 100 SE tasks, it is the single best of all methods studied, reaching the top tier on 85% of tasks, ahead of the same LLM run alone (75%) and ahead of every method in which the classical optimizer retains control. It is also less expensive: relative to the LLM-alone method, it uses roughly 30% fewer tokens and runs 1.4x faster, since the classical setup performs the inexpensive work, and the LLM is invoked only to finish.
We conclude that it is unwise to study classical learners or LLMs in isolation: there is much value in combining the two, and in the order that combination is applied.

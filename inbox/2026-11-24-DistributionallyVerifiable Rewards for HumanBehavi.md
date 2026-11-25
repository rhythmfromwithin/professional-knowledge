---
interest: medium
link: https://arxiv.org/abs/2611.28048
next_step: skim
priority: high
slack_ts: '1795593785.805419'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Distributionally-Verifiable Rewards for Human-Behavior Simulation
---
# Distributionally-Verifiable Rewards for Human-Behavior Simulation
> 原文: [https://arxiv.org/abs/2611.28048](https://arxiv.org/abs/2611.28048)

arXiv:2611.28048v1 Announce Type: new
Abstract: Large language models are increasingly used to simulate survey respondents in social-science research. A useful simulator should predict individual responses, reproduce population response distributions, and capture demographic differences. Common training approaches struggle to balance these goals: exact-match rewards encourage the model to concentrate on the most frequent human response, which is contradictory to the goal of distributional alignment. Meanwhile, aggregate distribution matching can look good even when demographic information is ignored. To this end, we introduce Distributionally-Verifiable Rewards (DVR), a reinforcement-learning reward that uses demographic group distribution gaps to guide individual responses, designed by aligning policy generated frequencies with human response frequencies within each question-group margins. We evaluate the method using the OpinionQA dataset and find that comparing with accuracy-only RLVR, DVR preserves per-response accuracy while reducing JSD by 34.5% in-distribution and 14.6% on held-out questions, with higher DPC point estimates on both splits. Comparing KL-SFT with the demographics-blind marginal further shows that low JSD is insufficient to establish fidelity to population heterogeneity, highlighting that accuracy, distributional fit, and demographic structure should be evaluated together.

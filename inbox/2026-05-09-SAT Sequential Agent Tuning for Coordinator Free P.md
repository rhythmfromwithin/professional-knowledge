---
interest: medium
link: https://arxiv.org/abs/2605.05216
next_step: skim
priority: high
slack_ts: '1778472606.446209'
source: cs.LG - Machine Learning
status: unread
title: 'SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM
  Training with Monotonic Improvement Guarantees'
---
# SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM Training with Monotonic Improvement Guarantees
> 原文: [https://arxiv.org/abs/2605.05216](https://arxiv.org/abs/2605.05216)

arXiv:2605.05216v1 Announce Type: new
Abstract: Large language models (LLMs) with a large number of parameters achieve strong performance but are often prohibitively expensive to deploy. Recent work explores using teams of smaller, more efficient LLMs that collectively match or even outperform a single large model. However, jointly updating multiple agents introduces compounding distribution shifts, making coordination and stability during training difficult. We address this by introducing Sequential Agent Tuning (SAT), a coordinator-free training paradigm. SAT represents the team as a factorized policy and employs block-coordinate updates over agents, enabling scalable, decentralized training without a central controller. Specifically, we develop a sequence-aware, on-policy advantage estimator that conditions on the evolving team policy, coupled with per-agent KL trust regions that isolate occupancy drift. Theoretically, this framework provides two critical guarantees. First, it ensures monotonic improvement, stabilizing the training process. Second, it establishes provable plug-and-play invariance: any agent can be upgraded to a stronger model without retraining the rest of the team, with a formal guarantee that the performance bound improves. Empirically, a team of three 4B agents (12B total) trained with SAT surpasses the much larger Qwen3-32B on AIME24/25 benchmarks by 3.9\% on average. We validate our plug-and-play theory by swapping in two 8B agents, which boosts the composite score by 10.4\%. We provide code and appendix of proof at https://github.com/Yydc/SAT-AAMAS

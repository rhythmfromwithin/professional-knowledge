---
interest: medium
link: https://arxiv.org/abs/2605.16302
next_step: skim
priority: high
slack_ts: '1779164093.645789'
source: cs.LG - Machine Learning
status: unread
title: Reducing Credit Assignment Variance via Counterfactual Reasoning Paths
---
# Reducing Credit Assignment Variance via Counterfactual Reasoning Paths
> 原文: [https://arxiv.org/abs/2605.16302](https://arxiv.org/abs/2605.16302)

arXiv:2605.16302v1 Announce Type: new
Abstract: Reinforcement learning for multi-step reasoning with large language models (LLMs) often relies on sparse terminal rewards, leading to poor credit assignment conditions where the final feedback is evenly propagated across all intermediate decisions. This results in high gradient variance, unstable training, and numerous ineffective updates, ultimately causing the model to fail and preventing sustained improvement. We introduce a counterfactual comparison-based credit assignment framework, which samples multiple reasoning trajectories under the same input. By treating their differences as an implicit approximation of alternative decisions, we construct an implicit process-level advantage estimator that transforms sparse terminal rewards into step-sensitive learning signals. Based on this, we propose Implicit Behavior Policy Optimization (IBPO), which significantly improves training stability and performance upper bounds on mathematical and code reasoning benchmarks, pointing to a promising direction for unlocking the performance potential of LLMs.

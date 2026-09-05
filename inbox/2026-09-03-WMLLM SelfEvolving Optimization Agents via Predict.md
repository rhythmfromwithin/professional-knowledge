---
interest: medium
link: https://arxiv.org/abs/2609.01608
next_step: skim
priority: high
slack_ts: '1788581039.066669'
source: cs.LG - Machine Learning
status: unread
title: 'WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling'
---
# WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling
> 原文: [https://arxiv.org/abs/2609.01608](https://arxiv.org/abs/2609.01608)

arXiv:2609.01608v1 Announce Type: new
Abstract: Black-box optimization problems remain challenging because of large, weakly structured, and high-dimensional search spaces. Existing methods often suffer from poor sample efficiency because they rely on direct candidate generation or trial-and-error refinement. A natural way to improve search efficiency is to use world modeling, which can help identify promising optimization directions before costly evaluation. Large language models can predict the outcomes of these candidates with nontrivial accuracy because of their implicit knowledge. Motivated by this observation, we propose WMLLM, a self-evolving optimization-agent framework based on predict-then-act world modeling. The agent first predicts promising directions and then acts to generate candidates. Combined with agentic multi-turn refinement, population-based search, and reinforcement learning, WMLLM refines both its implicit world model and its optimization strategy during search. Experiments on black-box optimization tasks, especially multi-objective molecular optimization, show that WMLLM improves sample efficiency and final optimization performance. On the multi-objective molecular optimization benchmark, WMLLM achieves state-of-the-art results under a limited evaluation budget.

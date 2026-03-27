---
title: "Implicit Turn-Wise Policy Optimization for Proactive User-LLM Interaction"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.23550
priority: high
status: unread
interest: medium
next_step: skim
---
# Implicit Turn-Wise Policy Optimization for Proactive User-LLM Interaction
> 原文: [https://arxiv.org/abs/2603.23550](https://arxiv.org/abs/2603.23550)

arXiv:2603.23550v1 Announce Type: new
Abstract: Multi-turn human-AI collaboration is fundamental to deploying interactive services such as adaptive tutoring, conversational recommendation, and professional consultation. However, optimizing these interactions via reinforcement learning is hindered by the sparsity of verifiable intermediate rewards and the high stochasticity of user responses. To address these challenges, we introduce Implicit Turn-wise Policy Optimization (ITPO). ITPO leverages an implicit process reward model to derive fine-grained, turn-wise process rewards from sparse outcome signals. Unlike volatile token-level rewards, these turn-level signals exhibit superior robustness and may utilize a normalization mechanism to further enhance training stability. We evaluate ITPO across three representative multi-turn collaborative tasks: math tutoring, document writing, and medical recommendation. Empirical results demonstrate that ITPO, when combined with PPO, GRPO, or RLOO, consistently achieves improved convergence than existing baselines. Elaborate trajectory analysis confirms that ITPO infers turn-wise preferences that are semantically aligned with human judgment. Code is publicly available at https://github.com/Graph-COM/ITPO.

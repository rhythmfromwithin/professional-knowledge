---
title: "ATPO: Adaptive Tree Policy Optimization for Multi-Turn Medical Dialogue"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.02216
priority: high
status: unread
interest: medium
next_step: skim
---
# ATPO: Adaptive Tree Policy Optimization for Multi-Turn Medical Dialogue
> 原文: [https://arxiv.org/abs/2603.02216](https://arxiv.org/abs/2603.02216)

arXiv:2603.02216v1 Announce Type: new
Abstract: Effective information seeking in multi-turn medical dialogues is critical for accurate diagnosis, especially when dealing with incomplete information. Aligning Large Language Models (LLMs) for these interactive scenarios is challenging due to the uncertainty inherent in user-agent interactions, which we formulate as a Hierarchical Markov Decision Process (H-MDP). While conventional Reinforcement Learning (RL) methods like Group Relative Policy Optimization (GRPO) struggle with long-horizon credit assignment and Proximal Policy Optimization (PPO) suffers from unstable value estimation in this context, we propose a novel uncertainty-aware Adaptive Tree Policy Optimization (ATPO) algorithm. Our method adaptively allocates the rollout budget to states with high uncertainty, quantified by a composite metric of Bellman error and action-value variance. This strategy enables more accurate value estimation, while fostering more efficient and diverse exploration. To mitigate the high computational cost of tree-based RL, we introduce two key optimizations: an uncertainty-guided pruning mechanism to minimize the number of rollouts, and an asynchronous search architecture that leverages KV cache reuse to maximize inference throughput. Extensive experiments on three public medical dialogue benchmarks demonstrate that our algorithm significantly outperforms several strong baselines, culminating in Qwen3-8B model surpassing the much larger GPT-4o ($+0.92\%$ accuracy).

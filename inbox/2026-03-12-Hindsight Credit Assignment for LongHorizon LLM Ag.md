---
title: "Hindsight Credit Assignment for Long-Horizon LLM Agents"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.08754
priority: high
status: unread
interest: medium
next_step: skim
---
# Hindsight Credit Assignment for Long-Horizon LLM Agents
> 原文: [https://arxiv.org/abs/2603.08754](https://arxiv.org/abs/2603.08754)

arXiv:2603.08754v1 Announce Type: new
Abstract: Large Language Model (LLM) agents often face significant credit assignment challenges in long-horizon, multi-step tasks due to sparse rewards. Existing value-free methods, such as Group Relative Policy Optimization (GRPO), encounter two fundamental bottlenecks: inaccurate step-level Q-value estimation and misaligned value baselines for intermediate states. To address these limitations, we introduce HCAPO, the first framework to integrate hindsight credit assignment into LLM agents. HCAPO leverages the LLM itself as a post-hoc critic to refine step-level Q-values through hindsight reasoning. Furthermore, HCAPO's multi-scale advantage mechanism effectively supplements the inaccurate value baselines at critical decision states. Evaluations across three challenging benchmarks, including WebShop and ALFWorld, demonstrate that HCAPO consistently outperforms state-of-the-art RL methods. Notably, HCAPO achieves a 7.7% improvement in success rate on WebShop and a 13.8% on ALFWorld over GRPO using the Qwen2.5-7B-Instruct model. These results indicate that HCAPO significantly enhances exploration efficiency, promotes concise decision-making, and ensures scalability in complex, long-horizon tasks.

---
interest: medium
link: https://arxiv.org/abs/2607.09207
next_step: skim
priority: medium
slack_ts: '1783998907.559319'
source: cs.DC - Distributed Computing
status: unread
title: Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training
---
# Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training
> 原文: [https://arxiv.org/abs/2607.09207](https://arxiv.org/abs/2607.09207)

arXiv:2607.09207v1 Announce Type: new
Abstract: It is well established that the reasoning capabilities of large language models (LLMs) can be improved by applying reinforcement learning (RL) in a post-training stage. In a standard RL iteration, the current model (the policy) generates experience through rollouts, and the resulting data is then used to update the policy during training. High-performance RL frameworks such as StreamRL and AReaL employ a disaggregated architecture and asynchronous rollouts to better exploit both rollout and training resources, thereby increasing overall system throughput.
Nonetheless, across varying RL setups (e.g., hardware configurations, model scales, staleness levels, and hyperparameters) and under changing workloads, it remains common for both rollout and training resources to experience idle periods.
In this paper, we present BiDiRL, a hybrid time-space multiplexing architecture for asynchronous, disaggregated RL designed to reduce resource idleness. First, we develop a hot-switch runtime that enables rapid switching between rollout and training resources with negligible overhead. Second, we propose a static, scheduling-aware planner based on time-performance modeling that chooses a hot-switch-friendly resource partition, so that rollout and training durations are roughly balanced at a coarse level. Third, at execution time, we introduce a bidirectional scheduler that further exploits runtime bubbles through fine-grained resource switching, allowing the bottleneck stage to temporarily borrow idle resources from the other pool. Across a wide range of workloads, datasets, and models on two 32-GPU testbeds, BiDiRL increases RL training throughput by up to 1.94x compared with RL systems including veRL, AReaL, and ROLL, without affecting convergence behavior.

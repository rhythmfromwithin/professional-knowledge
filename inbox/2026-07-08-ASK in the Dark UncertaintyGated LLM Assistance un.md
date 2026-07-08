---
interest: medium
link: https://arxiv.org/abs/2607.02686
next_step: skim
priority: high
slack_ts: '1783481428.106639'
source: cs.AI - Artificial Intelligence
status: unread
title: 'ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability'
---
# ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability
> 原文: [https://arxiv.org/abs/2607.02686](https://arxiv.org/abs/2607.02686)

arXiv:2607.02686v1 Announce Type: new
Abstract: Reinforcement learning agents operating under partial observability must act on incomplete information, making them natural candidates for guidance from small language models (SLMs) that carry broad reasoning priors. Yet integrating SLM guidance into this setting has proven difficult: across all test environments, vanilla uncertainty-gated approaches achieve an overwrite rate at or near zero, meaning the SLM almost never contributes an independent action. We trace this failure to the bare egocentric prompt, which provides insufficient context for genuine reasoning, and identify it as a context problem rather than a capacity problem. We propose ASK+, which supplies the SLM with trajectory-aware context (a partially revealed map, visited positions, and action history) and structured chain-of-thought reasoning, converting it from a passive redundancy check into a more informative consultant that occasionally corrects the policy. We further establish that the predictive entropy signal used for selective querying measures action uncertainty rather than state uncertainty and remains informative in POMDPs, making uncertainty-gated assistance viable beyond fully observable settings. The stateful prompt drives substantial gains: on DoorKey, where vanilla ASK matches PPO (both 89%), ASK+ reaches 93% success; on FourRooms, success climbs from 53% to 70%; on HigherLower, accuracy reaches 73.7%, matching the SLM-only upper bound. Across all environments, Qwen3.5-2B matches or exceeds Qwen3.5-4B, confirming that prompt design and selective gating dominate the impact of model scale, enabling guidance without large models.

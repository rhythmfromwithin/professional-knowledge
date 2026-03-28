---
interest: medium
link: https://arxiv.org/abs/2603.22292
next_step: skim
priority: high
slack_ts: '1774666190.997909'
source: cs.LG - Machine Learning
status: unread
title: 'Beyond Hard Constraints: Budget-Conditioned Reachability For Safe Offline
  Reinforcement Learning'
---
# Beyond Hard Constraints: Budget-Conditioned Reachability For Safe Offline Reinforcement Learning
> 原文: [https://arxiv.org/abs/2603.22292](https://arxiv.org/abs/2603.22292)

arXiv:2603.22292v1 Announce Type: new
Abstract: Sequential decision making using Markov Decision Process underpins many realworld applications. Both model-based and model free methods have achieved strong results in these settings. However, real-world tasks must balance reward maximization with safety constraints, often conflicting objectives, that can lead to unstable min/max, adversarial optimization. A promising alternative is safety reachability analysis, which precomputes a forward-invariant safe state, action set, ensuring that an agent starting inside this set remains safe indefinitely. Yet, most reachability based methods address only hard safety constraints, and little work extends reachability to cumulative cost constraints. To address this, first, we define a safetyconditioned reachability set that decouples reward maximization from cumulative safety cost constraints. Second, we show how this set enforces safety constraints without unstable min/max or Lagrangian optimization, yielding a novel offline safe RL algorithm that learns a safe policy from a fixed dataset without environment interaction. Finally, experiments on standard offline safe RL benchmarks, and a real world maritime navigation task demonstrate that our method matches or outperforms state of the art baselines while maintaining safety.

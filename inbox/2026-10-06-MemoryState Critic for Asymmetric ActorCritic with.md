---
title: "Memory-State Critic for Asymmetric Actor-Critic with Application to Vision-Based Pursuit-Evasion"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.03830
priority: high
status: unread
interest: medium
next_step: skim
---
# Memory-State Critic for Asymmetric Actor-Critic with Application to Vision-Based Pursuit-Evasion
> 原文: [https://arxiv.org/abs/2610.03830](https://arxiv.org/abs/2610.03830)

arXiv:2610.03830v1 Announce Type: new
Abstract: In partially observable Markov decision processes, the optimal policy generally depends on the history of observations and past actions. Asymmetric actor-critic methods have become popular to learn such policies when additional information, such as the true state of the environment, is available during training. The critic, which is not needed at execution, is given access to the state. A critic conditioned on the state alone is generally ill-defined and yields biased policy gradients. Conditioning on the state and the history, the history-state critic restores both. In this paper, we show that conditioning the critic on the state and the policy's own memory, i.e., the internal representation of the history through which the policy selects its actions, is already well-defined and gives unbiased policy gradients, removing the need for a second recurrent approximator of the history. We call it the memory state critic. It follows that a critic based on the policy's memory need not backpropagate its loss into that memory, even though the memory is a lossy encoding of the history. We evaluate the memory-state critic in a vision-based pursuit-evasion environment between two quadrotors across two arena types. The pursuer is the learning agent, and the evader is sampled per episode from a fixed pool of heuristic behaviours. The results show that the memory-state critic outperforms the history-state critic and converges faster. In addition to being unbiased compared to the state-only critic, it maintains a slight edge in the wall arena, where the actor's history carries information that the privileged state alone does not.

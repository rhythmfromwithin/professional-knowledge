---
title: "Territory Paint Wars: Diagnosing and Mitigating Failure Modes in Competitive Multi-Agent PPO"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.04983
priority: high
status: unread
interest: medium
next_step: skim
---
# Territory Paint Wars: Diagnosing and Mitigating Failure Modes in Competitive Multi-Agent PPO
> 原文: [https://arxiv.org/abs/2604.04983](https://arxiv.org/abs/2604.04983)

arXiv:2604.04983v1 Announce Type: new
Abstract: We present Territory Paint Wars, a minimal competitive multi-agent reinforcement learning environment implemented in Unity, and use it to systematically investigate failure modes of Proximal Policy Optimisation (PPO) under self-play. A first agent trained for $84{,}000$ episodes achieves only $26.8\%$ win rate against a uniformly-random opponent in a symmetric zero-sum game. Through controlled ablations we identify five implementation-level failure modes -- reward-scale imbalance, missing terminal signal, ineffective long-horizon credit assignment, unnormalised observations, and incorrect win detection -- each of which contributes critically to this failure in this setting.
After correcting these issues, we uncover a distinct emergent pathology: competitive overfitting, where co-adapting agents maintain stable self-play performance while generalisation win rate collapses from $73.5\%$ to $21.6\%$. Critically, this failure is undetectable via standard self-play metrics: both agents co-adapt equally, so the self-play win rate remains near $50\%$ throughout the collapse.
We propose a minimal intervention -- opponent mixing, where $20\%$ of training episodes substitute a fixed uniformly-random policy for the co-adaptive opponent -- which mitigates competitive overfitting and restores generalisation to $77.1\%$ ($\pm 12.6\%$, $10$ seeds) without population-based training or additional infrastructure. We open-source Territory Paint Wars to provide a reproducible benchmark for studying competitive MARL failure modes.

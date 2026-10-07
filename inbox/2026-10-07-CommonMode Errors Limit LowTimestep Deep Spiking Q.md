---
title: "Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2610.07808
priority: low
status: unread
interest: medium
next_step: skim
---
# Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks
> 原文: [https://arxiv.org/abs/2610.07808](https://arxiv.org/abs/2610.07808)

arXiv:2610.07808v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices. In value-based RL, deep spiking Q-networks (DSQNs) combine such efficiency with action-value estimation for decision making. However, existing DSQNs often require multiple simulation timesteps for competitive performance, increasing computational and energy costs, whereas reducing the timesteps can cause substantial performance degradation. We investigate this degradation from the perspective of Q-value estimation errors. By decomposing errors across actions into common-mode and differential-mode components, we find that low-timestep DSQNs suffer disproportionately from common-mode errors shared across action values, which are particularly detrimental to temporal-difference learning through bootstrapped targets. Based on this finding, we propose Common-Mode Compensation Deep Spiking Q-Network (CMC-DSQN), which uses an auxiliary ANN to compensate for common-mode errors in the SNN outputs. At inference, greedy action selection can be performed directly from the SNN outputs, allowing the auxiliary ANN to be completely removed and preserving the energy efficiency of SNNs. Extensive experiments on Atari and MiniAtar environments demonstrate substantial performance improvements under low-timestep settings. CMC-DSQN outperforms state-of-the-art DSQN baselines by nearly $20\%$ at $T=2$ and further surpasses the ANN baseline at $T=4$.

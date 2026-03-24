---
interest: medium
link: https://arxiv.org/abs/2603.15622
next_step: skim
priority: medium
slack_ts: '1774320340.431539'
source: cs.CV - Computer Vision
status: unread
title: 'SAC-NeRF: Adaptive Ray Sampling for Neural Radiance Fields via Soft Actor-Critic
  Reinforcement Learning'
---
# SAC-NeRF: Adaptive Ray Sampling for Neural Radiance Fields via Soft Actor-Critic Reinforcement Learning
> 原文: [https://arxiv.org/abs/2603.15622](https://arxiv.org/abs/2603.15622)

arXiv:2603.15622v1 Announce Type: new
Abstract: Neural Radiance Fields (NeRF) have achieved photorealistic novel view synthesis but suffer from computational inefficiency due to dense ray sampling during volume rendering. We propose SAC-NeRF, a reinforcement learning framework that learns adaptive sampling policies using Soft Actor-Critic (SAC). Our method formulates sampling as a Markov Decision Process where an RL agent learns to allocate samples based on scene characteristics. We introduce three technical components: (1) a Gaussian mixture distribution color model providing uncertainty estimates, (2) a multi-component reward function balancing quality, efficiency, and consistency, and (3) a two-stage training strategy addressing environment non-stationarity. Experiments on Synthetic-NeRF and LLFF datasets show that SAC-NeRF reduces sampling points by 35-48\% while maintaining rendering quality within 0.3-0.8 dB PSNR of dense sampling baselines. While the learned policy is scene-specific and the RL framework adds complexity compared to simpler heuristics, our work demonstrates that data-driven sampling strategies can discover effective patterns that would be difficult to hand-design.

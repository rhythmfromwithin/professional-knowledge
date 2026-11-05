---
title: "Energy-Efficient Reinforcement Learning for Large Language Models"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.05748
priority: medium
status: unread
interest: medium
next_step: skim
---
# Energy-Efficient Reinforcement Learning for Large Language Models
> 原文: [https://arxiv.org/abs/2611.05748](https://arxiv.org/abs/2611.05748)

arXiv:2611.05748v1 Announce Type: new
Abstract: Reinforcement learning for language models alternates between generating responses and training the policy. These stages place different demands on GPUs, creating opportunities to reduce clock frequency with little loss in throughput. Selecting frequencies online is difficult because response lengths change and frequency trials themselves consume time and energy. We present EE-RL (energy-efficient RL), an online controller that selects separate frequencies for generation and training during RL execution. It compares candidate settings with a prediction of the default GPU governor on the same token workload, and keeps the most energy-efficient setting that meets a throughput threshold. The controller then monitors throughput and energy and adjusts frequencies as the workload changes. Fixed-frequency sweeps on H100 and GB200 show GPU energy savings of up to 28.2% per valid training token across synchronous and asynchronous execution, while largely preserving throughput. EE-RL turns this headroom into online savings, reducing GPU energy per valid training token by up to 16.9% at a modest throughput cost.

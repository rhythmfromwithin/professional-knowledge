---
interest: medium
link: https://arxiv.org/abs/2609.09161
next_step: skim
priority: medium
slack_ts: '1789100103.282609'
source: cs.DC - Distributed Computing
status: unread
title: SMCC-Empowered Digital Twins for Sensorless Monitoring in Large-Scale AI-Driven
  IoT Systems
---
# SMCC-Empowered Digital Twins for Sensorless Monitoring in Large-Scale AI-Driven IoT Systems
> 原文: [https://arxiv.org/abs/2609.09161](https://arxiv.org/abs/2609.09161)

arXiv:2609.09161v1 Announce Type: new
Abstract: The deployment of AI-driven Digital Twins (DTs) in large-scale Internet-of-Things (IoT) ecosystems demands continuous, high-fidelity synchronization between the physical environment and its virtual replica. Conventional approaches rely on dense sensor deployments, which introduce prohibitive costs in terms of hardware, energy, and network bandwidth. In this paper, we propose SMCC-DT, an integrated Sensing-Memory-Communication-Computation (SMCC) framework that enables sensorless monitoring of physical assets by exploiting Integrated Sensing and Communication (ISAC) waveforms at the 6G Edge. Under the SMCC-DT paradigm, a single radio signal simultaneously extracts environmental telemetry (Sensing) and delivers it to an Edge server (Communication), where a large-scale AI model is loaded into constrained memory (Memory) and executed (Computation) to update the DT state. We formulate the DT synchronization problem as a cross-layer optimization that jointly allocates transmit power, beamforming vectors, memory partitions, and CPU frequency to minimize the end-to-end synchronization latency subject to sensing accuracy, throughput, memory capacity, and computational budget constraints. Because the resulting mixed-integer nonlinear program is NP-hard, we design a Proximal Policy Optimization (PPO)-based Deep Reinforcement Learning (DRL) agent, termed SMCCAGENT, that learns near-optimal resource allocation policies online. Extensive simulations over a 500-node industrial IoT testbed demonstrate that SMCC-DT reduces DT synchronization latency by 38.7% and total energy consumption by 27.4% compared to state-of-the-art orthogonal and compute-only baselines, while sustaining sensing accuracy above 95% and model inference throughput above 30 frames per second.

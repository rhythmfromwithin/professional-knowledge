---
title: "Embodied Foundation Models at the Edge: A Survey of Deployment Constraints and Mitigation Strategies"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.16952
priority: medium
status: unread
interest: medium
next_step: skim
---
# Embodied Foundation Models at the Edge: A Survey of Deployment Constraints and Mitigation Strategies
> 原文: [https://arxiv.org/abs/2603.16952](https://arxiv.org/abs/2603.16952)

arXiv:2603.16952v2 Announce Type: new
Abstract: Deploying foundation models in embodied edge systems is fundamentally a systems problem, not just a problem of model compression. Real-time control must operate within strict size, weight, and power constraints, where memory traffic, compute latency, timing variability, and safety margins interact directly. The Deployment Gauntlet organizes these constraints into eight coupled barriers that determine whether embodied foundation models can run reliably in practice. Across representative edge workloads, autoregressive Vision-Language-Action policies are constrained primarily by memory bandwidth, whereas diffusion-based controllers are limited more by compute latency and sustained execution cost. Reliable deployment therefore depends on system-level co-design across memory, scheduling, communication, and model architecture, including decompositions that separate fast control from slower semantic reasoning.

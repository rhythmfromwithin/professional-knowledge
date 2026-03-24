---
interest: medium
link: https://arxiv.org/abs/2603.19418
next_step: skim
priority: medium
slack_ts: '1774320366.047989'
source: cs.DC - Distributed Computing
status: unread
title: 'Speculative Policy Orchestration: A Latency-Resilient Framework for Cloud-Robotic
  Manipulation'
---
# Speculative Policy Orchestration: A Latency-Resilient Framework for Cloud-Robotic Manipulation
> 原文: [https://arxiv.org/abs/2603.19418](https://arxiv.org/abs/2603.19418)

arXiv:2603.19418v1 Announce Type: cross
Abstract: Cloud robotics enables robots to offload high-dimensional motion planning and reasoning to remote servers. However, for continuous manipulation tasks requiring high-frequency control, network latency and jitter can severely destabilize the system, causing command starvation and unsafe physical execution.
To address this, we propose Speculative Policy Orchestration (SPO), a latency-resilient cloud-edge framework. SPO utilizes a cloud-hosted world model to pre-compute and stream future kinematic waypoints to a local edge buffer, decoupling execution frequency from network round-trip time. To mitigate unsafe execution caused by predictive drift, the edge node employs an $\epsilon$-tube verifier that strictly bounds kinematic execution errors. The framework is coupled with an Adaptive Horizon Scaling mechanism that dynamically expands or shrinks the speculative pre-fetch depth based on real-time tracking error.
We evaluate SPO on continuous RLBench manipulation tasks under emulated network delays. Results show that even when deployed with learned models of modest accuracy, SPO reduces network-induced idle time by over 60% compared to blocking remote inference. Furthermore, SPO discards approximately 60% fewer cloud predictions than static caching baselines. Ultimately, SPO enables fluid, real-time cloud-robotic control while maintaining bounded physical safety.

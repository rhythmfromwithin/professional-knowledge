---
interest: medium
link: https://arxiv.org/abs/2604.22852
next_step: skim
priority: medium
slack_ts: '1777521053.740499'
source: cs.RO - Robotics
status: unread
title: 'SwarmDrive: Semantic V2V Coordination for Latency-Constrained Cooperative
  Autonomous Driving'
---
# SwarmDrive: Semantic V2V Coordination for Latency-Constrained Cooperative Autonomous Driving
> 原文: [https://arxiv.org/abs/2604.22852](https://arxiv.org/abs/2604.22852)

arXiv:2604.22852v1 Announce Type: new
Abstract: Cloud-hosted LLM inference for autonomous driving adds round-trip delay and depends on stable connectivity, while purely local edge models struggle under occlusion. We present SwarmDrive, a semantic Vehicle-to-Vehicle (V2V) coordination framework in which nearby vehicles run local Small Language Models (SLMs), share compact intent distributions only when uncertainty is high, and fuse them through event-triggered consensus. We evaluate SwarmDrive in a 5-seed executable study built around one occluded intersection case, combining matched operating-point comparisons with robustness sweeps. In that setting, SwarmDrive under its 6G communication setting ("Swarm 6G") raises success from 68.9% to 94.1% over a single local SLM while reducing latency from a 510 ms cloud reference to 151.4 ms. However, an increased number of participating vehicles leads to higher communication overhead and packet loss. SwarmDrive also evaluates the impact of swarm-size, packet-loss, and entropy-threshold sweeps and shows that the cooperative gain holds across ablations and is best balanced near an active swarm size of 4 vehicles and an entropy trigger threshold of 0.65 in the current prototype. These results show that semantic edge cooperation can work under tight latency constraints in the targeted intersection case, but they are not a deployment-grade validation of a real 6G stack.

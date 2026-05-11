---
interest: medium
link: https://arxiv.org/abs/2605.05527
next_step: skim
priority: medium
slack_ts: '1778472598.310699'
source: cs.DC - Distributed Computing
status: unread
title: 'EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge'
---
# EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge
> 原文: [https://arxiv.org/abs/2605.05527](https://arxiv.org/abs/2605.05527)

arXiv:2605.05527v1 Announce Type: new
Abstract: As edge computing expands, serving multiple deep neural network (DNN) models on a single shared GPU has become a common yet challenging scenario, where each scheduling decision affects the tail latency of all concurrent queues. Existing schedulers rely on local heuristics and fail to capture this global impact, while GPU spatial-sharing approaches sacrifice latency predictability. In this paper, we propose EdgeServing, a deadline-aware multi-DNN serving system for edge devices. EdgeServing adopts time-division GPU sharing with early-exit inference for high inference predictability, and introduces a stability score to quantify how each candidate scheduling decision impacts the future queue status. At runtime, it cohesively selects the model, exit point, and batch size to minimize predicted system-wide SLO impact. Experimental results on multiple hardware platforms show that EdgeServing consistently outperforms representative baselines in both SLO violation ratio and P95 latency, enabled by early-exit mechanism, which expands the scheduling action space under tight latency constraints.

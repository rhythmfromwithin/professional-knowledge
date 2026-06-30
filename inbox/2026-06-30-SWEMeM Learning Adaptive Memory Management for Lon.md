---
interest: medium
link: https://arxiv.org/abs/2606.28434
next_step: skim
priority: low
slack_ts: '1782792825.410539'
source: cs.SE - Software Engineering
status: unread
title: 'SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents'
---
# SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents
> 原文: [https://arxiv.org/abs/2606.28434](https://arxiv.org/abs/2606.28434)

arXiv:2606.28434v1 Announce Type: new
Abstract: Long-horizon software engineering agents often need to manage lengthy and noisy interaction histories under limited context budgets. Existing memory management methods typically rely on static compression workflows or impose rigid constraints on compression timing and granularity. Moreover, these approaches fail to jointly optimize memory management and issue resolution capabilities to improve performance while reducing token usage. We present SWE-MeM, a training framework for proactive and on-demand memory management in software engineering agents. SWE-MeM provides a flexible memory tool that lets agents decide when, what, and how to compress based on trajectory state, task progress, and remaining context budget. We train agents with synthesized proactive memory-management trajectories and Memory-aware GRPO, which jointly optimizes memory management and issue resolution through memory-aware trajectory splitting and step-level credit assignment. On SWE-Bench Verified, SWE-MeM achieves 43.4% and 60.2% resolve rate with 4B and 30B models, respectively, outperforming existing memory management baselines in both performance and efficiency.

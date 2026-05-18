---
interest: medium
link: https://arxiv.org/abs/2605.12655
next_step: skim
priority: high
slack_ts: '1779077921.813069'
source: cs.AI - Artificial Intelligence
status: unread
title: Macro-Action Based Multi-Agent Instruction Following through Value Cancellation
---
# Macro-Action Based Multi-Agent Instruction Following through Value Cancellation
> 原文: [https://arxiv.org/abs/2605.12655](https://arxiv.org/abs/2605.12655)

arXiv:2605.12655v1 Announce Type: new
Abstract: Multi-agent reinforcement learning (MARL) in real-world use cases may need to adapt to external natural language instructions that interrupt ongoing behavior and conflict with long-horizon objectives. However, conditioning rewards on instructions introduces a fundamental failure mode as Bellman updates couple value estimates across instruction contexts, leading to inconsistent values when instructions interrupt macro-actions. We propose Macro-Action Value Correction for Instruction Compliance (MAVIC), which corrects Bellman backups at instruction boundaries by correcting the incoming instruction objective and restoring the continuation value under the current objective. Unlike reward shaping, MAVIC modifies the bootstrapping target itself, enabling consistent value estimation under stochastic instruction switching within a unified policy. We provide theoretical analysis and an actor-critic implementation, and show that MAVIC achieves high instruction compliance while preserving base task performance in increasingly complex cooperative multi-agent environments.

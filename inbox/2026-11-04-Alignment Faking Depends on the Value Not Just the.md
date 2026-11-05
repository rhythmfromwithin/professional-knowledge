---
interest: medium
link: https://arxiv.org/abs/2611.03650
next_step: skim
priority: high
slack_ts: '1793859281.101439'
source: cs.AI - Artificial Intelligence
status: unread
title: Alignment Faking Depends on the Value, Not Just the Model
---
# Alignment Faking Depends on the Value, Not Just the Model
> 原文: [https://arxiv.org/abs/2611.03650](https://arxiv.org/abs/2611.03650)

arXiv:2611.03650v1 Announce Type: new
Abstract: Language models can follow a directive when they believe they are monitored and abandon it when they believe they are not, a pattern termed Alignment Faking. Prior work establishes this for harmful-content objectives and a handful of moral-foundations values, leaving open how it distributes across a wider value space. We argue it is value-dependent: whether compliance survives a change in perceived oversight is a property of the model--value pairing, not of the model alone. Our framework profiles Alignment Faking per value, scoring each model-value pair under three conditions: bare (no system prompt), unmonitored, and monitored. On 32 ValueBench dimensions across ten open- and closed-weight models (8B-~675B), compliance gaps span 0.05-0.50, with a distilled 70B above a ~675B model. We observe that majority of the structural variance depends on which model was asked about which value and not on the model or value alone. A six-category taxonomy over reasoning traces tracks the behavioural shift: training-signal reasoning dominates under monitoring and value-conflict reasoning dominates when unmonitored. We package per-model results as value cards, extending model cards with behavioral disposition. Code and data are available at https://github.com/respailab/VALET.

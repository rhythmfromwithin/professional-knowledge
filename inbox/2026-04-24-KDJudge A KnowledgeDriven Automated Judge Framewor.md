---
interest: medium
link: https://arxiv.org/abs/2604.19834
next_step: skim
priority: medium
slack_ts: '1777087204.426979'
source: cs.CV - Computer Vision
status: unread
title: 'KD-Judge: A Knowledge-Driven Automated Judge Framework for Functional Fitness
  Movements on Edge Devices'
---
# KD-Judge: A Knowledge-Driven Automated Judge Framework for Functional Fitness Movements on Edge Devices
> 原文: [https://arxiv.org/abs/2604.19834](https://arxiv.org/abs/2604.19834)

arXiv:2604.19834v1 Announce Type: new
Abstract: Functional fitness movements are widely used in training, competition, and health-oriented exercise programs, yet consistently enforcing repetition (rep) standards remains challenging due to subjective human judgment, time constraints, and evolving rules. Existing AI-based approaches mainly rely on learned scoring or reference-based comparisons and lack explicit rule-based, limiting transparency and deterministic rep-level validation. To address these limitations, we propose KD-Judge, a novel knowledge-driven automated judging framework for functional fitness movements. It converts unstructured rulebook standards into executable, machine-readable representations using an LLM-based retrieval-augmented generation and chain-of-thought rule-structuring pipeline. The structured rules are then incorporated by a deterministic rule-based judging system with pose-guided kinematic reasoning to assess rep validity and temporal boundaries. To improve efficiency on edge devices, including a high-performance desktop and the resource-constrained Jetson AGX Xavier, we introduce a dual strategy caching mechanism that can be selectively applied to reduce redundant and unnecessary computation. Experiments demonstrate reliable rule-structuring performance and accurate rep-level assessment, with judgment evaluation conducted on the CFRep dataset, achieving faster-than-real-time execution (real-time factor (RTF) < 1). When the proposed caching strategy is enabled, the system achieves up to 3.36x and 15.91x speedups on resource-constrained edge device compared to the non-caching baseline for pre-recorded and live-streaming scenarios, respectively. These results show that KD-Judge enables transparent, efficient, and scalable rule-grounded rep-level analysis that can complement human judging in practice.

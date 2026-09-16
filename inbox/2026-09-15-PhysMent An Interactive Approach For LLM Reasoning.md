---
interest: medium
link: https://arxiv.org/abs/2609.13152
next_step: skim
priority: high
slack_ts: '1789532920.413269'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'PhysMent: An Interactive Approach For LLM Reasoning In Physics Problems'
---
# PhysMent: An Interactive Approach For LLM Reasoning In Physics Problems
> 原文: [https://arxiv.org/abs/2609.13152](https://arxiv.org/abs/2609.13152)

arXiv:2609.13152v1 Announce Type: new
Abstract: Large language models (LLMs) perform strongly on static science benchmarks, yet their ability to reason about the physical world through active experimentation remains poorly understood. We introduce PhysMent, a benchmark that evaluates LLM physical reasoning via iterative, toolmediated interaction with a MuJoCo physics simulator. Unlike static benchmarks that supply all quantities upfront, PhysMent requires models to discover information by applying forces, querying object states, advancing time, and modifying scene geometry before answering. The benchmark comprises 105 scenes of classical mechanics, organized across four difficulty regimes (Easy/Hard and Single/Multi), three scene modalities (standard, object creation, hidden objects), and a scene-manipulation category, evaluated with a six-dimensional scoring framework. Results show that current models perform reasonably well on qualitative single-concept tasks (up to 80% accuracy) but degrade substantially on quantitative tasks that demand precise, multi-step experimental procedures: most models fall below 30% on the hardest single-concept category, where the bottleneck is procedural (adaptive multi-step tool use) rather than conceptual load. Across the seven models, accuracy ranges from 25% to 67%, with failures due to premature answer submission, inefficient exploration, and inconsistent grounding in simulator feedback rather than conceptual gaps.

---
interest: medium
link: https://arxiv.org/abs/2606.30704
next_step: skim
priority: high
slack_ts: '1782880930.514159'
source: cs.LG - Machine Learning
status: unread
title: 'From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators'
---
# From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators
> 原文: [https://arxiv.org/abs/2606.30704](https://arxiv.org/abs/2606.30704)

arXiv:2606.30704v1 Announce Type: new
Abstract: Large language models (LLMs) excel across a wide range of tasks, yet their instance-specific solutions often lack the structural consistency needed for reliable deployment. Workflows that encode recurring algorithmic patterns at the task level provide a principled framework, offering robustness across instance variations, interpretable traces for debugging, and reusability across problem instances. However, manually designing such workflows requires significant expertise and effort, limiting their broader application. While automatic workflow generation could address this bottleneck, existing methods either produce instance-specific solutions without learning task-level patterns, or cannot generalize beyond their training configurations. We present MetaFlow, which casts workflow generation as a meta-learning problem: given a task and an operator set, the model learns to compose solution strategies. MetaFlow trains in two stages: supervised fine-tuning on synthetic workflow data, followed by reinforcement learning with verifiable rewards (RLVR) that uses execution feedback across problem instances in the task to improve end-to-end success. The resulting model produces effective workflows for trained tasks and exhibits strong generalization to untrained tasks and novel operator sets. Across benchmarks in question answering, code generation, and mathematical reasoning, MetaFlow achieves performance comparable to state-of-the-art baselines on in-domain tasks with single inference, while demonstrating remarkable zero-shot generalization capabilities on out-of-domain tasks and operator sets.

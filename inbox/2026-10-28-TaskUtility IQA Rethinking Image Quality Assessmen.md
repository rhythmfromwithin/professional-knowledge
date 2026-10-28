---
title: "Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.35905
priority: medium
status: unread
interest: medium
next_step: skim
---
# Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks
> 原文: [https://arxiv.org/abs/2610.35905](https://arxiv.org/abs/2610.35905)

arXiv:2610.35905v1 Announce Type: new
Abstract: Image quality assessment (IQA) underpins embodied imaging pipelines by judging whether visual quality satisfies downstream tasks, yet most existing methods learn task-agnostic scores aligned with generic human ratings on static benchmarks. This objective mismatches embodied and interactive settings, where image adequacy depends on task goals, context, and action requirements that shape an agent's decisions. We argue that IQA should shift from score regression to goal-conditioned judgment defined by embodied task utility. To this end, we propose an MLLM-based embodied IQA agent framework that reasons about task requirements, grounds quality evidence, and produces decision-facing assessments. A compact VisDrone evidence study shows that conventional perceptual metrics and generic MLLM-based IQA scores are weak proxies for downstream VLM task success, while a task-conditioned utility score better predicts whether visual input supports the target task. These findings support a task-utility-oriented reframing of IQA for embodied, explainable, and decision-aware visual perception.

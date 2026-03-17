---
title: "Task-Specific Knowledge Distillation via Intermediate Probes"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.12270
priority: high
status: unread
interest: medium
next_step: skim
---
# Task-Specific Knowledge Distillation via Intermediate Probes
> 原文: [https://arxiv.org/abs/2603.12270](https://arxiv.org/abs/2603.12270)

arXiv:2603.12270v1 Announce Type: new
Abstract: Knowledge distillation from large language models (LLMs) assumes that the teacher's output distribution is a high-quality training signal. On reasoning tasks, this assumption is frequently violated. A model's intermediate representations may encode the correct answer, yet this information is lost or distorted through the vocabulary projection, where prompt formatting and answer-token choices creates brittle, noisy outputs.
We introduce \method{}, a distillation framework that bypasses this bottleneck by training lightweight probes on frozen teacher hidden states and using the probe's predictions, rather than output logits, as supervision for student training. This simple change yields consistent improvements across four reasoning benchmarks (AQuA-RAT, ARC Easy/Challenge, and MMLU), with gains most pronounced under limited data.
Probes trained on intermediate representations provide cleaner labels than the teacher's own outputs, effectively denoising the distillation signal. \method{} requires no architectural changes to student or teacher, is architecture-agnostic, and adds minimal compute since probe training is cheap and teacher representations can be cached. By exploiting internal representations, \method{} enables practitioners to extract more value from large teacher models without additional training data or architectural complexity.

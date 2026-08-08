---
interest: medium
link: https://arxiv.org/abs/2608.05217
next_step: skim
priority: low
slack_ts: '1786154719.411979'
source: cs.CR - Cryptography and Security
status: unread
title: A Survey of Adversarial Efficiency Degradation for Vision Transformer by Exploiting
  Input-adaptive Optimization
---
# A Survey of Adversarial Efficiency Degradation for Vision Transformer by Exploiting Input-adaptive Optimization
> 原文: [https://arxiv.org/abs/2608.05217](https://arxiv.org/abs/2608.05217)

arXiv:2608.05217v1 Announce Type: new
Abstract: Vision Transformers (ViTs) increasingly rely on input-adaptive inference, such as token pruning and early halting, to meet energy and latency budgets. This survey examines a recent class of adversarial efficiency degradation attacks that target these mechanisms to increase computation without necessarily degrading accuracy. We unify and compare two representative attacks, SlowFormer (a universal adversarial patch) and DeSparsify (per-image perturbations), across three popular token-pruning frameworks: A-ViT, ATS, and AdaViT. We standardize reporting using GFLOPs, accuracy loss, and an Attack Success (AS) metric that measures how much of the model's compute savings the attack takes away. Understanding these attacks is crucial for designing countermeasures that not only mitigate risk but also remain lightweight, since deployment often occurs in low-power settings such as mobile or embedded devices. To organize our analysis, we focus on three questions: how input-adaptive optimizations (e.g., token pruning and early halting) create attack surfaces for efficiency degradation; how such attacks operate in practice and which optimizations are most vulnerable; and which defenses exist today and whether they meaningfully restore efficiency under attack.

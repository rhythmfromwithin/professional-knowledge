---
title: "Few-Shot Degradation Is Not What It Seems: Behavioral Evidence, Representation Analysis, and a Random-Text Control Across 12 Models, 2 Tasks, and 2 Architectures"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2609.15990
priority: high
status: unread
interest: medium
next_step: skim
---
# Few-Shot Degradation Is Not What It Seems: Behavioral Evidence, Representation Analysis, and a Random-Text Control Across 12 Models, 2 Tasks, and 2 Architectures
> 原文: [https://arxiv.org/abs/2609.15990](https://arxiv.org/abs/2609.15990)

arXiv:2609.15990v1 Announce Type: new
Abstract: Few-shot prompting sometimes degrades language models instead of helping them, but why this happens is unknown. We evaluate 12 open-weight models on two Ukrainian tasks news classification and legal case outcome prediction and find that the effect is strongly task-dependent: the same models that gain +24 pp on news show only +3.4 pp on legal text, with two models degrading. To understand why, we look inside the models. Prior work measures how much hidden states shift between zero-shot and few-shot modes, but few-shot prompts are much longer, and that length difference alone moves representations. We propose a simple fix: replace demonstrations with length-matched random text to measure the shift caused by prompt length, then subtract it. The resulting metric content delta isolates how much the model's representations change because of what the demonstrations say, not how long they are. This changes the picture entirely: raw shift does not predict whether few-shot helps or hurts (r = 0.20), but content delta does (rho = +0.65, p = 0.043). Models that restructure representations more from demonstration content benefit more the opposite of the intuitive "distortion" explanation. Masking demonstrations in Llama 3.3 70B confirms the finding causally, recovering accuracy above the zero-shot baseline.

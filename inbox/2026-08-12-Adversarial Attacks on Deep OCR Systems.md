---
interest: medium
link: https://arxiv.org/abs/2608.07636
next_step: skim
priority: low
slack_ts: '1786501795.514649'
source: cs.CR - Cryptography and Security
status: unread
title: Adversarial Attacks on Deep OCR Systems
---
# Adversarial Attacks on Deep OCR Systems
> 原文: [https://arxiv.org/abs/2608.07636](https://arxiv.org/abs/2608.07636)

arXiv:2608.07636v1 Announce Type: new
Abstract: Deep-OCR (DeepSeek-OCR) advances document recognition by treating the visual modality as an optical compression medium, enabling long-context OCR at low token cost. However, its increased complexity may introduce new security vulnerabilities. In this paper, we present, to the best of our knowledge, the first pure black-box adversarial attack against a generative OCR vision-language model, where only the decoded string can be queried and no gradients, logits, or model internals are available. We recast the attack as a zeroth-order optimization problem driven by a bounded scalar loss defined directly on the string output via sequence similarity, and estimate the gradient with a random-direction finite-difference scheme whose query cost is independent of the image dimension. An Adam update with ell\_infinity projection yields imperceptible perturbations for both untargeted and targeted objectives. Pilot experiments on Deep-OCR validate the string-only attack and evaluation pipeline and expose severe qualitative decoder failures, including repetition, truncation, and prompt leakage. They also show that controlled targeted rewriting remains substantially harder than untargeted degradation; we avoid claiming targeted success until the pre-registered evaluation is complete.

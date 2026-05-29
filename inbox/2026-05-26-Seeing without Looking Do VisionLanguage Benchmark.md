---
interest: medium
link: https://arxiv.org/abs/2605.22903
next_step: skim
priority: medium
slack_ts: '1780028370.912309'
source: cs.CV - Computer Vision
status: unread
title: 'Seeing without Looking: Do Vision-Language Benchmarks Really Test Vision?'
---
# Seeing without Looking: Do Vision-Language Benchmarks Really Test Vision?
> 原文: [https://arxiv.org/abs/2605.22903](https://arxiv.org/abs/2605.22903)

arXiv:2605.22903v1 Announce Type: new
Abstract: Benchmark accuracy is often implicitly assumed to reflect grounded visual understanding in vision-language models (VLMs), yet it remains unclear to what extent such scores truly reflect reliance on visual evidence. Motivated by a surprising observation that removing a substantial fraction of image tokens only degrades model performance very slightly on a widely used hallucination benchmark, we systematically investigate this mismatch in a set of open-source VLMs. Our analysis spans multiple levels of granularity, spanning global visual degradation, localized occlusion, question reformulation, answer-space expansion, and decision-level analyses beyond standard accuracy. We further complement these behavioral results with a layer-wise analysis of vision-token geometry. Throughout the experiments, we find that although VLMs do incorporate visual input, their predictions are less sensitive to the loss of fine-grained visual evidence that standard accuracy should have suggested. Even when the final prediction remains unchanged, the model's internal support for the correct answer may already be weakened. We further complement a representation-level analysis, which shows increasing similarity among visual tokens in deeper layers, providing a possible explanation for our findings. Together, these results suggest that current benchmarks are not sufficient to reliably evaluate fine-grained visual grounding in VLMs.

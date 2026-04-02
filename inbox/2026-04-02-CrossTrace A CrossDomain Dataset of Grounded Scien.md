---
title: "CrossTrace: A Cross-Domain Dataset of Grounded Scientific Reasoning Traces for Hypothesis Generation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.28924
priority: high
status: unread
interest: medium
next_step: skim
---
# CrossTrace: A Cross-Domain Dataset of Grounded Scientific Reasoning Traces for Hypothesis Generation
> 原文: [https://arxiv.org/abs/2603.28924](https://arxiv.org/abs/2603.28924)

arXiv:2603.28924v1 Announce Type: new
Abstract: Scientific hypothesis generation is a critical bottleneck in accelerating research, yet existing datasets for training and evaluating hypothesis-generating models are limited to single domains and lack explicit reasoning traces connecting prior knowledge to novel contributions. I introduce CrossTrace, a dataset of 1,389 grounded scientific reasoning traces spanning biomedical research (518), AI/ML (605), and cross-domain work (266). Each trace captures the structured reasoning chain from established knowledge through intermediate logical steps to a novel hypothesis, with every step grounded in source paper text. I define an Input/Trace/Output schema that extends the Bit-Flip-Spark framework of HypoGen with step-level verification, a taxonomy of eight discovery patterns, and multi-domain coverage. Fine-tuning Qwen2.5-7B-Instruct on CrossTrace via QLoRA yields substantial improvements over the untuned baseline: IAScore rises from 0.828 to 0.968 (GPT-4o judge) and from 0.716 to 0.888 (Claude Opus 4.5), structural compliance improves from 0% to 100%, and spark cosine similarity increases from 0.221 to 0.620. Balanced cross-domain training (biomedical + AI/ML + CS) outperforms single-domain training, providing evidence that scientific reasoning patterns transfer across disciplines. Human validation of 150 stratified records confirms 99.7% step-level grounding accuracy and a 0.0% fabrication rate. To my knowledge, CrossTrace is the first large-scale, cross-domain dataset with step-level grounded reasoning traces for hypothesis generation, and my results demonstrate that such traces are an effective training signal whose benefits are at least partially domain-general.

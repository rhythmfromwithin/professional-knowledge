---
interest: medium
link: https://arxiv.org/abs/2607.09885
next_step: skim
priority: high
slack_ts: '1784172049.937379'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Index SLM Technical Report
---
# Index SLM Technical Report
> 原文: [https://arxiv.org/abs/2607.09885](https://arxiv.org/abs/2607.09885)

arXiv:2607.09885v1 Announce Type: new
Abstract: We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 trillion predominantly Chinese and English tokens; Index-1.9B-Pure, a control variant trained with an identical recipe but with all instruction-like data strictly filtered from the corpus; Index-1.9B-Chat, aligned from the base model with supervised fine-tuning and direct preference optimization; and Index-1.9B-Character, which augments the chat model with retrieval-augmented generation for few-shot role-playing customization. Pre-training employs a Warmup-Stable-Decay learning-rate schedule in which the concentration of curated data is raised substantially during the decay phase, together with a Norm-Head output layer that stabilizes training under large learning rates. On a suite of standard benchmarks covering examination, reasoning, mathematics, and code, Index-1.9B-Base attains an average score of 64.92, competitive with or exceeding open models of several times its size. We further report controlled studies on model depth, learning-rate magnitude and scheduling, the interaction between learning-rate decay and data quality, and the effect of including instruction data during pre-training, and we document an unexplained surge in benchmark performance midway through the constant-learning-rate phase. All models, together with evaluation code, are released at https://github.com/bilibili/Index-1.9B.

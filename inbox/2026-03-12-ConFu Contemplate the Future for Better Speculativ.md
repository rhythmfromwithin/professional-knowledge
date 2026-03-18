---
interest: medium
link: https://arxiv.org/abs/2603.08899
next_step: skim
priority: high
slack_ts: '1773802296.693569'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'ConFu: Contemplate the Future for Better Speculative Sampling'
---
# ConFu: Contemplate the Future for Better Speculative Sampling
> 原文: [https://arxiv.org/abs/2603.08899](https://arxiv.org/abs/2603.08899)

arXiv:2603.08899v1 Announce Type: new
Abstract: Speculative decoding has emerged as a powerful approach to accelerate large language model (LLM) inference by employing lightweight draft models to propose candidate tokens that are subsequently verified by the target model. The effectiveness of this paradigm critically depends on the quality of the draft model. While recent advances such as the EAGLE series achieve state-of-the-art speedup, existing draft models remain limited by error accumulation: they condition only on the current prefix, causing their predictions to drift from the target model over steps. In this work, we propose \textbf{ConFu} (Contemplate the Future), a novel speculative decoding framework that enables draft models to anticipate the future direction of generation. ConFu introduces (i) contemplate tokens and soft prompts that allow the draft model to leverage future-oriented signals from the target model at negligible cost, (ii) a dynamic contemplate token mechanism with MoE to enable context-aware future prediction, and (iii) a training framework with anchor token sampling and future prediction replication that learns robust future prediction. Experiments demonstrate that ConFu improves token acceptance rates and generation speed over EAGLE-3 by 8--11% across various downstream tasks with Llama-3 3B and 8B models. We believe our work is the first to bridge speculative decoding with continuous reasoning tokens, offering a new direction for accelerating LLM inference.

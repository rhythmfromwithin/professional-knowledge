---
interest: medium
link: https://arxiv.org/abs/2609.13478
next_step: skim
priority: low
slack_ts: '1789446772.293139'
source: cs.CR - Cryptography and Security
status: unread
title: 'BadEngram: Backdoor Attack on Gated Memory Components in LLMs'
---
# BadEngram: Backdoor Attack on Gated Memory Components in LLMs
> 原文: [https://arxiv.org/abs/2609.13478](https://arxiv.org/abs/2609.13478)

arXiv:2609.13478v1 Announce Type: new
Abstract: To expand open-weight models' capacity without proportionally increasing computation, recent language models incorporate gated parametric memories that retrieve learned values and inject them into intermediate representations. Despite these efficiency benefits, such modules create a distinct attack surface: their parameters can be modified independently of the backbone while directly shaping its computation. We introduce BadEngram, a post-training attack that exploits this surface to implant persistent, trigger-dependent behavior while leaving conventional backbone weights and the execution graph unchanged. We first establish the attack's feasibility and causally characterize its mechanism in a controlled Engram model, where BadEngram achieves 96.6% ASR on triggered inputs while limiting false activation on matched trigger-free inputs to 0.1% and preserving 99.6% clean accuracy. Replacing the retrieved memory values with their clean counterparts or closing the memory gates reduces ASR to at most 0.32%, confirming that the backdoor is expressed through the gated-memory pathway. We then test whether this vulnerability extends to production scale in Qwen3.8-Flash-Next's native Per-Layer Embedding subsystem. Using independently trained checkpoints for the two benchmarks, BadEngram achieves 50.4% ASR on HarmBench and 60.0% on AdvBench, while dormant-condition ASR remains 0.9% and 0.0%, respectively. These results identify native gated-memory parameters as a security-critical part of the model whose integrity cannot be inferred from an unchanged backbone.

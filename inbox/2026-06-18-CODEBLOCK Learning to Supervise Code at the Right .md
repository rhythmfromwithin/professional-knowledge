---
interest: medium
link: https://arxiv.org/abs/2606.18286
next_step: skim
priority: high
slack_ts: '1781759640.108089'
source: cs.LG - Machine Learning
status: unread
title: 'CODEBLOCK: Learning to Supervise Code at the Right Granularity'
---
# CODEBLOCK: Learning to Supervise Code at the Right Granularity
> 原文: [https://arxiv.org/abs/2606.18286](https://arxiv.org/abs/2606.18286)

arXiv:2606.18286v1 Announce Type: new
Abstract: Supervised fine-tuning of code LLMs typically applies uniform cross-entropy loss to all response tokens, implicitly assuming that every token provides equally useful learning signal. Recent token-level selection methods challenge this assumption in natural-language SFT by supervising only high-value tokens. However, directly transferring token-level masking to code can break syntactically and semantically coherent program units, because code depends on structural completeness and definition-use relations. We therefore propose CodeBlock, a structure-aware sparse supervision framework that selects structure-complete code evidence rather than isolated tokens. CodeBlock first selects high-quality instruction-response pairs, then partitions code responses into syntactically coherent coding items, estimates their utility by aggregating generalized cross-entropy over core logic tokens, and reranks them with data-flow reach and bridge signals to prioritize blocks that propagate or connect important program dependencies. During training, the full response remains available as context, while loss is applied only to selected code items and informative natural-language tokens. Experiments on six code-generation benchmarks show that CodeBlock achieves stronger average pass@1 than full-token SFT and competitive selection baselines, while using only 1.9% of supervised response tokens.

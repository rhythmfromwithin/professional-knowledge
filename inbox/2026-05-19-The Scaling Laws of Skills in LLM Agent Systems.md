---
interest: medium
link: https://arxiv.org/abs/2605.16508
next_step: skim
priority: high
slack_ts: '1779164096.716179'
source: cs.CL - Computation and Language (NLP)
status: unread
title: The Scaling Laws of Skills in LLM Agent Systems
---
# The Scaling Laws of Skills in LLM Agent Systems
> 原文: [https://arxiv.org/abs/2605.16508](https://arxiv.org/abs/2605.16508)

arXiv:2605.16508v1 Announce Type: new
Abstract: As agent systems scale, skills accumulate into large reusable libraries, yet their scaling laws remain poorly understood. Across 15 frontier LLMs, 1,141 real-world skills, and over 3M routing or execution decisions, we identify two coupled laws. Routing law: single-step routing accuracy decays logarithmically with library size ($R^2{>}0.97$ for all models), with errors progressing from local skill competition to cross-family drift and capture by overly general "black-hole skills". Execution law: before state realization, joint routing is approximately multiplicative, whereas correct execution can improve difficult downstream decisions by about $4{\times}$. A single parameter, the routing logarithmic decay slope $b$, couples the two laws: routing-side fits predict execution-side rescue across models, showing that the same library property controls both pre-execution collapse and downstream recoverability. The laws are actionable: law-guided optimization raises held-out routing accuracy from 71.3% to 91.7%, reduces hijack from 22.4% to 4.1%, and transfers directionally to downstream ClawBench and ClawMark execution settings, improving mean pass rate from 49.3% to 61.6% on ClawBench and from 28.4% to 34.5% on ClawMark. These results show that agent performance depends not only on model capability, but also on the structure, granularity, and exposure policy of the skill library.

---
interest: medium
link: https://arxiv.org/abs/2607.01468
next_step: skim
priority: low
slack_ts: '1783136959.955749'
source: cs.DB - Databases
status: unread
title: 'CADENZA in Action: Breaking the Monolith with Intent-Dependent Plan Spaces
  for Semantic Queries'
---
# CADENZA in Action: Breaking the Monolith with Intent-Dependent Plan Spaces for Semantic Queries
> 原文: [https://arxiv.org/abs/2607.01468](https://arxiv.org/abs/2607.01468)

arXiv:2607.01468v1 Announce Type: new
Abstract: Semantic query processing engines execute semantic operators, whose behavior is specified by natural-language intents, via model inference over multimodal data. Most existing optimizers optimize the operators at the granularity of monolithic implementations -- such as LLMs and embedding models -- forcing a trade-off between expensive model calls and cheaper alternatives that fail to capture intent-dependent semantics. We present CADENZA, a semantic operator optimizer that compiles an intent into decomposed steps, selects concrete physical implementations for each step, and tunes their parameters under user-specified quality-latency-cost preferences. In this demonstration, users interact with CADENZA through a web interface over multimodal databases, exploring how an intent is decomposed into alternative plans, how each plan is optimized, and how different preferences yield different winning plans.

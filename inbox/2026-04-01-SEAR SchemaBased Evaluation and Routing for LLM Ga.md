---
interest: medium
link: https://arxiv.org/abs/2603.26728
next_step: skim
priority: low
slack_ts: '1775185057.876029'
source: cs.DB - Databases
status: unread
title: 'SEAR: Schema-Based Evaluation and Routing for LLM Gateways'
---
# SEAR: Schema-Based Evaluation and Routing for LLM Gateways
> 原文: [https://arxiv.org/abs/2603.26728](https://arxiv.org/abs/2603.26728)

arXiv:2603.26728v1 Announce Type: new
Abstract: Evaluating production LLM responses and routing requests across providers in LLM gateways requires fine-grained quality signals and operationally grounded decisions. To address this gap, we present SEAR, a schema-based evaluation and routing system for multi-model, multi-provider LLM gateways. SEAR defines an extensible relational schema covering both LLM evaluation signals (context, intent, response characteristics, issue attribution, and quality scores) and gateway operational metrics (latency, cost, throughput), with cross-table consistency links across around one hundred typed, SQL-queryable columns. To populate the evaluation signals reliably, SEAR proposes self-contained signal instructions, in-schema reasoning, and multi-stage generation that produces database-ready structured outputs. Because signals are derived through LLM reasoning rather than shallow classifiers, SEAR captures complex request semantics, enables human-interpretable routing explanations, and unifies evaluation and routing in a single query layer. Across thousands of production sessions, SEAR achieves strong signal accuracy on human-labeled data and supports practical routing decisions, including large cost reductions with comparable quality.

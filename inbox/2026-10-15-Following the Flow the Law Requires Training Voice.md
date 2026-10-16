---
interest: medium
link: https://arxiv.org/abs/2610.18881
next_step: skim
priority: high
slack_ts: '1792123819.713159'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Following the Flow the Law Requires: Training Voice Agents to Transfer to
  Unseen Regulated Procedures in Debt Collection'
---
# Following the Flow the Law Requires: Training Voice Agents to Transfer to Unseen Regulated Procedures in Debt Collection
> 原文: [https://arxiv.org/abs/2610.18881](https://arxiv.org/abs/2610.18881)

arXiv:2610.18881v1 Announce Type: new
Abstract: Voice agents built on large language models (LLMs) now handle customer calls, but in regulated applications completing the task is not enough: the agent must follow a conversational flow set by law. In debt collection, it must confirm it is speaking to the debtor before mentioning the debt, identify itself and the creditor, state the amount, and avoid prohibited language. Every creditor turns these rules into its own procedure and revises it. We ask whether a small, self-hosted policy can be trained once and then follow regulated procedures it has never seen. One machine-readable specification per deployment, FlowSpec, generates the policy instruction, gates the tools, supplies the supervision and defines the tests; the agent speaks only approved catalogue sentences. We fine-tune a 9-billion-parameter model on 2,506 conversations from 297 randomized procedures and evaluate a Thai outbound-call agent on four unseen deployment procedures (three debt collection, one non-debt), one from a wholly withheld lineage. Documented checks, fixed by the procedure, rise from 67--71 percents to 93--100 percents, while grounded checks, fixed by the conversation, already pass at 97--100 percents before training; scenario pass rate rises from 15/43 to 40/43. An audit of the shared specification finds 11 defects, 3 of which its own metric did not expose.

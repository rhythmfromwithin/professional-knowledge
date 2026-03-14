---
title: "Quality-Driven Agentic Reasoning for LLM-Assisted Software Design: Questions-of-Thoughts (QoT) as a Time-Series Self-QA Chain"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.11082
priority: low
status: unread
interest: medium
next_step: skim
---
# Quality-Driven Agentic Reasoning for LLM-Assisted Software Design: Questions-of-Thoughts (QoT) as a Time-Series Self-QA Chain
> 原文: [https://arxiv.org/abs/2603.11082](https://arxiv.org/abs/2603.11082)

arXiv:2603.11082v1 Announce Type: new
Abstract: Recent advances in large language models (LLMs) have accelerated AI-assisted software development, yet practical deployment remains constrained by incomplete implementations, weak modularization, and inconsistent security practices. We introduce Questions-of-Thoughts (QoT), a quality-driven inference-time scaffold that turns a user goal into (i) an ordered sequence of engineering steps and (ii) stepwise self-questioning to verify constraints and reduce omission errors, while maintaining a lightweight reasoning record that stabilizes subsequent design decisions.
We evaluate QoT across three representative backend engineering domains: API Design, Data Communication, and File Systems. Each task requires multi-module decomposition and exposes standard failure modes in LLM-generated systems. To enable data-driven comparison, we score generated artifacts using an ISO/IEC-inspired quality rubric that measures Scalability, Completeness, Modularity, and Security. We report domain-wise gains as the change in total quality score, defined as the QoT score minus the NoQoT score. Results show capacity-dependent improvements: QoT yields consistent quality improvements for larger models and more complex domains, while smaller models may exhibit trade-offs under tight context and planning budgets.
We release an open artifact with prompts, scoring guidelines, raw generations, and scripts that reproduce the reported tables and figures to support applied AI and data analytics research.

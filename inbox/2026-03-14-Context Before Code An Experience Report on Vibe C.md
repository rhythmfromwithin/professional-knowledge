---
interest: medium
link: https://arxiv.org/abs/2603.11073
next_step: skim
priority: low
slack_ts: '1773974641.579749'
source: cs.SE - Software Engineering
status: unread
title: 'Context Before Code: An Experience Report on Vibe Coding in Practice'
---
# Context Before Code: An Experience Report on Vibe Coding in Practice
> 原文: [https://arxiv.org/abs/2603.11073](https://arxiv.org/abs/2603.11073)

arXiv:2603.11073v1 Announce Type: new
Abstract: Code-generating tools are increasingly used in software development, yet experience reports on conversational "vibe coding" under production constraints remain limited. This paper presents an experience report from a small full-stack team that applied contextual prompting and explicit architectural constraints to build (i) a multi-project agent learning platform designed for sustained, production-oriented use and (ii) an academic retrieval-augmented generation system.
The agent platform supports multiple isolated projects, each with structured memory and background processing, thereby enforcing project-level isolation. The RAG system provides citation-grounded answers, role-based access control, and evaluation tracking.
Across both systems, vibe coding accelerated scaffolding and integration. However, the generated code often under-specified isolation rules and infrastructure constraints when these were not explicitly defined. Consequently, aspects such as multi-tenancy, access control, memory policies, and asynchronous processing required deliberate architectural design and verification. We observe a shift in engineering effort from boilerplate implementation toward constraint specification and enforcement auditing. We also identify recurring architectural "non-delegation zones" where conversational code generation remains insufficient for production reliability.

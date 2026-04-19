---
interest: medium
link: https://arxiv.org/abs/2604.14590
next_step: skim
priority: medium
slack_ts: '1776569840.910719'
source: cs.DC - Distributed Computing
status: unread
title: 'AgileLog: A Forkable Shared Log for Agents on Data Streams'
---
# AgileLog: A Forkable Shared Log for Agents on Data Streams
> 原文: [https://arxiv.org/abs/2604.14590](https://arxiv.org/abs/2604.14590)

arXiv:2604.14590v1 Announce Type: new
Abstract: In modern data-streaming systems, alongside traditional programs, a new type of entity has emerged that can interact with streaming data: AI agents. Unlike traditional programs, AI agents use LLM reasoning to accomplish high-level tasks specified in natural language over streaming data. Unfortunately, current streaming systems cannot fully support agents: they lack the fundamental mechanisms to avoid the performance interference caused by agentic tasks and to safely handle agentic writes. We argue that the shared log, the core abstraction underlying streaming data, must support creating forks of itself, and that such a forkable shared log serves as a great substrate for agents acting on streaming data. We propose AgileLog, a new shared log abstraction that provides novel forking primitives for agentic use cases. We design Bolt, an implementation of the AgileLog abstraction, that uses novel techniques to make forks cheap, and provide logical and performance isolation.

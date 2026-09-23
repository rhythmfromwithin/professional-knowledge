---
title: "AkasicMEM: Governed Enterprise Memory for Agents"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.25563
priority: low
status: unread
interest: medium
next_step: skim
---
# AkasicMEM: Governed Enterprise Memory for Agents
> 原文: [https://arxiv.org/abs/2609.25563](https://arxiv.org/abs/2609.25563)

arXiv:2609.25563v1 Announce Type: new
Abstract: Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge. Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle. These requirements interact when information from enterprise sources persists in memory. As this information is repeatedly derived and reused under changing principals and policies, source restrictions may be bypassed, resulting in information leakage. Preventing such leakage requires authorization continuity, under which source restrictions remain effective throughout source-to-memory and memory-to-memory derivation and reuse. Existing approaches address these concerns individually, but do not treat source--memory integration, memory governance, and authorization continuity as combined core design targets across the memory lifecycle. We define Governed Enterprise Memory as agent memory designed around this combined scope and present AkasicMEM as its realization. AkasicMEM realizes authorization continuity through transitive lineage, policy composition during memory formation, and policy re-evaluation during retrieval. It is built on GraphAI's AkasicDB, a unified vector--graph--relational database whose storage and execution substrate enables the underlying operations of these mechanisms to be jointly optimized and executed.

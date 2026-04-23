---
interest: medium
link: https://arxiv.org/abs/2604.16339
next_step: skim
priority: high
slack_ts: '1776915192.388259'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise
  Multi-Agent LLM Systems'
---
# Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems
> 原文: [https://arxiv.org/abs/2604.16339](https://arxiv.org/abs/2604.16339)

arXiv:2604.16339v1 Announce Type: new
Abstract: Multi-agent large language model (LLM) systems are rapidly emerging as the dominant architecture for enterprise AI automation, yet production deployments exhibit failure rates between 41% and 86.7%, with nearly 79% of failures originating from specification and coordination issues rather than model capability limitations. This paper identifies Semantic Intent Divergence--the phenomenon whereby cooperating LLM agents develop inconsistent interpretations of shared objectives due to siloed context and absent process models--as a primary yet formally unaddressed root cause of multi-agent failure in enterprise settings. We propose the Semantic Consensus Framework (SCF), a process-aware middleware comprising six components: a Process Context Layer for shared operational semantics, a Semantic Intent Graph for formal intent representation, a Conflict Detection Engine for real-time identification of contradictory, contention-based, and causally invalid intent combinations, a Consensus Resolution Protocol using a policy--authority--temporal hierarchy, a Drift Monitor for detecting gradual semantic divergence, and a Process-Aware Governance Integration layer for organizational policy enforcement. Evaluation across 600 runs spanning three multi-agent frameworks (AutoGen, CrewAI, LangGraph) and four enterprise scenarios demonstrates that SCF is the only approach to achieve 100% workflow completion--compared to 25.1% for the next-best baseline--while detecting 65.2% of semantic conflicts with 27.9% precision and providing complete governance audit trails. The framework is protocol-agnostic and compatible with MCP and A2A communication standards.

---
interest: medium
link: https://arxiv.org/abs/2608.20481
next_step: skim
priority: low
slack_ts: '1787622058.198179'
source: cs.CR - Cryptography and Security
status: unread
title: 'AEGIS: Preventing Cross-Domain Resource Abuse in MCP'
---
# AEGIS: Preventing Cross-Domain Resource Abuse in MCP
> 原文: [https://arxiv.org/abs/2608.20481](https://arxiv.org/abs/2608.20481)

arXiv:2608.20481v1 Announce Type: new
Abstract: The Model Context Protocol (MCP) is an open source JSON-RPC protocol that standardizes how large language models (LLMs) interact with external systems through programmatic functions known as tools. Attackers or malicious agents can exploit certain modalities of these MCP tools to degrade the overall quality of service of agent-based applications. For example, an agent may request an excessively large search radius or very long videos, overloading backend systems and potentially causing slowdowns or denial-of-service. Each modality including text, images, video, and location introduces distinct vectors for resource abuse, complicating the development of consistent mitigation strategies. Moreover, multimodal and crossdomain tools expose diverse request schemas and parameters, making it difficult to define policies that are both generalizable and precise enough to enforce meaningful resource constraints. In this paper, we present AEGIS, a policy enforcement component that enables administrators to define fine-grained safeguards against resource abuse across heterogeneous MCP tools and modalities. AEGIS leverages the reasoning capabilities of large language models to analyze, categorize, and normalize diverse tool invocations into a unified, policy-friendly representation accessible to security practitioners. Integrated with the Open Policy Agent and the ContextForge AI Gateway, AEGIS detects and mitigates abusive behaviors while preserving the flexibility of MCP-based agent ecosystems.

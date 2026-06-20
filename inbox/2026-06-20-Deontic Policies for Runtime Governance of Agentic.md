---
interest: medium
link: https://arxiv.org/abs/2606.19464
next_step: skim
priority: high
slack_ts: '1781930799.738389'
source: cs.AI - Artificial Intelligence
status: unread
title: Deontic Policies for Runtime Governance of Agentic AI Systems
---
# Deontic Policies for Runtime Governance of Agentic AI Systems
> 原文: [https://arxiv.org/abs/2606.19464](https://arxiv.org/abs/2606.19464)

arXiv:2606.19464v1 Announce Type: new
Abstract: Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. This includes specifying what agents are permitted and prohibited from doing, what they areobliged to do after certain actions (e.g., notify the CISO), under what conditions a standing obligation may be waived, and which rules take precedence when policies conflict. This governance problem exceeds what current policy engines provide. Systems such as XACML, Rego, and Cedar address only the permit/prohibit subset of this governance structure. They do not provide obligation lifecycle management, meta-policy conflict resolution, dispensations that waive obligations in specific circumstances, and ontological reasoning over domain class hierarchies commonly found in applications such as healthcare, cybersecurity, or data privacy. We propose AgenticRei, which realizes key governance requirements such as obligations, dispensations, policy conflict resolutions, and reasoning over policies, as well as the basic permit/prohibit constraints. We use a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language) and evaluated at runtime by a high-performance logic engine entirely outside the LLM. The same pipeline governs both tool invocations by the agent and agent-to-agent messages. We show through examples that deontic policies capture governance constraints around security and privacy that mostly cannot be expressed in current production engines. Our approach composes naturally with industry-standard frameworks like A2AS.

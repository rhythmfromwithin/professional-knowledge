---
interest: medium
link: https://arxiv.org/abs/2609.00052
next_step: skim
priority: low
slack_ts: '1788408224.079459'
source: cs.CR - Cryptography and Security
status: unread
title: 'AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes'
---
# AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes
> 原文: [https://arxiv.org/abs/2609.00052](https://arxiv.org/abs/2609.00052)

arXiv:2609.00052v1 Announce Type: new
Abstract: Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs. All existing audits decide backbone identity from the text-output channel, which is structurally fragile for agentic APIs because modern serving stacks (OpenAI, Anthropic, Gemini, Cloudflare Workers AI, LangGraph) discard text and expose only structured actions when the model calls a tool, and provider-injected system prompts can distort text distributions enough that text-channel tests falsely accuse honest providers of substituting the claimed model. We observe that recent agentic post-training internalizes tool-use directly into the weights, opening a new audit channel that the serving stack still exposes and that is largely invariant to deployment context. We introduce Agentic Provenance (AgentProv), the first action-based identity audit for agentic LLM APIs: AgentProv fingerprints a deployed model through its categorical tool-call distribution and decides identity via an MMD permutation test. AgentProv catches every substituted model (100% on 630 evaluated checkpoint pairs), while holding the false-positive rate under system-prompt injection at 7% (vs. 67% for MET and 53% for RUT). On third-party API endpoints, AgentProv's disagreements with MET are consistent with an independent token-count side-channel that detects provider-injected system prompts.

---
title: "MCPGuard: Finding Conformance Gaps in MCP SDKs via Dual-Track Analysis and Dynamic Adjudication"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2611.03662
priority: high
status: unread
interest: medium
next_step: skim
---
# MCPGuard: Finding Conformance Gaps in MCP SDKs via Dual-Track Analysis and Dynamic Adjudication
> 原文: [https://arxiv.org/abs/2611.03662](https://arxiv.org/abs/2611.03662)

arXiv:2611.03662v1 Announce Type: new
Abstract: The Model Context Protocol (MCP) connects large language model agents to external tools and services through official SDKs that implement message validation and session logic. Specification constraints omitted by these SDKs may propagate to downstream applications, highlighting the importance of SDK-level conformance testing. Yet existing MCP conformance tools mainly exercise running endpoints and reveal little about whether SDK models enforce specification requirements. We present MCPGuard, an automated LLM-based framework for detecting specification-to-SDK conformance gaps. Its structural track aligns JSON Schema constraints with normalized SDK models and produces constraint-specific evidence. Its behavioral track extracts normative prose rules, retrieves bounded function-level slices, and audits them with LLMs for candidate omissions. An evidence-aware dynamic adjudicator then inspects complete source context and builds PoCs to validate candidates. A shared kernel with language-specific adapters enables analysis across SDKs. On the official Python 1.26.0 and TypeScript 1.29.0 SDKs, MCPGuard confirms 13 and 19 findings, respectively, none of which are exposed by two black-box baselines. Tests on open MCP servers further show that these gaps can systematically propagate downstream. By making SDK conformance of specification constraints directly testable, MCPGuard complements conventional endpoint-oriented conformance suites.

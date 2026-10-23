---
title: "MCP vs CLI for AI Agents: A Comparative Analysis of Tool Integration Strategies for Autonomous Systems"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.30157
priority: high
status: unread
interest: medium
next_step: skim
---
# MCP vs CLI for AI Agents: A Comparative Analysis of Tool Integration Strategies for Autonomous Systems
> 原文: [https://arxiv.org/abs/2610.30157](https://arxiv.org/abs/2610.30157)

arXiv:2610.30157v1 Announce Type: new
Abstract: AI agents require interfaces to interact with external systems such as files, APIs, databases, and cloud services. Two competing paradigms have emerged: CLI (Command Line Interface), where agents execute shell commands directly, and MCP (Model Context Protocol), a structured JSON-RPC protocol providing governed, typed tool access. This paper presents a comparative analysis across 14 evaluation dimensions, supported by worked examples, security assessment against established compliance frameworks, and economic modeling. Our analysis indicates that CLI provides superior efficiency for single-user, local-only workflows, while MCP addresses requirements that CLI fundamentally cannot satisfy, including fine-grained access control, credential isolation, structured audit, and multi-tenant governance. We further examine how progressive disclosure techniques eliminate MCP's historical weakness (context window overhead), yielding token efficiency comparable to CLI while preserving its architectural benefits. A hybrid architecture is recommended for production systems. This analysis draws upon academic, government, and industry sources including NSA formal guidance (CSI U/OO/6030316-26), OWASP security standards, and economic modeling from BCG and Gartner.

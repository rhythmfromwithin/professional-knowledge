---
interest: medium
link: https://arxiv.org/abs/2611.23234
next_step: skim
priority: low
slack_ts: '1795243595.249379'
source: cs.SE - Software Engineering
status: unread
title: 'Tracing the Messy Middle: A Runtime Transaction Schema for AI Coding Agents'
---
# Tracing the Messy Middle: A Runtime Transaction Schema for AI Coding Agents
> 原文: [https://arxiv.org/abs/2611.23234](https://arxiv.org/abs/2611.23234)

arXiv:2611.23234v1 Announce Type: new
Abstract: AI coding agents are increasingly integrated into software development, yet the field lacks a systematic feedback loop to improve their behavior in practice. Artifact datasets capture final outputs such as code patches, commits, and benchmark outcomes, but omit the messy middle of the development lifecycle: the failed retries, fallback strategies, routing decisions, and abandoned sessions that determine operational cost, reliability, and productivity.
We propose an observability framework that captures these runtime behaviors as structured transaction records, enabling engineering coaching grounded in behavioral evidence, workflow optimization at the stages where tasks break down, and routing policy iteration measured by total task cost rather than per-request price. We define the runtime transaction schema this architecture requires and demonstrate initial feasibility through Agent Token Manager (Atm), a local-first prototype that reconciles gateway records and transcript evidence without exposing prompt content to external collectors. Finally, we identify three open research problems that must be solved to scale these feedback mechanisms: trace reconciliation without shared request identifiers, outcome linking across asynchronous systems, and intervention causality. Treating the linkage between sessions and artifacts as a fundamental infrastructure requirement provides a structured foundation for understanding and optimizing agent behavior.

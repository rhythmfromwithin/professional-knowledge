---
interest: medium
link: https://arxiv.org/abs/2605.12694
next_step: skim
priority: low
slack_ts: '1778817948.326559'
source: cs.SE - Software Engineering
status: unread
title: 'Agentic Interpretation: Lattice-Structured Evidence for LLM-Based Program
  Analysis'
---
# Agentic Interpretation: Lattice-Structured Evidence for LLM-Based Program Analysis
> 原文: [https://arxiv.org/abs/2605.12694](https://arxiv.org/abs/2605.12694)

arXiv:2605.12694v1 Announce Type: new
Abstract: Large language models can consult information that fixed static analyzers cannot, such as documentation, current security advisories, version-specific metadata, and informal API contracts. This makes LLMs a compelling option for program analyses that depend on information beyond the source program, or that are otherwise not amenable to conventional static analyzers. However, directly asking an LLM for a one-shot whole-program analysis is brittle because it compresses many evidence-dependent judgments into a single opaque answer, rather than exposing which conclusions are supported or disputed and using intermediate findings to guide later, more focused searches. In this paper, we propose agentic interpretation, a framework that brings the discipline of lattice-based static analysis to LLM-driven program reasoning. At a high level, agentic interpretation decomposes a high-level analysis goal into localized claims, and tracks the LLM's judgment about each claim in a finite-height lattice. A worklist algorithm governs how claims and their judgments evolve during the analysis. We introduce a formal model of agentic interpretation, explore the design space it opens, and illustrate the approach with a worked example analyzing code that depends on opaque third-party components.

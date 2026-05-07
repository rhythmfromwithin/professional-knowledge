---
interest: medium
link: https://arxiv.org/abs/2605.03117
next_step: skim
priority: low
slack_ts: '1778125808.374289'
source: cs.SE - Software Engineering
status: unread
title: 'ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault
  Localization and Program Repair'
---
# ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair
> 原文: [https://arxiv.org/abs/2605.03117](https://arxiv.org/abs/2605.03117)

arXiv:2605.03117v1 Announce Type: new
Abstract: Repository-level fault localization (FL) and automated program repair (APR) require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization. We present ARISE (Agentic Repository-level Issue Solving Engine), which augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest. We evaluate on SWE-bench Lite (300 real GitHub issues, 11 Python repositories) using Qwen2.5-Coder-32B-Instruct as the backbone. Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points. These localization gains translate directly into repair success, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent. Controlled ablations confirm that the improvement is driven by the data-flow graph rather than the tool schema, and that large code models consume structured slice output directly without requiring a natural-language summarization layer. The graph builder and slicing API are designed as a framework-agnostic, drop-in toolset for future APR research.

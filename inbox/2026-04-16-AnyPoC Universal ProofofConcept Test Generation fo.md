---
title: "AnyPoC: Universal Proof-of-Concept Test Generation for Scalable LLM-Based Bug Detection"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.11950
priority: low
status: unread
interest: medium
next_step: skim
---
# AnyPoC: Universal Proof-of-Concept Test Generation for Scalable LLM-Based Bug Detection
> 原文: [https://arxiv.org/abs/2604.11950](https://arxiv.org/abs/2604.11950)

arXiv:2604.11950v1 Announce Type: new
Abstract: While recent LLM-based agents can identify many candidate bugs in source code, their reports remain static hypotheses that require manual validation, limiting the practicality of automated bug detection. We frame this challenge as a test generation task: given a candidate report, synthesizing an executable proof-of-concept test, or simply a PoC - such as a script, command sequence, or crafted input - to trigger the suspected defect. Automated PoC generation can act as a scalable validation oracle, enabling end-to-end autonomous bug detection by providing concrete execution evidence. However, naive LLM agents are unreliable validators: they are biased toward "success" and may reward-hack by producing plausible but non-functional PoCs or even hallucinated traces. To address this, we present AnyPoC, a general multi-agent framework that (1) analyzes and fact-checks a candidate bug report, (2) iteratively synthesizes and executes a PoC while collecting execution traces, and (3) independently re-executes and scrutinizes the PoC to mitigate hallucination and reward hacking. In addition, AnyPoC also continuously extracts and evolves a PoC knowledge base to handle heterogeneous tasks. AnyPoC operates on candidate bug reports regardless of their source and can be paired with different bug reporters. To demonstrate practicality and generality, we apply AnyPoC, with a simple agentic bug reporter, on 12 critical software systems across diverse languages/domains (many with millions of lines of code) including Firefox, Chromium, LLVM, OpenSSL, SQLite, FFmpeg, and Redis. Compared to the state-of-the-art coding agents, e.g., Claude Code and Codex, AnyPoC produces 1.3x more valid PoCs for true-positive bug reports and rejects 9.8x more false-positive bug reports. To date, AnyPoC has discovered 122 new bugs (105 confirmed, 86 already fixed), with 45 generated PoCs adopted as official regression tests.

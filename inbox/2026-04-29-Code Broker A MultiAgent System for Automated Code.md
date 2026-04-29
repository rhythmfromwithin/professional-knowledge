---
interest: medium
link: https://arxiv.org/abs/2604.23088
next_step: skim
priority: low
slack_ts: '1777434594.158169'
source: cs.SE - Software Engineering
status: unread
title: 'Code Broker: A Multi-Agent System for Automated Code Quality Assessment'
---
# Code Broker: A Multi-Agent System for Automated Code Quality Assessment
> 原文: [https://arxiv.org/abs/2604.23088](https://arxiv.org/abs/2604.23088)

arXiv:2604.23088v1 Announce Type: new
Abstract: We present Code Broker, a multi agent system built with Google Agent Development Kit ADK that analyses Python code from files, local directories, or GitHub repositories and generates actionable quality assessment reports. The system employs a hierarchical five agents architecture in which a root orchestrator coordinates a sequential pipeline agent, which in turn dispatches three specialised agents in parallel a Correctness Assessor, a Style Assessor, and a Description Generator before synthesising findings through an Improvement Recommender. Reports score four dimensions correctness, security, style, and maintainability and are rendered in both Markdown and HTML. Code Broker combines LLM based reasoning with deterministic static-analysis signals from Pylint, uses asynchronous execution with retry logic to improve robustness, and explores lightweight session memory for retaining and querying prior assessment context. We position the paper as a technical report on system design and prompt or tool orchestration, and present a preliminary qualitative evaluation on representative Python codebases. The results suggest that parallel specialised agents produce readable, developer oriented feedback, while also highlighting current limitations in evaluation depth, security tooling, large repository handling, and the current use of only in memory persistence. All code and reproducibility materials are available at: https://github.com/Samir-atra/agents\_intensive\_dev.

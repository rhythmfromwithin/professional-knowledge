---
interest: medium
link: https://arxiv.org/abs/2605.04050
next_step: skim
priority: high
slack_ts: '1778385534.471499'
source: cs.AI - Artificial Intelligence
status: unread
title: 'LCM: Lossless Context Management'
---
# LCM: Lossless Context Management
> 原文: [https://arxiv.org/abs/2605.04050](https://arxiv.org/abs/2605.04050)

arXiv:2605.04050v1 Announce Type: new
Abstract: We introduce Lossless Context Management (LCM), a deterministic architecture for LLM memory that outperforms Claude Code on long-context tasks. When benchmarked using Opus 4.6, our LCM-augmented coding agent, Volt, achieves higher scores than Claude Code on the OOLONG long-context eval, including at every context length between 32K and 1M tokens.
LCM may be considered both a vindication and extension of the recursive paradigm pioneered by Recursive Language Models (RLMs). Our results demonstrate that recursive context manipulation can outperform not just conventional LLMs, but frontier coding agents with native file-system access.
LCM departs from RLM by decomposing symbolic recursion into two deterministic, engine-managed mechanisms: recursive context compression, in which a hierarchical summary DAG automatically compacts older messages while retaining lossless pointers to every original; and recursive task partitioning, in which engine-managed parallel primitives like LLM-Map replace model-written loops. This trade-off, analogous to the move from GOTO to structured control flow in program-ming language design, sacrifices maximal flexibility for termination guarantees, zero-cost continuity on short tasks, and lossless retrievability of all prior state.

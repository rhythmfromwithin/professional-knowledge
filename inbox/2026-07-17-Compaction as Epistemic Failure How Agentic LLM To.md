---
interest: medium
link: https://arxiv.org/abs/2607.13071
next_step: skim
priority: low
slack_ts: '1784344398.849949'
source: cs.SE - Software Engineering
status: unread
title: 'Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed
  Results from Killed Processes'
---
# Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes
> 原文: [https://arxiv.org/abs/2607.13071](https://arxiv.org/abs/2607.13071)

arXiv:2607.13071v1 Announce Type: new
Abstract: Agentic LLM coding tools compress long session histories into compaction summaries that subsequent sessions inherit as ground truth. This paper documents a failure mode in Claude Code where partial standard output from timed-out commands (exit code 143) is recorded in compaction summaries as confirmed results, propagating false positives across sessions and model versions without re-verification. The underlying mechanism is a conflation of observation and persistence, where information that appeared in the terminal is treated as equivalent to information written to durable storage. This finding extends the analysis of LLM self-evaluation failures reported in prior work on non-determinism in LLM-as-judge grading by showing that agentic tools exhibit analogous reliability deficits when reporting on their own operational outcomes. The failure has direct implications for any workflow that relies on agentic session continuity for data processing, scientific computation, or multi-step automation.

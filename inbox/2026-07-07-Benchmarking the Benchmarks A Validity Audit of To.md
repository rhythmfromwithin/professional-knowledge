---
interest: medium
link: https://arxiv.org/abs/2607.02577
next_step: skim
priority: low
slack_ts: '1783397053.161409'
source: cs.SE - Software Engineering
status: unread
title: 'Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation'
---
# Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation
> 原文: [https://arxiv.org/abs/2607.02577](https://arxiv.org/abs/2607.02577)

arXiv:2607.02577v1 Announce Type: new
Abstract: Tool-calling benchmarks are increasingly used to rank language-model agents, yet their scores are often treated as ground truth without validating the evaluators themselves. We present a systematic validity and reproducibility audit of four major tool-calling benchmark families: BFCL v4, {\tau}2-Bench, LiveMCPBench, and MCP-Atlas. Across 496 expert-reviewed benchmark tasks, we find 92 evaluator-human disagreements, corresponding to an 18.5% misalignment rate. The failures are not isolated annotation mistakes: deterministic benchmarks exhibit brittle state matching, trajectory lock-in, incorrect ground truths, substring-based communication failures, and reward-basis misalignment, while LLM-judge benchmarks exhibit rubric drift, hallucinated completion, answer-only scoring, and substantial run-to-run variance. In LiveMCPBench, 23 repeated evaluations of the same setup produce scores ranging from 57.9% to 76.8%, a spread of 18.9 percentage points, large enough to change leaderboard conclusions. These results show that current tool-calling scores can reflect evaluator artifacts rather than agent capability. We introduce a unified taxonomy of tool-calling evaluation failures, release trace-level audit artifacts and corrected evaluation components, and argue for decomposed metrics that separately measure tool invocation, task completion, and outcome verification. Our findings suggest that progress in tool-using agents requires benchmarks whose evaluators are themselves reproducible, auditable, and aligned with human judgments of task success. We further introduce Tool-Veritas, a configurable benchmark that combines deterministic state verification with optional qualitative judging, and Harness Lab, an open-source system for benchmark execution, trace inspection, repeated-run comparison, and evaluator debugging.

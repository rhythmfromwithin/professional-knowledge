---
interest: medium
link: https://arxiv.org/abs/2604.04979
next_step: skim
priority: low
slack_ts: '1775791742.804059'
source: cs.SE - Software Engineering
status: unread
title: 'Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents'
---
# Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents
> 原文: [https://arxiv.org/abs/2604.04979](https://arxiv.org/abs/2604.04979)

arXiv:2604.04979v1 Announce Type: new
Abstract: Coding agents repeatedly consume long tool observations even though only a small fraction of each observation matters for the next step. We study task-conditioned tool-output pruning: given a focused query and one tool output, return the smallest verbatim evidence block the agent should inspect next. We introduce a benchmark of 11,477 examples built from SWE-bench repository interactions and synthetic multi-ecosystem tool outputs, with a manually curated 618-example test set. We fine-tune Qwen 3.5 2B with LoRA and compare it against larger zero-shot models and heuristic pruning baselines. Our model reaches 0.86 recall and 0.80 F1 while removing 92% of input tokens, outperforming zero-shot Qwen 3.5 35B A3B by 11 recall points and all heuristic baselines by a wide margin.

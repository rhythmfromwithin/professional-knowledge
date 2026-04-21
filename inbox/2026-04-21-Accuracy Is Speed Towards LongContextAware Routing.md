---
interest: medium
link: https://arxiv.org/abs/2604.15732
next_step: skim
priority: medium
slack_ts: '1776742299.001769'
source: cs.DC - Distributed Computing
status: unread
title: 'Accuracy Is Speed: Towards Long-Context-Aware Routing for Distributed LLM
  Serving'
---
# Accuracy Is Speed: Towards Long-Context-Aware Routing for Distributed LLM Serving
> 原文: [https://arxiv.org/abs/2604.15732](https://arxiv.org/abs/2604.15732)

arXiv:2604.15732v1 Announce Type: new
Abstract: Distributed LLM serving systems optimize per-request latency and throughput. However, under long-context workloads, inference accuracy becomes more variable. When incorrect responses trigger retries, accuracy directly translates into cumulative user-visible delay that is not captured by single-shot latency metrics.
In this work, we argue that under long-context serving, \textbf{accuracy becomes speed} through retry dynamics. We introduce \textit{Time-to-Correct-Answer (TTCA)}, a metric that measures the wall-clock time required to obtain the first correct response. Our measurement study shows that prompt characteristics such as length and language amplify accuracy variance, which inflates TTCA. We demonstrate \textit{Lightweight Accuracy-Aware Routing (LAAR)}, a capability-based routing design that reduces TTCA. Our results suggest that in long-context distributed serving, accuracy should be treated as a first-class systems objective.

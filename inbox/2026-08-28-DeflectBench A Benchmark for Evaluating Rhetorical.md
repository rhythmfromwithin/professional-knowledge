---
interest: medium
link: https://arxiv.org/abs/2608.26119
next_step: skim
priority: high
slack_ts: '1787986067.549259'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'DeflectBench: A Benchmark for Evaluating Rhetorical Fallacy Generation in
  LLMs'
---
# DeflectBench: A Benchmark for Evaluating Rhetorical Fallacy Generation in LLMs
> 原文: [https://arxiv.org/abs/2608.26119](https://arxiv.org/abs/2608.26119)

arXiv:2608.26119v1 Announce Type: new
Abstract: Whether large language models can be prompted to generate rhetorical fallacies on demand, and whether current safety post-training constrains this behavior, has received less attention than the related question of detecting fallacies in existing text. We close this gap with DeflectBench, evaluating 23,990 generations from four frontier models across three deflection strategies (whataboutism, ad hominem, red herring), seven prompt framings, and 80 claims spanning four controversy levels. Refusal is governed primarily by request structure rather than claim content. Per claim refusal varies by only 11 percentage points across the 80 claims, while a single prompt frame change can swing within model refusal by nearly 100 percentage points and switching the requested fallacy type can swing it by over 80 percentage points within explicit framings. An educational debate coach prompt framing collapses refusal to near zero across all four model families, but the bypassed behavior is not clean compliance. Models typically produce labeled compliance, naming the requested manipulation in the same response that contains it. The four models distribute differently across refusal, labeled compliance, soft refusal, and clean compliance. The code and dataset are released at https://github.com/ArtKanke/DeflectBench.

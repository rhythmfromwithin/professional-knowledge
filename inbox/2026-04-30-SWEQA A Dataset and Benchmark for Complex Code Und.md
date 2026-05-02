---
interest: medium
link: https://arxiv.org/abs/2604.24814
next_step: skim
priority: low
slack_ts: '1777692898.659809'
source: cs.SE - Software Engineering
status: unread
title: 'SWE-QA: A Dataset and Benchmark for Complex Code Understanding'
---
# SWE-QA: A Dataset and Benchmark for Complex Code Understanding
> 原文: [https://arxiv.org/abs/2604.24814](https://arxiv.org/abs/2604.24814)

arXiv:2604.24814v1 Announce Type: new
Abstract: In this paper, we introduce SWE-QA, a text and code corpus aimed at benchmarking multi-hop code comprehension, addressing the gap between simplified evaluation tasks and the complex reasoning required in real-world software development. While existing code understanding benchmarks focus on isolated snippets, developers must routinely connect information across multiple dispersed code segments. The dataset comprises 9,072 multiple-choice questions systematically generated from 12 Python repositories of SWE-bench, evaluating several recurrent reasoning patterns like Declaration-and-Call questions that link entity definitions to their usage, and Interacting-Entity questions that examine the dynamic relationships among multiple collaborating components. Generated through parsing-based entity extraction and Large Language Model assisted question construction with carefully validated distractors, the benchmark distinguishes genuine comprehension from superficial pattern matching. Evaluation of 15 language models (360M to 671B parameters) reveals significant challenges in multi-hop reasoning, with best performance reaching 74.41% accuracy. Dense architectures consistently outperform mixture-of-experts models by 10-14 percentage points, while reasoning-enhanced variants show inconsistent benefits.

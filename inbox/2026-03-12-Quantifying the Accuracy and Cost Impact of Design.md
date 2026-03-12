---
title: "Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.08877
priority: high
status: unread
interest: medium
next_step: skim
---
# Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search
> 原文: [https://arxiv.org/abs/2603.08877](https://arxiv.org/abs/2603.08877)

arXiv:2603.08877v1 Announce Type: new
Abstract: Agentic Retrieval-Augmented Generation (RAG) systems combine iterative search, planning prompts, and retrieval backends, but deployed settings impose explicit budgets on tool calls and completion tokens. We present a controlled measurement study of how search depth, retrieval strategy, and completion budget affect accuracy and cost under fixed constraints. Using Budget-Constrained Agentic Search (BCAS), a model-agnostic evaluation harness that surfaces remaining budget and gates tool use, we run comparisons across six LLMs and three question-answering benchmarks. Across models and datasets, accuracy improves with additional searches up to a small cap, hybrid lexical and dense retrieval with lightweight re-ranking produces the largest average gains in our ablation grid, and larger completion budgets are most helpful on HotpotQA-style synthesis. These results provide practical guidance for configuring budgeted agentic retrieval pipelines and are accompanied by reproducible prompts and evaluation settings.

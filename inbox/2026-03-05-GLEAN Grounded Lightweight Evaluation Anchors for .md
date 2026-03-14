---
interest: medium
link: https://arxiv.org/abs/2603.02212
next_step: skim
priority: low
slack_ts: '1773456088.252519'
source: cs.DB - Databases
status: unread
title: 'GLEAN: Grounded Lightweight Evaluation Anchors for Contamination-Aware Tabular
  Reasoning'
---
# GLEAN: Grounded Lightweight Evaluation Anchors for Contamination-Aware Tabular Reasoning
> 原文: [https://arxiv.org/abs/2603.02212](https://arxiv.org/abs/2603.02212)

arXiv:2603.02212v1 Announce Type: new
Abstract: Tabular reasoning benchmarks mix semantic inference, numerical computation, and brittle table formatting, yet evaluations for small models remain vulnerable to contamination, dataset artifacts, and retrieval failures. We propose GLEAN, a lightweight evaluation protocol that integrates contamination-aware probes, weak-supervision governance, retrieval-reasoning diagnostics, and structured error attribution under tight hardware constraints. We evaluate across TabFact, WTQ via Squall, TableBench, RobuT, and SciTab under a 16GB GPU budget. Using Squall gold SQL as an executable anchor (95.2% execution), GLEAN assigns a deterministic error taxonomy (L0-L4 plus L0.5 context miss) and reveals a stable error-mode separation: TAPEX errors skew toward grounding (L3) while TAPAS errors skew toward hallucination/abstention (L2/L0). We validate evidence-row heuristics against SQL-derived rows on simple queries (0.62 precision / 0.71 recall; hybrid recall 0.81) and show that retrieval Recall@K can saturate even when end-to-end EM/F1 remains limited, motivating attribution beyond raw recall. We release a modular framework with audits and sensitivity checks to make small-model tabular evaluation more contamination-aware and diagnostic.

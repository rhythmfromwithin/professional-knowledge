---
interest: medium
link: https://arxiv.org/abs/2604.02382
next_step: skim
priority: low
slack_ts: '1775531918.626999'
source: cs.SE - Software Engineering
status: unread
title: 'Ambig-IaC: Multi-level Disambiguation for Interactive Cloud Infrastructure-as-Code
  Synthesis'
---
# Ambig-IaC: Multi-level Disambiguation for Interactive Cloud Infrastructure-as-Code Synthesis
> 原文: [https://arxiv.org/abs/2604.02382](https://arxiv.org/abs/2604.02382)

arXiv:2604.02382v1 Announce Type: new
Abstract: The scale and complexity of modern cloud infrastructure have made Infrastructure-as-Code (IaC) essential for managing deployments. While large Language models (LLMs) are increasingly being used to generate IaC configurations from natural language, user requests are often underspecified. Unlike traditional code generation, IaC configurations cannot be executed cheaply or iteratively repaired, forcing the LLMs into an almost one-shot regime. We observe that ambiguity in IaC exhibits a tractable compositional structure: configurations decompose into three hierarchical axes (resources, topology, attributes) where higher-level decisions constrain lower-level ones. We propose a training-free, disagreement-driven framework that generates diverse candidate specifications, identifies structural disagreements across these axes, ranks them by informativeness, and produces targeted clarification questions that progressively narrow the configuration space. We introduce \textsc{Ambig-IaC}, a benchmark of 300 validated IaC tasks with ambiguous prompts, and an evaluation framework based on graph edit distance and embedding similarity. Our method outperforms the strongest baseline, achieving relative improvements of +18.4\% and +25.4\% on structure and attribute evaluations, respectively.

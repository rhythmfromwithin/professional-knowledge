---
interest: medium
link: https://arxiv.org/abs/2607.01366
next_step: skim
priority: high
slack_ts: '1783136958.476139'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Auto-FL-Research: Agentic Search for Federated Learning Algorithms'
---
# Auto-FL-Research: Agentic Search for Federated Learning Algorithms
> 原文: [https://arxiv.org/abs/2607.01366](https://arxiv.org/abs/2607.01366)

arXiv:2607.01366v1 Announce Type: new
Abstract: Federated learning (FL) research often depends on many small but consequential algorithmic choices: optimizer variants, server aggregation rules, local training schedules, normalization, regularization, and model architecture. These choices are expensive to explore manually and difficult to compare fairly when candidate changes can also alter the FL training or evaluation path. In this work, we present Auto-FL-Research (AFR), a constrained coding-agent workflow for FL algorithmic recipe search. Agents may propose and implement candidate training algorithms, including server aggregation rules, client update schedules, local objectives, and registered model variants, while task profiles fix the mutation surface, compute budget, communication contract, and final model evaluation. Each campaign records candidate scores, runtime, edited files, artifacts, and failure status. We evaluate AFR on five healthcare cross-silo FLamby tasks and on grouped-client profiles for the five fixed LEAF datasets plus the LEAF synthetic task. Five-seed repeat evaluations support gains on four FLamby tasks and five of six LEAF profiles, while also exposing seed-sensitive and search-selected failure cases. Same-budget controls show that several gains correspond to FL-recipe changes, whereas other improvements are recovered by fixed-surface scalar controls or fail under repeat or held-out evaluation. These mixed outcomes are part of the contribution: they show how agent-generated candidates can be separated into repeated FL mechanisms, fixed-surface tuning effects, and selected single-run artifacts.

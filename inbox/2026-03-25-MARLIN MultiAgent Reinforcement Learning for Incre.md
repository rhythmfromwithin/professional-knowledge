---
title: "MARLIN: Multi-Agent Reinforcement Learning for Incremental DAG Discovery"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.20295
priority: high
status: unread
interest: medium
next_step: skim
---
# MARLIN: Multi-Agent Reinforcement Learning for Incremental DAG Discovery
> 原文: [https://arxiv.org/abs/2603.20295](https://arxiv.org/abs/2603.20295)

arXiv:2603.20295v1 Announce Type: new
Abstract: Uncovering causal structures from observational data is crucial for understanding complex systems and making informed decisions. While reinforcement learning (RL) has shown promise in identifying these structures in the form of a directed acyclic graph (DAG), existing methods often lack efficiency, making them unsuitable for online applications. In this paper, we propose MARLIN, an efficient multi agent RL based approach for incremental DAG learning. MARLIN uses a DAG generation policy that maps a continuous real valued space to the DAG space as an intra batch strategy, then incorporates two RL agents state specific and state invariant to uncover causal relationships and integrates these agents into an incremental learning framework. Furthermore, the framework leverages a factored action space to enhance parallelization efficiency. Extensive experiments on synthetic and real datasets demonstrate that MARLIN outperforms state of the art methods in terms of both efficiency and effectiveness.

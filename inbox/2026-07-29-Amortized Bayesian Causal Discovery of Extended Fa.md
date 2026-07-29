---
title: "Amortized Bayesian Causal Discovery of Extended Factor Graphs"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.22934
priority: medium
status: unread
interest: medium
next_step: skim
---
# Amortized Bayesian Causal Discovery of Extended Factor Graphs
> 原文: [https://arxiv.org/abs/2607.22934](https://arxiv.org/abs/2607.22934)

arXiv:2607.22934v1 Announce Type: new
Abstract: Learning causal graphs from interventional data is a challenging problem with broad applications. In molecular biology, for example, a central goal is to uncover gene regulatory networks from large-scale perturbation data. An ideal algorithm for this task should scale to thousands of nodes, incorporate interventions even when their targets are unknown, quantify uncertainty, and provide identifiability guarantees. However, existing approaches---e.g. approaches using score-based optimization or approximate Bayesian inference---often fail to meet all of these criteria. To address these limitations, we develop Amortized Bayesian Causal Discovery of Extended Factor Graphs (ABCDEFG). Our method guarantees exact acyclicity, scales to graphs with thousands of nodes, and naturally handles interventions even when their targets are unknown. Additionally, ABCDEFG estimates a posterior distribution whose maximum a posteriori estimate provably identifies the true causal graph up to an equivalence class. On simulated datasets, ABCDEFG achieves state-of-the-art accuracy, producing a well-calibrated posterior distribution while outperforming previous score-based and approximate Bayesian methods. Applied to large-scale single-cell perturbation data, ABCDEFG identifies both established and novel gene targets of growth factors.

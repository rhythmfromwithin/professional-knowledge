---
title: "Near-Equivalent Q-learning Policies for Dynamic Treatment Regimes"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.19440
priority: medium
status: unread
interest: medium
next_step: skim
---
# Near-Equivalent Q-learning Policies for Dynamic Treatment Regimes
> 原文: [https://arxiv.org/abs/2603.19440](https://arxiv.org/abs/2603.19440)

arXiv:2603.19440v1 Announce Type: new
Abstract: Precision medicine aims to tailor therapeutic decisions to individual patient characteristics. This objective is commonly formalized through dynamic treatment regimes, which use statistical and machine learning methods to derive sequential decision rules adapted to evolving clinical information. In most existing formulations, these approaches produce a single optimal treatment at each stage, leading to a unique decision sequence. However, in many clinical settings, several treatment options may yield similar expected outcomes, and focusing on a single optimal policy may conceal meaningful alternatives. We extend the Q-learning framework for retrospective data by introducing a worst-value tolerance criterion controlled by a hyperparameter $\varepsilon$, which specifies the maximum acceptable deviation from the optimal expected value. Rather than identifying a single optimal policy, the proposed approach constructs sets of $\varepsilon$-optimal policies whose performance remains within a controlled neighborhood of the optimum. This formulation shifts Q-learning from a vector-valued representation to a matrix-valued one, allowing multiple admissible value functions to coexist during backward recursion. The approach yields families of near-equivalent treatment strategies and explicitly identifies regions of treatment indifference where several decisions achieve comparable outcomes. We illustrate the framework in two settings: a single-stage problem highlighting indifference regions around the decision boundary, and a multi-stage decision process based on a simulated oncology model describing tumor size and treatment toxicity dynamics.

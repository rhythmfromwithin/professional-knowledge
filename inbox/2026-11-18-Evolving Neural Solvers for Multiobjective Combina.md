---
title: "Evolving Neural Solvers for Multi-objective Combinatorial Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2611.22060
priority: low
status: unread
interest: medium
next_step: skim
---
# Evolving Neural Solvers for Multi-objective Combinatorial Optimization
> 原文: [https://arxiv.org/abs/2611.22060](https://arxiv.org/abs/2611.22060)

arXiv:2611.22060v1 Announce Type: new
Abstract: Multi-objective combinatorial optimization (MOCO) seeks high-quality solutions that represent different trade-offs among conflicting objectives. Existing neural methods typically train a dedicated model for each preference or condition a single model on different preferences. Training dedicated models becomes more costly as the number of preferences increases, while a shared model can produce duplicate solutions for different preferences, limiting the benefit of denser preference queries. We propose the Evolving Neural Solver (ENS), which trains only a small set of preference-specific models and takes advantage of evolutionary computation to evolve them into a diverse collection of solvers for better solution quality and Pareto front coverage. ENS first trains a model at an estimated knee-point preference to target a balanced compromise, then obtains the remaining initial models through parameter transfer toward the extremes, so as to preliminarily approximate the Pareto front. It then evolves these models to find more candidates that can generate non-dominated solutions through evolution strategies. Experimental results on classic MOCO problems show that ENS outperforms state-of-the-art neural MOCO methods in terms of hypervolume in most evaluated settings.

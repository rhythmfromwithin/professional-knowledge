---
title: "Yukthi Opus: A Multi-Chain Hybrid Metaheuristic for Large-Scale NP-Hard Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2601.01832
priority: low
status: unread
interest: medium
next_step: skim
---
# Yukthi Opus: A Multi-Chain Hybrid Metaheuristic for Large-Scale NP-Hard Optimization
> 原文: [https://arxiv.org/abs/2601.01832](https://arxiv.org/abs/2601.01832)

arXiv:2601.01832v3 Announce Type: replace
Abstract: We present Yukthi Opus (YO), a multi-chain hybrid metaheuristic designed for NP-hard optimization under explicit evaluation budget constraints. YO integrates three complementary mechanisms in a structured two-phase architecture: Markov Chain Monte Carlo (MCMC) for global exploration, greedy local search for exploitation, and simulated annealing with adaptive reheating to enable controlled escape from local minima. A dedicated burn-in phase allocates evaluations to probabilistic exploration, after which a hybrid optimization loop refines promising candidates. YO further incorporates a spatial blacklist mechanism to avoid repeated evaluation of poor regions and a multi-chain execution strategy to improve robustness and reduce sensitivity to initialization.
We evaluate YO on three benchmarks: the Rastrigin function (5D) with ablation studies, the Traveling Salesman Problem with 50 to 200 cities, and the Rosenbrock function (5D) with comparisons against established optimizers including CMA-ES, Bayesian optimization, and accelerated particle swarm optimization. Results show that MCMC exploration and greedy refinement are critical for solution quality, while simulated annealing and multi-chain execution primarily improve stability and variance reduction. Overall, YO achieves competitive performance on large and multimodal problems while maintaining predictable evaluation budgets, making it suitable for expensive black-box optimization settings.

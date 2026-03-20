---
interest: medium
link: https://arxiv.org/abs/2603.12528
next_step: skim
priority: low
slack_ts: '1773974668.765399'
source: cs.DB - Databases
status: unread
title: Weighted Set Multi-Cover on Bounded Universe and Applications in Package Recommendation
---
# Weighted Set Multi-Cover on Bounded Universe and Applications in Package Recommendation
> 原文: [https://arxiv.org/abs/2603.12528](https://arxiv.org/abs/2603.12528)

arXiv:2603.12528v1 Announce Type: new
Abstract: The weighted set multi-cover problem is a fundamental generalization of set cover that arises in data-driven applications where one must select a small, low-cost subset from a large collection of candidates under coverage constraints. In data management settings, such problems arise naturally either as expressive database queries or as post-processing steps over query results, for example, when selecting representative or diverse subsets from large relations returned by database queries for decision support, recommendation, fairness-aware data selection, or crowd-sourcing. While the general weighted set multi-cover problem is NP-complete, many practical workloads involve a \emph{bounded universe} of items that must be covered, leading to the Weighted Set Multi-Cover with Bounded Universe (WSMC-BU) problem, where the universe size is constant. In this paper, we develop exact and approximation algorithms for WSMC-BU. We first discuss a dynamic programming algorithm that solves WSMC-BU exactly in $O(n^{\ell+1})$ time, where $n$ is the number of input sets and $\ell=O(1)$ is the universe size. We then present a $2$-approximation algorithm based on linear programming and rounding, running in $O(\mathcal{L}(n))$ time, where $\mathcal{L}(n)$ denotes the complexity of solving a linear program with $O(n)$ variables. To further improve efficiency for large datasets, we propose a faster $(2+\varepsilon)$-approximation algorithm with running time $O(n \log n + \mathcal{L}(\log W))$, where $W$ is the ratio of the total weight to the minimum weight, and $\varepsilon$ is an arbitrary constant specified by the user. Extensive experiments on real and synthetic datasets demonstrate that our methods consistently outperform greedy and standard LP-rounding baselines in both solution quality and runtime, making them suitable for data-intensive selection tasks over large query outputs.

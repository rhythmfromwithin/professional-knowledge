---
interest: medium
link: https://arxiv.org/abs/2603.12560
next_step: skim
priority: low
slack_ts: '1774148043.601039'
source: cs.DB - Databases
status: unread
title: Towards Output-Optimal Uniform Sampling and Approximate Counting for Join-Project
  Queries
---
# Towards Output-Optimal Uniform Sampling and Approximate Counting for Join-Project Queries
> 原文: [https://arxiv.org/abs/2603.12560](https://arxiv.org/abs/2603.12560)

arXiv:2603.12560v1 Announce Type: new
Abstract: Uniform sampling and approximate counting are fundamental primitives for modern database applications, ranging from query optimization to approximate query processing. While recent breakthroughs have established optimal sampling and counting algorithms for full join queries, a significant gap remains for join-project queries, which are ubiquitous in real-world workloads. The state-of-the-art ``propose-and-verify'' framework \cite{chen2020random} for these queries suffers from fundamental inefficiencies, often yielding prohibitive complexity when projections significantly reduce the output size.
In this paper, we present the first asymptotically optimal algorithms for fundamental classes of join-project queries, including matrix, star, and chain queries. By leveraging a novel rejection-based sampling strategy and a hybrid counting reduction, we achieve polynomial speedups over the state of the art. We establish the optimality of our results through matching communication complexity lower bounds, which hold even against algebraic techniques like fast matrix multiplication. Finally, we delineate the theoretical limits of the problem space. While matrix and star queries admit efficient sublinear-time algorithms, we establish a significantly stronger lower bound for chain queries, demonstrating that sublinear algorithms are impossible in general.

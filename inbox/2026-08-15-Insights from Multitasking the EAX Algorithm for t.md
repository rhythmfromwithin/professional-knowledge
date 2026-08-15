---
title: "Insights from Multi-tasking the EAX Algorithm for the Travelling Salesperson Problem"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.12772
priority: low
status: unread
interest: medium
next_step: skim
---
# Insights from Multi-tasking the EAX Algorithm for the Travelling Salesperson Problem
> 原文: [https://arxiv.org/abs/2608.12772](https://arxiv.org/abs/2608.12772)

arXiv:2608.12772v1 Announce Type: new
Abstract: Evolutionary multitasking allows several related problems to be solved in a single run of an algorithm. In this paper, we investigate integrating evolutionary multitasking with Edge Assembly Crossover (MT-EAX) to solve the classical Travelling Salesperson Problem (TSP). To fairly compare MT-EAX against standard EAX under strict compute budgets, we evaluate three scaling methods: generation scaling, population scaling, and balanced scaling. Our results show that generationally scaled MT-EAX is highly effective compute-wise in the early stages of the search, saving $60\%$ to $90\%$ of compute for equal or better solution quality. We observe that instance geometry has a significant impact, with clustered, normally distributed instances securing larger improvements than uniformly distributed ones. However, when scaling by population or utilising explicit solution transfer, the results are negative due to population starvation and incompatible cross-instance parent selection. We demonstrate that the advantage of MT-EAX derives from increased diversity through parallel search in early generations, which can be successfully preserved using a decoupled configuration to often strictly outperform or match standard EAX performance at final convergence.

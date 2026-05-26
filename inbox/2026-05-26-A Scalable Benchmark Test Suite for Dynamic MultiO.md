---
title: "A Scalable Benchmark Test Suite for Dynamic Multi-Objective Optimization with a Changing Number of Objectives"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.25785
priority: low
status: unread
interest: medium
next_step: skim
---
# A Scalable Benchmark Test Suite for Dynamic Multi-Objective Optimization with a Changing Number of Objectives
> 原文: [https://arxiv.org/abs/2605.25785](https://arxiv.org/abs/2605.25785)

arXiv:2605.25785v1 Announce Type: new
Abstract: Dynamic multi-objective optimization with a changing number of objectives has recently attracted increasing attention due to its relevance to real-world problems whose evaluation criteria may evolve over time. However, existing benchmark test suites for this problem setting suffer from a fundamental limitation: when the number of objectives changes, the objective functions themselves also change implicitly. This makes it difficult to isolate and evaluate an algorithm's capability to handle dynamics in the number of objectives alone. In this paper, we analyze this issue in detail and show that several theoretical properties claimed in prior studies rely on an assumption that is violated by commonly used test suites. To address this problem, we propose a scalable benchmark test suite in which the objective functions are fixed throughout the optimization process, while the number of active objectives changes over time. Our benchmark is constructed by defining a maximum-objective problem and dynamically selecting subsets of objectives. To avoid degeneracy issues in classical DTLZ and WFG problems, we adopt Minus-DTLZ and Minus-WFG formulations, in which all objectives are mutually conflicting. Extensive benchmark studies using representative algorithms from the literature demonstrate the usefulness and flexibility of the proposed test suite.

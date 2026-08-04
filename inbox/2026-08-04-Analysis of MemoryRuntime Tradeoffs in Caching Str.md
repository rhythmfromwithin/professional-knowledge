---
title: "Analysis of Memory-Runtime Trade-offs in Caching Strategies for Genetic Programming Symbolic Regression"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.29116
priority: low
status: unread
interest: medium
next_step: skim
---
# Analysis of Memory-Runtime Trade-offs in Caching Strategies for Genetic Programming Symbolic Regression
> 原文: [https://arxiv.org/abs/2607.29116](https://arxiv.org/abs/2607.29116)

arXiv:2607.29116v1 Announce Type: new
Abstract: Genetic Programming Symbolic Regression (GPSR) generates mathematical expressions to model input-output relationships using an evolutionary process. A significant challenge in GPSR lies in the repeated evaluation of entire expressions or their sub-expression, which inflates computational runtime. To address this inefficiency, caching mechanisms have been employed to reduce redundant computations. However, prior studies predominantly employ a single caching strategy, offering limited insights into their comparative performance or memory-runtime trade-offs. In this paper, we present a comprehensive analysis of caching mechanisms for GPSR on synthetic and real-world datasets. We also include an empirical study of key-value usage frequencies under an infinitely large cache, offering insights into optimal cache sizing. Furthermore, we provide actionable guidelines for configuring caching strategies based on computational and memory constraints. Our findings indicate that complex caching mechanisms necessitate a minimum cache size to achieve computational time reductions. Conversely, lightweight caching strategies, such as Least Recently Used (LRU) and, notably, First-In-First-Out (FIFO), can significantly decrease computation time for fitness evaluations, which are a substantial component of the overall runtime.

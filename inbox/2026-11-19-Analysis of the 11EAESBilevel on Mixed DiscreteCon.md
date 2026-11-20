---
interest: medium
link: https://arxiv.org/abs/2611.24251
next_step: skim
priority: low
slack_ts: '1795157492.779409'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Analysis of the (1+1)-EA-ES-Bilevel on Mixed Discrete-Continuous Optimization
  Problems with Interactions
---
# Analysis of the (1+1)-EA-ES-Bilevel on Mixed Discrete-Continuous Optimization Problems with Interactions
> 原文: [https://arxiv.org/abs/2611.24251](https://arxiv.org/abs/2611.24251)

arXiv:2611.24251v1 Announce Type: new
Abstract: Mixed discrete-continuous optimization problems can pose challenges -- especially for previous integrated approaches -- when interactions cause beneficial discrete changes to be rejected before sufficient continuous adjustment. We introduce ProximityOneMax as a simple benchmark with pairwise discrete-continuous interactions. On this function, we prove an exponential lower bound on the expected time for the (1+1)-EA-ES-Integrated to reach the target accuracy when initialized near a continuous optimum for a suboptimal discrete configuration with a sufficiently small step size. Experiments show frequent entries into such states from random initialization. We introduce the (1+1)-EA-ES-Bilevel, which uses an upper-level (1+1)-EA to optimize discrete variables and a lower-level (1+1)-ES to optimize continuous variables for each fixed discrete offspring before selection. For several interaction benchmarks and sufficiently small target values $\epsilon > 0$ that require an optimal discrete configuration, using fixed continuous initialization and a suitable fixed budget per lower-level call, we prove that the expected number of fitness evaluations to reach objective value at most $\epsilon$ is $\Theta(n\_d \cdot \log n\_d \cdot n\_c \cdot \log(R/\sqrt{\epsilon}))$, where $n\_d$ is the number of discrete variables, $n\_c$ is the number of continuous variables, and $R$ bounds the distances from the fixed continuous starting point to all relevant continuous optima for fixed discrete configurations.

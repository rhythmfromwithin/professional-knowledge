---
interest: medium
link: https://arxiv.org/abs/2604.06976
next_step: skim
priority: low
slack_ts: '1775791746.143639'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Anytime Analysis on BinVal: Adaptive Parameters Help'
---
# Anytime Analysis on BinVal: Adaptive Parameters Help
> 原文: [https://arxiv.org/abs/2604.06976](https://arxiv.org/abs/2604.06976)

arXiv:2604.06976v1 Announce Type: new
Abstract: While most theoretical run time analyses of discrete randomized search heuristics provide bounds on the expected number of evaluations to find the global optimum, we consider the anytime performance of evolutionary and estimation-of-distribution algorithms. For this purpose, we analyze the fixed-target run time of various algorithms using BinVal as fitness function and bound the run time to optimize the most significant $k \in o(n)$ bits of a bit string with length $n$. We analyze the run times such that they hold not only for a fixed $k$, but simultaneously for all $k \in o(n)$.
For the standard (1+1) EA with fixed mutation rate $1/n$, we show that the fixed-target run time for all $k \in o(n)$ is in $\Theta(n \log k)$. Using an EDA instead, we get an expected number of evaluations of $\Theta(k \log n)$ for the sig-cGA. Replacing in the standard (1+1) EA the fixed mutation rate with a self-adjusting rate, we show that the fixed-target run time for $k \in o(n)$ and a constant $\varepsilon >0$ arbitrarily close to zero is in $\mathcal{O}\left(k^{1+\varepsilon}\right)$ for this algorithm. In particular, this run time is independent of $n$, holds simultaneously for all $k \in o(n)$, and is close to the run time of $\Theta(k \log k)$ for the (1+1) EA with the best fixed mutation rate if $k$ is known.

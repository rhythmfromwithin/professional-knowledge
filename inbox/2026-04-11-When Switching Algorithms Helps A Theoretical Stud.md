---
interest: medium
link: https://arxiv.org/abs/2604.07473
next_step: skim
priority: low
slack_ts: '1776051539.081399'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'When Switching Algorithms Helps: A Theoretical Study of Online Algorithm Selection'
---
# When Switching Algorithms Helps: A Theoretical Study of Online Algorithm Selection
> 原文: [https://arxiv.org/abs/2604.07473](https://arxiv.org/abs/2604.07473)

arXiv:2604.07473v1 Announce Type: new
Abstract: Online algorithm selection (OAS) aims to adapt the optimization process to changes in the fitness landscape and is expected to outperform any single algorithm from a given portfolio. Although this expectation is supported by numerous empirical studies, there are currently no theoretical results proving that OAS can yield asymptotic speedups (apart from some artificial examples for hyper-heuristics). Moreover, theory-based guidelines for when and how to switch between algorithms are largely missing.
In this paper, we present the first theoretical example in which switching between two algorithms -- the $(1+\lambda)$ EA and the $(1+(\lambda,\lambda))$ GA -- solves the OneMax problem asymptotically faster than either algorithm used in isolation. We show that an appropriate choice of population sizes for the two algorithms allows the optimum to be reached in $O(n\log\log n)$ expected time, faster than the $\Theta(n\sqrt{\frac{\log n \log\log\log n}{\log\log n}})$ runtime of the best of these two algorithms with optimally tuned parameters.
We first establish this bound under an idealized switching rule that changes from the $(1+\lambda)$ to the $(1+(\lambda,\lambda))$ GA at the optimal time. We then propose a realistic switching strategy that achieves the same performance. Our analysis combines fixed-start and fixed-target perspectives, illustrating how different algorithms dominate at different stages of the optimization process. This approach offers a promising path toward a deeper theoretical understanding of OAS.

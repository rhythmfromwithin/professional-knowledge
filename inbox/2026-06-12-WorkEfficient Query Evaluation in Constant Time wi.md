---
interest: medium
link: https://arxiv.org/abs/2301.08178
next_step: skim
priority: low
slack_ts: '1781239689.237789'
source: cs.DB - Databases
status: unread
title: Work-Efficient Query Evaluation in Constant Time with PRAMs
---
# Work-Efficient Query Evaluation in Constant Time with PRAMs
> 原文: [https://arxiv.org/abs/2301.08178](https://arxiv.org/abs/2301.08178)

arXiv:2301.08178v5 Announce Type: replace
Abstract: The article studies query evaluation in parallel constant time in the CRCW PRAM model. While it is well-known that all relational algebra queries can be evaluated in constant time on an appropriate CRCW PRAM model, this article is interested in the efficiency of evaluation algorithms, that is, in the number of processors or, asymptotically equivalent, in the work. Naive evaluation in the parallel setting results in huge (polynomial) bounds on the work of such algorithms and in presentations of the result sets that can be extremely scattered in memory. The article discusses some obstacles for constant-time PRAM query evaluation. It presents algorithms for relational operators and explores three settings, in which efficient sequential query evaluation algorithms exist: acyclic queries, semijoin algebra queries, and join queries -- the latter in the worst-case optimal framework. Under mild assumptions -- that data values are numbers of polynomial size in the size of the database or that the relations of the database are suitably sorted -- constant-time algorithms are presented that are weakly work-efficient in the sense that work $\mathcal{O}(T^{1+\varepsilon})$ can be achieved, for every $\varepsilon>0$, compared to the time $T$ of an optimal sequential algorithm. Important tools are the algorithms for approximate prefix sums and compaction from Goldberg and Zwick (1995).

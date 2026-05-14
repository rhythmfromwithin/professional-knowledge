---
title: "The Distributed Complexity Landscape on Trees Depends on the Knowledge About the Network Size"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.12787
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Distributed Complexity Landscape on Trees Depends on the Knowledge About the Network Size
> 原文: [https://arxiv.org/abs/2605.12787](https://arxiv.org/abs/2605.12787)

arXiv:2605.12787v1 Announce Type: new
Abstract: One of the central models in distributed computing is Linial's LOCAL model [SIAM J. Comp. 1992]. Over time, researchers have studied distributed graph problems in the LOCAL model under slightly different assumptions, such as whether nodes know the exact network size $n$, only a polynomial upper bound on $n$, or nothing at all. We ask whether these differences are merely technical or fundamentally affect the theory of Locally Checkable Labelings (LCLs), one of the most studied problem classes.
LCLs are graph problems whose valid solutions can be characterized by a finite set of allowed constant-radius neighborhoods. Since their introduction by Naor and Stockmeyer [FOCS 1995], they have become central in distributed computing, and the last decade has seen major progress in understanding their complexity. For example, Chang, Kopelowitz, and Pettie [FOCS 2016] showed that the randomized complexity of any LCL on $n$-node graphs is at least its deterministic complexity on $\sqrt{\log n}$-node graphs. Later, Chang and Pettie [FOCS 2017] showed that any randomized $n^{o(1)}$-round algorithm for LCLs on bounded-degree trees can be turned into a deterministic $O(\log n)$-round algorithm. Then, Balliu et al. [STOC 2018] showed that such automatic speedups are impossible for general bounded-degree graphs. However, these results fundamentally rely on nodes knowing $n$. How much does this assumption affect the theory of LCLs?
Our work shows that if nodes are oblivious to $n$, or know only a polynomial upper bound on it, then even on trees, the theory of LCLs changes significantly. While the fundamental classification of problems remains the same, we show the landscape becomes much more complex: for example, for LCLs, randomness helps in more cases; some problems have very unnatural complexities; and some have a lower bound that depends on which definition of $\Omega$ we use!

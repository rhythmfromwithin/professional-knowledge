---
interest: medium
link: https://arxiv.org/abs/2607.09170
next_step: skim
priority: medium
slack_ts: '1784085262.263469'
source: cs.DC - Distributed Computing
status: unread
title: Distributed Symmetry Breaking on Hyperbolic Random Graphs
---
# Distributed Symmetry Breaking on Hyperbolic Random Graphs
> 原文: [https://arxiv.org/abs/2607.09170](https://arxiv.org/abs/2607.09170)

arXiv:2607.09170v1 Announce Type: new
Abstract: Real-world networks like the internet share patterns like a power law degree distribution and a high clustering coefficient. Many of these properties are captured by the generative model of hyperbolic random graphs (HRGs), which provides a theoretical framework for studying such networks. Motivated by the observation that several algorithms perform better on real-world networks than their worst-case guarantees suggest, we design and analyse distributed algorithms under the assumption that the input graph is an HRG. Indeed, prior work has shown that the classical symmetry-breaking problem of $\Delta+1$ colouring, where $\Delta$ is the maximum degree of the graph, can be solved in 2 rounds on HRGs [Maus and Ruff; SODA'26].
In stark contrast to this 2-round algorithm for $\Delta+1$ colouring, we prove that the related symmetry-breaking problems of maximal independent set (MIS) and maximal matching (MM) are substantially harder: we establish a lower bound of $\Omega\left(\frac{\log\log n}{\log\log\log n}\right)$ for MIS and MM on HRGs. Our lower bound techniques rely on new structural insights that may be of independent interest: we show that HRGs contain $d$-ary trees with large height and degree which enables us to adapt and lift prior impossibility results for distributed algorithms to the setting of HRGs.
We also show that these lower bounds are polynomial tight: we design algorithms tailored to HRGs that solve MIS and MM in $\tilde{\mathcal{O}}(\log^{5/3}\log n)$ rounds with high probability in the LOCAL model, improving over the general worst-case lower bound of $\Omega\left(\min\left\{\log \Delta, \sqrt{\log n}\right\}\right)$ rounds [Khoury and Schild; FOCS'25].

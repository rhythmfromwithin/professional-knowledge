---
interest: medium
link: https://arxiv.org/abs/2605.14375
next_step: skim
priority: medium
slack_ts: '1779077923.351329'
source: cs.DC - Distributed Computing
status: unread
title: Semi-Synchronous Exploration in Dynamic Graphs
---
# Semi-Synchronous Exploration in Dynamic Graphs
> 原文: [https://arxiv.org/abs/2605.14375](https://arxiv.org/abs/2605.14375)

arXiv:2605.14375v1 Announce Type: new
Abstract: We study the fundamental problem of graph exploration in dynamic graphs using mobile agents. We consider $1$-interval connected dynamic graphs, where the topology may change arbitrarily from round to round as long as the graph remains connected, and edges are assigned with the dynamic port labeling at each round. The execution follows a semi-synchronous scheduler, under which an adversary may deactivate an arbitrary subset of agents in each round. For a graph with $n$ nodes and $k$ agents, we show that exploration is impossible if the adversary can deactivate at least $ \left\lceil \frac{k}{n-2} \right\rceil - 1$ agents per round, even when agents are equipped with unbounded memory, have global communication and full visibility. This yields an upper bound, implying that exploration is solvable only when the adversary deactivates at most $\left\lceil \frac{k}{n-2} \right\rceil - 2$ agents per round. We further establish that achieving exploration at this threshold requires agents to have both $1$-hop visibility and $1$-hop communication. Finally, we present the exploration algorithm using $k$ agents when the adversary deactivates at most $ \left\lceil \frac{k}{n-2} \right\rceil - 2$ agents, assuming agents are equipped with $1$-hop visibility and global communication, and matches the adversarial deactivation bound implied by the impossibility results.

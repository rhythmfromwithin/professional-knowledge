---
interest: medium
link: https://arxiv.org/abs/2605.30546
next_step: skim
priority: medium
slack_ts: '1780462688.356639'
source: cs.DC - Distributed Computing
status: unread
title: Energy-Efficient Aggregation and Minimum-Degree Spanning Trees in Radio Networks
---
# Energy-Efficient Aggregation and Minimum-Degree Spanning Trees in Radio Networks
> 原文: [https://arxiv.org/abs/2605.30546](https://arxiv.org/abs/2605.30546)

arXiv:2605.30546v1 Announce Type: new
Abstract: We study the aggregation problem in synchronous multi-hop radio networks with $O(\log n)$-bit messages and no collision detection. Each node initially holds a value, and the goal is to compute a global aggregate such as the sum of all values. Aggregation tasks arise naturally in wireless sensor networks, where nodes are often battery-powered and radio activity is the dominant source of energy consumption. Accordingly, our main objective is to minimize the energy complexity, defined as the maximum number of rounds in which any node is awake.
Our main result is a randomized distributed algorithm that, with high probability, constructs and executes an aggregation schedule in $O(n \operatorname{polylog} n)$ rounds and using $O(\Delta^\ast \operatorname{polylog} n)$ energy, where $\Delta^\ast$ is the minimum possible maximum degree of a spanning tree of the network graph. This guarantee is nearly optimal: for any aggregation schedule and any graph, there exists a node that must be awake for at least $\Delta^\ast$ rounds.
As a by-product, the algorithm also computes a spanning tree whose maximum degree is within an $O(\log n)$ factor of $\Delta^\ast$, with the same round and energy guarantees. For every tree edge, both endpoints learn that the edge belongs to the tree.

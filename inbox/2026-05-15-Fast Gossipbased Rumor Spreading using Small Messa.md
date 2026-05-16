---
interest: medium
link: https://arxiv.org/abs/2605.14376
next_step: skim
priority: medium
slack_ts: '1778903343.222029'
source: cs.DC - Distributed Computing
status: unread
title: Fast Gossip-based Rumor Spreading using Small Messages
---
# Fast Gossip-based Rumor Spreading using Small Messages
> 原文: [https://arxiv.org/abs/2605.14376](https://arxiv.org/abs/2605.14376)

arXiv:2605.14376v1 Announce Type: new
Abstract: We study gossip algorithms for the fundamental rumor spreading problem, where the goal is to disseminate a rumor from a given source node to all nodes in an arbitrary (and unknown) graph. Gossip algorithms allow each node to call only one neighbor per round and are therefore highly message-efficient, with low per-node communication overhead per round. The state of the art present fast gossip algorithms, however they typically leverage large-sized messages. This undermines the light-weight communication advantage of gossip, since even though only one neighbor is contacted per round, the message size can be linear in $n$, the network size. Hence, a fundamental question is whether one can perform fast gossip using small messages.
The main contribution of this paper is to answer the above question in the affirmative and present two gossip algorithms that achieve fast rumor spreading using messages of polylog{n} size. Specifically, we present the following algorithms:
1. An algorithm that runs in $O(c \log n / \Phi\_c)$ rounds for every $c \geq 1$, and $\Phi\_c$ is the weak conductance. Our bound in terms of weak conductance is essentially optimal.
2. An algorithm that depends on the network diameter (and is independent of the graph's conductance), which runs in $\tilde{O}(D+\sqrt{n})$ rounds with high probability. Our algorithm can be modified to output a minimum spanning tree (MST) in the same number of rounds, which is essentially round-optimal (even for non-gossip algorithms).
Our gossip algorithms use graph sketches [Ahn, Guha, McGregor, SODA 2012] in a novel way to overcome communication bottlenecks and achieve small communication overhead with small message sizes.

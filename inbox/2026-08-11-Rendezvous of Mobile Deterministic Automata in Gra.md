---
title: "Rendezvous of Mobile Deterministic Automata in Graphs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.06482
priority: medium
status: unread
interest: medium
next_step: skim
---
# Rendezvous of Mobile Deterministic Automata in Graphs
> 原文: [https://arxiv.org/abs/2608.06482](https://arxiv.org/abs/2608.06482)

arXiv:2608.06482v1 Announce Type: new
Abstract: Two mobile agents, modeled as identical deterministic finite automata (DFA) navigating in synchronous rounds in a graph with unlabeled nodes, have to meet at some node. The well-researched task of meeting in a graph is known as rendezvous. Agents start at adversarially chosen distinct nodes in possibly different rounds. An instance of the rendezvous problem is the underlying graph, together with the initial nodes $u$ and $v$ of the agents. Such an instance is feasible, if there exists a DFA (possibly working only for this instance), such that its identical copies starting at nodes $u$ and $v$, with an arbitrary delay, accomplish rendezvous. A DFA is RV-universal for a class of instances, if it guarantees rendezvous of its copies starting at the designated nodes with arbitrary delay, for all feasible instances of this class. Our goal is to investigate the existence of RV-universal DFA.
We start by observing that if agents cannot mark nodes in any way then there does not exist a RV-universal DFA even for the class of instances where the underlying graph is a line. Hence we allow the use of identical pebbles to mark the nodes by the agents. We consider stationary pebbles that can be dropped by agents at nodes but cannot be picked up, and movable pebbles that can be dropped by agents and later picked up. We observe that, even in the more powerful scenario of movable pebbles, if agents are equipped with any finite number of pebbles, there is no RV-universal DFA for the class of all instances. Hence we restrict attention to instances where the underlying graph is a tree. Our main contribution are two contrasting results showing that movability of pebbles is a crucial feature. We first prove that for any finite number of stationary pebbles there is no RV-universal DFA for trees, and then we design a RV-universal DFA for trees, where each agent is equipped with a single movable pebble.

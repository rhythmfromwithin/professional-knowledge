---
interest: medium
link: https://arxiv.org/abs/2608.17388
next_step: skim
priority: medium
slack_ts: '1787362728.456199'
source: cs.DC - Distributed Computing
status: unread
title: Generalizing and accelerating consistency checking for non-transactional distributed
  storage systems
---
# Generalizing and accelerating consistency checking for non-transactional distributed storage systems
> 原文: [https://arxiv.org/abs/2608.17388](https://arxiv.org/abs/2608.17388)

arXiv:2608.17388v1 Announce Type: new
Abstract: Linearizability checkers check if an operation history, observed by concurrent clients, is linearizable. They are used in testing distributed storage systems, and use the classic Wing-Gong (WG) linearizability checking algorithm.
In this paper, we generalize the WG algorithm to make linearizability checkers more versatile: we can check other non-transactional consistency guarantees, like ordered sequential consistency provided by Zookeeper. Equipped with this generalization, we can also check for system-specific consistency guarantees that introduce additional ordering constraints over operations in a history, as per the system's specification.
Our experiments with 8 distributed storage systems show that checking for system-specific consistency guarantees is easy to realize, reduces false negatives in testing, helps debug consistency violations, can be up to 370x faster, and can scale to more concurrent clients within the same checking time budget. We report 6 new consistency violation bugs, out of which 5 could not be found with existing consistency checkers.

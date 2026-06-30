---
interest: medium
link: https://arxiv.org/abs/2606.28972
next_step: skim
priority: medium
slack_ts: '1782792822.099629'
source: cs.DC - Distributed Computing
status: unread
title: Five Ways to Build a Concurrent Linked From Coarse-Grain Locking to Lock-Free
  Algorithms
---
# Five Ways to Build a Concurrent Linked From Coarse-Grain Locking to Lock-Free Algorithms
> 原文: [https://arxiv.org/abs/2606.28972](https://arxiv.org/abs/2606.28972)

arXiv:2606.28972v1 Announce Type: new
Abstract: Linked lists are one of the most basic data structures in computer science. But when many threads try to use the same linked list at the same time, things get complicated. In this paper, we look at five different ways to make a linked list work correctly and efficiently with multiple threads running at once. We start with the simplest approach -- one big lock for the whole list -- and step by step improve it, ending with a lock-free design that uses no locks at all. We implemented all five versions in C++ and measured how fast each one is across different workloads (read-heavy, balanced, and write-heavy) and different list sizes. Our results show that the right choice of algorithm depends heavily on how the list is used: the coarse-grain and lazy lists win under read-heavy workloads with small key ranges, while the lock-free list becomes competitive when key ranges are large and more threads are running. Fine-grain locking, despite its theoretical appeal, pays a heavy cost from per-node lock overhead and consistently performs the worst in our tests.

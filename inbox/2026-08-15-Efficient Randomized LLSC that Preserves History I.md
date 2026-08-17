---
interest: medium
link: https://arxiv.org/abs/2608.12946
next_step: skim
priority: medium
slack_ts: '1786931059.943089'
source: cs.DC - Distributed Computing
status: unread
title: Efficient Randomized LL/SC that Preserves History Independence
---
# Efficient Randomized LL/SC that Preserves History Independence
> 原文: [https://arxiv.org/abs/2608.12946](https://arxiv.org/abs/2608.12946)

arXiv:2608.12946v1 Announce Type: new
Abstract: We study the fundamental problem of implementing $m$ linearizable LL/SC objects with constant expected step complexity in a system of $n$ processes, using bounded base objects commonly available in hardware. Assuming that each process may have at most $\tau$ outstanding LL operations, the best known deterministic algorithm requires $\Omega(n^2\tau + m)$ base objects (CAS and registers) [Blelloch and Wei, DISC 2020]. Previously, no comparable randomized algorithm was known.
By employing randomization and FADD in addition to CAS and registers, we obtain a space bound of $O(n\tau+m)$ against the weak adaptive adversary. For $m=O(1)$ this matches a lower bound for algorithms using CAS and registers [Aghazadeh and Woelfel, PODC 2015].
In addition, our object can be employed by quiescently history-independent (QHI) algorithms: Whenever no operation on the object is pending and no process has an outstanding LL operation, its internal memory state is uniquely determined by the values of the $m$ LL/SC objects. An important application is a QHI dynamic hashing algorithm presented at STOC 2025, which uses $\Theta(m)$ hardware LL/SC objects to maintain a hash table of size $m$ [Attiya, Bender, Farach-Colton, Oshman, and Schiller, STOC 2025]. But LL/SC is not available in hardware, and prior to our work no wait-free or efficiently lock-free software implementation of LL/SC with similar properties was known. Our work demonstrates that one can actually implement the hashing algorithm on available hardware, without an asymptotic increase in step and space complexity, under the reasonable assumption that $m=\Omega(n)$.

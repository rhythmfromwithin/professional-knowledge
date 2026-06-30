---
interest: medium
link: https://arxiv.org/abs/2606.28889
next_step: skim
priority: medium
slack_ts: '1782792821.299109'
source: cs.DC - Distributed Computing
status: unread
title: Concurrent Splay-Based Tree
---
# Concurrent Splay-Based Tree
> 原文: [https://arxiv.org/abs/2606.28889](https://arxiv.org/abs/2606.28889)

arXiv:2606.28889v1 Announce Type: new
Abstract: Most work on efficient concurrent ordered indices, such as concurrent binary search trees, B-trees, skip lists, etc., has focused on data structures that provide good \emph{worst-case} guarantees. In real workloads, objects are often accessed at different rates, since access distributions may be non-uniform. Many efficient distribution-adaptive data structures exist in the sequential case; however, they are often complicated to make efficient in the concurrent case.
The most prominent distribution-adaptive data structure is Splay Tree. Its most important advantage is that it does not store any balancing information and provides a reasonable performance improvement on extremely skewed workloads, such as Zipfian workloads. This paper proposes a splay-like rotation design for concurrent binary search trees. Instead of moving an accessed node to the root, rotations use two depth thresholds that are based on the static-optimality complexity computed from the number of accesses to the node: a node is rotated only when it is substantially deeper than the upper threshold, and rotations of the node stop before reaching the lower threshold. This design aims to preserve the main practical benefit of splaying on skewed workloads while reducing contention near the root.
We present two variants of the rotation design: one using an exact 64-bit access counter per node and one using a 6-bit approximate counter. We prove static optimality for the corresponding sequential read-only tree and evaluate both rotation designs by implementing them on top of the concurrent AVL tree of Bronson et al. Our experiments show that the approach can improve throughput on several skewed workloads.

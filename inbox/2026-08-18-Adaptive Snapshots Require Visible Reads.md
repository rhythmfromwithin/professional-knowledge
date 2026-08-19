---
interest: medium
link: https://arxiv.org/abs/2608.13705
next_step: skim
priority: medium
slack_ts: '1787103711.829059'
source: cs.DC - Distributed Computing
status: unread
title: Adaptive Snapshots Require Visible Reads
---
# Adaptive Snapshots Require Visible Reads
> 原文: [https://arxiv.org/abs/2608.13705](https://arxiv.org/abs/2608.13705)

arXiv:2608.13705v1 Announce Type: new
Abstract: Snapshots are widely used to record the state of a running execution. Snapshots have been extensively studied in the literature, with the goal of improving performance and extending functionality. In this work, we consider $adaptive$ snapshots over a set of $m$ components. Adaptive snapshots provide a Click() operation that logically creates a new snapshot and an Observe$(i)$ operation that returns the state of component $i$ at the most recent Click(). Several constructions of adaptive snapshots have recently been proposed; interestingly, none of them employs invisible reads, even though invisible reads can improve performance, sometimes significantly. In this paper, we ask whether it is possible to build an adaptive snapshot with invisible reads. We show that, even when restricting the snapshot algorithm to the single-writer, single-scanner setting, under reasonable assumptions satisfied by all existing adaptive snapshot implementations, adaptive snapshots with invisible reads are not linearizable.

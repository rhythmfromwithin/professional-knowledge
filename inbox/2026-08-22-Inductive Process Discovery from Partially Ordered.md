---
interest: medium
link: https://arxiv.org/abs/2608.20211
next_step: skim
priority: low
slack_ts: '1787362754.497329'
source: cs.DB - Databases
status: unread
title: Inductive Process Discovery from Partially Ordered Event Data
---
# Inductive Process Discovery from Partially Ordered Event Data
> 原文: [https://arxiv.org/abs/2608.20211](https://arxiv.org/abs/2608.20211)

arXiv:2608.20211v1 Announce Type: new
Abstract: The Inductive Miner (IM) family is a prominent class of process discovery techniques, combining efficient recursive decomposition with soundness-by-construction guarantees. However, IM techniques usually assume traces to be totally ordered sequences of activity occurrences. This assumption is convenient, but can introduce systematic bias: activities may have durations, events may share coarse timestamps, or the data may constrain only some event pairs. Forcing such executions into arbitrary sequences hides inherent concurrency and may introduce sequential dependencies that were never observed as causal constraints. Partial orders provide a more faithful representation, but integrating them into IM discovery is challenging because standard abstractions are sequence-based; directly reusing them would require linearizing each partial order, which becomes prohibitively expensive under high concurrency. We introduce a lifting of IM discovery from total orders to partially ordered traces. Instead of redesigning the miner and its cut detection logic, we redefine the trace abstraction layer and the recursive projections to operate directly on partial orders. The approach is conservative over totally ordered traces, avoids linearization explosion, and preserves the recursive structure and guarantees that make IM attractive. Experimental results show that the proposed lifting avoids the combinatorial overhead of linearization, reduces sensitivity to arbitrary tie-breaking in timestamped event data, and allows process behavior to be learned from fewer observations by preserving concurrency at the trace level.

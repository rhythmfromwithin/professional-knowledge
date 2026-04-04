---
interest: medium
link: https://arxiv.org/abs/2604.00159
next_step: skim
priority: low
slack_ts: '1775270914.367779'
source: cs.DB - Databases
status: unread
title: Reasoning about Transactional Isolation Levels with Isolde
---
# Reasoning about Transactional Isolation Levels with Isolde
> 原文: [https://arxiv.org/abs/2604.00159](https://arxiv.org/abs/2604.00159)

arXiv:2604.00159v1 Announce Type: new
Abstract: Most databases can be configured to operate under isolation levels weaker than serializability. These enforce fewer restrictions on the concurrent access to data and consequently allow for more performant implementations. While formal frameworks for rigorously specifying isolation levels exist, reasoning about the semantic differences between specifications remains notoriously difficult.
This paper proposes a tool -- Isolde -- that can automatically generate examples that are allowed by an isolation level but disallowed by another. This simple primitive unlocks a range of useful reasoning tasks, including checking equivalence between definitions, and verifying (by refutation) subtle semantic properties of isolation levels. For example, Isolde allowed us to easily and automatically reproduce a famously elusive result from the literature and to discover a previously unknown bug in the alternative specification of a standard isolation level used in a state-of-the-art isolation checker.

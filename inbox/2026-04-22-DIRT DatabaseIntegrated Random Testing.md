---
interest: medium
link: https://arxiv.org/abs/2604.16373
next_step: skim
priority: low
slack_ts: '1776828605.142599'
source: cs.DB - Databases
status: unread
title: 'DIRT: Database-Integrated Random Testing'
---
# DIRT: Database-Integrated Random Testing
> 原文: [https://arxiv.org/abs/2604.16373](https://arxiv.org/abs/2604.16373)

arXiv:2604.16373v1 Announce Type: new
Abstract: Database management systems (DBMSs) are notoriously complex, making them difficult to test effectively, especially during early development when many features are incomplete. Traditional testing tools like SQLancer and SQLSmith are highly effective for mature databases, but they struggle with high false positive rates and low actionability when applied to evolving systems. We present DIRT, a paradigm designed specifically for testing databases during development, which integrates a testing framework directly into the DBMS, enabling the random testing process to evolve in tandem with the system and reducing false positives by construction. We introduce generation actions, an abstraction for allowing database developers rather than testing experts to specify correctness properties. We evaluate DIRT on Turso, an actively developed SQLite-compatible OLTP engine, and show that it finds 23 unique, confirmed bugs--significantly outperforming off-the-shelf SQLancer variants in terms of true positive rate and usefulness of bug reports. Our results demonstrate that embedding testing infrastructure within the DBMS can dramatically improve its effectiveness and usability during development.

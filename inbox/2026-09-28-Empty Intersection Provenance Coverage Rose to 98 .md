---
interest: medium
link: https://arxiv.org/abs/2609.30308
next_step: skim
priority: low
slack_ts: '1790571559.868959'
source: cs.SE - Software Engineering
status: unread
title: 'Empty Intersection: Provenance Coverage Rose to 98% and Neither Verification
  Decision Moved'
---
# Empty Intersection: Provenance Coverage Rose to 98% and Neither Verification Decision Moved
> 原文: [https://arxiv.org/abs/2609.30308](https://arxiv.org/abs/2609.30308)

arXiv:2609.30308v1 Announce Type: new
Abstract: Two structural defenses for provenance, a grade on every row, so that a verification routine cannot mistake the system's own output for an observation, and a single write ingress, so that the grade is enforced rather than merely conventional, were measured against the production deployment that motivated them, over a frozen snapshot of 194,620 rows and the two verification decisions the snapshot supports. Neither reaches either decision. Both were prescribed by a companion paper, which diagnosed that deployment: its verification routines decided outcomes using values the system itself had written. Neither prescription is new: both are established practice in fields that do not cite one another, and no prior work measuring whether either changes a verdict was found, so what is offered here is the measurement and not the prescriptions. Filtering the verification queries by grade turns both decisions from pass to undetermined; widening the grade vocabulary raises classified coverage from 36.1% to 98.4%; a single ingress requiring a grade refuses 3,070 writes. None of the three gives either decision admissible input. The prescriptions do not fail at what they specify. Each is stated over the population and makes no reference to any decision, so neither says which rows a decision will read, and the rows each intervention repairs and the 32 rows the decisions read do not intersect. The intervention that changed the most rows shows the reach most plainly: all 121,296 rows it moved from unnameable to named fall outside both query windows. This paper reports the conditions, measured rather than designed, under which the decisions would have admissible input at all, and notes that the two decisions are blocked for different reasons.

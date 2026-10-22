---
interest: medium
link: https://arxiv.org/abs/2610.25108
next_step: skim
priority: low
slack_ts: '1792642772.629329'
source: cs.DB - Databases
status: unread
title: Which Code Changes Need Re-embedding? CIPBench and the Limits of Multi-Signal
  Index Maintenance
---
# Which Code Changes Need Re-embedding? CIPBench and the Limits of Multi-Signal Index Maintenance
> 原文: [https://arxiv.org/abs/2610.25108](https://arxiv.org/abs/2610.25108)

arXiv:2610.25108v1 Announce Type: new
Abstract: Repository-level retrieval-augmented generation systems must keep vector indexes synchronized with continuously evolving code, yet there is no principled basis for deciding which changed code units actually need new embeddings. We ask whether the retrieval impact of a code change can be anticipated before that embedding is computed.
Across 10 open-source repositories in Python, Go, and JavaScript, we characterize how a change propagates from syntactic substantiality through embedding displacement to retrieval impact. The links are informative but not deterministic: syntactic class separates displacement sharply, yet impact depends on a unit's retrieval exposure as much as on how far its representation moves, and recurring counterexamples bound what any single signal can decide. We formalize the decision as CIPBench, a benchmark that scores maintenance policies under a strict pre-embedding information boundary.
Prediction works, and one signal exhausts it. A ranker using only a unit's change history substantially reduces retrieval harm relative to random and recency-based scheduling. Combining it with three further signals--individually discriminative and largely unassociated with one another--leaves the decision statistically unchanged across every budget we evaluate, for reasons we trace to the structure of the score rather than to its tuning. What pays off is not ranking but filtering: units whose text is unchanged from the indexed state can be skipped with no risk and, in the most reversion-heavy project, at nearly half the embedding cost. Signal-level informativeness is therefore not evidence of decision-level value, and separating the two requires evaluating the decision a signal produces rather than its association with the outcome.

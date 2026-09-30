---
title: "Epistemic Typing as a PostgreSQL Table Access Method: Adversarial Conflict Resolution Under Confidence Forgery and Sybil Coordination"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.36795
priority: low
status: unread
interest: medium
next_step: skim
---
# Epistemic Typing as a PostgreSQL Table Access Method: Adversarial Conflict Resolution Under Confidence Forgery and Sybil Coordination
> 原文: [https://arxiv.org/abs/2609.36795](https://arxiv.org/abs/2609.36795)

arXiv:2609.36795v1 Announce Type: new
Abstract: We describe KNDB, a PostgreSQL 18 table access method (TAM) that types every row with an engine-assigned epistemic kind (MEASURED, INFERRED, or DERIVED) and resolves per-slot conflicts inside every write-time heapam callback. Rows land as ordinary heap tuples; seven of the 44 TAM callbacks are overridden (tuple\_insert, multi\_insert, tuple\_update, tuple\_delete, tuple\_insert\_speculative, tuple\_complete\_speculative, relation\_toast\_am), the other 37 delegate to heap; we provide a completeness argument over the interface as a paper artefact. This paper reports the engineering behind that decision and the adversarial evaluation that motivated it. On a confidence-forgery workload where an attacker asserts INFERRED writes with confidence in [0.95,1.0] against honest MEASURED writes with confidence in [0.5,0.9], KNDB beats a confidence-only baseline by 63 percentage points on the Book-Author fusion dataset and 92.7 points on the Zheng crowdsourcing dataset. Both wins are proven load-bearing on the kind axis by a source-rebuild disable-and-test in which the lattice is neutralised and the win vanishes. Against four truth-discovery baselines (TruthFinder, CRH, CATD, ACCU) reimplemented from the original equations and validated to within 0.3 percentage points of the published numbers, KNDB is competitive below a per-dataset density-saturation cell and dominant at or above it. We formalise the cell as k\* ~ rho\_alg \* h\_top, where h\_top is per-slot top honest surface-form support, and validate the prediction within +/-20% on Book-Author and +/-30% on Zheng. Because the kind axis is assigned by the engine from independent metadata and cannot be forged at write time, KNDB's k\* is unbounded. The paper is honest about where KNDB loses: CRH and ACCU outperform KNDB below saturation on Zheng, and KNDB scores zero on three temporal knowledge-editing benchmarks whose ground truth is last-writer-wins.

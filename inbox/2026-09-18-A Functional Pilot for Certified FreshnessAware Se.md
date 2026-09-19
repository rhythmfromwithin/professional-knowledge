---
interest: medium
link: https://arxiv.org/abs/2609.19855
next_step: skim
priority: low
slack_ts: '1789791393.608289'
source: cs.DB - Databases
status: unread
title: A Functional Pilot for Certified Freshness-Aware Semantic--Spatial Range Retrieval
---
# A Functional Pilot for Certified Freshness-Aware Semantic--Spatial Range Retrieval
> 原文: [https://arxiv.org/abs/2609.19855](https://arxiv.org/abs/2609.19855)

arXiv:2609.19855v1 Announce Type: new
Abstract: Geographic applications need every object inside a radius that satisfies a semantic threshold, yet embedding indexes return approximate top-ranked lists and may omit qualifying records silently. We present FRESH-GEORANGE, a semantic- spatial range design that separates source-watermark freshness from optional record age. Geographic cells and semantic mi- croblocks provide admissible pruning bounds; a graph proposes verification order but supplies no correctness evidence. Exact mode scans every nonprunable block and the delta overlay. Certified mode may stop early and reports a deterministic query- specific recall lower bound from verified answers and unresolved records. A reproducible CPU pilot uses 2,500 real OpenFlights airport records, a 2,000-record base, and 740 simulated insert, delete, and text-revision events; it evaluates 180 unique queries over five seeds. Exact mode achieved 100.00% set recall on every query. The 95-percent mode achieved 99.91% empirical mean recall with a 99.41% reported mean certificate and no observed bound violation. However, its 7.24 ms median latency was 5.85 times the 1.24 ms spatial-first exact baseline, and full-history delta replay became slower than rebuilding at larger batches. The prototype therefore validates the completeness mechanism, not performance superiority or production freshness. Submission- scale evaluation requires real map diffs, official recent baselines, and truly incremental versioned maintenance.

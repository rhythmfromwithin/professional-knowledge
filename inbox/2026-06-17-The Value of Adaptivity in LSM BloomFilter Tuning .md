---
title: "The Value of Adaptivity in LSM Bloom-Filter Tuning: A Log-Law and a Two-Clock Frontier"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2606.18138
priority: low
status: unread
interest: medium
next_step: skim
---
# The Value of Adaptivity in LSM Bloom-Filter Tuning: A Log-Law and a Two-Clock Frontier
> 原文: [https://arxiv.org/abs/2606.18138](https://arxiv.org/abs/2606.18138)

arXiv:2606.18138v1 Announce Type: new
Abstract: Log-structured merge (LSM) trees attach an approximate-membership filter to every run and must split a fixed memory budget across them. The static optimum is known (Monkey); a large systems literature then makes the allocation adaptive, tracking shifting hotness online. We ask a prior question: when is that adaptivity worth its machinery? We give three analytical answers and validate them on synthetic sweeps, real Twitter production cache traces, and a real RocksDB engine. First, a log-law: optimal bits-per-key is affine in the logarithm of access frequency, at a fixed slope. Second, a robustness law: because the workload enters only logarithmically, the excess read cost from a hotness misestimate is half the size-weighted variance of the log error, and a common-factor misestimate is absorbed by the budget multiplier, so coarse estimates lose little. Third, an adaptivity-value frontier: since compaction rebuilds filters for free on its own clock, the value of continuous tracking over an allocation recomputed only at compaction grows quadratically in the within-epoch drift, with a closed-form scale. This yields a three-regime policy (coarse-at-compaction suffices, then track, then at extreme drift fall back to uniform) and predicts that more skew makes fine tracking matter less. On a real cluster, reallocating only at compaction captures 96-99% of tracking's benefit; on RocksDB the false-positive primitive holds within four percent to eight bits per key. The contribution is a characterization of when adaptive tuning pays; we add no new filter and no engine fork. Code and pre-registration are public.

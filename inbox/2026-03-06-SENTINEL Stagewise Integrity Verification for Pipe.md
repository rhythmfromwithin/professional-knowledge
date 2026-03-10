---
title: "SENTINEL: Stagewise Integrity Verification for Pipeline Parallel Decentralized Training"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.03592
priority: medium
status: unread
interest: medium
next_step: skim
---
# SENTINEL: Stagewise Integrity Verification for Pipeline Parallel Decentralized Training
> 原文: [https://arxiv.org/abs/2603.03592](https://arxiv.org/abs/2603.03592)

arXiv:2603.03592v1 Announce Type: new
Abstract: Decentralized training introduces critical security risks when executed across untrusted, geographically distributed nodes. While existing Byzantine-tolerant literature addresses data parallel (DP) training through robust aggregation methods, pipeline parallelism (PP) presents fundamentally distinct challenges. In PP, model layers are distributed across workers where the activations and their gradients flow between stages rather than being aggregated, making traditional DP approaches inapplicable. We propose SENTINEL, a verification mechanism for PP training without computation duplication. SENTINEL employs lightweight momentum-based monitoring using exponential moving averages (EMAs) to detect corrupted inter-stage communication. Unlike existing Byzantine-tolerant approaches for DP that aggregate parameter gradients across replicas, our approach verifies sequential activation/gradient transmission between layers. We provide theoretical convergence guarantees for this new setting that recovers classical convergence rates when relaxed to standard training. Experiments demonstrate successful training of up to 4B-parameter LLMs across untrusted distributed environments with up to 176 workers while maintaining model convergence and performance.

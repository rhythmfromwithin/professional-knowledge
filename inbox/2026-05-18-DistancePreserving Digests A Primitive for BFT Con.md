---
title: "Distance-Preserving Digests: A Primitive for BFT Consensus"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.15329
priority: low
status: unread
interest: medium
next_step: skim
---
# Distance-Preserving Digests: A Primitive for BFT Consensus
> 原文: [https://arxiv.org/abs/2605.15329](https://arxiv.org/abs/2605.15329)

arXiv:2605.15329v1 Announce Type: new
Abstract: Every BFT consensus protocol uses collision-resistant hashes to compare validator state. Collision resistance destroys distance: two validators agreeing on 19 of 20 transactions produce unrelated hashes, indistinguishable from validators sharing nothing. This forces three design constraints across the BFT literature: validators must synchronize state before voting, agreement quality cannot be measured until votes are counted, and hierarchical committees must be large enough for independent BFT, limiting tree depth. This paper introduces distance-preserving transaction digests, a primitive that replaces collision-resistant hashes with commutative vector sums in 8-dimensional space. The primitive has three properties hashes lack: distance is proportional to disagreement, weighted means are exact, and set differences are identifiable via bloom filter diff. We demonstrate three applications: a two-phase BFT protocol (Proxima) that achieves single-round finality when validators agree; tree-structured consensus with groups of 10 validators (vs 128 in Ethereum), enabled because distance filtering replaces per-group BFT; and cross-shard consistency verification at 128 bytes per shard pair, replacing the per-transaction coordination of two-phase commit. Safety is proved: fewer than N/3 Byzantine validators cannot cause conflicting finalization, independent of Phase 1 clustering or tree topology. At N =100,000, Proxima Tree uses 2.2x fewer messages than HotStuff (a structural property unaffected by parallelism). Single-core finality is 0.9s vs 18s for HotStuff; multi-core BLS narrows but does not eliminate this gap.

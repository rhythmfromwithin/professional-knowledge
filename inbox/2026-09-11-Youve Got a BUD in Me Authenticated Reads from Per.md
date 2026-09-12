---
interest: medium
link: https://arxiv.org/abs/2609.11251
next_step: skim
priority: low
slack_ts: '1789186434.705479'
source: cs.DB - Databases
status: unread
title: 'You''ve Got a BUD in Me: Authenticated Reads from Per-Block Write Logs'
---
# You've Got a BUD in Me: Authenticated Reads from Per-Block Write Logs
> 原文: [https://arxiv.org/abs/2609.11251](https://arxiv.org/abs/2609.11251)

arXiv:2609.11251v1 Announce Type: cross
Abstract: Blockchains usually pay for authenticated reads by maintaining a structure that spans the entire state. We show how validators can support historical membership and exclusion proofs by authenticating each block's writes instead. A Block Update Digest (BUD) commits a write log whose predecessor pointers link successive modifications of each key. A SuperBUD summarizes last writes over a window; an exponential hierarchy turns long unchanged intervals into short proofs. The digest count is logarithmic in the gap within the hierarchy's range, with one additional digest per top-level window beyond it. We prove soundness against adversarial provers and up to f Byzantine validators, and completeness for queries anchored by a post-deployment modification, assuming archive, attestation, and committee evidence is available. Across a 50x increase in state size, the measured base-BUD path rises by 1.24x, compared with 3.1x and 69.5x for in-memory and cache-bounded disk-backed Merkle Patricia tries. On the synthetic trace, two-digest read-layer payloads stay below 800 bytes, and warm hash-path verification takes at most 146 microseconds at p99.

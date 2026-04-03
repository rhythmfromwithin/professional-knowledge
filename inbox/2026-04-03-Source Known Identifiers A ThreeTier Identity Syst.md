---
interest: medium
link: https://arxiv.org/abs/2604.00151
next_step: skim
priority: medium
slack_ts: '1775185093.481469'
source: cs.DC - Distributed Computing
status: unread
title: 'Source Known Identifiers: A Three-Tier Identity System for Distributed Applications'
---
# Source Known Identifiers: A Three-Tier Identity System for Distributed Applications
> 原文: [https://arxiv.org/abs/2604.00151](https://arxiv.org/abs/2604.00151)

arXiv:2604.00151v1 Announce Type: new
Abstract: Distributed applications need identifiers that satisfy storage efficiency, chronological sortability, origin metadata embedding, zero-lookup verifiability, confidentiality for external consumers, and multi-century addressability. Based on our literature survey, no existing scheme provides all six of these identifier properties within a unified system.
This paper introduces Source Known Identifiers (SKIDs), a three-tier identity system that projects a single entity identity across trust boundaries, addressing all six properties. The first tier, Source Known ID (SKID), is a 64-bit signed integer embedding a timestamp with a 250-millisecond precision, application topology, and a per-entity-type sequence counter. It serves as the database primary key, providing compact storage (8 bytes) and natural B-tree ordering for optimized database indexing. The second tier, Source Known Entity ID (SKEID), extends the SKID into a 128-bit Universally Unique Identifier (UUID) compatible value by adding an entity type discriminator, an epoch selector, and a BLAKE3 keyed message authentication code (MAC). SKEIDs enable zero-lookup verification of identifier origin, integrity, and entity type within trusted environments, with a big-endian byte layout that preserves chronological ordering in lexicographic UUID string comparisons. The third tier, Secure SKEID, encrypts the entire SKEID using AES-256 symmetric encryption as a single-block pseudorandom permutation, producing ciphertext indistinguishable from random bytes while remaining compatible with standard UUID data-type parsers in string representation. Deterministic bidirectional transformations connect all three tiers.

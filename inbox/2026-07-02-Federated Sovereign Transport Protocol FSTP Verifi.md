---
interest: medium
link: https://arxiv.org/abs/2607.00213
next_step: skim
priority: low
slack_ts: '1782965357.565749'
source: cs.CR - Cryptography and Security
status: unread
title: 'Federated Sovereign Transport Protocol (FSTP): Verifiable Coordination Without
  Disclosure'
---
# Federated Sovereign Transport Protocol (FSTP): Verifiable Coordination Without Disclosure
> 原文: [https://arxiv.org/abs/2607.00213](https://arxiv.org/abs/2607.00213)

arXiv:2607.00213v1 Announce Type: new
Abstract: This paper introduces the Federated Sovereign Transport Protocol (FSTP), a synchronization boundary and transport layer for federated networks in which nodes have heterogeneous privacy requirements. Existing federation protocols leave data confinement to operator policy: they define message formats and delivery semantics but impose no structural constraint on what a conforming server may emit. FSTP addresses this gap by making data confinement a property of the protocol itself.
The central mechanism is a synchronization agent whose output type set is formally closed. Raw internal data cannot appear in any federation message because the constraint is enforced by the Rust type system at compile time, not by a runtime check. A contextual identity model derives a separate, unlinkable identifier for each federation relationship, preventing cross-context correlation structurally. A Blocklace-based event substrate provides tamper-evident, partially ordered logging with synchronization cost proportional to the symmetric difference between node states, and supports data erasure without breaking the hash chain.
The result is proof without exposure: a federation participant can verify that a process occurred, that a credential is authentic, and that an outcome is uncorrupted without accessing the internal data that produced these artifacts. FSTP is developed as the inter-node transport layer of Velyzor, a governance platform for institutions with demanding confidentiality requirements. The specification and reference implementation are released as open-source infrastructure under Apache 2.0; source code and figures accompany this paper.

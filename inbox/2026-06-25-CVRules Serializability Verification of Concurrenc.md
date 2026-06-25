---
interest: medium
link: https://arxiv.org/abs/2606.25409
next_step: skim
priority: low
slack_ts: '1782360756.664649'
source: cs.DB - Databases
status: unread
title: 'CV-Rules: Serializability Verification of Concurrency Control Protocols via
  Explicit Transaction Ordering'
---
# CV-Rules: Serializability Verification of Concurrency Control Protocols via Explicit Transaction Ordering
> 原文: [https://arxiv.org/abs/2606.25409](https://arxiv.org/abs/2606.25409)

arXiv:2606.25409v1 Announce Type: cross
Abstract: We present CV-rules, an alternative characterization of serializability in which a transaction order constructed by a protocol satisfies two per-read conditions, C-rule (Causality) and V-rule (View Consistency), that constrain the reads-from relation and competing writers. While classical Multi-Version Serialization Graph (MVSG) reasoning characterizes serializability via its acyclicity, our approach requires explicit order construction, enabling direct proofs that build on the protocol's own mechanisms. We prove that CV-rules, serializability, and MVSG acyclicity are all equivalent. Moreover, the C/V separation reveals that serializability is polynomial-time decidable for any fixed bound on the width of the order forced by C-rule. We verify five protocols: Two-Phase Locking, Multi-Version Timestamp Ordering, Serial Safety Net (SSN), Aria, and SnapChain. For SSN and Aria, whose original papers defined only certification conditions, we identify explicit transaction orders arising from their mechanisms; we also prove that Aria's unique-write constraint is unnecessary for serializability. SnapChain, in contrast, is designed directly from CV-rules, enforcing V-rule by construction. All results except the complexity bounds are mechanized in Lean with no additional axioms and no admitted goals.

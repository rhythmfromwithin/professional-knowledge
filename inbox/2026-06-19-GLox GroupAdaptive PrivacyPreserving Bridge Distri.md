---
interest: medium
link: https://arxiv.org/abs/2606.19620
next_step: skim
priority: low
slack_ts: '1781847259.484869'
source: cs.CR - Cryptography and Security
status: unread
title: 'G-Lox: Group-Adaptive, Privacy-Preserving Bridge Distribution with Two-Party
  Computation'
---
# G-Lox: Group-Adaptive, Privacy-Preserving Bridge Distribution with Two-Party Computation
> 原文: [https://arxiv.org/abs/2606.19620](https://arxiv.org/abs/2606.19620)

arXiv:2606.19620v1 Announce Type: new
Abstract: We present G-Lox (group-adaptive Lox), a bridge-distribution system that preserves Lox-style distributor blindness while enabling hidden, stateful group-level adaptation. G-Lox places adaptive assignment logic behind a two-server privacy wall, so no single server learns group identifiers or group-to-bridge assignments. Private state access and state-dependent updates use two-server DPF/FSS protocols and secure two-party computation, supporting blockage reporting, transport-aware reassignment, and privacy-preserving group splitting.
We evaluate G-Lox through system measurements and policy simulation. In our C++/EMP implementation over real TCP sockets, private state access has low client-visible overhead: across state sizes up to 2^16, communication remains in the low-KiB range per iteration. At M=1024, the client sends 1,968 bytes, receives 1,280 bytes, and completes an iteration in about 0.25 s. Simulations with group-specific blocking and Sybil enumeration show that G-Lox improves robustness over Lox- and rBridge-like baselines among systems that maintain broad issuance.

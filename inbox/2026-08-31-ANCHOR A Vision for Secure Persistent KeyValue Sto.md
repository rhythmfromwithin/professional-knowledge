---
interest: medium
link: https://arxiv.org/abs/2608.27819
next_step: skim
priority: low
slack_ts: '1788152840.156199'
source: cs.DB - Databases
status: unread
title: 'ANCHOR: A Vision for Secure Persistent Key-Value Stores in Disaggregated Data
  Centers'
---
# ANCHOR: A Vision for Secure Persistent Key-Value Stores in Disaggregated Data Centers
> 原文: [https://arxiv.org/abs/2608.27819](https://arxiv.org/abs/2608.27819)

arXiv:2608.27819v1 Announce Type: new
Abstract: Persistent key-value stores (PKVS) are increasingly deployed in disaggregated settings that split compute, memory, and storage across separate server pools. This shift redraws the trust boundary: data that would remain within a single machine is now transported, cached, and rewritten across multiple hosts, expanding exposure to both network attackers and intra-infrastructure adversaries.
This paper presents ANCHOR, a vision for end-to-end integrity and freshness in disaggregated PKVS. ANCHOR proposes a two-part semantics-aware architecture: 1) Persistence path: ANCHOR outlines encrypting and authenticating PKVS persistent files and preventing rollback with manifest versioning. 2) Volatile path: ANCHOR treats caches, indexes, and filters as untrusted hints unless accompanied by verifiable provenance, enforced by a TEE-resident policy. Finally, we outline key invariants and discuss enclave-friendly batching and asynchronous I/O to amortize verification without undermining disaggregation's performance and elasticity benefits.

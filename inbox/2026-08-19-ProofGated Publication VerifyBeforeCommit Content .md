---
interest: medium
link: https://arxiv.org/abs/2608.14643
next_step: skim
priority: low
slack_ts: '1787276734.904039'
source: cs.DB - Databases
status: unread
title: 'Proof-Gated Publication: Verify-Before-Commit Content Integrity for Serverless
  Data-Mesh Lakehouses'
---
# Proof-Gated Publication: Verify-Before-Commit Content Integrity for Serverless Data-Mesh Lakehouses
> 原文: [https://arxiv.org/abs/2608.14643](https://arxiv.org/abs/2608.14643)

arXiv:2608.14643v1 Announce Type: new
Abstract: Federated data meshes give domain teams ownership of their data products, and serverless compute is an attractive substrate for domain-owned writes. Both trends weaken correctness at publication. Open table formats such as Apache Iceberg and Delta Lake guarantee that a commit is atomic and that readers see an isolated snapshot, but not that the rows persisted equal the rows the job intended to write; publication is decided from the writer's exit status. A serverless job that silently drops a partition, truncates a file on retry, or duplicates a chunk still produces a valid, atomic, isolated, and wrong snapshot.
This paper presents PVDM, a proof-gated publication protocol with four phases: Physical (write to rollbackable staging), Verify (a keyed multiset proof that written content equals declared intent, stored by an independent notary), Durable (replay completed chunks across serverless retries), and Metadata (commit the catalog last, only if the proof passed). Metadata commits only if the proof passes, so a failing proof yields no consumer-visible snapshot. The verification primitive is a keyed, incremental multiset hash over identity and content projections, telling missing or duplicated rows apart from corrupted values.
A dependency-free reference gate, a thirty-case adversarial suite, and a reproducible benchmark catch eight thousand of eight thousand injected faults up to one million rows with no false blocks. We also run PVDM end-to-end on Apache Spark 4.0 and Apache Iceberg 1.11 at up to one hundred million rows, where every injected fault is blocked on the real commit path, the gated publish costs about seventeen milliseconds regardless of table size, and verification overhead is about a fifth of the write. The primitives are prior art; the contribution is composing them into a fail-closed, notarized, verify-before-commit protocol for serverless federated writes.

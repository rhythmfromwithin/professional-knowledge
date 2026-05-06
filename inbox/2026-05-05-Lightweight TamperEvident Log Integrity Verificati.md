---
interest: medium
link: https://arxiv.org/abs/2605.00065
next_step: skim
priority: low
slack_ts: '1778039477.840659'
source: cs.CR - Cryptography and Security
status: unread
title: 'Lightweight Tamper-Evident Log Integrity Verification for IoT Edge Environments:
  A Merkle Tree Pipeline with Adaptive Chunking'
---
# Lightweight Tamper-Evident Log Integrity Verification for IoT Edge Environments: A Merkle Tree Pipeline with Adaptive Chunking
> 原文: [https://arxiv.org/abs/2605.00065](https://arxiv.org/abs/2605.00065)

arXiv:2605.00065v1 Announce Type: new
Abstract: Integrity of audit logs produced by Internet of Things (IoT) devices is a prerequisite for post-incident forensics, regulatory compliance, and operational accountability. While blockchain-backed logging infrastructures can satisfy this requirement, they introduce consensus overhead, network dependencies, and deployment complexity that are often prohibitive at the IoT edge.
This paper presents a lightweight and evaluated integrity verification pipeline that combines Merkle-tree commitments with resource-aware adaptive chunking to provide tamper evidence without relying on distributed ledger technologies. The proposed pipeline operates in three stages: (i) resource-aware batch ingestion via adaptive chunk sizing, (ii) Merkle-tree construction with O(logn) inclusion proof generation, and (iii) deterministic single-entry verification against a trusted root anchor.
We further report an implementation audit that identified and corrected two evaluation defects: a double-counting bug in tampering metrics and a redundant full-tree reconstruction during batch appends. Using the corrected implementation, five-run benchmarks on synthetic IoT log datasets demonstrate throughput exceeding 130,000 logs/s for 100,000 records. The system achieves per-entry verification latency of approximately 22 ms, proof generation latency of 22 ms, an average proof size of 1,006 bytes, and peak memory usage below 5 MB.
Tampering detection achieves perfect precision, recall, and F1-score (1.0) across corruption ratios ranging from 1% to 50%.

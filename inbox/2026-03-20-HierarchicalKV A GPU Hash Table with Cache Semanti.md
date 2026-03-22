---
interest: medium
link: https://arxiv.org/abs/2603.17168
next_step: skim
priority: low
slack_ts: '1774148072.726649'
source: cs.DB - Databases
status: unread
title: 'HierarchicalKV: A GPU Hash Table with Cache Semantics for Continuous Online
  Embedding Storage'
---
# HierarchicalKV: A GPU Hash Table with Cache Semantics for Continuous Online Embedding Storage
> 原文: [https://arxiv.org/abs/2603.17168](https://arxiv.org/abs/2603.17168)

arXiv:2603.17168v1 Announce Type: new
Abstract: Traditional GPU hash tables preserve every inserted key -- a dictionary assumption that wastes scarce High Bandwidth Memory (HBM) when embedding tables routinely exceed single-GPU capacity. We challenge this assumption with cache semantics, where policy-driven eviction is a first-class operation. We introduce HierarchicalKV (HKV), the first general-purpose GPU hash table library whose normal full-capacity operating contract is cache-semantic: each full-bucket upsert (update-or-insert) is resolved in place by eviction or admission rejection rather than by rehashing or capacity-induced failure. HKV co-designs four core mechanisms -- cache-line-aligned buckets, in-line score-driven upsert, score-based dynamic dual-bucket selection, and triple-group concurrency -- and uses tiered key-value separation as a scaling enabler beyond HBM. On an NVIDIA H100 NVL GPU, HKV achieves up to 3.9 billion key-value pairs per second (B-KV/s) find throughput, stable across load factors 0.50-1.00 (<5% variation), and delivers 1.4x higher find throughput than WarpCore (the strongest dictionary-semantic GPU baseline at lambda=0.50) and up to 2.6-9.4x over indirection-based GPU baselines. Since its open-source release in October 2022, HKV has been integrated into multiple open-source recommendation frameworks.

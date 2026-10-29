---
interest: medium
link: https://arxiv.org/abs/2610.33306
next_step: skim
priority: low
slack_ts: '1793251498.073509'
source: cs.DB - Databases
status: unread
title: 'Nemo: Efficient Caching with Index Pushdown for Disaggregated OLTP Databases'
---
# Nemo: Efficient Caching with Index Pushdown for Disaggregated OLTP Databases
> 原文: [https://arxiv.org/abs/2610.33306](https://arxiv.org/abs/2610.33306)

arXiv:2610.33306v1 Announce Type: new
Abstract: Storage-disaggregated databases decouple compute from storage, improving elasticity but suffering from network bottlenecks. Most cloud databases use page-based B+trees and buffer pools. Under disaggregation, each index traversal incurs serial network round-trips. Page-granularity transfers and caching also amplify network traffic and lower cache efficiency. Pushing down the full index to storage and caching only hot records at compute is appealing, but an efficient design must (1) provide a holistic record cache that accelerates both point and range queries, (2) mitigate the negative search penalty of confirming non-existence via remote probes, and (3) enforce phantom protection despite the index being encapsulated by the storage service.
We introduce Nemo, a holistic index-and-buffer design optimized for storage-disaggregated OLTP with index pushdown. Nemo employs a tree-structured record buffer that unifies caching and buffering and accelerates both point and range queries. It further reduces the negative search penalty by caching negative search results. Nemo provides phantom protection that requires no knowledge of the storage-side data layout and is robust against large key domains, varying data skew, and partition schemes. Experiments show that Nemo outperforms page-based B+Tree and the state-of-the-art 2-Tree by up to 11.42x and 2.97x on positive point queries, and achieves up to 4.76x speedup on negative searches over a hash-indexed record cache. For phantom protection, Nemo outperforms PCL by up to 1.55x even under a dense key domain. Moreover, Nemo maintains stable performance while PCL degrades sharply as the key domain grows large and sparse.

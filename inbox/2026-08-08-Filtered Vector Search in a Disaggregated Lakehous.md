---
interest: medium
link: https://arxiv.org/abs/2608.05441
next_step: skim
priority: low
slack_ts: '1786328462.342389'
source: cs.DB - Databases
status: unread
title: 'Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format
  Pruning with Per-File ANN'
---
# Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format Pruning with Per-File ANN
> 原文: [https://arxiv.org/abs/2608.05441](https://arxiv.org/abs/2608.05441)

arXiv:2608.05441v1 Announce Type: new
Abstract: Approximate nearest-neighbor (ANN) search increasingly runs alongside structured data - "find the 10 nearest documents where tenant='acme' AND lang='en'" - yet similarity and filtering are usually bolted together: a specialized vector index for one, a separate filter step for the other. We ask what happens when both live inside an open lakehouse table (Apache Iceberg over Parquet on object storage), where the engine already owns a mature file-pruning stack (partition pruning, zone-maps, a bitmap index). We embed an IVF index in place in each Parquet file's footer and make filtered vector queries fast not with a new filtering algorithm but by composing the table's existing file pruning with per-file ANN: the planner prunes data files by the predicate first, then runs IVF only over the survivors. The index is built distributed and non-destructively - a metadata-only Iceberg replace that every other engine still reads - and a rendezvous-hashed per-file cache keeps object-store read latency from swamping the algorithmic win. The payoff comes entirely from file pruning. On an 11.5M x 768 table, warm IVF search is ~32x faster than brute force at recall@10 >= 0.90, a selective predicate having pruned 355 of 444 data files before ANN runs; on 5M real IBM Granite embeddings, a filter arriving across a join prunes four of five region partitions and runs nearly two orders of magnitude (~94x: 14.7 s -> 157 ms) faster than the query-time join at identical top-k, once the reduction is materialized into a region-partitioned layout. We characterize when the composition pays off - it requires file-level locality on the filter column, and the residual predicate is only safe to push into the search over a provably pure (partitioned) column, not a merely sorted one - and report the failure modes we hit bolting ANN onto a lakehouse engine.

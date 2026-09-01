---
title: "PUFFER: Incremental Fuzzy Deduplication for Continuously Evolving Corpora"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.28622
priority: low
status: unread
interest: medium
next_step: skim
---
# PUFFER: Incremental Fuzzy Deduplication for Continuously Evolving Corpora
> 原文: [https://arxiv.org/abs/2608.28622](https://arxiv.org/abs/2608.28622)

arXiv:2608.28622v1 Announce Type: new
Abstract: Large language model training corpora grow through successive, often redundant releases, so each release must be deduplicated against both itself and the accumulated history. At trillion-token scale, this requires incremental ingestion, bounded resident memory, deterministic retry, and dataset-scoped lifecycle control without repeated corpus-wide rebuilding. We introduce PUFFER (Provenance-aware Updatable Fuzzy Filtering for Evolving Repositories), a MinHash-LSH fuzzy-deduplication pipeline built around two design choices. First, PUFFER stores each LSH band as immutable, dataset-tagged, memory-mapped sorted segments, enabling exact historical band-key membership checks without RAM proportional to corpus size. Second, T-fanout tiered compaction periodically merges segments to control screening fanout, trading lower query cost against additional index-maintenance writes while preserving membership decisions. Across N ingested keys and K equal-sized releases, PUFFER's cumulative maintenance cost is O(N log N log\_T K), compared with Theta(KN) for repeated snapshot rebuilding. Dataset-tagged segments also support dataset-scoped withdrawal: removal is constant-time for uncompacted or protected datasets, while post-compaction withdrawal reconstructs only the affected merged segment, even if the original dataset is unavailable. In our implementation, PUFFER completed cumulative index-stage ingestion for one billion documents in about 1.75 hours in a single process, using 128 bytes per document for a 16-band index. A classical resident MinHash-LSH table required about 6.5 KB per document and exceeded a 900 GiB RAM cap. In a ten-hour comparison capped at one billion documents, PUFFER was 11x faster than LSHBloom and 35x faster than Milvus-LSH. PUFFER is deployed on more than 30 billion documents, and we release it as open-source software at https://github.com/Zyphra/puffer.

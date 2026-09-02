---
title: "Client-side transparent caching for remote ROOT data analysis"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.00400
priority: medium
status: unread
interest: medium
next_step: skim
---
# Client-side transparent caching for remote ROOT data analysis
> 原文: [https://arxiv.org/abs/2609.00400](https://arxiv.org/abs/2609.00400)

arXiv:2609.00400v1 Announce Type: new
Abstract: High-energy physics analyses often process the same data as physicists refine algorithms and test new ideas. With data increasingly read from remote storage, each iteration is subject to network latency and depends on network bandwidth and shared-storage throughput, which can vary substantially under load. We present uCache (xrd-ucache), a transparent client-side cache implemented as an XRootD client plugin that requires neither server-side deployment nor changes to analysis code. It uses local storage on the analysis machine as a cache layer between the network and memory. The cache stores only the data actually read by an analysis. It can also rebuild cached data into a branch-aligned, recompressed form, eliminating most of the input/output and decompression costs of subsequent passes. We benchmark the cache using the Analysis Grand Challenge top quark pair analysis on public CMS Open Data compressed with zlib and LZMA. Filling the cache adds essentially no overhead compared with a direct read. Subsequent passes are 1.6-8.8 times faster from the byte cache and 2.1-15.7 times faster from the recompressed cache. For a typical analysis, a 1 TB cache suffices for datasets of 10-20 TB. The largest improvements occur when the remote data source is heavily loaded or geographically distant.

---
interest: medium
link: https://arxiv.org/abs/2606.04268
next_step: skim
priority: medium
slack_ts: '1780548669.242909'
source: cs.DC - Distributed Computing
status: unread
title: 'ACEAPEX: Parallel LZ77 Decoding via Encode-Time Absolute Offset Resolution'
---
# ACEAPEX: Parallel LZ77 Decoding via Encode-Time Absolute Offset Resolution
> 原文: [https://arxiv.org/abs/2606.04268](https://arxiv.org/abs/2606.04268)

arXiv:2606.04268v1 Announce Type: new
Abstract: LZ77-based codecs exhibit a fundamental sequential bottleneck in decoding: each back-reference depends on previously decompressed data, preventing multi-core scaling. We present ACEAPEX, a parallel LZ77 codec that stores all back-references as absolute positions in the decompressed output and organizes data into self-contained 1 MB blocks, enabling embarrassingly parallel block-level decoding. Integrated into lzbench, ACEAPEX achieves 10,160 MB/s on EPYC 4344P (8 cores) and 10,869 MB/s on EPYC 9575F for FASTQ genomic data -- up to 3.1x faster than zstd -3 at comparable compression ratios. We further implement a GPU wavefront decoder on NVIDIA H100 SXM, measuring 44.0 GB/s on enwik9 and 20.3 GB/s on FASTQ (wavefront match phase, BIT-PERFECT verified). With a depth-limited encoder variant (-1.5% ratio on enwik9), GPU throughput reaches 77.2 GB/s on a single H100 and 249.9 GB/s on two H100s in NVLink configuration. To our knowledge, this is the first reported GPU LZ77 decode with near-standard compression ratio verified byte-for-byte.

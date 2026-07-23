---
title: "What Governs Decode Throughput in Absolute-Offset GPU LZ77? A Work-Granularity Mechanism and an Encode-Time Min-Match-Length Lever"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.18541
priority: medium
status: unread
interest: medium
next_step: skim
---
# What Governs Decode Throughput in Absolute-Offset GPU LZ77? A Work-Granularity Mechanism and an Encode-Time Min-Match-Length Lever
> 原文: [https://arxiv.org/abs/2607.18541](https://arxiv.org/abs/2607.18541)

arXiv:2607.18541v1 Announce Type: new
Abstract: The ACEAPEX line of work established a lossless LZ77 format whose back-references are absolute output positions, giving parallel, compressed-resident GPU decode with sub-millisecond region seek. What it did not establish is what governs the decode throughput of such a format, or how to improve it. This paper answers both. Through controlled ablations on an NVIDIA H100 we show that decode throughput is governed not by occupancy, compute, address scatter, or launch parallelism, but by work granularity: throughput is a function of the average match length, because a short match leaves most lanes of a cooperating warp idle. A synthetic copy kernel confirms a 3.5x throughput span (212 to 744 GB/s) as average match length grows from 32 to 1024 bytes. Real data sit at the low end (mean match length 6.5 on enwik9, 10.1 on FASTQ). We then show that this mechanism yields a practical, encode-side lever: raising the minimum match length by distance class (6/8/10/12 to 12/16/24/32) improves both compression ratio and decode throughput simultaneously on all eight tested datasets, with no exceptions and no change to the decode kernel. FASTQ decode rises from 142.6 to 178.6 GB/s while ratio improves 1.8%; enwik9 throughput rises 78%. This is not a trade-off: both gains follow from one cause, removing short matches whose far offsets cost more entropy than they save. All figures are bit-perfect (FNV on GPU paths, byte compare on CPU paths) and git-verifiable. Scope is explicit: figures are match-phase, device-resident; entropy and host transfer are outside the timer; seek is read/block-level, not coordinate-level; and we do not claim to exceed the hardware bandwidth ceiling.

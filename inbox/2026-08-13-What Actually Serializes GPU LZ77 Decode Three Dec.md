---
interest: medium
link: https://arxiv.org/abs/2608.10188
next_step: skim
priority: medium
slack_ts: '1786588289.070199'
source: cs.DC - Distributed Computing
status: unread
title: 'What Actually Serializes GPU LZ77 Decode: Three Decoders, Three Mechanisms,
  and an Encode-Time Lever That Removes the Last One'
---
# What Actually Serializes GPU LZ77 Decode: Three Decoders, Three Mechanisms, and an Encode-Time Lever That Removes the Last One
> 原文: [https://arxiv.org/abs/2608.10188](https://arxiv.org/abs/2608.10188)

arXiv:2608.10188v1 Announce Type: new
Abstract: The sequential part of GPU LZ77 decode is not where the field assumes it is. Across three decoder architectures on an H100 we measure that parse, not copy, holds 64-72% of device-resident decode time; that bounding back-reference chain depth - provable, and costing 0.006% in ratio - moves latency by at most 2.8% and, for the file's own latency spike, provably by nothing at all, since a byte-level comparison of all 15,499 blocks shows the cap alters none of the 181 blocks involved; that self-overlapping matches are periodic fills rather than dependency chains, which makes them fully parallel and speeds the match layer by 2.75-8.42x bit-perfect; and that the last genuinely sequential element, a four-entry distance history, can be removed by the encoder for 0.540% of ratio, growing the dependency-free parse run from 4 commands to 706. We also report the floor the format runs into: with a median match of 7 bytes against a 128-byte cache line, bus efficiency is 4.4% and a coalesced write of the same data is 39x faster. A separate section records ten hypotheses these measurements refuted, including one methodological error of our own. Every reproducible claim carries a machine-checkable record: a fresh clone of the tagged release passes 17 of 17 checks reachable without a GPU, none failing.

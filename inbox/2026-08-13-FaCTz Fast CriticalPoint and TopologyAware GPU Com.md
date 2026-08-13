---
interest: medium
link: https://arxiv.org/abs/2608.10586
next_step: skim
priority: medium
slack_ts: '1786588276.087019'
source: cs.DC - Distributed Computing
status: unread
title: 'FaCTz: Fast Critical-Point and Topology-Aware GPU Compression for Scientific
  Vector Fields'
---
# FaCTz: Fast Critical-Point and Topology-Aware GPU Compression for Scientific Vector Fields
> 原文: [https://arxiv.org/abs/2608.10586](https://arxiv.org/abs/2608.10586)

arXiv:2608.10586v1 Announce Type: new
Abstract: Error-bounded lossy compression is essential for storing and transferring the vector-field data produced by large-scale scientific simulations. Although it enforces a user-specified error bound to limit numerical distortion, it does not preserve the field's topology: small admissible perturbations can create or eliminate critical points on which downstream feature analysis depends. Existing GPU compressors achieve high throughput but are topology-agnostic, whereas the only compressor with provable critical-point preservation (cpSZ) runs on the CPU at throughput far below the data-generation rates of modern GPU-based systems. We observe that, although preserving critical points is inherently a coupled and sequential constraint, it can be reformulated into independent parallel tasks, either on a per-block basis or, speculatively, on a per-point basis. We present FaCTz, the first GPU-based error-bounded lossy compressor that guarantees critical-point preservation. FaCTz provides a block-wise mode optimized for throughput and a speculative per-point mode optimized for compression ratio. Across three vector-field datasets, FaCTz preserves every critical point while achieving throughput of up to 60 GB/s, approximately two orders of magnitude (up to approximately 640x) faster than the multithreaded CPU implementation of cpSZ. Its speculative mode further improves the compression ratio by approximately a factor of two over the throughput-oriented mode.

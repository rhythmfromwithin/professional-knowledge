---
interest: medium
link: https://arxiv.org/abs/2604.22808
next_step: skim
priority: medium
slack_ts: '1777521049.061769'
source: cs.CV - Computer Vision
status: unread
title: 'FreqFormer: Hierarchical Frequency-Domain Attention with Adaptive Spectral
  Routing for Long-Sequence Video Diffusion Transformers'
---
# FreqFormer: Hierarchical Frequency-Domain Attention with Adaptive Spectral Routing for Long-Sequence Video Diffusion Transformers
> 原文: [https://arxiv.org/abs/2604.22808](https://arxiv.org/abs/2604.22808)

arXiv:2604.22808v1 Announce Type: new
Abstract: Long-sequence video diffusion transformers hit a quadratic self-attention cost that dominates runtime and memory for very long token sequences. Most efficient attention methods use one approximation everywhere, yet video features are spectrally structured: low frequencies carry global layout and coarse motion; high frequencies carry texture and fine detail. We present FreqFormer, a frequency-aware heterogeneous attention framework. Token features are split into spectral bands with different operators: dense global attention on compressed low-frequency content, structured block-sparse attention on mid frequencies, and sliding-window local attention on high frequencies. A lightweight spectral routing network allocates heads across bands using layer statistics and the diffusion timestep, shifting compute toward global structure early in denoising and detail later. Cross-band summary tokens provide cheap residual exchange. FreqFormer is paired with a fused GPU execution plan that co-schedules dense, sparse, and local branches to cut kernel launches and memory traffic. We give a consistent complexity model, an orthonormal-decomposition view of approximation, and simulation-based systems numbers (throughput, arithmetic intensity, memory traffic, duration scaling). In simulations from 64K to 1M tokens, FreqFormer substantially reduces estimated attention FLOPs and KV-related memory traffic versus dense attention while keeping a hardware-friendly pattern, supporting spectrally structured heterogeneous attention as a practical direction for long-video diffusion transformers.

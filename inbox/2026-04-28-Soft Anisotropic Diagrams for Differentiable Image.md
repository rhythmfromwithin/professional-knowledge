---
interest: medium
link: https://arxiv.org/abs/2604.21984
next_step: skim
priority: medium
slack_ts: '1777434585.339599'
source: cs.CV - Computer Vision
status: unread
title: Soft Anisotropic Diagrams for Differentiable Image Representation
---
# Soft Anisotropic Diagrams for Differentiable Image Representation
> 原文: [https://arxiv.org/abs/2604.21984](https://arxiv.org/abs/2604.21984)

arXiv:2604.21984v2 Announce Type: new
Abstract: We introduce Soft Anisotropic Diagrams (SAD), an explicit and differentiable image representation parameterized by a set of adaptive sites in the image plane. In SAD, each site specifies an anisotropic metric and an additively weighted distance score, and we compute pixel colors as a softmax blend over a small per-pixel top-K subset of sites. We induce a soft anisotropic additively weighted Voronoi partition (i.e., an Apollonius diagram) with learnable per-site temperatures, preserving informative gradients while allowing clear, content-aligned boundaries and explicit ownership. Such a formulation enables efficient rendering by maintaining a per-query top-K map that approximates nearest neighbors under the same shading score, allowing GPU-friendly, fixed-size local computation. We update this list using our top-K propagation scheme inspired by jump flooding, augmented with stochastic injection to provide probabilistic global coverage. Training follows a GPU-first pipeline with gradient-weighted initialization, Adam optimization, and adaptive budget control through densification and pruning. Across standard benchmarks, SAD consistently outperforms Image-GS and Instant-NGP at matched bitrate. On Kodak, SAD reaches 46.0 dB PSNR with 2.2 s encoding time (vs. 28 s for Image-GS), and delivers 4-19 times end-to-end training speedups over state-of-the-art baselines. We demonstrate the effectiveness of SAD by showcasing the seamless integration with differentiable pipelines for forward and inverse problems, efficiency of fast random access, and compact storage.

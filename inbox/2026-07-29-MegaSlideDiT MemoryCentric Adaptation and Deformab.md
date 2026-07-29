---
title: "MegaSlide-DiT: Memory-Centric Adaptation and Deformable Local Attention for Efficient Video Diffusion"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.22696
priority: medium
status: unread
interest: medium
next_step: skim
---
# MegaSlide-DiT: Memory-Centric Adaptation and Deformable Local Attention for Efficient Video Diffusion
> 原文: [https://arxiv.org/abs/2607.22696](https://arxiv.org/abs/2607.22696)

arXiv:2607.22696v1 Announce Type: new
Abstract: High-resolution video diffusion models built on Diffusion Transformers (DiTs) deliver strong fidelity but quickly exhaust the memory budget of a single workstation. A 100 billion-plus parameter DiT easily requires over a terabyte of persistent state, while naive spatiotemporal self-attention grows quadratically in sequence length. These two walls -- parameter memory and activation memory -- prevent researchers from adapting massive generative models without large GPU clusters. We revisit this problem from a systems perspective and introduce MegaSlide-DiT, a prototype that demonstrates how a pre-trained 105B DiT can be adapted on a single H200 GPU with 1.5 TB of host RAM. Our key insight is that the GPU need not own the model state: all persistent weights, master weights and optimizer moments remain in host memory, while only transient shards are streamed to the GPU on demand. Simultaneously, we replace quadratic global attention with 3D Deformable Slide Attention (3D-DSA), a motion-adaptive local attention operator that reduces both memory and computational complexity to linear in the sequence length. We report detailed memory accounting, execution traces and evaluation results to substantiate our design. MegaSlide-DiT does not claim to train a 105B model from scratch on a single GPU, nor does it magically solve bandwidth limits; rather, it offers a pragmatic path for full-parameter adaptation of massive video diffusion models on high-end workstations.

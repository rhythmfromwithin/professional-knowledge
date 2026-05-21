---
interest: medium
link: https://arxiv.org/abs/2605.16259
next_step: skim
priority: high
slack_ts: '1779337378.826569'
source: cs.LG - Machine Learning
status: unread
title: Systematic Optimization of Real-Time Diffusion Model Inference on Apple M3
  Ultra
---
# Systematic Optimization of Real-Time Diffusion Model Inference on Apple M3 Ultra
> 原文: [https://arxiv.org/abs/2605.16259](https://arxiv.org/abs/2605.16259)

arXiv:2605.16259v1 Announce Type: new
Abstract: While real-time image generation using diffusion models has advanced rapidly on NVIDIA GPUs, systematic optimization research on non-CUDA platforms such as Apple Silicon remains extremely limited. In this study, we conducted comprehensive optimization experiments across 10 phases targeting the Apple M3 Ultra (60-core GPU, 512 GB unified memory) with the goal of achieving real-time camera img2img transformation. We explored a wide range of techniques including CoreML conversion, quantization, Token Merging, Neural Engine utilization, compact model exploration, frame interpolation, kNN search-based synthesis, pix2pix-turbo, optical flow frame skipping, and knowledge distillation, quantitatively evaluating the effectiveness of each approach. Ultimately, by combining CoreML conversion of the distillation-specialized model SDXS-512 with a 3-thread camera pipeline, we achieved real-time camera img2img transformation at 22.7 FPS at 512x512 resolution. The primary contribution of this work is the systematic demonstration that optimization insights established for CUDA are not necessarily effective on Apple Silicon's unified memory architecture. We reveal an optimization landscape fundamentally different from that of NVIDIA GPUs -- including the absence of speedup from quantization, the ineffectiveness of parallel inference, and the unsuitability of the Neural Engine for large-scale models -- and provide practical guidelines for diffusion model inference on Apple Silicon.
